# Technology stack  


## Frontend
- **React** → interactive dashboard
- **Tailwind CSS** → fast, clean styling
- Optional: **Next.js** → for routing or server-side rendering

**Role:** Allows users to input industry + region, view AI-generated lead briefs, and export to CSV.

---

## Backend
- **Python + FastAPI** → handles requests from frontend
- Calls **OpenAI GPT-4** to generate summaries, pain points, and outreach hooks
- Fetches company data from APIs or web sources

**Role:** Core processing, AI integration, and serving data to frontend.

---

## Database
- **MongoDB**: No fixed schema → great for storing semi-structured data like AI-generated lead briefs, which may have variable fields (news snippets, outreach hooks, optional metadata).


**What it stores:**  
- Leads (company name, industry, location, size, news, AI outreach hook)  
- Optional: search history (industry + region + timestamp)

**Role:** Store AI-generated leads so users can view/export them later.

---

## AI
- **OpenAI GPT-4** → summarize company info, extract pain points, generate outreach hooks
- Optional: **Hugging Face NLP models** → extract keywords or analyze sentiment from news

**Role:** Provides the intelligence that makes the tool valuable.

---

## Export / CRM Integration
- **CSV export** → MVP
- Optional Phase 2: HubSpot API integration for direct import

**Role:** Allows sales reps to use AI-generated leads in real workflows.

---

## Containerization / Deployment
- **Docker** → containerized backend (FastAPI), frontend (React), and database (MongoDB)
- Optional: **Docker Compose** → run multi-container environment locally

**Role:** Makes the app portable, production-ready, and easy to demo.

---

