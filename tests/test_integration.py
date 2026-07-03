"""Integration tests — hit the live Conductor + Label Studio APIs.
Skip automatically when services are unreachable (CI), run on the box."""
import json
import urllib.request


def _get(url, timeout=6):
    return json.load(urllib.request.urlopen(url, timeout=timeout))


def test_conductor_api_reachable(require_conductor, conductor_url):
    d = _get(f"{conductor_url}/api/metadata/workflow")
    assert isinstance(d, list), "Conductor /metadata/workflow should return a list"


def test_label_studio_api_reachable(require_ls, ls_url):
    # LS root responds (auth-gated endpoints need a token; a live socket + HTTP is enough here)
    import urllib.error
    try:
        urllib.request.urlopen(f"{ls_url}/version", timeout=6)
    except urllib.error.HTTPError as e:
        assert e.code in (200, 401, 403), f"unexpected LS status {e.code}"
