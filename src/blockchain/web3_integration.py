from web3 import Web3

def connect():
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    print("Connected:", w3.is_connected())
    return w3


def load_contract(w3):
    contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"

    abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "amount",
				"type": "int256"
			}
		],
		"name": "updateBalance",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "balances",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "user",
				"type": "string"
			}
		],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
    ]

    return w3.eth.contract(address=contract_address, abi=abi)


def send_balances(contract, w3, account, balances):
    print("\nSending data to blockchain...\n")

    for user, amount in balances.items():
        tx = contract.functions.updateBalance(user, amount).transact({
            "from": account
        })

        receipt = w3.eth.wait_for_transaction_receipt(tx)
        print(f"✔ {user} updated: {amount}")