import os
import re
from textwrap import dedent
from typing import Optional, List, Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()
# -------------------
# ENV / MODEL / AGENT
# -------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("❌ GROQ_API_KEY not found. Please export it before running.")

model = Groq(id="llama-3.1-8b-instant")

terra_agent = Agent(
    model=model,
    instructions=dedent("""\
        Act as a NASA Terra Data speciallist named as TerraNaut AI Agent. Analyze questions as an expert NASA Terra Data Analyst.
        - If general, answer simply.
        - If specific, answer in detail.
        - Use web search when helpful and include references.
        - Keep answers concise and impact-focused.
        - Respond in Markdown.
    """),
    tools=[DuckDuckGoTools()],
    markdown=True,
)


# -------------------
# FASTAPI SETUP
# -------------------
app = FastAPI(title="TerraNaut QnA API", version="1.0.0")

# CORS (open for development — restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["https://your-frontend-domain.com"] later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------
# SCHEMAS
# -------------------
class AskRequest(BaseModel):
    question: str
    context: Optional[str] = None
    temperature: float = Field(0.2, ge=0.0, le=1.0)
    return_sources: bool = True


class SourceItem(BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None


class AskResponse(BaseModel):
    ok: bool
    message_markdown: str
    message_text: str
    sources: List[SourceItem] = []
    meta: Dict[str, Any] = {}


# -------------------
# UTILITY FUNCTIONS
# -------------------
def extract_links(md: str) -> List[SourceItem]:
    """Extract markdown links like [title](url) into a list."""
    items: List[SourceItem] = []
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^\)]+)\)", md):
        items.append(SourceItem(title=m.group(1), url=m.group(2)))
    return items


def strip_markdown(md: str) -> str:
    """Convert markdown text to plain text."""
    text = re.sub(r"`{1,3}[^`]*`{1,3}", "", md)
    text = re.sub(r"!\[[^\]]*\]\([^\)]*\)", "", text)
    text = re.sub(r"\[[^\]]*\]\((https?://[^\)]+)\)", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_]{1,3}", "", text)
    text = re.sub(r"^\s*-\s+", "• ", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# -------------------
# ROUTES
# -------------------
@app.get("/")
def root():
    return {"message": "Welcome to the TerraNaut QnA API. Visit /docs for API documentation."}

@app.get("/health")
def health():
    return {"status": "ok", "model": model.id}


@app.post("/v1/ask", response_model=AskResponse)
def ask(req: AskRequest):
    """
    Simple Terra QnA endpoint:
    - Accepts a question (and optional context)
    - Returns Markdown + plain text + extracted links
    """
    try:
        # Combine question + context into a single prompt
        prompt = f"{'Context:\n' + req.context + '\n\n' if req.context else ''}Question:\n{req.question.strip()}"

        # Run the agent
        reply = terra_agent.run(prompt, temperature=req.temperature)

        # Extract content safely (reply may be a RunOutput object)
        md = getattr(reply, "content", str(reply)).strip()

        txt = strip_markdown(md)
        sources = extract_links(md) if req.return_sources else []

        return AskResponse(
            ok=True,
            message_markdown=md,
            message_text=txt,
            sources=sources,
            meta={"model": model.id},
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------
# ENTRY POINT
# -------------------
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
