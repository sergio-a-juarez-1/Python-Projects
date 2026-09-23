# Okta Suspicious Activity & System Log Monitor

A professional security monitoring and automated auditing tool written in Python for Identity and Access Management (IAM) and Security Operations (SecOps) administrators. This utility queries the Okta System Log API over a tight, rolling time window to extract, filter, and flag immediate authentication anomalies and potential brute-force risks.

## Features

* **Real-Time Security Auditing:** Automatically monitors your tenant's event stream over a customizable relative time window (defaulting to the past 60 minutes).
* **Targeted Threat Filtering:** Implements strict API expressions to filter specifically for authentication failures (`outcome.result eq "FAILURE"`) across all core authentication mechanisms.
* **ISO-8601 Temporal Precision:** Dynamically computes precise time deltas using standard timezones to align perfectly with Okta's backend ingestion clocks.
* **Visual Alert Ledger:** Prints a scannable security digest mapping event timestamps directly to the target actor login and the specific API rejection reason.
* **Production-Safe Configurations:** Enforces network safety using request timeout thresholds and abstracts your authorization layers to keep secrets safe from source repositories.

## Prerequisites

* Python 3.6+
* An active Okta Tenant (Developer, Preview, or Enterprise)
* An Okta API Token (SSWS token) with read access to system log event streams

## Installation

1. Clone or download this utility to your secure security automation pipeline or monitoring host.
2. Install the necessary network dependency:
   ```bash
   pip install requests
   ```

## Configuration

This tool pulls API authentication context natively from the underlying system environment variables to prevent local hardcoding.

### Terminal Environment Variables
Inject your enterprise security keys into your terminal environment context prior to launching the scanner:
```bash
export OKTA_API_TOKEN="your_ssws_token_here"
export OKTA_TENANT_URL="https://okta.com"
```

## Usage

Run the System Log Monitor from your server console or schedule it as a recurrent cron job:

```bash
python system_monitor.py
```

1. The script initializes and confirms the presence of valid environment variables.
2. It requests a rolling delta log of authentication failure actions.
3. Review the terminal console for structured alert lines showing matching events, or use standard terminal redirection to pass logs to downstream SIEM solutions:
   ```bash
   python system_monitor.py >> okta_security_alerts.log
   ```

## API References
* [Okta System Log API Documentation](https://okta.com)
