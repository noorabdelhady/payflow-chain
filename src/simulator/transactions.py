import random

users = ["U1", "U2", "U3", "U4", "U5"]
merchants = ["M1", "M2", "M3"]

def generate_transactions(n=30):
    transactions = []

    for i in range(n):
        tx = {
            "id": i + 1,
            "from": random.choice(users),
            "to": random.choice(merchants),
            "amount": random.randint(1, 20),
            "type": random.choice(["purchase", "subscription", "service"])
        }
        transactions.append(tx)

    return transactions