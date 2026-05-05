def process_on_chain(transactions):
    print("\nBEFORE (Traditional Blockchain)\n")

    for tx in transactions:
        print(f"Tx {tx['id']}: {tx['from']} → {tx['to']} | ${tx['amount']}")

    blockchain_calls = len(transactions)
    gas_used = blockchain_calls

    return blockchain_calls, gas_used