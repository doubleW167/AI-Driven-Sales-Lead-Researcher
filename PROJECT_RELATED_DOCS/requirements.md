# Scenario
<p align="justify">
Sarah, a Head of Sales at a small B2B SaaS company has 3 sales reps and sells a software product to mid-sized logistics companies. 

Her biggest pain: they spend too much time researching leads manually (LinkedIn, news, Crunchbase etc..). She wants sometjhing that helps her and hear team quickly identify good leads and what to say in outreach emails. 

</p>

## Customer needs 

In an interview with Sarah the next goal is to ask some questions in order to clarify the exact needs and to determine project costs and also how much the company is willing to pay for. 

- What does your typical workflow look like?
- What are your biggest pain points?
- How much are you willing to pay for?
- What kind of output or dashboard

1. "I start with LinkedIn Sales Navigator to search for logistics companies that match our ICP (mid-sized, 50–500 employees, in North America).

    Then I manually check their company websites to confirm relevance.

    I google for news about them (funding, expansion, new contracts).

    I add the good ones into our HubSpot CRM and tag them for reps.

    Each rep then spends 15–30 minutes writing personalized outreach emails."
<br>
2. Biggest pain points:
    - Time sink: researching each lead takes 20–30 minutes, and they need 50+ per week.
    - Quality: often they can’t tell if a company is actually a good fit until much later.
    - Context for outreach: sales emails are too generic because reps don’t know enough about the company’s situation.
<br>
3. If this tool saves each rep even 5–10 hours a week, it’s worth $100–200/month per seat.
<br>
4. They would like a dashboard that shows:
    - Company name, size, location
    - Industry tags
    - Recent news / funding
    - AI-suggested “Outreach Hook” (1–2 sentences they can paste into emails)
    - Ability to export leads to CSV or push to HubSpot.
    - Clean and minimal — sales reps don’t want to “learn” a new tool, they just want the info.
<br>
5. CRM integration:
    - HubSpot is a must.
    - Even a “Export to CSV/Excel” button is fine for v1, as long as they can import manually.

## MVP 

From here a typical MVP for this particular situation could look something like this: 

- **Input**: industry + region
- **Output**: list of 20 companies + AI-generated lead briefs (pain points + outreach hook)
- Simple dashboard to view/export
- CSV export (CRM integration can come later)


## Scope and user flow 
- Sales rep enters industry + region in the dashboard.
- System fetches companies from public APIs or scraping sources.
- AI generates lead briefs: company summary, recent news, outreach hook.
- Dashboard displays 20 leads with key info.
- Option to export to CSV for HubSpot import.

## Functional/Non functional requirements 

Must-have: input form, AI-generated lead briefs, dashboard view, CSV export.

Nice-to-have: direct HubSpot integration, batch processing (50+ leads), lead scoring.

## Goals and metrics
The goal of this project is to save a minimum of **10-15 hours/week per rep.** on lead research. 
<br>
Futhermore, it is important to generate accurant or relevant outreach hooks for at least **80%** of the time.
<br>
The goal is also to keep the dashboard/output as minimalistic as possible, assuring an learning curve of <b>&lt;5 min.</b>