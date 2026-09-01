# Okta Mock User Generator

A lightweight Python automation script designed to quickly generate and populate mock user profiles within an Okta tenant for development, testing, and staging environments.

The script dynamically fetches a standard 10,000-word vocabulary list from MIT's public servers, randomizes first and last names, maps matching Mailinator email addresses, generates high-entropy 20-character passwords, and provisions active accounts via the Okta Users API.

## Features

* **Automated Wordlist Fetching:** Automatically pulls 10,000 common words to form random user combinations.
* **Instant Activation:** Auto-activates provisioned users on creation using Okta URL parameters (`activate=true`).
* **Secure Entropy Passwords:** Generates randomized 20-character passwords utilizing alphanumeric and punctuation characters.
* **Environment Configuration:** Supports loading sensitive credentials from the host environment to keep keys out of version control.
* **Resilient Error Logging:** Catches HTTP errors (such as duplicate profiles or password validation failures) and prints Okta's API rejection reasons.

## Prerequisites

* Python 3.6+
* An active Okta Developer or Enterprise Tenant
* An Okta API Token (SSWS token) with permissions to create and manage users

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies:

```bash
pip install requests
```

## Configuration

The script safely checks your operating system environment variables first. You can run the script by either setting up variables or adding fallback parameters inside the file.

### Option A: Environment Variables (Recommended)

Set your variables directly inside your terminal session before launching:

```bash
export OKTA_API_TOKEN="your_ssws_token_here"
export OKTA_TENANT_URL="https://okta.com"
```

### Option B: Direct Script Modification

Open the source file and update the configuration fallbacks near the top:

```python
TOKEN = os.environ.get("OKTA_API_TOKEN", "YOUR_OKTA_API_TOKEN")
TENANT = os.environ.get("OKTA_TENANT_URL", "https://okta.com")
```

## Usage

Execute the script from your terminal:

```bash
python main.py
```

1. Enter the total number of test profiles you want to construct when prompted by the terminal.
2. The script will sequentially query the Okta API to build and activate the user base.
3. Review the terminal console for output logs displaying successful profile details or targeted API errors.

## API References

* [Okta Users API Documentation](https://okta.com)
