import os
import random
import string
import sys
import requests

# 1. Fetch and cleanly decode the word list (eliminates the raw bytes slicing bug)
WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"
try:
    response = requests.get(WORD_SITE, timeout=10)
    response.raise_for_status()
    # Decode directly from bytes to string to remove b'' wrappers
    WORDS = [word.decode("utf-8") for word in response.content.splitlines()]
except requests.RequestException as e:
    print(f"Error fetching the word list: {e}")
    sys.exit(1)

# 2. Secure configuration via Environment Variables (Fallback to placeholders)
TOKEN = os.environ.get("OKTA_API_TOKEN", "[Replace-With-Token]")
TENANT = os.environ.get("OKTA_TENANT_URL", "https://[REPLACE].okta.com")

if TOKEN == "[Replace-With-Token]" or TENANT == "https://[REPLACE].okta.com":
    print("Warning: Please set your OKTA_API_TOKEN and OKTA_TENANT_URL environment variables.")

headers = {
    "Authorization": f"SSWS {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
my_params = {"activate": "true"}  # Okta API handles booleans as string parameters best

# 3. Prompt user for input
try:
    number = int(input("How many users do you want to create: "))
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)

# 4. Process user generation loop
for n in range(number):
    fn = random.choice(WORDS).lower()
    ln = random.choice(WORDS).lower()
    
    # Generate a strong password safely
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password_value = "".join(random.choice(password_chars) for _ in range(20))
    
    body = {
        "profile": {
            "firstName": fn.capitalize(),
            "lastName": ln.capitalize(),
            "login": f"{fn}.{ln}@mailinator.com",
            "email": f"{fn}.{ln}@mailinator.com",
        },
        "credentials": {
            "password": {"value": password_value}
        }
    }
    
    # Send request and catch failures
    try:
        url = f"{TENANT}/api/v1/users"
        r = requests.post(url, headers=headers, params=my_params, json=body, timeout=10)
        r.raise_for_status()
        
        print(
            f"\nUser nr. {n+1} - {body['profile']['firstName']} {body['profile']['lastName']} "
            f"(login: {body['profile']['login']}) has been created successfully.\n"
            f"Password: {password_value}\n"
        )
    except requests.HTTPError as http_err:
        print(f"\n[Error] Failed to create user {n+1}: Status {r.status_code}")
        try:
            # Output the specific Okta error message if available
            print(f"Details: {r.json().get('errorCauses', [{}])[0].get('errorSummary', r.text)}")
        except Exception:
            print(f"Details: {r.text}")
    except requests.RequestException as req_err:
        print(f"\n[Network Error] User {n+1} skipped: {req_err}")
