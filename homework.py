from web3 import Web3

# --- Connect to Sepolia RPC ---
SEPOLIA_RPC = "https://rpc.sepolia.org"
w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC))

# --- Student Data ---
STUDENT_DATA = {
    "wallet_address": "0x6a60f998969358abd93886508BBf28818d9C861D",
    "tx_hash": "0x4a75236e179a30623af512db57a0bf069834f69020079a466b1fc9f6a83533da",
    "colleague_address": "0xA895D3c728a77bedEa2081E2090fcB1679D305D9",
    "tx_metainfo": {
        "recipient": "0xA895D3c728a77bedEa2081E2090fcB1679D305D9",
        "value_eth": 0.001,
        "fee_eth": 0.000031500000189,
        "block_number": 10430813,
    },
}

# --- Function to fetch wallet and transaction data ---
def get_wallet_data(address):
    tx_hash = STUDENT_DATA["tx_hash"]

    # --- Wallet balance ---
    balance_wei = w3.eth.get_balance(address)
    balance_eth = float(w3.fromWei(balance_wei, "ether"))

    # --- Transaction data ---
    try:
        tx = w3.eth.get_transaction(tx_hash)
    except Exception as e:
        print("Error fetching transaction:", e)
        tx = {}

    # --- Transaction value in ETH ---
    tx_value_eth = float(w3.fromWei(tx["value"], "ether")) if tx else 0.0

    return {
        "balance_wei": balance_wei,
        "balance_eth": balance_eth,
        "tx": dict(tx) if tx else {},
        "tx_value_eth": tx_value_eth,
    }

# --- Example usage ---
if __name__ == "__main__":
    data = get_wallet_data(STUDENT_DATA["wallet_address"])
    print(data)