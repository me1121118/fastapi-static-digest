import os
import hashlib
from typing import Dict
from starlette.staticfiles import StaticFiles
from starlette.responses import Response

class StaticDigest:
    """Manages static asset cache-busting with content hashes and immutable headers."""

    def __init__(self, directory: str):
        self.directory = directory
        self.manifest: Dict[str, str] = {}
        self._build_manifest()

    def _build_manifest(self) -> None:
        if not os.path.exists(self.directory):
            return
        for root, _, files in os.walk(self.directory):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.directory).replace("\\", "/")
                with open(full_path, "rb") as f:
                    content = f.read()
                digest = hashlib.sha256(content).hexdigest()[:8]
                base, ext = os.path.splitext(rel_path)
                hashed_rel = f"{base}.{digest}{ext}"
                self.manifest[rel_path] = hashed_rel

    def url_for(self, filename: str, prefix: str = "/static") -> str:
        hashed = self.manifest.get(filename, filename)
        return f"{prefix.rstrip('/')}/{hashed.lstrip('/')}"
