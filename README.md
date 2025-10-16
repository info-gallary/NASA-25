# NASA Space Apps 2025 — Earth Data Explorer 🚀

Harness interactive 3D, geospatial maps, and narrative storytelling to explore NASA Earth data — it feels like a mission, not a menu.

[![Node >= 20](https://img.shields.io/badge/node-%3E%3D20-339933?logo=node.js&logoColor=white)](#quick-start)
[![React 19](https://img.shields.io/badge/react-19-61DAFB?logo=react&logoColor=black)](#tech-stack)
[![Vite 7](https://img.shields.io/badge/vite-7-646CFF?logo=vite&logoColor=white)](#tech-stack)
[![Live](https://img.shields.io/badge/live-demo-blue)](#demo)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](#license--credits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success.svg)](#contributing)

---

## Table of Contents
- [Demo](#demo)
- [Why This Is Different](#why-this-is-different)
- [Quick Start](#quick-start)
- [Core Scripts](#core-scripts)
- [Project Map](#project-map)
- [Tech Stack](#tech-stack)
- [A Guided First Run](#a-guided-first-run)
- [Deploy](#deploy)
- [Contributing](#contributing)
- [License & Credits](#license--credits)

---

## Demo 🎥
- Video walkthrough: https://youtu.be/eD398Lv5WI0?si=_OAyVT4Woylku6pD
- Live deployment: https://your-live-deployment-url.example/

> Replace the live link above before committing to main.

## Why This Is Different ✨
- Mission‑style flow: launch, navigate, and discover insights across curated scenes.
- Seamless 3D + maps: Three.js models meet Leaflet/Mapbox views for context.
- Data stories: guided narratives for wildfires, surface temperature, pollution, and more.
- Friendly AI assist: a built‑in chatbot helps explain datasets and views.
- Delightful details: ambient audio, motion, and polished loading experiences.

## Quick Start ⚡
- Requirements: Node >= 20
- Install & run:

```bash
cd NASA-Space-Apps-25
npm install
npm run dev
# then open http://localhost:5173
```

## Core Scripts 🧰
- `npm run dev` — start Vite dev server
- `npm run build` — build for production
- `npm run preview` — preview the production build
- `npm run lint` — run ESLint
- `npm run manifest` — generate data manifest

## Project Map 🗺️
- App entry: `NASA-Space-Apps-25/src/App.jsx`
- Landing: `NASA-Space-Apps-25/src/pages/Terra25LandingPage.jsx`
- Terra mission: `NASA-Space-Apps-25/src/pages/TerraDetailsPage.jsx`
- Instruments: `NASA-Space-Apps-25/src/pages/ModisPage.jsx`, `NASA-Space-Apps-25/src/pages/MisrPage.jsx`, `NASA-Space-Apps-25/src/pages/MopittPage.jsx`
- Data insights hub: `NASA-Space-Apps-25/src/pages/data-insights/DataInsightsPage.jsx`
- Data stories: `NASA-Space-Apps-25/src/pages/data-insights/pages/WildfireStory.jsx`, `.../SurfaceTempPage.jsx`, `.../PollutionPage.jsx`, `.../TopologyStory.jsx`, `.../DeforestationStory.jsx`
- 3D models: `NASA-Space-Apps-25/src/components/3Dmodels/`
- Events explorer: `NASA-Space-Apps-25/src/pages/events/`
- Catalog experience: `NASA-Space-Apps-25/src/pages/catalog/`

## Tech Stack 🧪
- React 19 + Vite 7
- Three.js + React Three Fiber + Drei
- Tailwind CSS 4 (via Vite plugin)
- Leaflet + React‑Leaflet, Mapbox GL
- Plotly, GSAP, Framer Motion
- Model Viewer, OGL, Axios, Papa Parse

## A Guided First Run 🛰️
- Launch: start the dev server and open the landing scene.
- Explore: enter Terra details, then hop into instrument views (MODIS/MISR/MOPITT).
- Discover: open Data Insights and step through a story (e.g., Wildfires > Timeline > Map).
- Compare: use the Catalog to analyze outcomes side‑by‑side.
- Ask: try the chatbot to explain what you’re seeing.

## Deploy 🚢
- Includes `vercel.json` for Vercel deployments.
- Production build:

```bash
cd NASA-Space-Apps-25
npm run build
```

## Contributing 🤝
- Keep UX immersive: prefer narrative flows over raw lists.
- Small, focused PRs; describe UX intent and data sources.
- Run `npm run lint` before opening a PR.

## License & Credits 📄
- License: MIT (see `NASA-Space-Apps-25/LICENSE`)
- © 2025 Krish Vaghasia
- © 2025 Nisarg Vashi
- © 2025 Vansh Tandel

