# Graph Report - D:/programming/projects/ai-job-search/ai-job-search  (2026-07-26)

## Corpus Check
- 149 files · ~93,334 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1074 nodes · 1569 edges · 76 communities (66 shown, 10 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 60 edges (avg confidence: 0.83)
- Token cost: 428,021 input · 0 output

## Community Hubs (Navigation)
- Jobdanmark CLI Implementation
- Freehire CLI Implementation
- Jobnet CLI Implementation
- Security Guard Tests
- Jobindex CLI Implementation
- LinkedIn CLI Implementation
- Salary Excel Converter Tests
- Jobbank CLI Package Manifest
- Jobbank CLI Commands
- Jobdanmark CLI Package Manifest
- Jobindex CLI Package Manifest
- Company Match Scoring Tests
- PDF Verification Tests
- Template and Apply Contracts
- Jobbank TypeScript Config
- Jobdanmark TypeScript Config
- Jobindex TypeScript Config
- Jobnet CLI Package Manifest
- Jobnet TypeScript Config
- Portal Generation and Setup Onboarding
- Freehire CLI Package Manifest
- LinkedIn CLI Package Manifest
- Company Search Tests
- Profile Expansion and Gmail Sync
- Interview Prep and Outcome Tracking
- Salary Data Loading and Validation
- Fuzzy Name Matching Utilities
- Salary Data Shape Validation Tests
- Reporting and Job Triage
- Portal Skill Design Patterns
- Freehire TypeScript Config
- LinkedIn TypeScript Config
- HTML Report Command Tests
- Skill Linter Tests
- Jobdanmark API Endpoints
- Repo Governance and Funding
- Untrusted Input and Command Bar
- Freehire and LinkedIn API Contracts
- Jobbank and Jobindex Scraping
- CI Fork-Safety and PDF Checks
- Outcome Follow-Up Tests
- Jobbank CLI Contract Tests
- Jobnet API Constraints
- LaTeX Compile and Page Budgets
- Drafter-Reviewer Scoring Workflow
- Skill Gap and Learning Plan
- CI Checks and Changelog
- Jobdanmark CLI Contract Tests
- Jobindex CLI Contract Tests
- Jobnet CLI Contract Tests
- ATS Verification and Salary Tools
- Application Archive and Documents
- Notion Sync Command Tests
- Security Guards and Privacy
- Freehire CLI Test Helpers
- LinkedIn CLI Test Helpers
- Pip Mascot Brand Identity
- Salary Entry Formatting
- Framework Version Checker
- Skill Linter Tool
- Jobindex Search Quirks
- Upstream Update and PR Process
- README Asset Tests
- Validate Flag Preflight Tests
- Gemini Research Agent
- Upstream Update Checker
- Refactored Company Search Tests
- LaTeX Install Prerequisites
- Custom Template Registration
- Competency Expansion Discovery
- CI Python Tool Tests
- Profile Reset Command
- Vulnerability Reporting Policy

## God Nodes (most connected - your core abstractions)
1. `match_score()` - 25 edges
2. `search_company()` - 21 edges
3. `run_guards()` - 20 edges
4. `DetectColumnTypeTests` - 18 edges
5. `parse_sheet()` - 18 edges
6. `/apply Command` - 16 edges
7. `compilerOptions` - 15 edges
8. `compilerOptions` - 15 edges
9. `compilerOptions` - 15 edges
10. `compilerOptions` - 15 edges

## Surprising Connections (you probably didn't know these)
- `gemini-research-expert Agent` --semantically_similar_to--> `Cloudflare Block -> WebSearch Fallback`  [INFERRED] [semantically similar]
  .claude/agents/gemini-research-expert.md → .agents/skills/jobbank-search/SKILL.md
- `CI job: Compile example CV and cover letter` --semantically_similar_to--> `Compiled PDF Verification (mandatory)`  [INFERRED] [semantically similar]
  .github/workflows/ci.yml → CLAUDE.md
- `salary_lookup.py Benchmark Tool` --semantically_similar_to--> `pdftotext as an Optional Dependency`  [INFERRED] [semantically similar]
  tools/README_SALARY_TOOL.md → SETUP.md
- `gmail_sync/state.json Idempotency State` --semantically_similar_to--> `seen_jobs.json Dedup Store`  [INFERRED] [semantically similar]
  .claude/commands/gmail-sync.md → .claude/skills/job-scraper/SKILL.md
- `Optional Salary Benchmarking Setup` --references--> `salary_data.json Data Format`  [AMBIGUOUS]
  SETUP.md → tools/README_SALARY_TOOL.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Job-Portal Search Skill Family (search + detail, bun CLI, fork context)** — _agents_skills_freehire_search_skill_freehire_search_skill, _agents_skills_linkedin_search_skill_linkedin_search_skill, _agents_skills_jobbank_search_skill_jobbank_search_skill, _agents_skills_jobdanmark_search_skill_jobdanmark_search_skill, _agents_skills_jobindex_search_skill_jobindex_search_skill, _agents_skills_jobnet_search_skill_jobnet_search_skill [EXTRACTED 1.00]
- **Shared CLI Contract: json|table|plain formats and stderr {error,code} exit 1** — _agents_skills_jobbank_search_cli_readme_error_envelope_contract, _agents_skills_freehire_search_cli_readme_freehire_cli, _agents_skills_jobdanmark_search_cli_readme_jobdanmark_cli, _agents_skills_jobindex_search_cli_readme_jobindex_cli, _agents_skills_jobnet_search_cli_readme_jobnet_cli, _agents_skills_linkedin_search_cli_readme_linkedin_cli [INFERRED 0.95]
- **Controlled-Vocabulary Resolution Before Search (facets, autocomplete, occupations, filter codes)** — _agents_skills_freehire_search_url_reference_jobs_facets_endpoint, _agents_skills_jobdanmark_search_cli_readme_autocomplete_endpoint, _agents_skills_jobdanmark_search_cli_readme_locations_endpoint, _agents_skills_jobnet_search_cli_readme_esco_occupation_search, _agents_skills_jobnet_search_cli_readme_typeahead_suggestions, _agents_skills_jobbank_search_cli_readme_filter_code_tables [INFERRED 0.85]
- **End-to-End Job Search Pipeline (scrape to outcome)** — _claude_skills_job_scraper_skill_job_scraper, _claude_commands_rank_rank, _claude_commands_apply_apply, _claude_commands_outcome_outcome, _claude_commands_interview_interview, _claude_commands_gmail_sync_gmail_sync [EXTRACTED 1.00]
- **Seven Reference Files of the job-application-assistant Skill** — _claude_skills_job_application_assistant_01_candidate_profile_candidate_profile, _claude_skills_job_application_assistant_02_behavioral_profile_behavioral_profile, _claude_skills_job_application_assistant_03_writing_style_writing_style_guide, _claude_skills_job_application_assistant_04_job_evaluation_job_evaluation_framework, _claude_skills_job_application_assistant_05_cv_templates_cv_templates_guide, _claude_skills_job_application_assistant_06_cover_letter_templates_cover_letter_guide, _claude_skills_job_application_assistant_07_interview_prep_interview_prep_guide [EXTRACTED 1.00]
- **Repo-Wide Never-Fabricate / Honest-Gap Invariant** — _claude_commands_apply_grounding_audit, _claude_commands_apply_requirement_coverage, _claude_commands_outcome_no_new_claims, _claude_commands_interview_consistency_brief, _claude_commands_rank_triage_scoring, _claude_skills_upskill_skill_never_fabricate_resources, _claude_skills_job_application_assistant_03_writing_style_interview_backtrack_test, _claude_commands_notion_sync_documents_never_leave [INFERRED 0.85]
- **CI pipeline jobs guarding the framework** — _github_workflows_ci_lint, _github_workflows_ci_security_guards, _github_workflows_ci_python_tests, _github_workflows_ci_dependency_review, _github_workflows_ci_latex_smoke, _github_workflows_ci_cli_checks, _github_workflows_ci_placeholder_integrity [EXTRACTED 1.00]
- **Core job-search lifecycle: setup -> scrape -> rank -> apply -> interview -> outcome -> calibration** — readme_setup_command, readme_scrape_command, readme_rank_command, readme_apply_command, readme_interview_command, readme_outcome_command [EXTRACTED 1.00]
- **Layered defenses for untrusted job-posting content** — security_threat_model, security_untrusted_input_rules, security_permission_allowlist, documents_readme_pasted_posting_trust_boundary, claude_verification_checklist [INFERRED 0.85]
- **Job-Application Delivery Persona (bird + necktie + envelope + flight loop)** — assets_mascot_pip_flight_loop_pip_mascot, assets_mascot_pip_flight_loop_business_necktie, assets_mascot_pip_flight_loop_carried_envelope, assets_mascot_pip_flight_loop_flight_loop_animation [INFERRED 0.85]

## Communities (76 total, 10 thin omitted)

### Community 0 - "Jobdanmark CLI Implementation"
Cohesion: 0.07
Nodes (25): autocomplete, AutocompleteGroup, AutocompleteItem, categories, Category, cleanText(), detail, DetailResult (+17 more)

### Community 1 - "Freehire CLI Implementation"
Cohesion: 0.10
Nodes (34): GET /api/v1/jobs/{slug}, ALIAS, commaList(), Flags, FlagValue, main(), parseFlags(), parseIntFlag() (+26 more)

### Community 2 - "Jobnet CLI Implementation"
Cohesion: 0.09
Nodes (20): detail, DetailApiResponse, formatDetailPlain(), outputPlain(), Occupation, OccupationAlias, occupations, buildSearchParams() (+12 more)

### Community 3 - "Security Guard Tests"
Cohesion: 0.11
Nodes (15): CleanTreeTests, GitignoreGuardTests, GitignoreNegationTests, GuardRepoFixture, ManifestGuardTests, PermissionGuardTests, CompletedProcess, Path (+7 more)

### Community 4 - "Jobindex CLI Implementation"
Cohesion: 0.11
Nodes (22): buildUrl(), decodeHtmlEntities(), detail, DetailResult, extractIdFromUrl(), numericEntity(), parseDetailPage(), stripTags() (+14 more)

### Community 5 - "LinkedIn CLI Implementation"
Cohesion: 0.14
Nodes (23): Flags, main(), parseFlags(), DetailOpts, normalizeId(), runDetail(), buildUrl(), renderTable() (+15 more)

### Community 6 - "Salary Excel Converter Tests"
Cohesion: 0.13
Nodes (11): DetectColumnTypeTests, FakeWorksheet, detect_column_type(), header_matches(), main(), parse_sheet(), Return True when a header contains a meaningful pattern match.      Patterns m, Remove count/index words from a header to derive a category name. (+3 more)

### Community 7 - "Jobbank CLI Package Manifest"
Cohesion: 0.08
Nodes (25): bin, jobbank, dependencies, @bunli/core, @bunli/utils, node-html-parser, zod, description (+17 more)

### Community 8 - "Jobbank CLI Commands"
Cohesion: 0.14
Nodes (14): detail, search, extractCdata(), extractJobIdFromUrl(), extractLink(), fetchWithUA(), findJobPosting(), ParsedDescription (+6 more)

### Community 9 - "Jobdanmark CLI Package Manifest"
Cohesion: 0.08
Nodes (25): bin, jobdanmark, dependencies, @bunli/core, @bunli/utils, node-html-parser, zod, description (+17 more)

### Community 10 - "Jobindex CLI Package Manifest"
Cohesion: 0.08
Nodes (25): bin, jobindex, dependencies, @bunli/core, @bunli/utils, node-html-parser, zod, description (+17 more)

### Community 11 - "Company Match Scoring Tests"
Cohesion: 0.11
Nodes (8): match_score(), Compute a match score between 0 and 100 for ranking results., MatchScoreTests, TestMatchScoreAnglicize, TestMatchScoreExactMatch, TestMatchScoreNoOverlap, TestMatchScoreShortQuery, TestMatchScoreSubstring

### Community 12 - "PDF Verification Tests"
Cohesion: 0.16
Nodes (12): Exception, ParsePageCountTests, RunToolTests, VerifyPdfTests, build_parser(), main(), normalize_text(), parse_page_count() (+4 more)

### Community 13 - "Template and Apply Contracts"
Cohesion: 0.13
Nodes (24): ACTIVE-TEMPLATE Managed Block, /add-template Command, Profile-Agnostic Placeholder Tokens, TEMPLATE.md Manifest, /apply Command, ATS and Keyword Verification (Step 5d), Factual Grounding Audit, Requirement Coverage (Matched or Honestly Gapped) (+16 more)

### Community 14 - "Jobbank TypeScript Config"
Cohesion: 0.08
Nodes (23): compilerOptions, lib, module, moduleResolution, noFallthroughCasesInSwitch, noImplicitAny, noUnusedLocals, noUnusedParameters (+15 more)

### Community 15 - "Jobdanmark TypeScript Config"
Cohesion: 0.08
Nodes (23): compilerOptions, lib, module, moduleResolution, noFallthroughCasesInSwitch, noImplicitAny, noUnusedLocals, noUnusedParameters (+15 more)

### Community 16 - "Jobindex TypeScript Config"
Cohesion: 0.08
Nodes (23): compilerOptions, lib, module, moduleResolution, noFallthroughCasesInSwitch, noImplicitAny, noUnusedLocals, noUnusedParameters (+15 more)

### Community 17 - "Jobnet CLI Package Manifest"
Cohesion: 0.08
Nodes (23): bin, jobnet, dependencies, @bunli/core, @bunli/utils, zod, description, devDependencies (+15 more)

### Community 18 - "Jobnet TypeScript Config"
Cohesion: 0.08
Nodes (23): compilerOptions, lib, module, moduleResolution, noFallthroughCasesInSwitch, noImplicitAny, noUnusedLocals, noUnusedParameters (+15 more)

### Community 19 - "Portal Generation and Setup Onboarding"
Cohesion: 0.12
Nodes (20): Access Rules Surfaced Not Bypassed, /add-portal Command, Mandatory Live Query Test, Portal-Skill Contract, url-reference.md Parsing Anchors, Zero Runtime Dependency Default, Mandatory Test Compile Gate, Tool-Agnostic Sync Contract (+12 more)

### Community 20 - "Freehire CLI Package Manifest"
Cohesion: 0.11
Nodes (17): bin, freehire-search, dependencies, description, devDependencies, @types/bun, typescript, @types/bun (+9 more)

### Community 21 - "LinkedIn CLI Package Manifest"
Cohesion: 0.11
Nodes (17): bin, linkedin-search, dependencies, description, devDependencies, @types/bun, typescript, @types/bun (+9 more)

### Community 22 - "Company Search Tests"
Cohesion: 0.30
Nodes (7): Search for a company by name. Returns matching entries sorted by relevance., search_company(), _entry(), _make_data(), TestSearchCompanyBasicMatch, TestSearchCompanyCityFilter, TestSearchCompanyScoreThreshold

### Community 23 - "Profile Expansion and Gmail Sync"
Cohesion: 0.15
Nodes (16): Additive-Only Source-Traceable Enrichment, /expand Command, Batch Approval Gate Before Any Write, /gmail-sync Command, Email Signal Classification Table, gmail_sync/state.json Idempotency State, Five Canonical Status Buckets, Calibration Handoff to /setup Path A (+8 more)

### Community 24 - "Interview Prep and Outcome Tracking"
Cohesion: 0.16
Nodes (16): 30-Day Staleness Flag, Consistency Brief (No Claim Off The Paper), /interview Command, Mock Interview Roleplay, Stage-Specific Prep Pack, Per-Application Archive Folder, Follow-Up Branch (10-Day Threshold, Max Two), Follow-Ups Make No New Claims (+8 more)

### Community 25 - "Salary Data Loading and Validation"
Cohesion: 0.20
Nodes (13): collect_validation_issues(), fail_data_error(), load_data(), main(), print_validation_report(), Validate the salary data shape before lookups use it.      Preserves historica, Load and JSON-parse salary_data.json; exit with a helpful message if missing/inv, Load, parse, and validate salary_data.json for lookups. (+5 more)

### Community 26 - "Fuzzy Name Matching Utilities"
Cohesion: 0.17
Nodes (11): anglicize(), extract_core_words(), match_score_optimized(), normalize(), Normalize string for robust fuzzy matching., Convert Danish/Nordic characters to anglicized equivalents., Extract meaningful words from a company name, ignoring noise., Compute a match score between 0 and 100 using precalculated query values. (+3 more)

### Community 27 - "Salary Data Shape Validation Tests"
Cohesion: 0.21
Nodes (3): Category-shape and duplicate-name checks (reuses assert_invalid_data)., ValidateDataShapeTests, ValidateDataTests

### Community 28 - "Reporting and Job Triage"
Cohesion: 0.19
Nodes (15): Mandatory HTML Escaping of CSV Values, /html-report Command, Self-Contained Offline Dashboard, Documents Never Leave The Machine, Job Search Pipeline Database Schema, Idempotent Upsert on Key, /notion-sync Command, Silently-Optional Connection Preflight (+7 more)

### Community 29 - "Portal Skill Design Patterns"
Cohesion: 0.18
Nodes (14): Location-as-Facet (region/country/city), FREEHIRE_API_URL Base-URL Override, freehire Search Skill, Hosted-Service Dependency (Best-Effort, No SLA), Job-Portal-Skill Pattern, Partial Facet Data / Unresolved Region Bucket, Tech-First Trigger Scoping, Exponential Backoff with Jitter on 429/5xx (+6 more)

### Community 30 - "Freehire TypeScript Config"
Cohesion: 0.14
Nodes (13): compilerOptions, allowImportingTsExtensions, module, moduleResolution, noEmit, skipLibCheck, strict, target (+5 more)

### Community 31 - "LinkedIn TypeScript Config"
Cohesion: 0.14
Nodes (13): compilerOptions, allowImportingTsExtensions, module, moduleResolution, noEmit, skipLibCheck, strict, target (+5 more)

### Community 32 - "HTML Report Command Tests"
Cohesion: 0.14
Nodes (8): HtmlReportCommandFileTests, HtmlReportGitignoreTests, HtmlReportLintIntegrationTests, Tests for the /html-report command and its gitignore rule.  Mirrors the patter, Structural checks on the command file itself., lint_skills.py rejects command files that don't start with '# /<name>'., reports/ must be gitignored — it holds personal generated output., lint_skills.py must pass after the command is added.

### Community 33 - "Skill Linter Tests"
Cohesion: 0.29
Nodes (5): LinterRepoFixture, CompletedProcess, Path, run_linter(), SettingsShapeTests

### Community 34 - "Jobdanmark API Endpoints"
Cohesion: 0.20
Nodes (11): GET /api/search/autocomplete, Filter Objects Require displayText, jobdanmark-cli, JSON-LD-First Detail Parse with Rendered-HTML Fallback, GET /api/search/locations, POST /api/jobsearch/search/{page}, Jobdanmark 10-Category Taxonomy, Jobdanmark Search Skill (+3 more)

### Community 35 - "Repo Governance and Funding"
Cohesion: 0.18
Nodes (11): Project Funding Channels (GitHub Sponsors + Ko-fi), Fork Base-Repository Warning, Portable Portal Search Skills Pointer, Thin-Pointer Design (Single Source of Truth), No Alternative-Harness Ports or Duplicate Workflow Sources, Community Forks & Adaptations Discussion (#78), Market-Specific Skills Live in Forks, The One Rule: This Repo Is a Universal Template (+3 more)

### Community 36 - "Untrusted Input and Command Bar"
Cohesion: 0.20
Nodes (11): The Bar for New Commands, Pasted Posting Trust Boundary, postings/ Manual Drop Folder, /apply drafter-reviewer workflow, Drafter-Reviewer Separation, /rank ranked shortlist triage, Relevance-Weighted CV Cutting, Token-Efficient Reviewer Dispatch (+3 more)

### Community 37 - "Freehire and LinkedIn API Contracts"
Cohesion: 0.20
Nodes (10): freehire-cli, Zero Runtime Dependencies (bun + fetch), freehire Job Object (public_slug schema), GET /api/v1/jobs/search, public_slug as Stable Public Identifier, stderr Error Envelope Contract ({error, code}, exit 1), linkedin-cli, data-entity-urn Job Card Parsing (+2 more)

### Community 38 - "Jobbank and Jobindex Scraping"
Cohesion: 0.20
Nodes (10): Jobbank Numeric Filter Code Tables (cvtype/amt/erf/udd/branche), jobbank-cli, Schema.org JobPosting JSON-LD Extraction, RSS Description Parse Strategy (' hos ' split), RSS 100-Item Cap (no pagination), Jobbank Job Card CSS Extraction (div.job-item), Jobbank RSS Feed URL (/job/rss), Jobbank Search URL Pattern (+2 more)

### Community 39 - "CI Fork-Safety and PDF Checks"
Cohesion: 0.22
Nodes (10): CI job: Dependency review (upstream PRs only), Fork-Friendly CI Design, CI job: Compile example CV and cover letter, CI job: Placeholder integrity (upstream template only), Candidate Profile (placeholder template), Compiled PDF Verification (mandatory), Workflow for New Job Applications, CV/Cover Letter Verification Checklist (+2 more)

### Community 41 - "Jobbank CLI Contract Tests"
Cohesion: 0.28
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 42 - "Jobnet API Constraints"
Cohesion: 0.25
Nodes (8): incrementViews=false on Detail Fetch, jobnet-cli, Search Omits HTML Description for Brevity, x-csrf: 1 Required Header, Mutually Exclusive Geographic Search Modes (region vs postal+radius), Jobnet-Search Skill, Order-Matches-Intent (PublicationDate/BestMatch/ApplicationDate), STAR Official Danish Government Job Portal

### Community 43 - "LaTeX Compile and Page Budgets"
Cohesion: 0.29
Nodes (8): Compile and Inspect PDFs (Step 5), CV Compile-and-Inspect Loop, needspace Orphaned cventry Fix, Relevance-Weighted Cutting, Hard 2-Page Budget, cover.cls XeLaTeX Document Class, lettercontent/itemize Compile Pitfall, Hard 1-Page / 250-300 Word Budget

### Community 44 - "Drafter-Reviewer Scoring Workflow"
Cohesion: 0.25
Nodes (8): Drafter-Reviewer Two-Agent Workflow, Part A / Part B Reviewer Feedback Protocol, Token-Efficiency Rules (Inline Drafts, No Re-Reads), Parallel Scoring Agents (~5 Jobs Each), Mapping Behavior to Job Posting Language, Motivation Filter (Energize vs Drain), Five Scoring Dimensions, Weighting and Verdict Thresholds

### Community 45 - "Skill Gap and Learning Plan"
Cohesion: 0.29
Nodes (8): Deduplicated Competency Map, Direct Lookup Plus Inference (Approaches A and B), Fit-Weighted Hard Skill Diff (Pass 1), Gap Heatmap, Learning Plan and Study Order, LLM Synthesis of Missed Gaps (Pass 2), Never Fabricate Study Resources, upskill Skill (/upskill)

### Community 46 - "CI Checks and Changelog"
Cohesion: 0.25
Nodes (8): CI job: CLI checks (Bun typecheck + fixture tests), No Live Portal Requests in CI, Keep a Changelog 1.1.0, Release 1.0.0 Baseline, Semantic Versioning 2.0.0, Portal-Skill Contract, freehire-search portal skill, linkedin-search portal skill

### Community 47 - "Jobdanmark CLI Contract Tests"
Cohesion: 0.32
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 48 - "Jobindex CLI Contract Tests"
Cohesion: 0.32
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 49 - "Jobnet CLI Contract Tests"
Cohesion: 0.32
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 50 - "ATS Verification and Salary Tools"
Cohesion: 0.25
Nodes (8): ATS & Keyword Verification of the CV Text Layer, ATS Verification on the PDF Text Layer, pdftotext as an Optional Dependency, Optional Salary Benchmarking Setup, convert_salary_excel.py Excel-to-JSON Converter, Company Name Fuzzy Matcher, salary_data.json Data Format, salary_lookup.py Benchmark Tool

### Community 51 - "Application Archive and Documents"
Cohesion: 0.29
Nodes (8): applications/<company>_<role>/ Archive Layout, documents/ Career Source Materials Folder, outcome.md Status Format, /gmail-sync application status detection, /interview stage-specific prep pack, /outcome result recording and archiving, Profile Depth Matters, /setup profile onboarding

### Community 53 - "Security Guards and Privacy"
Cohesion: 0.33
Nodes (7): CI job: Security guards (permissions, gitignore, manifests), /html-report offline tracker dashboard, /notion-sync one-way pipeline view, Claude Code Permission Allowlist, Personal Data Boundaries, Threat Model, Honestly Stated, Stale .claude/settings.local.json From an Older Clone

### Community 54 - "Freehire CLI Test Helpers"
Cohesion: 0.33
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 55 - "LinkedIn CLI Test Helpers"
Cohesion: 0.33
Nodes (3): CLI_PATH, CLIResult, runCLI()

### Community 56 - "Pip Mascot Brand Identity"
Cohesion: 0.48
Nodes (7): AI Job Search Brand Identity Asset, Necktie Detail (Professional Job-Seeker Cue), Carried Sealed Envelope (Application Letter Prop), Carrier-Pigeon Delivery Metaphor, Looping Flight Animation (Wing-Flap Cycle), Pip - Project Mascot, Pixel-Art Visual Style (Teal Palette, Transparent Background)

### Community 57 - "Salary Entry Formatting"
Cohesion: 0.43
Nodes (3): format_entry(), Format a single company entry for display., FormatEntryTests

### Community 58 - "Framework Version Checker"
Cohesion: 0.57
Nodes (6): get_base_commit(), has_non_trivial_changes(), main(), parse_frontmatter(), Path, run_git()

### Community 59 - "Skill Linter Tool"
Cohesion: 0.62
Nodes (6): check_command(), check_settings(), check_skill(), main(), Path, rel()

### Community 60 - "Jobindex Search Quirks"
Cohesion: 0.33
Nodes (6): hitcount_html Total Parsing (Danish dot-thousands), jobindex-cli, GET /jobsoegning.json, City-in-Query Workaround for Missing Area Filter, Jobindex Search Skill, UI-Only Filters (employment type, hours, remote)

### Community 61 - "Upstream Update and PR Process"
Cohesion: 0.40
Nodes (6): PR Verification Section, CI job: Lint skills, commands, settings, framework_version Frontmatter Marker, Prefer Tagged Releases Over Raw master, Claims Get Verified (reproduce on the real path), Pulling Upstream Updates Into Your Fork

### Community 64 - "Gemini Research Agent"
Cohesion: 0.40
Nodes (5): Browser User-Agent Header, Cloudflare Block -> WebSearch Fallback, gemini-research-expert Agent, Headless Gemini CLI Research (gemini -p), Prompt-Formulate / Execute / Synthesize / QA Methodology

### Community 65 - "Upstream Update Checker"
Cohesion: 0.70
Nodes (4): get_framework_version_from_text(), main(), parse_semver(), run_git()

### Community 67 - "LaTeX Install Prerequisites"
Cohesion: 0.67
Nodes (3): Basic MiKTeX Silent Auto-Install Configuration, Minimal TeX Install (TinyTeX/BasicTeX) Package Set, Setup Prerequisites (Claude Code, Python, Bun, LaTeX)

## Ambiguous Edges - Review These
- `Optional Salary Benchmarking Setup` → `salary_data.json Data Format`  [AMBIGUOUS]
  SETUP.md · relation: references
- `Looping Flight Animation (Wing-Flap Cycle)` → `AI Job Search Brand Identity Asset`  [AMBIGUOUS]
  assets/mascot/pip_flight_loop.gif · relation: conceptually_related_to

## Knowledge Gaps
- **254 isolated node(s):** `name`, `version`, `description`, `type`, `main` (+249 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Optional Salary Benchmarking Setup` and `salary_data.json Data Format`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Looping Flight Animation (Wing-Flap Cycle)` and `AI Job Search Brand Identity Asset`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `freehire-cli` connect `Freehire and LinkedIn API Contracts` to `Freehire CLI Implementation`, `Portal Skill Design Patterns`?**
  _High betweenness centrality (0.006) - this node is a cross-community bridge._
- **Why does `GET /api/v1/jobs/{slug}` connect `Freehire CLI Implementation` to `Freehire and LinkedIn API Contracts`?**
  _High betweenness centrality (0.005) - this node is a cross-community bridge._
- **What connects `name`, `version`, `description` to the rest of the system?**
  _254 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Jobdanmark CLI Implementation` be split into smaller, more focused modules?**
  _Cohesion score 0.07030527289546716 - nodes in this community are weakly interconnected._
- **Should `Freehire CLI Implementation` be split into smaller, more focused modules?**
  _Cohesion score 0.0966183574879227 - nodes in this community are weakly interconnected._