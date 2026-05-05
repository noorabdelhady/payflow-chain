from src.simulator.transactions import generate_transactions
from src.batching.before import process_on_chain
from src.batching.rollup import batch_transactions, process_batched
from src.blockchain.web3_integration import connect, load_contract, send_balances

def main():
    print("PAYFLOW CHAIN SIMULATION\n")

    # Generate transactions
    transactions = generate_transactions(30)

    # BEFORE
    before_calls, before_gas = process_on_chain(transactions)

    # AFTER
    balances = batch_transactions(transactions)
    after_calls, after_gas = process_batched(balances)

    # Results
    print("\nRESULTS COMPARISON\n")

    print(f"Before → Transactions: {before_calls}, Gas: {before_gas}")
    print(f"After  → Transactions: {after_calls}, Gas: {after_gas}")

    reduction = ((before_calls - after_calls) / before_calls) * 100

    print(f"\nReduction: {reduction:.2f}%")

    # connect blockchain
    w3 = connect()
    contract = load_contract(w3)

    # use first account from Ganache
    account = w3.eth.accounts[0]

    # send results to blockchain
    send_balances(contract, w3, account, balances)

if __name__ == "__main__":
    main()