from web3 import Web3

SEPOLIA_RPC = "https://rpc.sepolia.org"

w3 = Web3(Web3.HTTPProvider(SEPOLIA_RPC))

STUDENT_DATA = {
    "wallet_address": "0x6a60f998969358abd93886508BBf28818d9C861D",
    "tx_hash": "0x4a75236e179a30623af512db57a0bf069834f69020079a466b1fc9f6a83533da",
    "colleague_address": "0xA895D3c728a77bedEa2081E2090fcB1679D305D9",
    "tx_metainfo": {
        "recipient": "0xA895D3c728a77bedEa2081E2090fcB1679D305D9",
        "value_eth": 0.001,
        "fee_eth": 0.000031,
        "block_number": 10430813,
    },
}


def get_wallet_data(w3, address):
    tx_hash = STUDENT_DATA["tx_hash"]

    # wallet balance
    balance_wei = w3.eth.get_balance(address)
    balance_eth = float(w3.from_wei(balance_wei, "ether"))

    # transaction data
    tx = w3.eth.get_transaction(tx_hash)

    # tx value in ETH
    tx_value_eth = float(w3.from_wei(tx["value"], "ether"))

    return {
        "balance_wei": balance_wei,
        "balance_eth": balance_eth,
        "tx": dict(tx),
        "tx_value_eth": tx_value_eth,
    }