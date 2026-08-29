---
framework_version: 1.1.0
---

# Job Evaluation Framework

<!-- Personalized by /setup (Path B) on 2026-07-26 -->

## Candidate eligibility baseline

Akshit is an **Indian citizen resident in Pune**. For roles located in India the eligibility gate below is not applicable - skip it and go straight to scoring.

For **international roles**, the gate is fully in force and is the first thing to check: Akshit needs visa sponsorship and relocation support. Treat "must have existing work authorization in <country>", "no sponsorship available", or a security-clearance requirement as a **hard FAIL** and report it with the quoted wording rather than drafting. Postings that explicitly say they sponsor, or that name India-based hiring, are a **PASS** and worth calling out as a positive in the application.

## Eligibility Gate — run before scoring

If the candidate is not a citizen or permanent resident of the country they are applying in, run this first. It is a hard filter, not a scoring dimension, and it is separate from work-permit *timing*: timing asks "can they work the required hours yet?", eligibility asks "are they permitted to hold this job at all?". A candidate can pass timing and still be categorically excluded.

Read the posting's eligibility / work rights / "who can apply" section **verbatim** and classify:

| Posting wording | Verdict |
|-----------------|---------|
| Names a **citizenship or permanent-residency requirement** ("must be a citizen of X", "permanent resident", "PR required", "full working rights" where the employer means citizen/PR) | **FAIL — hard stop.** Do not score, do not draft. Quote the exact wording back to the user. |
| Requires a **security clearance** at any level | **FAIL** in most countries, since clearance is normally gated on citizenship. Verify the specific scheme rather than assuming. |
| **Explicitly names** the candidate's permit class, or says "international applicants welcome", "visa holders considered", "we sponsor" | **PASS** — verified acceptance. Worth noting as a positive in the application. |
| **Silent** on citizenship or residency | **PROCEED, but mark unverified.** Check the employer's own careers or international-applicant page before drafting. |

**Two rules that are easy to get wrong:**

1. **Silence is not permission.** Large graduate programs frequently gate eligibility on their own website rather than in the job ad. Highest-risk categories: professional-services firms, government and defence, banking, telecommunications, and anything touching critical infrastructure.
2. **A company-wide "we accept international applicants" statement is not role-level permission.** The common pattern is a general welcome followed by a *named list* of the specific programs or service lines it covers. Confirm the **specific posting or stream** appears on that list before drafting.

**Report an eligibility failure to the user with the quoted source** rather than silently dropping the role. They may know something about their own status that the profile does not record.

If the candidate's permit also constrains *hours* or *start date* (a student visa with a term-time cap, a permit that begins on graduation), record that as a second gate under this section during `/setup`, with the specific dates. Do not merge it with the eligibility question above — they fail for different reasons and need different answers.

A role that fails this gate is not scored and not drafted. Everything below applies only to roles that pass it.

## Scoring Dimensions

Evaluate each job posting against these five dimensions:

### 1. Technical Skills Match (0-100)
How well do the required/preferred skills align with the candidate's capabilities?

| Score | Meaning |
|-------|---------|
| 80-100 | Core requirements are primary skills |
| 60-79 | Most requirements match, 1-2 gaps that are learnable |
| 40-59 | Partial match, significant upskilling needed |
| 0-39 | Fundamental mismatch |

**Strong match areas:** Python, Java, Kotlin, Spring Boot, FastAPI, REST API design, microservices, backend architecture; LLM/RAG systems (LangChain, LangGraph, embeddings, hybrid retrieval, cross-encoders, prompt engineering, OpenAI APIs, Hugging Face Transformers, pgvector); Docker, OpenShift, Jenkins, CI/CD, Linux, GCP; SQL and performance optimization; Pytest, Pydantic, TDD

**Moderate match areas:** C++; Vue.js, TypeScript, React (frontend is real but secondary); Kubernetes (used, not owned at depth); AWS and Azure (personal project only - GCP is the certified/production cloud); Streamlit; OCR and document-processing pipelines; multithreading and concurrency

**Weak match areas:** Classical ML / data science (scikit-learn, statistical modelling, feature engineering, experiment design) - Akshit's AI work is LLM/RAG application engineering, not model training; MLOps platforms (MLflow, Kubeflow, SageMaker, Vertex AI pipelines); model fine-tuning and training infrastructure; data engineering at scale (Spark, Kafka, Airflow, dbt, warehousing); Go, Rust, Scala, C#, PHP, Ruby; mobile development; deep frontend specialization (Next.js, state management, design systems); Terraform / IaC; observability stacks (Prometheus, Grafana, Datadog) beyond basic logging; people management

**Scoring note:** A posting asking for "ML Engineer" that means *model training* is a much weaker fit than the title suggests. Read the responsibilities, not the title - if the work is RAG, LLM orchestration, inference serving, or AI application engineering, score it high; if it is training, evaluation, and experimentation on models, score it 40-59 and say so.

### 2. Experience Match (0-100)
Does work history align with what they're looking for?

| Score | Meaning |
|-------|---------|
| 80-100 | Direct experience in the same domain and role type |
| 60-79 | Related experience, transferable skills clear |
| 40-59 | Adjacent experience, would need to make the case |
| 0-39 | Unrelated experience |

**Seniority baseline:** ~3 years of professional experience (Aug 2023 - present), currently Associate/SDE-II after an early promotion. Target band is **SDE-II / Software Engineer II / mid-level**. Score "Senior Engineer" postings asking for 5+ years at 40-59 unless the responsibilities genuinely match; score "SDE-I / Junior / Graduate" postings low on career alignment - they are a backwards step.

**Strong:** Backend engineering in Java/Kotlin/Spring Boot and Python/FastAPI; enterprise banking and regulatory compliance systems; LLM/RAG application engineering (enterprise chatbot, semantic search, embedding pipelines); performance and query optimization; CI/CD ownership on Docker/OpenShift/Jenkins

**Moderate:** Full-stack work with Vue/TypeScript/React frontends; cloud-native deployment on GCP; document ingestion and OCR pipelines; agentic LLM orchestration with LangGraph (POC-level at work, deeper in the personal project); multi-cloud deployment (personal project only)

**Entry-level:** Model training and classical ML; data engineering platforms; SRE and observability ownership; team leadership and people management; client-facing or pre-sales engineering

### 3. Behavioral/Culture Fit (0-100)
Does the role and company culture match the behavioral profile?

| Score | Meaning |
|-------|---------|
| 80-100 | Culture strongly matches behavioral preferences |
| 60-79 | Mixed signals but mostly compatible |
| 40-59 | Some friction areas |
| 0-39 | Significant culture mismatch |

**Red flags to research:** Department disorganization, work dominated by maintenance over development, poor chemistry with leadership, culture mismatches. Check reviews, media coverage, LinkedIn connections, and network contacts for insider perspective.

**Akshit-specific red flags:** Service/consultancy body-shop model (hard deal-breaker - see below); chronically shifting requirements or unclear ownership; heavy governance with no engineering counterweight; AI work that never escapes POC status *in a posting that sells itself on AI* (a posting that never mentions AI is not committing this sin - see the two-track rule under Career Alignment).

**Green flags:** stated ownership and autonomy, frequent shipping, visible senior engineering bench, and **either** LLM systems actually in production **or** genuine backend depth - scale, latency budgets, architecture ownership, systems that carry real traffic.

### 4. Location & Logistics (Pass/Fail + Notes)
Akshit's geography is deliberately wide. Location is rarely a FAIL - grade it in tiers instead:
- **Pune (on-site or hybrid): PASS - Tier 1.** Home city, no relocation needed.
- **Fully remote within India: PASS - Tier 1.**
- **Other Indian metros (Bangalore, Hyderabad, NCR/Gurgaon, Mumbai, Chennai): PASS - Tier 2.** Relocation acceptable; note whether the employer offers relocation support.
- **International with visa sponsorship / relocation support: PASS - Tier 3.** Confirm sponsorship explicitly (see the eligibility baseline at the top of this file) before drafting.
- **International with no sponsorship, or requiring existing local work rights: FAIL.** Quote the wording back to the user.
- **Smaller Indian cities with no remote option: FLAG** - discuss before drafting.
- **Frequent international travel: FLAG** (discuss with user).

### 5. Career Alignment & Motivation (0-100)
Does this role advance career goals and contain tasks that energize?

| Score | Meaning |
|-------|---------|
| 80-100 | Strongly aligned with career direction, clear growth path |
| 60-79 | Good role but only partially aligned with long-term goals |
| 40-59 | Decent job but doesn't build toward career goals |
| 0-39 | Dead end or backwards step |

**Career goals — two co-equal tracks:**

Akshit's search runs on **two tracks of equal weight: backend engineering depth and applied AI/LLM engineering.** Either one, on its own, satisfies the career direction. Score them symmetrically.

- **Backend track:** deep backend and distributed-systems work - API and service architecture, high-throughput systems, performance and database engineering, end-to-end ownership from design through deployment. A strong backend role with **no AI content whatsoever is a full-marks career fit**, not a compromise.
- **AI track:** roles where **AI/LLM systems reach production** rather than stalling as POCs - retrieval, orchestration, inference serving, agentic workflows. A strong AI role with limited classical backend scope is likewise a full-marks fit.
- Consolidate the SDE-II level at a **product-engineering company** where engineering is the product, with a visible path toward senior
- Work alongside **strong senior engineers** in a genuine code-review and technical-depth culture
- Optionally: an international move, if it comes with sponsorship and a step up in engineering quality

**Scoring rule (important):** Do **not** deduct career-alignment points from a backend-heavy posting because it does not mention AI, and do not deduct from an AI-heavy posting because it is light on traditional backend. Score against whichever track the posting sits on. A role that hits **both** tracks is exceptional and should score at the very top of the band, but hitting one track well is already a strong score (80+). The low scores are reserved for roles that are shallow on both - ticket-queue maintenance, thin CRUD work with no scale or ownership, and AI work permanently confined to demos.

**Motivation filter:** Evaluate not just whether Akshit *can* do the tasks, but whether the tasks will *energize* them.
- **Tasks that energize:** designing and building backend services end to end; API and service architecture at throughput; performance optimization, profiling, and database tuning; hard debugging; LLM/RAG application engineering (retrieval quality, orchestration, agentic workflows); shipping POCs into production; learning a new part of the stack under senior guidance. **Backend and AI items in this list carry equal weight** - a posting full of the backend items and none of the AI items is just as energizing as the reverse.
- **Tasks that drain:** work with unclear direction that gets thrown away and redone; AI work confined permanently to demos; ticket-queue maintenance; approval-chain overhead with no engineering payoff
- **Non-task factors:** degree of autonomy, technical credibility of the manager, seniority of the surrounding engineering bench, whether the team ships often

**Life situation alignment:**
- **Security:** Currently employed and not under time pressure - can be selective and should be. A move must be a clear step up, not lateral.
- **Compensation baseline:** Target band **Rs. 26-35 LPA**; treat offers materially below Rs. 26 LPA as a filter-out. Flag postings that publish a band below this. **Never surface compensation figures in a CV or cover letter.** (Updated 2026-08-29 from the prior Rs. 25 LPA floor.)
- **Flexibility:** No recorded family or schedule constraints. On-site, hybrid, and remote are all workable; relocation within India and internationally (with sponsorship) is on the table.
- **Professional development:** Highest priority is production AI/LLM exposure plus senior mentorship. A role offering both can outweigh a moderate compensation difference; a role offering neither should score low on this dimension regardless of pay.

## Calibration from Past Applications

<!-- Empty. Populated by /setup Path A once documents/applications/<company>_<role>/ folders with -->
<!-- job_posting.md + outcome.md pairs exist, or incrementally by /outcome as results come in. -->
No application history recorded yet.

### 6. Salary Benchmark

If the salary lookup tool is configured (`salary_data.json` exists), look up the company:
```
python salary_lookup.py "<Company Name>" --json
```

If a city is known from the posting, add `--city "<City>"` to narrow results.

**If the tool is not configured, or returns no data for this company, fall back to a web search** rather than skipping the benchmark entirely: search for `"<Company Name>" salary <role/level> India` and check sites that publish crowdsourced compensation data (Glassdoor, AmbitionBox, Levels.fyi, Naukri's salary insights, Payscale). Treat anything found this way as an **indirect estimate**, not a confirmed figure - label it as such in the evaluation output, and note the source. Only skip the benchmark section entirely if neither the tool nor a web search surfaces anything usable.

Present findings as:
```
### Salary Benchmark
| Metric | Value |
|--------|-------|
| [Category] index | XX.X (+/-X.X% vs baseline) |
| Overall index | XX.X (+/-X.X% vs baseline) |
```

Interpret results relative to the baseline defined in the data file's metadata. For index-based data, higher typically means above-market compensation.

If the salary tool is not configured, skip this section.

## Output Format

Present the evaluation as:

```
## Job Fit Evaluation: [Role] at [Company]

| Dimension | Score | Notes |
|-----------|-------|-------|
| Technical Skills | XX/100 | [brief note] |
| Experience Match | XX/100 | [brief note] |
| Behavioral Fit | XX/100 | [brief note] |
| Location | PASS/FAIL | [brief note] |
| Career Alignment | XX/100 | [brief note] |

**Overall Score: XX/100** (weighted average of scored dimensions)

### Verdict: [Strong Fit / Good Fit / Moderate Fit / Weak Fit / Poor Fit]

### Key Strengths for This Role
- [bullet points]

### Gaps to Address
- [bullet points]

### Recommendation
[1-2 sentences: apply/skip/apply with caveats]

### Company Research Checklist
- [ ] Checked company website (mission, values, recent news)
- [ ] Checked review sites (Glassdoor, Jobindex, etc.)
- [ ] Checked LinkedIn for team size, recent hires, connections
- [ ] Checked media for restructuring, growth, or workplace issues
- [ ] Identified network contacts who may know the team/manager
```

## Weighting
- Technical Skills: 30%
- Experience Match: 25%
- Behavioral Fit: 15%
- Career Alignment: 30%

(Location is pass/fail, not weighted)

## Thresholds
- **Strong Fit** (75+): Definitely apply, tailor everything
- **Good Fit** (60-74): Apply, address gaps in cover letter
- **Moderate Fit** (45-59): Consider carefully, discuss with user
- **Weak Fit** (30-44): Probably skip unless strategic reasons
- **Poor Fit** (<30): Skip

## Pre-Application: Call the Employer (Best Practice)

Before writing the application, consider whether the candidate should call the contact person listed in the posting. **Only call if there are substantive questions** - never call just to "be remembered."

### When to Suggest Calling
- The posting has unclear or ambiguous requirements
- It's unclear which competencies are essential vs. nice-to-have
- The role description is vague about day-to-day tasks
- There's a named contact person who invites questions

### Good Questions to Ask
- "What are the primary challenges in this role?"
- "How is time typically divided across the listed responsibilities?"
- "Which competencies are most critical for success in this position?"
- "What does success look like in the first 6-12 months?"

### Rules for the Call
- Prepare a 30-second "elevator pitch" about your background in case they ask
- The call's purpose is **gathering information**, not delivering a pitch
- Take notes - use what you learn to tailor the application
- Reference the conversation naturally in the cover letter ("After speaking with [name], I was especially drawn to...")
