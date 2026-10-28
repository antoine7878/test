from fastapi.testclient import TestClient


def test_index(client: TestClient) -> None:
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]
    assert "/static/js/htmx.min.js" in r.text


def test_current_time_partial(client: TestClient) -> None:
    r = client.get("/partials/time", headers={"HX-Request": "true"})
    assert r.status_code == 200
    assert r.text.startswith("<time")


def test_htmx_static(client: TestClient) -> None:
    r = client.get("/static/js/htmx.min.js")
    assert r.status_code == 200
