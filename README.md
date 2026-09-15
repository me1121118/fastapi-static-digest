# fastapi-static-digest

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-static-digest/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Cache-busting static file server and manifest generator for FastAPI with immutable HTTP headers.

---

## 🚀 Features

- ⚡ **Cache-Busting Hashes**: Computes short SHA-256 digests for static assets (`main.a1b2c3d4.css`).
- 🚀 **1-Year Immutable Caching**: Automatically serves fingerprinted files with `Cache-Control: public, max-age=31536000, immutable`.
- 📁 **Manifest Generator**: Simple template helper function `static_url("app.js")` resolves hashed URLs.

---

## 📦 Installation

```bash
pip install fastapi-static-digest
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI
from fastapi_static_digest import StaticDigest

app = FastAPI()
static = StaticDigest(directory="static")
static.mount_to(app, path="/static")

# In templates or endpoints:
print(static.url_for("styles.css"))  # /static/styles.8f3a9e1b.css
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this cache-busting tool accelerated your frontend delivery, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
