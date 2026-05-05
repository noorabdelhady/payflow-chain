from flask import Flask, render_template, jsonify
from src.simulator.transactions import generate_transactions
from src.batching.before import process_on_chain
from src.batching.rollup import batch_transactions, process_batched
from src.blockchain.web3_integration import connect, load_contract, send_balances

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/run_simulation')
def run_simulation():
    # 1. Generate 30 mock transactions
    transactions = generate_transactions(30)
    
    # 2. Before applying rollup (Traditional)
    before_calls, before_gas = process_on_chain(transactions)
    
    # 3. After applying rollup (PayFlow Chain)
    balances = batch_transactions(transactions)
    after_calls, after_gas = process_batched(balances)
    
    # 4. Calculate reduction percentage
    reduction = ((before_calls - after_calls) / before_calls) * 100
    
    # 5. Try updating the blockchain (if Ganache is running)
    blockchain_status = "Skipped"
    try:
        w3 = connect()
        if w3.is_connected():
            contract = load_contract(w3)
            # Use the first account from Ganache
            account = w3.eth.accounts[0]
            send_balances(contract, w3, account, balances)
            blockchain_status = "Success: Balances saved on-chain"
        else:
            blockchain_status = "Ganache Not Connected"
    except Exception as e:
        # Ignore errors for the UI so the graph still shows up
        blockchain_status = f"Error: {str(e)}"
    
    return jsonify({
        "transactions": transactions,
        "balances": balances,
        "metrics": {
            "before_calls": before_calls,
            "after_calls": after_calls,
            "before_gas": before_gas,
            "after_gas": after_gas,
            "reduction": round(reduction, 2)
        },
        "blockchain_status": blockchain_status
    })

if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=False, port=5000)
