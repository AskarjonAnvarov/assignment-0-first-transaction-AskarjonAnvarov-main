# Assignment 0 - First Transaction on Sepolia

## Objective

Learn to work with the Ethereum testnet: create a wallet, obtain test ETH, send a transaction, and programmatically retrieve its data using web3.py.

## Steps

### 1. Create a Wallet

Install [MetaMask](https://metamask.io/) and switch to the **Sepolia** network.

### 2. Get Test ETH

Visit a faucet and request test ETH to your address:
- https://faucets.chain.link/sepolia
- https://www.alchemy.com/faucets/ethereum-sepolia

You will need at least **0.002 ETH** (0.001 for the transfer + gas fees).

### 3. Send a Transaction

Send **>= 0.001 ETH** to a colleague's Sepolia address (ask a classmate for their address, or use a second wallet you create).

Save the **tx hash** and the **recipient address** - you will need both.

### 4. Fill in `STUDENT_DATA` in `homework.py`

```python
STUDENT_DATA = {
    "wallet_address": "0xYOUR_ADDRESS",
    "tx_hash": "0xYOUR_TX_HASH",
    "colleague_address": "0xCOLLEAGUE_ADDRESS",
    "tx_metainfo": {
        "recipient": "0xRECIPIENT_ADDRESS",
        "value_eth": 0.001,
        "fee_eth": 0.000021,
        "block_number": 1234567,
    },
}
```

You can find the transaction details on [Sepolia Etherscan](https://sepolia.etherscan.io/) by searching for your tx hash.

### 5. Implement `get_wallet_data()` in `homework.py`

Implement `get_wallet_data()` which returns:

| Key | Type | Description |
|-----|------|-------------|
| `balance_wei` | `int` | Wallet balance in wei |
| `balance_eth` | `float` | Wallet balance in ETH |
| `tx` | `dict` | Transaction data (result of `w3.eth.get_transaction`) |
| `tx_value_eth` | `float` | Transaction value in ETH |

### 6. Test locally

```bash
pip install -r requirements.txt
pytest tests/test_visible.py -v
```

### 7. Submit your solution

```bash
git add homework.py
git commit -m "solution"
git push
```

After `push`, autograding will run. Check results in the **Actions** tab.

## Grading Criteria (10 points total)

| Points | Condition |
|--------|-----------|
| 1 | Wallet created (valid Sepolia address with balance) |
| 2 | Transaction created (tx hash exists on-chain) |
| 2 | Transaction metainfo is correct (recipient, ETH value, fee, block number) |
| 5 | `get_wallet_data()` works as expected |

## Useful Links

- [web3.py docs](https://web3py.readthedocs.io/)
- [`w3.eth.get_balance`](https://web3py.readthedocs.io/en/stable/web3.eth.html#web3.eth.Eth.get_balance)
- [`w3.eth.get_transaction`](https://web3py.readthedocs.io/en/stable/web3.eth.html#web3.eth.Eth.get_transaction)
- [`w3.from_wei`](https://web3py.readthedocs.io/en/stable/web3.main.html#web3.Web3.from_wei)
