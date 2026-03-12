from web3 import Web3
from typing import Dict, Any


# ============================================================
# TASK 1: FILL IN WITH YOUR DATA
# ============================================================
# 1. wallet_address      - your Sepolia address (MetaMask)
# 2. tx_hash             - hash of the transaction you sent to a colleague
# 3. colleague_address   - colleague's address (see README)
# 4. tx_metainfo         - dict with transaction details:
#      recipient          - recipient address from your transaction
#      value_eth          - ETH value sent in the transaction
#      fee_eth            - transaction fee in ETH
#      block_number       - block number the transaction was included in
# ============================================================

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


# ============================================================
# TASK 2: IMPLEMENT THIS FUNCTION
# ============================================================

def get_wallet_data(w3, address):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = float(w3.from_wei(balance_wei, "ether"))

    tx = w3.eth.get_transaction(STUDENT_DATA["tx_hash"])
    tx_value_eth = float(w3.from_wei(tx["value"], "ether"))

    return {
        "balance_wei": balance_wei,
        "balance_eth": balance_eth,
        "tx": dict(tx),
        "tx_value_eth": tx_value_eth,
    }
