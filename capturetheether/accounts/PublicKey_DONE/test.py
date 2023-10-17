from coincurve import PublicKey as CCPublicKey
from eth_account._utils.legacy_transactions import \
    serializable_unsigned_transaction_from_dict
from eth_account._utils.signing import to_standard_v
from eth_keys.datatypes import Signature
from eth_rlp import HashableRLP
from hexbytes import HexBytes
from web3 import Web3

INFURA_URL_MAINNET = "..."
INFURA_URL_TESTNET = "..."


def pub_key_from_tx_eth(txid, chain):
    """Obtain the public key from an Ethereum transaction"""
    w3test = Web3(Web3.HTTPProvider(INFURA_URL_TESTNET))
    transaction = w3test.eth.get_transaction(txid)
    vrs = (
        to_standard_v(transaction["v"]),
        int.from_bytes(transaction["r"], "big"),
        int.from_bytes(transaction["s"], "big"),
    )
    signature = Signature(vrs=vrs)
    tx_dict = {
        "nonce": transaction.nonce,
        "gasPrice": transaction.gasPrice,
        "gas": transaction.gas,
        "to": transaction.to,
        "value": transaction.value,
    }
    if chain == "ETH":
        tx_dict["chainId"] = "0x01"
    elif chain == "tETH":
        tx_dict["chainId"] = "0x03"
    if "input" in transaction:
        tx_dict["data"] = transaction["input"]
    serialized_tx = serializable_unsigned_transaction_from_dict(tx_dict)
    rec_pub = signature.recover_public_key_from_msg_hash(serialized_tx.hash())
    if rec_pub.to_checksum_address() != transaction["from"]:
        raise ValueError("Unable to obtain public key from transaction: " + f"{txid}")
    return rec_pub
