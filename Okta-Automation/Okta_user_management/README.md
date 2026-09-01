# Okta User Lifecycle Management CLI

A professional Command Line Interface (CLI) automation tool written in Python for identity and access management (IAM) administrators. This script simplifies individual Okta user administration by auditing accounts and executing complex lifecycle operations safely.

Because the Okta API requires active accounts to be transitioned into a `DEPROVISIONED` state before they can be completely purged, this utility intelligently chains lifecycle events together to automate the process safely.

## Features

* **Instant Profile Audits:** Queries user records via the Okta API using a unique login name to retrieve live account states, profile IDs, names, and email records.
* **Smart Lifecycle Routing:** Dynamically adapts its operational paths based on the target user's current account state (`ACTIVE`, `STAGED`, `DEPROVISIONED`, etc.).
* **Automated Two-Step Purges:** Safely deactivates active profiles before firing subsequent deletion calls to bypass strict Okta security constraints.
* **Safe Account Restoration:** Provides a quick pathway to safely reactivate dormant or deprovisioned user bases.
* **Production-Safe Engine:** Replaces hazardous recursion models with stable control loops and extracts sensitive API details from environmental variables to prevent credential exposure.

## Prerequisites

* Python 3.6+
* An active Okta Developer, Preview, or Enterprise Tenant
* An Okta API Token (SSWS token) with permissions to modify and delete user accounts

## Installation

1. Clone or download this utility repository to your workspace.
2. Install the necessary network dependency:
   ```bash
   pip install requests
   ```

## Configuration

The application checks host operating system environment variables first to protect keys from source control trackers.

### Option A: Terminal Environment Variables (Recommended)
Inject your secure credentials straight into your current terminal process context before execution:
```bash
export OKTA_API_TOKEN="your_ssws_token_here"
export OKTA_TENANT_URL="https://okta.com"
```

### Option B: Local Code Fallback Configuration
Alternatively, open the script manually and insert your deployment details directly into the default variables at the top of the file:
```python
TOKEN = os.environ.get("OKTA_API_TOKEN", "YOUR_OKTA_API_TOKEN")
TENANT_URL = os.environ.get("OKTA_TENANT_URL", "https://okta.com")
```

## Usage

Launch the management CLI from your system console:

```bash
python main.py
```

1. Type the exact **Okta login name** (usually an email address) of the user you wish to manage.
2. Review the structured summary block outputting their metadata and live state.
3. Follow the interactive prompts (`y/n`) to trigger deactivations, permanent structural deletions, or account reactivations.
4. Type `exit` at the login prompt to terminate the session safely.

## API References
* [Okta Users Lifecycle API Documentation](https://okta.com)
