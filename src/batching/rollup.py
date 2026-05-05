def batch_transactions(transactions):
    print("\nAFTER (Rollup Batching)\n")

    balances = {}

    for tx in transactions:
        sender = tx["from"]
        receiver = tx["to"]
        amount = tx["amount"]

        balances[sender] = balances.get(sender, 0) - amount
        balances[receiver] = balances.get(receiver, 0) + amount

    print("Final Aggregated Balances:\n")
    for entity, balance in balances.items():
        print(f"{entity}: {balance}")

    return balances


def process_batched(balances):
    blockchain_calls = len(balances)
    gas_used = blockchain_calls

    return blockchain_calls, gas_used