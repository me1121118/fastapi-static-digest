import os
import tempfile
import pytest
from fastapi_static_digest import StaticDigest

def test_static_digest():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "style.css")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("body { background: #000; }")

        digest_mgr = StaticDigest(directory=tmpdir)
        url = digest_mgr.url_for("style.css", prefix="/static")
        assert url.startswith("/static/style.")
        assert url.endswith(".css")
        assert url != "/static/style.css"
