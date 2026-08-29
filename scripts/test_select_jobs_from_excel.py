"""Tests for the Excel job-selection helper used by /apply_from_excel."""

from __future__ import annotations

from pathlib import Path

import pytest
from export_jobs_xlsx import export

from select_jobs_from_excel import filter_by_threshold, load_findings, main, resolve_workbook_path


@pytest.fixture
def report() -> dict:
    return {
        "run_date": "2026-08-17",
        "focus": "Test fixture",
        "portals_run": ["linkedin-search"],
        "portals_skipped": [],
        "portal_health": [],
        "jobs": [
            {
                "fit": "High",
                "title": "Senior Backend Engineer",
                "company": "Alpha",
                "location": "Pune, India",
                "location_tier": "Tier 1",
                "posted": "within 14 days",
                "track": "Backend",
                "seniority": "Senior - one level above band",
                "notes": "Strong stack match.",
                "url": "https://example.com/alpha",
            },
            {
                "fit": "Medium",
                "title": "AI Engineer",
                "company": "Beta",
                "location": "Bengaluru, India",
                "location_tier": "Tier 2",
                "posted": "within 14 days",
                "track": "AI",
                "seniority": "Unprefixed - likely in band",
                "notes": "Adjacent match.",
                "url": "https://example.com/beta",
            },
            {
                "fit": "Low",
                "title": "QA Engineer",
                "company": "Gamma",
                "location": "Mumbai, India",
                "location_tier": "Tier 2",
                "posted": "within 14 days",
                "track": "Unclear",
                "seniority": "Unprefixed",
                "notes": "Weak match.",
                "url": "https://example.com/gamma",
            },
        ],
        "observations": [],
    }


@pytest.fixture
def workbook(report, tmp_path) -> Path:
    return export(report, tmp_path / "job_findings_2026-08-17.xlsx")


def test_load_findings_reads_every_row(workbook):
    jobs = load_findings(workbook)
    assert [j["company"] for j in jobs] == ["Alpha", "Beta", "Gamma"]


def test_load_findings_extracts_hyperlink_target_not_label(workbook):
    jobs = load_findings(workbook)
    assert jobs[0]["url"] == "https://example.com/alpha"


def test_filter_by_threshold_high_keeps_only_high():
    jobs = [{"fit": "High"}, {"fit": "Medium"}, {"fit": "Low"}]
    assert [j["fit"] for j in filter_by_threshold(jobs, "High")] == ["High"]


def test_filter_by_threshold_medium_keeps_high_and_medium():
    jobs = [{"fit": "High"}, {"fit": "Medium"}, {"fit": "Low"}]
    assert [j["fit"] for j in filter_by_threshold(jobs, "Medium")] == ["High", "Medium"]


def test_filter_by_threshold_low_keeps_everything():
    jobs = [{"fit": "High"}, {"fit": "Medium"}, {"fit": "Low"}]
    assert len(filter_by_threshold(jobs, "Low")) == 3


def test_filter_by_threshold_is_case_insensitive():
    jobs = [{"fit": "High"}, {"fit": "Medium"}]
    assert [j["fit"] for j in filter_by_threshold(jobs, "medium")] == ["High", "Medium"]


def test_filter_by_threshold_rejects_unknown_value():
    with pytest.raises(ValueError):
        filter_by_threshold([{"fit": "High"}], "Excellent")


def test_resolve_workbook_path_appends_xlsx_extension(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    reports_dir = tmp_path / "out" / "reports"
    reports_dir.mkdir(parents=True)
    (reports_dir / "job_findings_2026-08-17.xlsx").write_bytes(b"")
    resolved = resolve_workbook_path("job_findings_2026-08-17")
    assert resolved == Path("out/reports/job_findings_2026-08-17.xlsx")


def test_resolve_workbook_path_leaves_explicit_path_alone(tmp_path):
    explicit = tmp_path / "custom" / "report.xlsx"
    assert resolve_workbook_path(str(explicit)) == explicit


def test_main_prints_filtered_jobs_as_json(workbook, capsys):
    assert main([str(workbook), "--threshold", "High"]) == 0
    out = capsys.readouterr().out
    assert '"company": "Alpha"' in out
    assert "Beta" not in out


def test_main_returns_error_for_missing_workbook(tmp_path, capsys):
    assert main([str(tmp_path / "nope.xlsx")]) == 1
    assert "no such workbook" in capsys.readouterr().err


def test_main_returns_error_for_bad_threshold(workbook, capsys):
    assert main([str(workbook), "--threshold", "Excellent"]) == 1
    assert "unknown threshold" in capsys.readouterr().err
