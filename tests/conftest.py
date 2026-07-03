"""Shared test fixtures. Integration/smoke tests skip gracefully when the
Conductor / Label Studio services are not reachable (e.g. in GitHub CI),
so unit tests stay green everywhere and the live tests run on the box."""
import os, socket, glob, json
from urllib.parse import urlparse
import pytest

CONDUCTOR_URL = os.environ.get("CONDUCTOR_URL", "http://localhost:8000")
LS_URL = os.environ.get("LS_URL", "http://localhost:8085")


def _reachable(url, timeout=2.0):
    u = urlparse(url)
    port = u.port or (443 if u.scheme == "https" else 80)
    try:
        with socket.create_connection((u.hostname, port), timeout=timeout):
            return True
    except OSError:
        return False


def workflow_defs():
    return sorted(glob.glob("conductor/*_def.json"))


def workflow_names():
    names = []
    for f in workflow_defs():
        try:
            names.append(json.load(open(f))["name"])
        except Exception:
            pass
    return names


@pytest.fixture(scope="session")
def conductor_url():
    return CONDUCTOR_URL


@pytest.fixture(scope="session")
def ls_url():
    return LS_URL


@pytest.fixture
def require_conductor():
    if not _reachable(CONDUCTOR_URL):
        pytest.skip(f"Conductor not reachable at {CONDUCTOR_URL}")


@pytest.fixture
def require_ls():
    if not _reachable(LS_URL):
        pytest.skip(f"Label Studio not reachable at {LS_URL}")
