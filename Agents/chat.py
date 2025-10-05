from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

db_url = "terra_qna.db"
db = SqliteDb(db_file=db_url, session_table="sessions")

model = Groq(id="llama-3.1-8b-instant")

terra_agent = Agent(
    model=model,
    instructions=dedent(
                    f"""Act as a NASA Scientist Bot, Analyze the given question as an expert NASA's Terra Data Analyzer. use web to get more insights and make sure that your answers are based on impact point of view that a user should understand that.
                    - if a general question, answer in a simple way.
                    - if a specific question, answer in a detailed way.
                    - give proper links and references.
                    - very concise answer and short answer to the point of the question.
                    - give answer in proper markdown format.
                    """),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

def interactive_terra_qna():
    """Interactive Terra QnA with user input"""
    print("\n=== Interactive Terra QnA ===")
    print("🌍 Terra 25th Anniversary QnA Chatbot")
    print("Ask me anything about Terra satellite data!")
     
    while True:
        try:
            question = input(f"\nUser: ").strip()
            
            if question.lower() in ['quit', 'exit', 'bye']:
                print(f"🛰️ Thanks! Keep exploring Terra data!")
                break
            
            if not question:
                continue
            
            print("Terra Bot: ", end="", flush=True)
            
            terra_agent.print_response(
                question,
                stream=True
            )
            
        except KeyboardInterrupt:
            print(f"\n🛰️ Goodbye!")
            break

if __name__ == "__main__":
    interactive_terra_qna()