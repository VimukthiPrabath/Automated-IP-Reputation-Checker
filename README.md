# Automated IP Reputation Checker

An automated security operations (SOC) tool designed to check the reputation of multiple IP addresses using the AbuseIPDB API. This script rapidly processes lists of IPs, identifies malicious nodes, and exports the intelligence into a structured CSV format for further analysis.

## 🚀 Features
*   **Bulk IP Processing:** Analyzes multiple IP addresses from a simple text file.
*   **Automated Threat Intelligence:** Integrates directly with the AbuseIPDB API.
*   **Rate Limiting Handled:** Built-in delays to respect API rate limits.
*   **CSV Data Export:** Automatically generates formatted reports (`malicious_ips.csv`) including Abuse Confidence Score, ISP, Country, and Total Reports.
*   **Secure Credential Management:** Utilizes `.env` files to keep API keys secure.

## 🛠️ Prerequisites
*   Python 3.x
*   `requests` library
*   `python-dotenv` library
*   AbuseIPDB Free API Key

## ⚙️ Installation & Usage
1. Clone this repository:
   ```bash
   git clone [https://github.com/VimukthiPrabath/Automated-IP-Reputation-Checker.git](https://github.com/VimukthiPrabath/Automated-IP-Reputation-Checker.git)