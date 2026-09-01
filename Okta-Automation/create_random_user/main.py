import string, json, requests, random, urllib.request

# word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# response = urlopen(word_site)
# txt = response.read()
# WORDS = txt.splitlines()

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

#WORDS = ['random','Words','generator','didnot','work']

token = "[Replace-With-Token]"
tenant = "https://[REPLACE].okta.com"

headers = {"Authorization" : "SSWS " + token,
           "Accept" : "application/json",
           "Content-Type" : "application/json"}
my_params = {"activate" : True}

number = int(input("How many users do you want to create: "))

for n in range(number):
    fn = str(random.choice(WORDS).lower())
    ln = str(random.choice(WORDS).lower())
    body = {"profile": {
        "firstName":"{}".format(fn[2:-1].capitalize()),
        "lastName":"{}".format(ln[2:-1].capitalize()),
        "login":"{}.{}@mailinator.com".format(fn[2:-1],ln[2:-1]),
        "email":"{}.{}@mailinator.com".format(fn[2:-1],ln[2:-1]),
    },
        "credentials":{
            "password":{"value":"".join([random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(string.punctuation) for n in range(20)])}
        }
    }
    r = requests.post("{}/api/v1/users".format(tenant), headers=headers, params=my_params, data=json.dumps(body))

    print("\nUser nr. {4} - {0} {1} (login: {2}, email: {2}) has just been created with the following password: {3}.\n".format(body["profile"]["firstName"],body["profile"]["lastName"],body["profile"]["login"],body["credentials"]["password"]["value"],n+1))
