import os
import secrets  # Cryptographically secure randomness
import string
import sys
import requests

# 1. Fetch and cleanly decode the word list 
WORD_SITE = "https://mit.edu"
try:
    response = requests.get(WORD_SITE, timeout=10)
    response.raise_for_status()
    # Decode directly from bytes to string 
    WORDS = [word.decode("utf-8") for word in response.content.splitlines()]
except requests.RequestException as e:
    print(f"Error fetching the word list: {e}")
    sys.exit(1)

# 2. Secure configuration via Environment Variables 
TOKEN = os.environ.get("OKTA_API_TOKEN", "[Replace-With-Token]")
TENANT = os.environ.get("OKTA_TENANT_URL", "https://[REPLACE].okta.com")

if TOKEN == "[Replace-With-Token]" or TENANT == "https://[REPLACE].okta.com":
    print("Warning: Please set your OKTA_API_TOKEN and OKTA_TENANT_URL environment variables.")

headers = {
    "Authorization": f"SSWS {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}
# requests automatically serializes True to "true" in query parameters
my_params = {"activate": True}  

# 3. Prompt user for input
try:
    number = int(input("How many users do you want to create: "))
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)

# 4. Process user generation loop
for n in range(number):
    # secrets.choice ensures non-predictable name combinations
    fn = secrets.choice(WORDS).lower()
    ln = secrets.choice(WORDS).lower()
    
    # Generate a cryptographically strong password safely
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password_value = "".join(secrets.choice(password_chars) for _ in range(20))
    
    # Changed domain from mailinator.com to a safe example.com placeholder
    test_email = f"{fn}.{ln}@example.com"
    
    body = {
        "profile": {
            "firstName": fn.capitalize(),
            "lastName": ln.capitalize(),
            "login": test_email,
            "email": test_email,
        },
        "credentials": {
            "password": {"value": password_value}
        }
    }
    
    # Send request and catch failures
    try:
        url = f"{TENANT.rstrip('/')}/api/v1/users"
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
