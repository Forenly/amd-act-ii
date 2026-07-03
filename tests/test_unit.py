"""Unit tests — pure, no network. Always run (green in CI).
Validate repo hygiene + the Conductor workflow definition(s) are well-formed."""
import os, json
from conftest import workflow_defs


def _flatten(tasks):
    out = []
    for t in tasks:
        out.append(t)
        if t.get("type") == "FORK_JOIN":
            for branch in t.get("forkTasks", []):
                out.extend(_flatten(branch))
        for case in (t.get("decisionCases") or {}).values():
            out.extend(_flatten(case))
        out.extend(_flatten(t.get("defaultCase") or []))
        out.extend(_flatten(t.get("loopOver") or []))
    return out


def test_repo_has_readme():
    assert os.path.exists("README.md"), "repo must have README.md"


def test_has_workflow_def():
    assert workflow_defs(), "expected at least one conductor/*_def.json"


def test_workflow_defs_wellformed():
    for f in workflow_defs():
        d = json.load(open(f))
        assert d.get("name"), f"{f}: missing name"
        assert d.get("tasks"), f"{f}: missing tasks"
        assert d.get("schemaVersion") == 2, f"{f}: expected schemaVersion 2"
        assert d.get("ownerEmail"), f"{f}: missing ownerEmail"


def test_task_reference_names_unique():
    for f in workflow_defs():
        d = json.load(open(f))
        refs = [t["taskReferenceName"] for t in _flatten(d["tasks"])]
        assert len(refs) == len(set(refs)), f"{f}: duplicate taskReferenceName {refs}"


def test_join_targets_exist():
    """Every JOIN.joinOn must reference a task that exists in the def."""
    for f in workflow_defs():
        d = json.load(open(f))
        all_refs = {t["taskReferenceName"] for t in _flatten(d["tasks"])}
        for t in _flatten(d["tasks"]):
            if t.get("type") == "JOIN":
                for j in t.get("joinOn", []):
                    assert j in all_refs, f"{f}: JOIN references unknown task '{j}'"
