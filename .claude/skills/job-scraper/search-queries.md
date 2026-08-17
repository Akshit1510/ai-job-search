# Search Queries for Job Scraper

<!-- Populated by /setup (Path B) on 2026-07-26 for Akshit Maheshwari -->
<!-- Re-run `/setup --section search` to update as priorities shift -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; Danish demos and any skill you add with `/add-portal` are included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

## Search Sites

Primary (CLI-backed):
- **linkedin.com/jobs** — via the `linkedin-search` CLI. Main source for Indian tech roles. Filter: Pune / Bangalore / Hyderabad / Remote India, or by country for international.
- **freehire.me** — via the `freehire-search` CLI. Country-agnostic, startup and remote-leaning.

Primary (WebSearch `site:` fallback — no CLI ships for these; scaffold one with `/add-portal` if you use them heavily):
- **naukri.com** — the dominant Indian job board. Highest volume for Indian SDE roles.
- **instahyre.com** — curated Indian tech hiring, product-company skewed.
- **wellfound.com** (formerly AngelList Talent) — startup roles, often remote-friendly and international.

Secondary (company career pages via Google):
- Direct `site:` searches against target-company career domains (see Priority 5: Target-company career pages).

## Query Categories

Queries are grouped by priority. Combine each with a location term from the Location Filter below where the site supports it.

**Priority 1 has two co-equal tracks, 1A and 1B.** Backend engineering and AI/LLM engineering carry the **same weight** in this search. Run both every time — do not treat 1B as a fallback for when 1A comes up empty, and do not rank a 1B result below a 1A result for being a backend role. See the two-track scoring rule in `04-job-evaluation.md`.

### Priority 1A: AI / LLM Engineering

The strongest differentiator — production RAG, LangChain/LangGraph, embeddings, and semantic search at enterprise scale.

```
site:naukri.com "AI Engineer" LangChain OR RAG Pune OR Bangalore OR Remote
site:naukri.com "LLM Engineer" OR "GenAI Engineer" India
site:linkedin.com/jobs "AI Engineer" RAG India
site:linkedin.com/jobs "LLM Engineer" OR "Generative AI Engineer" Pune OR Bangalore OR Hyderabad
site:linkedin.com/jobs "Applied AI Engineer" Python India
site:instahyre.com "AI Engineer" OR "Machine Learning Engineer" LLM
site:wellfound.com "AI Engineer" LangChain remote
site:naukri.com "RAG" OR "vector database" OR "embeddings" engineer India
site:linkedin.com/jobs "AI Platform Engineer" OR "LLM Infrastructure" India
```

**Scoring caution:** many "Machine Learning Engineer" postings mean *model training*, which is a weak match (see `04-job-evaluation.md`). Read the responsibilities before scoring — retrieval, orchestration, and inference serving are strong; training, evaluation, and experimentation are not.

### Priority 1B: Backend Engineering / SDE-II

Equal-priority track, not a fallback. The straight continuation of the Deutsche Bank line — Java, Kotlin, Spring Boot, Python, FastAPI, microservices, and systems that carry real throughput. **A backend role with zero AI content is a first-class result.**

```
site:naukri.com "SDE 2" OR "SDE II" OR "Software Engineer II" Java OR Kotlin Pune OR Bangalore
site:naukri.com "Backend Engineer" Spring Boot Pune OR Bangalore OR Hyderabad
site:linkedin.com/jobs "Backend Engineer" Java Spring Boot India
site:linkedin.com/jobs "Software Engineer II" OR "SDE-2" microservices India
site:linkedin.com/jobs "Backend Engineer" Python FastAPI India
site:instahyre.com "Backend Engineer" Java OR Kotlin OR Python
site:naukri.com "Kotlin" backend developer India
site:wellfound.com "Backend Engineer" Python remote
site:linkedin.com/jobs "Distributed Systems" engineer Java OR Kotlin India
site:linkedin.com/jobs "Platform Engineer" OR "Infrastructure Engineer" backend India
site:naukri.com "high throughput" OR "low latency" OR "scalable systems" backend engineer India
site:linkedin.com/jobs "API Engineer" OR "Microservices" "Software Engineer" Pune OR Bangalore OR Hyderabad
site:naukri.com "Senior Software Engineer" backend Java OR Python Pune OR Bangalore
site:instahyre.com "SDE 2" OR "Software Engineer II" backend
site:wellfound.com "Backend Engineer" Java OR Kotlin remote
site:linkedin.com/jobs "Server Side" OR "Backend Developer" Spring Boot OR FastAPI India
```

**Scoring caution:** the deal-breaker filter still applies here. Backend req volume on naukri is dominated by service/consultancy body-shops — screen hard for "deputation", "client location", "resource", "bench", and "C2H" before surfacing (see Hard Filters below).

### Priority 2: Fintech & Financial Technology

Direct domain transfer from regulatory trade-exception and enterprise banking systems.

```
site:naukri.com fintech "Backend Engineer" OR "Software Engineer" Pune OR Bangalore
site:linkedin.com/jobs fintech backend engineer Java OR Python India
site:linkedin.com/jobs "trading systems" OR "regulatory reporting" engineer India
site:linkedin.com/jobs payments OR banking "Software Engineer II" India
site:instahyre.com fintech backend engineer
```

### Priority 3: Full-Stack

Wider net using the Vue/TypeScript/React side alongside the backend.

```
site:naukri.com "Full Stack Engineer" Java OR Python React OR Vue Pune OR Bangalore
site:linkedin.com/jobs "Full Stack Engineer" Python React India
site:linkedin.com/jobs "Full Stack Developer" Spring Boot TypeScript India
site:wellfound.com "Full Stack Engineer" remote
```

### Priority 4: International with sponsorship

Only worth running periodically — sponsorship-explicit postings are a small slice. Always confirm sponsorship wording before drafting (see the eligibility gate in `04-job-evaluation.md`).

```
site:linkedin.com/jobs "AI Engineer" "visa sponsorship" Europe OR UK OR Netherlands OR Germany
site:linkedin.com/jobs "Backend Engineer" "relocation" OR "sponsorship" Dubai OR Singapore OR Amsterdam
site:linkedin.com/jobs "Software Engineer" "we sponsor" OR "visa support" LLM OR RAG
```

### Priority 5: Target-company career pages

Add companies here as you identify them. Pattern:

```
site:<company>.com/careers "Software Engineer" OR "AI Engineer" India
```

Candidate categories to seed from: AI-first product companies, Indian product unicorns and scale-ups (payments, SaaS, developer tooling), global product companies with strong Pune/Bangalore/Hyderabad engineering centers, and AI infrastructure companies hiring remotely.

## Location Filter

Akshit's geography is intentionally wide. Grade rather than reject:

- **Tier 1 — Pune** (on-site or hybrid): home city, no relocation needed. Highest preference.
- **Tier 1 — Fully remote within India**: equal preference to Pune.
- **Tier 2 — Other Indian metros**: Bangalore, Hyderabad, Gurgaon/NCR, Mumbai, Chennai. Relocation acceptable; note whether relocation support is offered.
- **Tier 3 — International with visa sponsorship / relocation support**: acceptable, but sponsorship must be explicit in the posting or on the employer's careers page.
- **FAIL — International without sponsorship**, or requiring existing local work rights.
- **FLAG — Smaller Indian cities with no remote option**: surface for discussion rather than auto-including.

## Hard Filters (apply before ranking)

- **Skip service/consultancy body-shops.** Staffing-style IT services, client-site deployment, and resource-augmentation roles are a recorded deal-breaker. Watch for: "deputation", "client location", "resource", "bench", "C2H", and staffing-agency postings that name no end client.
- **Skip roles below the SDE-II band.** Graduate, trainee, junior, and SDE-I postings are a backwards step.
- **Flag published salary bands below ~Rs. 25 LPA.** Most Indian postings hide compensation; only filter when a band is actually stated.
- **Deprioritize pure support/maintenance roles** — L2/L3 production support, ticket-queue work, and legacy maintenance as the primary responsibility.
- **Do not filter out a backend role for lacking AI.** Backend and AI are co-equal tracks. The absence of LLM/RAG content in an otherwise strong backend posting is not a mark against it. Filter on depth — scale, ownership, architecture — not on which of the two tracks the role sits on.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

With no focus argument, `/scrape` runs **both 1A and 1B** and returns them as a single merged pool ranked on merit, not on which track they came from.

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- `/scrape ai` → Priority 1A queries plus custom LLM/RAG-specific searches
- `/scrape backend` → Priority 1B queries plus custom searches for the posting's stack (Java/Kotlin/Spring Boot, Python/FastAPI, distributed systems)
- `/scrape remote` → all priorities filtered to remote, plus Wellfound and freehire emphasis
- `/scrape fintech` → Priority 2 queries plus named fintech company career pages
