# 🛡️ WebScout

**Web Application Vulnerability & Technology Scanner**

> Built by [Mursalin](https://github.com/themursalin) · Python · CLI + HTML Reports

---

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Topic-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

WebScout is an open-source reconnaissance and vulnerability assessment tool designed to fingerprint web technologies, audit HTTP security headers, and surface known CVEs for detected libraries and frameworks — all from a single Python script.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Technology Detection** | Fingerprints 30+ technologies: JS frameworks, CMS, web servers, CDNs |
| 🏷️ **Version Extraction** | Extracts version numbers from HTML, scripts, headers, and meta tags |
| 🔐 **Security Header Audit** | Checks for HSTS, CSP, X-Frame-Options, CORP, and more |
| 💣 **Vulnerability Matching** | Cross-references detected versions against a curated CVE database |
| 🍪 **Cookie Analysis** | Audits cookies for Secure, HttpOnly, and SameSite flags |
| 📋 **Multiple Output Formats** | Terminal (colored), JSON, and full HTML report |
| 🎨 **Clean CLI Interface** | Minimal, readable output with ANSI colors |

---

## 📁 Project Structure

```
webscout/
├── main.py                      # CLI entry point
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
├── webscout/
│   ├── __init__.py
│   ├── scanners/
│   │   ├── signatures.py        # Technology fingerprint database
│   │   ├── tech_detector.py     # HTML/header/script fingerprinting
│   │   ├── header_analyzer.py   # Security header auditor
│   │   └── vuln_checker.py      # CVE cross-reference engine
│   ├── reporters/
│   │   └── report_builder.py    # Text / JSON / HTML report assembly
│   └── utils/
│       ├── banner.py            # CLI banner
│       ├── http_client.py       # Requests wrapper
│       └── logger.py            # Logging configuration
├── tests/
│   └── test_scanners.py         # Unit tests (pytest)
└── docs/
    └── ARCHITECTURE.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/mursalin/webscout.git
cd webscout
pip install -r requirements.txt
```

### Usage

```bash
# Basic scan (colored terminal output)
python main.py https://example.com

# Save as JSON
python main.py https://example.com -o json -f report.json

# Save as HTML report
python main.py https://example.com -o html -f report.html

# Custom timeout and user-agent
python main.py https://example.com --timeout 15 --user-agent "MyScanner/1.0"

# Suppress banner
python main.py https://example.com --no-banner
```

---

## 🖥️ Sample Output

```
 ██╗    ██╗███████╗██████╗ ███████╗ ██████╗ ██╗   ██╗████████╗
 ...

  Crafted by Mursalin · github.com/mursalin/webscout
  v1.0.0  |  Use responsibly & only on authorized targets
────────────────────────────────────────────────────────────────────────

  WEBSCOUT SCAN REPORT
──────────────────────────────────────────────────────────────────────
  Target   : https://example.com
  Scanned  : 2025-01-15 14:32:00 UTC
  Status   : 200
  TLS/HTTPS: ✅ Yes

  [1] DETECTED TECHNOLOGIES

  CMS
    • WordPress  v6.2.1
  JavaScript Library
    • jQuery  v3.6.0
  Web Server
    • Nginx  v1.18.0

  [2] HTTP SECURITY HEADERS
  Missing headers (3):
    🟠 [HIGH]   Content-Security-Policy
    🟡 [MEDIUM] X-Frame-Options
    🔵 [LOW]    Referrer-Policy

  [3] VULNERABILITY FINDINGS

  🟠 [HIGH]  jQuery v3.6.0
     CVE:          CVE-2020-11022
     Description:  XSS vulnerability via passing HTML containing <option> elements.
     Fix version:  3.5.0
```

---

## ⚙️ Configuration

All options are passed via CLI flags:

| Flag | Default | Description |
|---|---|---|
| `url` | *(required)* | Target URL |
| `-o, --output` | `text` | Output format: `text`, `json`, `html` |
| `-f, --file` | *(stdout)* | Output filename |
| `--timeout` | `10` | Request timeout (seconds) |
| `--user-agent` | WebScout/1.0 | HTTP User-Agent |
| `--no-banner` | False | Suppress the ASCII banner |

---

## 🧪 Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## 🗺️ Roadmap

- [ ] Integrate with [NVD API](https://nvd.nist.gov/developers/vulnerabilities) for live CVE data
- [ ] Add subdomain enumeration module
- [ ] SSL/TLS certificate analysis
- [ ] Detect open redirects and basic OWASP checks
- [ ] Async scanning for speed improvements
- [ ] Docker container support

---

## ⚠️ Legal Disclaimer

**WebScout is intended for authorized security testing only.**  
Only scan targets you own or have explicit written permission to test.  
Unauthorized scanning may violate computer crime laws in your jurisdiction.

---

## 📄 License

[MIT License](LICENSE) © 2025 Mursalin

---

## 🙏 Acknowledgements

- [Wappalyzer](https://www.wappalyzer.com/) — inspiration for technology fingerprinting
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [NVD / NIST](https://nvd.nist.gov/) — CVE reference database
