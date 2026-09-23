# Okta Group Auditing & Membership Sync

A robust Python automation utility designed for Identity and Access Management (IAM) administrators to safely audit, query, and synchronize user memberships within Okta Groups. 

This utility addresses large enterprise environments by implementing automated pagination handling, preventing partial data snapshots when tracking extensive directory groups.

## Features

* **Exact Group Lookups:** Resolves user-friendly group names into canonical Okta Group IDs cleanly using targeted query filtering.
* **Resilient Pagination Handling:** Automatically follows Okta HTTP `Link` pagination headers to comfortably extract thousands of members without data cutoff or timeout failures.
* **Live Status Breakdown:** Displays a visual ledger of all group members alongside their real-time lifecycle states (`ACTIVE`, `STAGED`, `DEPROVISIONED`).
* **Idempotent Membership Control:** Includes clean function architectures to safely add or remove individual user IDs to/from target groups.
* **Environment Isolation:** Relies entirely on system environment variables to isolate sensitive SSWS authorization tokens from application logic and code repositories.

## Prerequisites

* Python 3.6+
* An active Okta Developer, Preview, or Enterprise Tenant
* An Okta API Token (SSWS token) with adequate permissions to read groups and manage memberships

## Installation

1. Download or clone this repository to your local administrative workspace.
2. Install the necessary network dependency:
   ```bash
   pip install requests
   ```

## Configuration

The application validates host operating system environment variables at launch to secure your access keys.

### Terminal Environment Variables
Inject your secure tenant credentials directly into your active terminal process session context before execution:
```bash
export OKTA_API_TOKEN="your_ssws_token_here"
export OKTA_TENANT_URL="https://okta.com"
```

## Usage

Launch the Group Audit tool from your system console:

```bash
python group_sync.py
```

1. Enter the exact **Okta Group Name** you wish to audit at the command prompt.
2. The tool resolves the group ID and fetches the entire membership population sequentially.
3. Review the structured index list detailing user login mappings and their current account state.

## API References
* [Okta Groups API Documentation](https://okta.com)
