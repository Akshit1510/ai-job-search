# /apply_from_excel - Batch-Apply from a Job-Findings Workbook

You are running the full `/apply` Drafter-Reviewer workflow against every posting in a
job-findings workbook (produced by `/scrape`'s Step 5.5 export) that meets a minimum fit
threshold. `/apply_from_excel` is a **loop around `/apply`**, not a replacement for it -
every posting still gets the complete 6-step workflow (fit evaluation, drafting, review,
revision, PDF compile+inspect, verification) defined in `.claude/commands/apply.md`.

This is a **long-running, multi-job batch operation** - each posting costs roughly what one
full `/apply` run costs (an evaluation, a reviewer agent dispatch, two LaTeX compiles, PDF
reads). Always show the filtered list and its count before starting, and get one explicit
go-ahead for the whole batch - never start drafting without it.

---

## Step 0: Parse Input

`$ARGUMENTS` is expected as `<excel-name> <threshold>`, e.g.:
- `/apply_from_excel job_findings_2026-08-17.xlsx High`
- `/apply_from_excel job_findings_2026-08-17 Medium`

Parsing rules:
- **Excel name**: a bare filename (no `out/reports/` prefix, `.xlsx` optional) resolves under
  `out/reports/`. An explicit path is used as-is. `scripts/select_jobs_from_excel.py` handles
  both cases.
- **Threshold**: one of `High`, `Medium`, `Low` (case-insensitive). Meaning: include every row
  whose `Fit` is at least this good - `High` includes only High, `Medium` includes High+Medium,
  `Low` includes everything. This mirrors the ordinal used by the exporter (`FIT_ORDER` in
  `scripts/export_jobs_xlsx.py`).
- If either argument is missing or the threshold isn't one of the three values, use
  `AskUserQuestion` to get it - do not guess a workbook name or default the threshold silently.

---

## Step 1: Load & Filter the Workbook

Run the selector script with the project's dedicated venv (per `CLAUDE.md`, never system Python):

```bash
D:/programming/pythonEnvs/ai-job-search/Scripts/python.exe scripts/select_jobs_from_excel.py <excel-name> --threshold <threshold>
```

This prints a single JSON object: `{"workbook": "<resolved path>", "threshold": "<Level>", "jobs": [...]}`,
where each job carries `fit`, `title`, `company`, `location`, `location_tier`, `track`,
`seniority`, `notes`, `url`.

If the script exits non-zero (missing workbook, bad threshold, or the workbook has no
`Findings` sheet), show the error and stop - do not fall back to guessing at the file.

---

## Step 2: Exclude Already-Applied and Already-Drafted Jobs

Before presenting anything, narrow the list:

1. Read `job_search_tracker.csv` (if it exists). Drop any job whose company+title already
   appears there - it has been applied to or consciously tracked, same exclusion rule
   `/rank` uses.
2. For each remaining job, check whether `out/applications/<company>_<role>/` already exists
   (derive the folder name the same way `/apply` Step 2 does). If it exists, drop the job and
   note it separately - re-drafting would silently overwrite prior work, and that decision
   belongs to the user, not this loop.
3. If a job's URL is a duplicate of another job already in the list (can happen if the same
   posting appears twice in the workbook), keep only one.

---

## Step 3: Confirm the Batch

Present the final list before doing anything else:

```
## Apply-from-Excel - <workbook name>, threshold: <Level>

<N> postings match (Fit >= <Level>), after excluding <A> already-applied and <B> already-drafted.

| # | Fit | Title | Company | Location | URL |
|---|-----|-------|---------|----------|-----|
| 1 | High | ... | ... | ... | [Link](...) |

Excluded (already applied): <list, or "none">
Excluded (already drafted, folder exists): <list, or "none">

This will run the full /apply workflow (evaluation → draft → review → revise → compile →
verify) for each of the <N> postings above, sequentially. That's roughly <N> full
application cycles - expect this to take a while.
```

Then ask explicitly: **"Proceed with all <N>? You can also give me a smaller subset by number."**

Do not proceed without an explicit go-ahead. If the user gives a subset, use only those.

---

## Step 4: Run `/apply` for Each Job, Sequentially

For each job in the confirmed list, in the order presented (High fit first):

1. Announce which job is starting: `Starting <#>/<N>: <Title> at <Company>`.
2. Run the **complete** `.claude/commands/apply.md` workflow with the job's `url` as
   `$ARGUMENTS` - Steps 0 through 6 exactly as that command defines them, including the
   mandatory PDF compile-and-inspect step (Step 5) and the verification checklist (Step 6).
3. **Skip the interactive "Should I proceed with drafting?" pause from `/apply` Step 1.**
   The user already made that call by setting the fit threshold and confirming the batch in
   Step 3 above - stopping to ask again for every single job would defeat the purpose of a
   batch command. Instead:
   - Run the Step 1 fit evaluation in full and keep its output.
   - If the evaluation surfaces a **hard deal-breaker that the workbook's quick fit label
     couldn't have caught** - an explicit location FAIL requiring unsponsored relocation, a
     stated comp figure below the recorded floor, or a confirmed service/staffing body-shop -
     **stop that job, do not draft**, log it under "Skipped (deal-breaker found on full
     evaluation)" in the final summary, and move to the next job.
   - Otherwise, continue straight into Step 2 (drafting) without pausing.
4. After each job finishes (or is skipped), record its outcome: company, role, verdict
   (drafted / skipped + reason), and the output file paths if drafted.
5. If a job's `/apply` run fails outright (compile error that can't be resolved, dead
   posting URL, WebFetch failure), log it as failed with the reason and continue to the next
   job - one bad posting must not abort the whole batch.

---

## Step 5: Final Summary

After the loop finishes (or is interrupted), report:

```
## Apply-from-Excel Complete - <workbook name>, threshold: <Level>

Processed <N> postings: <D> drafted, <S> skipped (deal-breaker), <F> failed.

### Drafted
| Company | Title | Files |
|---------|-------|-------|
| ... | ... | out/applications/<company>_<role>/{main,cover}_<company>_<role>.pdf |

### Skipped (deal-breaker found on full evaluation)
- <Company> - <Title>: <reason>

### Failed
- <Company> - <Title>: <reason>
```

Close with the same next-step prompt `/apply` itself uses per drafted job: submitted ones
go through `/outcome <company>`, interview-stage ones through `/interview`.

---

## Important Rules

1. **Never skip a step of `/apply` itself.** This command loops the workflow; it does not
   abbreviate it. Every drafted job still gets the reviewer agent, the mandatory PDF
   compile-and-inspect, and the full verification checklist.
2. **One confirmation for the whole batch, not one per job.** Step 3's confirmation is what
   authorizes skipping `/apply`'s own per-job "should I proceed" pause. Without that batch
   confirmation, do not draft anything.
3. **A full evaluation can still veto a workbook fit label.** The workbook's Fit column is a
   quick signal from `/scrape`; `/apply` Step 1's evaluation (with company research) is
   authoritative. When they disagree on a genuine deal-breaker, the full evaluation wins and
   the job is skipped, not forced through.
4. **Never overwrite an existing application folder.** A job whose `out/applications/<company>_<role>/`
   already exists is excluded in Step 2 and reported, not silently redrafted.
5. **One bad posting does not stop the batch.** Compile errors, dead links, or fetch failures
   on one job are logged and the loop continues to the next.
6. **Read the venv path from `CLAUDE.md`, never assume system Python.** Same rule the
   `/scrape` Step 5.5 export follows.
