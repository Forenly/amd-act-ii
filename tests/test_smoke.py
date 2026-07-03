"""Smoke test — end-to-end sanity: this repo's Conductor workflow(s) are
actually registered on the running Conductor. Skips when Conductor is down."""
import json
import urllib.request
from conftest import workflow_names


def test_workflow_registered(require_conductor, conductor_url):
    registered = {w["name"] for w in json.load(
        urllib.request.urlopen(f"{conductor_url}/api/metadata/workflow", timeout=6))}
    for name in workflow_names():
        assert name in registered, (
            f"workflow '{name}' defined in repo but not registered on Conductor "
            f"(run: python conductor/register.py)")


def test_repo_declares_a_workflow():
    assert workflow_names(), "repo must declare at least one Conductor workflow"
