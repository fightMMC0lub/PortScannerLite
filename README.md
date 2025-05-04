# 🔍 PortScannerLite

A simple Python-based port scanner that checks for open ports on a target IP address or domain.

---

### 🚀 Features

- Scan a host for open ports
- Multithreading for faster scanning
- Simple and clean command-line interface (CLI)
- Save scan reports to a file

---

## 📦 Installation

### Clone the repository:

```bash
git clone https://github.com/fightMMC0lub/PortScannerLite.git
cd PortScannerLite

```

### Install dependencies:

```bash
pip install -r requirements.txt

```
#Usage

```bash
python portscanner.py --host 192.168.1.1 --start 1 --end 1024

```

### 📥 Arguments

| Argument  | Description                         | Example              |
|-----------|-------------------------------------|----------------------|
| `--host`  | Target IP or domain to scan         | `--host google.com`  |
| `--start` | Start of port range (default: 1)    | `--start 1`          |
| `--end`   | End of port range (default: 1024)   | `--end 1024`         |

### Output

```bash
results/scan_report.txt

```
### ⚠️ Disclaimer
This tool is for educational use only.do not scan devices or domains you don’t own or don’t have permission to scan.
