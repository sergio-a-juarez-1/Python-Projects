import os
import sys
import requests

# 1. Fetch secure configuration from Environment Variables
TOKEN = os.environ.get("OKTA_API_TOKEN", "[REPLACE]")
TENANT_URL = os.environ.get("OKTA_TENANT_URL", "https://[REPLACE].okta.com")

if TOKEN == "[REPLACE]" or "[REPLACE]" in TENANT_URL:
    print("Warning: Please set your OKTA_API_TOKEN and OKTA_TENANT_URL environment variables.")

# Clean up base URL string formatting
BASE_URL = TENANT_URL.rstrip("/")
if not BASE_URL.startswith("http"):
    BASE_URL = f"https://{BASE_URL}"

HEADERS = {
    "Authorization": f"SSWS {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def get_user(login):
    """Fetches a user profile by login string. Returns user object or None."""
    url = f"{BASE_URL}/api/v1/users"
    params = {"filter": f'profile.login eq "{login}"'}
    
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=10)
        
        if r.status_code == 401:
            print("\n[Error 401] Unauthorized. Please verify your Okta API Token.")
            return None
        
        r.raise_for_status()
        users = r.json()
        
        if not users:
            print(f"\nCould not find user matching login: '{login}'")
            return None
            
        return users[0]
        
    except requests.RequestException as e:
        print(f"\nNetwork or API error occurred while fetching user: {e}")
        return None


def deactivate_user(user_id, display_name):
    """Deactivates an active user account."""
    url = f"{BASE_URL}/api/v1/users/{user_id}/lifecycle/deactivate"
    try:
        r = requests.post(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        print(f"\nSuccess: User {display_name} has been DEACTIVATED (Status: {r.status_code})")
        return True
    except requests.RequestException as e:
        print(f"\nFailed to deactivate user: {e}")
        return False


def reactivate_user(user_id, display_name):
    """Reactivates a deprovisioned user account."""
    url = f"{BASE_URL}/api/v1/users/{user_id}/lifecycle/activate"
    params = {"sendEmail": "false"}
    try:
        r = requests.post(url, headers=HEADERS, params=params, timeout=10)
        r.raise_for_status()
        print(f"\nSuccess: User {display_name} has been REACTIVATED.")
        return True
    except requests.RequestException as e:
        print(f"\nFailed to reactivate user: {e}")
        return False


def delete_user(user_id, display_name):
    """Permanently deletes a deprovisioned user account."""
    url = f"{BASE_URL}/api/v1/users/{user_id}"
    try:
        r = requests.delete(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        print(f"\nSuccess: User {display_name} has been permanently DELETED (Status: {r.status_code})")
        return True
    except requests.RequestException as e:
        print(f"\nFailed to delete user: {e}")
        return False


def main():
    print("=== Okta User Lifecycle Management CLI ===")
    
    while True:
        login = input("\nEnter User's login (or type 'exit' to quit): ").strip()
        if login.lower() == 'exit':
            print("Exiting utility.")
            break
        if not login:
            continue

        user = get_user(login)
        if not user:
            continue

        user_id = user["id"]
        status = user["status"]
        profile = user.get("profile", {})
        fn = profile.get("firstName", "Unknown")
        ln = profile.get("lastName", "Unknown")
        email = profile.get("email", "N/A")
        display_name = f"{fn} {ln}"

        # Visual alignment output blocks
        print(f"\n{'User Details':-^40}")
        print(f"{'Status:':<15} {status}")
        print(f"{'ID:':<15} {user_id}")
        print(f"{'Name:':<15} {display_name}")
        print(f"{'Email:':<15} {email}")
        print("-" * 40)

        # Logical tree handling based on user state
        if status != "DEPROVISIONED":
            choice = input("\nDeactivate User and then Delete? (y/n): ").strip().lower()
            if choice == 'y':
                if deactivate_user(user_id, display_name):
                    # Okta requires users to be in DEPROVISIONED state before running a DELETE request
                    delete_user(user_id, display_name)
            elif choice == 'n':
                sub_choice = input("Do you want to ONLY Deactivate the user? (y/n): ").strip().lower()
                if sub_choice == 'y':
                    deactivate_user(user_id, display_name)
        else:
            choice = input("\nUser is already Deactivated.\nWould you like to permanently Delete the User? (y/n): ").strip().lower()
            if choice == 'y':
                delete_user(user_id, display_name)
            elif choice == 'n':
                sub_choice = input("Would you like to Reactivate the User? (y/n): ").strip().lower()
                if sub_choice == 'y':
                    reactivate_user(user_id, display_name)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting cleanly.")
        sys.exit(0)
