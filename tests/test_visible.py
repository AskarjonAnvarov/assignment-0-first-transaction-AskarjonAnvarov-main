"""
Visible tests - you can run them locally:
    pytest tests/test_visible.py -v
"""

from homework import get_wallet_data, STUDENT_DATA


def test_function_exists():
    """get_wallet_data must exist and be callable."""
    assert callable(get_wallet_data)


def test_student_data_has_required_fields():
    """STUDENT_DATA must contain all required keys."""
    required_keys = {"wallet_address", "tx_hash", "colleague_address", "tx_metainfo"}
    missing = required_keys - set(STUDENT_DATA.keys())
    assert not missing, f"Missing keys in STUDENT_DATA: {missing}"


def test_tx_metainfo_has_required_fields():
    """tx_metainfo must contain all required keys."""
    required_keys = {"recipient", "value_eth", "fee_eth", "block_number"}
    missing = required_keys - set(STUDENT_DATA.get("tx_metainfo", {}).keys())
    assert not missing, f"Missing keys in tx_metainfo: {missing}"


def test_get_wallet_data_signature():
    """get_wallet_data must accept (w3, address) and return a dict."""
    import inspect

    sig = inspect.signature(get_wallet_data)
    params = list(sig.parameters.keys())
    assert len(params) >= 2, "get_wallet_data must accept at least 2 parameters (w3, address)"
