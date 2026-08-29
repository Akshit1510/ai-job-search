---
framework_version: 1.0.0
---

# Interview Preparation Guide

<!-- Populated by /setup (Path B) on 2026-07-26 from the CV. The S/T/A framing is drawn from -->
<!-- documented work; the R lines use the CV's own numbers. Fill in the [ ] gaps with details -->
<!-- only you know before using these in an interview. -->

## STAR Format

Structure answers as: **Situation** (context), **Task** (your responsibility), **Action** (what you did), **Result** (outcome).

Keep answers to 1-2 minutes. Be specific. End with what you learned or would do differently.

## Ready-Made STAR Examples

### 1. Enterprise RAG chatbot over Confluence (end-to-end ownership, applied AI)
**S:** Employees at Deutsche Bank were losing time hunting for answers spread across thousands of Confluence pages and attached documents in inconsistent formats - PDFs, Word, Excel, and scanned images.
**T:** Build an internal chatbot that could actually answer those queries, covering the full path from raw documents to a usable interface.
**A:** Built ingestion pipelines to extract and normalize content from every source format, including a reusable OCR and image-indexing framework so visual documents were retrievable too. Built embedding pipelines on pgvector, then a retrieval layer using LangChain with Hugging Face LLMs, and a Streamlit UI on top. Deployed on Docker and OpenShift through Jenkins, with Pytest coverage in CI.
**R:** Shipped as a working internal tool answering employee queries across the documentation corpus. [Add: adoption numbers, user count, or feedback if you have them - this answer is much stronger with one concrete usage figure.]
**Use for:** "Tell me about a project you owned end to end", "Describe your experience with RAG/LLM systems", "Tell me about something you built from scratch"

### 2. Multithreaded ingestion rework (initiative, performance engineering)
**S:** The document ingestion and indexing pipeline for the chatbot was slow enough to be a bottleneck on how fresh the knowledge base could stay.
**T:** Make ingestion fast enough to be practical at the corpus size, without destabilizing it.
**A:** Profiled the pipeline to find where time was actually going, then restructured ingestion and indexing to run multithreaded across documents. [Add: what specifically was the bottleneck - I/O on document fetch, embedding calls, or parsing? Naming it makes this answer far more credible.]
**R:** Cut ingestion and indexing time by roughly 40-50%.
**Use for:** "Tell me about a time you improved performance", "Describe a time you took initiative", "How do you approach optimization?"

### 3. Embedding corruption in production (debugging persistence)
**S:** The embedding pipeline behind the chatbot was producing corrupted embeddings, which degraded retrieval quality in ways that were not obvious from the surface - answers got worse without an error being thrown.
**T:** Find the root cause and make the pipeline reliable, not just patched.
**A:** [Add the actual diagnostic path: how did you first notice? What did you check - dimension mismatches, encoding issues, partial writes, concurrency during the multithreading work, model version drift? What was the root cause and the fix?] This is your strongest debugging story - it needs your specifics to land.
**R:** Resolved the corruption and stabilized the pipeline for scalable, repeatable ingestion.
**Use for:** "Tell me about the hardest bug you've debugged", "Describe a time something failed silently", "How do you handle production issues?"

### 4. Regulatory trade-exception platform (ownership, scale, cross-functional work)
**S:** Deutsche Bank needed a platform to handle regulatory trade exceptions with high-throughput banking workflows.
**T:** As the newly promoted SDE-II, lead the backend.
**A:** Designed and built scalable REST APIs in Java, Kotlin, and Spring Boot with Gradle, working with the frontend team on the Vue.js/TypeScript client. Introduced caching and reworked request flows, and optimized the SQL behind the heaviest paths. Owned releases and the CI/CD pipeline across Jenkins, TeamCity, OpenShift, and Linux.
**R:** Request flows 30-40% faster, application load down 30%, SQL queries ~35% faster at peak. Stable releases with minimal production issues.
**Use for:** "Tell me about a system you designed", "Describe working with cross-functional teams", "How do you handle scale and performance?", "Tell me about your leadership experience"

### 5. Natural-language-to-SQL generator (self-directed AI work)
**S:** Analysts needed complex, bank-specific SQL queries that were slow and error-prone to write by hand.
**T:** Explore whether an LLM could generate them reliably enough to be useful - this was self-initiated POC work, not assigned.
**A:** Built a generator using LangGraph for orchestration with LangChain and LLMs in Python, handling bank-specific schema and query patterns. [Add: how did you handle correctness - schema grounding, validation against the DB, retry on failure? And what were the accuracy limits you found?]
**R:** Working POC demonstrating automated generation of complex bank-specific queries. **Be precise in interviews: this was a POC, not a production system.** The honest framing - what worked, what the failure modes were, what productionizing would have required - is more impressive than overclaiming.
**Use for:** "Tell me about a time you took initiative", "Describe an AI project", "Tell me about something that didn't fully ship"

### 6. AI resume optimization platform (self-driven depth, current)
**S:** Wanted to go deeper on LLM system design than the day job allowed.
**T:** Build a full LLM platform independently, end to end.
**A:** Designed a provider-abstraction layer unifying OpenAI Responses API and Hugging Face Transformers behind one interface with REST, streaming, and structured JSON output. Built a resume optimization pipeline using Pydantic-validated schemas with deterministic retry logic, and a scoring engine grading job fit on relevance, skills match, impact, clarity, and ATS compatibility. FastAPI backend, React frontend, GPU inference with CUDA/FP16, Dockerized across AWS/GCP/Azure.
**R:** Ongoing since Oct 2025. [Add: what's working, what you learned that changed how you'd build the systems at work.]
**Use for:** "What do you do outside work?", "How do you stay current?", "Tell me about a technical decision you made and why"

## STAR Candidates (Complete Manually)

### Volunteer teaching with NSS (communication, explaining to non-experts)
**Source:** CV - Volunteer Teacher, National Service Scheme, Punjab Engineering College (Sep 2019 - Jul 2023)
**What happened:** Delivered free academic tutoring to underprivileged students across four years alongside the B.Tech.
**Why it matters:** All six examples above are engineering stories. This is the only evidence for "explain something technical to a non-technical audience", "tell me about mentoring someone", and sustained commitment outside required work - all standard interview questions that currently have no backing example.
**S/T/A/R stub:**
- Situation:
- Task:
- Action: [Which subjects, what age group, how did you adapt when a student was not following?]
- Result: [Any concrete outcome - students' results, how long you kept it up, what it changed about how you explain things now]

## Common Tough Questions

### "Why are you leaving Deutsche Bank?" / "Why are you looking?"
> Draft: "I've had a good three years there - I was promoted early, and I got to build real AI systems inside a regulated environment, which is not easy. What I'm looking for now is somewhere the AI work has a clearer path to production. The chatbot shipped internally, but the natural-language-to-SQL work stayed a POC, and I want to be somewhere those systems become the product rather than a side track. I'm also looking for more senior engineers around me to learn from."
>
> **Rules:** stay forward-looking, no criticism of the bank, do not lead with compensation, and do not say "bureaucracy" - it reads as a complaint about structure rather than about ambition.

### "You've only worked at one company." / "You don't have startup experience."
> Draft: "That's true - three years, one employer. What it bought me is depth in a domain where getting it wrong has regulatory consequences, so I learned to build carefully. And within that constraint I self-started: nobody assigned me the RAG chatbot or the LangGraph work, I proposed and built them. I also build independently outside work - I'm currently running a full LLM platform project end to end. The thing I'd be adding to your team is that I already know how to operate where correctness matters."

### "You don't have [ML training / Kubernetes at depth / Go / data engineering]."
> Draft pattern: name the gap directly, bridge to the nearest real experience, then show the learning track record. "You're right that I haven't trained models - my AI work is application-side: retrieval, orchestration, inference, getting LLM systems to be reliable in production. What I'd bring is [nearest adjacent experience]. And on picking things up: I went from no LLM experience to shipping an internal RAG system, and got Google Cloud certified alongside the day job."
>
> **Never bluff a gap.** Interviewers probe, and the honest answer plus a concrete learning example beats a vague claim every time.

### "Where do you see yourself in 5 years?"
> Draft: "Senior engineer owning the architecture of AI-backed systems, not just building them - the design decisions about retrieval, orchestration, and how these systems fail. I'd also like to be the senior engineer other people can learn from; I've had good mentorship and I know what it's worth." Tailor the specifics to the role's actual growth path.

### "What's your biggest weakness?"
> Draft: "I get frustrated when direction shifts and work gets thrown away, and early on I'd just absorb that. What I've learned to do is push the ambiguity to the front - ask the scoping questions and get the success criteria written down before I start building, rather than after. It's made me better at the conversation, not just the code."
>
> **Rules:** genuine, with a concrete mitigation. Avoid the humble-brag weaknesses ("I'm a perfectionist") - experienced interviewers discount them instantly.

### "What are your compensation expectations?"
> Baseline is Rs. 26-35 LPA (current ask: Rs. 26 LPA+). Deflect first if it comes early: "I'd rather understand the role and scope before putting a number on it - what range has been budgeted?" If pressed, anchor at the upper end of your band and cite the AI + backend combination as the reason. Never volunteer your current salary unless required.

### "Why this company specifically?"
> Customize per company. Must reference: specific projects, company values, market position, or team structure. Never give a generic answer.

## Questions You Should Ask Interviewers

### About the Role
- "What does a typical week look like in this role?"
- "What would success look like in the first 6 months?"
- "What's the biggest challenge the team is facing right now?"

### About the Team
- "How big is the team, and how do you divide work?"
- "What does the development/project lifecycle look like, from idea to production?"
- "How do you onboard new team members?"

### About Tech & Growth
- "What's your current tech stack for [relevant area]?"
- "Is there room to grow into more architectural or strategic decisions?"
- "How does the team stay current with new tools and methods?"

### About Culture (use these to prevent disappointment)
- "How would you describe the team culture?"
- "What does professional development look like here?"
- "Is there flexibility for remote/hybrid work?"
- "What's the balance between development/new projects and maintenance work?"
- "How would you describe the leadership style in this team?"
- "What do people who thrive here have in common?"

## Phone/Video Interview Tips
- Have STAR examples written out (use this file)
- Keep a glass of water nearby
- Smile when speaking (it changes your tone)
- Ask for clarification if a question is vague
- It's OK to take 5 seconds to think before answering
- End with: "Is there anything else you'd like to know about my background?"

## After the Application (Best Practice)

### Follow-Up Etiquette
- **Don't call to "stand out"** or to learn more about the role post-submission - this risks a negative impression
- If the employer specified a timeline, respect it and wait
- If no timeline was given and significant time has passed (2+ weeks), a brief call to ask about status is acceptable
- If you have genuinely new, relevant information to share, a short follow-up is fine

### Thank-You Notes
- When you receive any update (interview invitation, rejection, or status update), send a brief thank-you message
- Express appreciation for their time and the process
- Keep it short (2-3 sentences)

## Roleplay Guidelines
When the user asks for interview practice:
1. Ask which role/company to simulate
2. Start with easy warm-up questions ("Tell me about yourself")
3. Progress to role-specific technical questions
4. Include 1-2 behavioral questions using the competencies from the job posting
5. End with a tough question or curveball
6. After each answer, give brief feedback: what worked, what to sharpen
7. Suggest which STAR example would work best for each question
