import requests

base = input("Pierwsza waluta: ")
other = input("Druga waluta: ")

res = requests.get("http://data.fixer.io/api/latest?access_key=c7f1183aea154957f61206a64c1a488f&base=EUR&symbols=PLN,USD", params={"base":base, "symbols":other})

if res.status_code != 200:
    raise Exception("Error: API request unsuccessful")

data = res.json()
print(data)

rate = data["rates"][other]
print(f"1 {base} jest równoważny {rate} {other}")
