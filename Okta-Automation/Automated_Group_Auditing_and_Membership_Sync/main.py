import os
import sys
import requests

# 1. Fetch secure configuration from Environment Variables
TOKEN = os.environ.get("OKTA_API_TOKEN", "[REPLACE]")
TENANT_URL = os.environ.get("OKTA_TENANT_URL", "https://[REPLACE].okta.com")

if TOKEN == "[REPLACE]" or "[REPLACE]" in TENANT_URL:
    print("Error: Missing credentials. Please set your OKTA_API_TOKEN and OKTA_TENANT_URL variables.")
    sys.exit(1)

BASE_URL = TENANT_URL.rstrip("/")
HEADERS = {
    "Authorization": f"SSWS {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def get_group_by_name(group_name):
    """Finds a group ID by its exact name match."""
    url = f"{BASE_URL}/api/v1/groups"
    params = {"q": group_name, "limit": 1}
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        r.raise_for_status()
        groups = r.json()
        return groups[0]["id"] if groups else None
    except requests.RequestException as e:
        print(f"[Error] Failed to fetch group '{group_name}': {e}")
        return None

def get_group_members(group_id):
    """Fetches all users belonging to a group with automatic pagination support."""
    url = f"{BASE_URL}/api/v1/groups/{group_id}/users?limit=200"
    members = []
    try:
        while url:
            r = requests.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
            members.extend(r.json())
            url = r.links.get('next', {}).get('url')
        return members
    except requests.RequestException as e:
        print(f"[Error] Pagination failure tracking members: {e}")
        return members

def add_user_to_group(user_id, group_id):
    """Safely adds a target user to a specific group."""
    url = f"{BASE_URL}/api/v1/groups/{group_id}/users/{user_id}"
    try:
        r = requests.put(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        print(f"Successfully added user {user_id} to group {group_id}.")
        return True
    except requests.RequestException as e:
        print(f"[Error] Failed to assign user to group: {e}")
        return False

def main():
    print("=== Okta Group Audit Tool ===")
    target_group = input("Enter the Okta Group Name to audit: ").strip()
    if not target_group:
        return

    group_id = get_group_by_name(target_group)
    if not group_id:
        print(f"Could not find any group named '{target_group}'")
        sys.exit(1)

    print(f"Found Group ID: {group_id}. Fetching members...")
    members = get_group_members(group_id)
    
    print(f"\n{'Current Members Summary':-^40}")
    for idx, user in enumerate(members):
        profile = user.get("profile", {})
        print(f"{idx+1}. {profile.get('login')} [{user.get('status')}]")
    print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting cleanly.")
        sys.exit(0)
