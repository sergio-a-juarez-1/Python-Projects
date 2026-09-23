import os
import sys
from datetime import datetime, timedelta, timezone
import requests

# 1. Fetch secure configuration from Environment Variables
TOKEN = os.environ.get("OKTA_API_TOKEN", "[REPLACE]")
TENANT_URL = os.environ.get("OKTA_TENANT_URL", "https://[REPLACE].okta.com")

if TOKEN == "[REPLACE]" or "[REPLACE]" in TENANT_URL:
    print("Error: Missing configuration environment parameters.")
    sys.exit(1)

BASE_URL = TENANT_URL.rstrip("/")
HEADERS = {
    "Authorization": f"SSWS {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def monitor_security_events(minutes_back=60):
    """Scans system logs for critical authentication failures within a relative window."""
    url = f"{BASE_URL}/api/v1/logs"
    
    # ISO-8601 formatting for accurate relative log range targeting
    start_time = (datetime.now(timezone.utc) - timedelta(minutes=minutes_back)).isoformat()
    
    # Filter targets explicitly failed authentication mechanisms
    log_filter = 'outcome.result eq "FAILURE" and eventType sw "user.authentication"'
    params = {
        "since": start_time,
        "filter": log_filter,
        "limit": 100
    }
    
    try:
        print(f"Scanning for failure events since: {start_time}")
        r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        r.raise_for_status()
        events = r.json()
        
        if not events:
            print("No suspicious authentication failures discovered in this window.")
            return

        print(f"\nFound {len(events)} security warning alerts:")
        print(f"{'Timestamp':<25} {'Actor Login':<30} {'Reason'}")
        print("=" * 75)
        
        for event in events:
            timestamp = event.get("published", "N/A")
            actor = event.get("actor", {}).get("alternateId", "System/Unknown")
            outcome = event.get("outcome", {}).get("reason", "Unknown Auth Block")
            print(f"{timestamp[:22]:<25} {actor:<30} {outcome}")
            
    except requests.RequestException as e:
        print(f"[Network/API Error] System Log querying failed: {e}")

if __name__ == "__main__":
    try:
        # Default tracking checks past 1 hour of activities
        monitor_security_events(minutes_back=60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        sys.exit(0)
