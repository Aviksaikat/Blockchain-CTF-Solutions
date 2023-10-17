#!/usr/bin/python3
import rlp
from brownie import web3
from colorama import Fore
from eth_account import Account
from eth_account._utils.legacy_transactions import ALLOWED_TRANSACTION_KEYS
from eth_account._utils.signing import (
    extract_chain_id, serializable_unsigned_transaction_from_dict,
    to_standard_v)
from eth_account.messages import defunct_hash_message
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * https://ethereum.stackexchange.com/questions/13778/get-public-key-of-any-ethereum-account


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, owner = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # print(target.owner())
    target_address = target.owner()
    block_number = web3.eth.block_number

    block = web3.eth.get_block(block_number, True)

    transaction = web3.eth.getTransaction(block.transactions[-1]["hash"].hex())
    # print(tx)
    # # print(extract_chain_id(tx['v'])[1])
    # # print(web3.toInt(tx['r']))
    # # print(web3.toInt(tx['s']))
    # #exit()

    # s = web3.eth.account._keys.Signature(vrs=(
    # 	to_standard_v(extract_chain_id(tx['v'])[1]),
    # 	web3.toInt(tx['r']),
    # 	web3.toInt(tx['s'])
    # ))

    # tt = { k:tx[k] for k in ALLOWED_TRANSACTION_KEYS - {"chainId", "data"}}
    # ut = serializable_unsigned_transaction_from_dict(tt)

    # print(tt)
    # #print(ut.hash())
    # msg_hash = web3.keccak(ut.hash())
    # #print(msg_hash)

    # public_key = s.recover_public_key_from_msg_hash(ut.hash())
    # print(public_key)

    # #print(target.owner())
    # print(s.recover_public_key_from_msg_hash(ut.hash()).to_checksum_address())
    # print(tx["from"].lower())

    # Create the RLP-encoded data of the transaction
    tx_data = {
        "nonce": transaction["nonce"],
        "gasPrice": transaction["gasPrice"],
        "gas": transaction["gas"],
        "to": transaction["to"] or "",
        "value": transaction["value"],
        "data": b"",
        "chainId ": transaction["v"],
    }
    encoded_tx = rlp.encode(tx_data)
    print(encoded_tx)
    # Compute the message hash
    message_hash = defunct_hash_message(encoded_tx)

    # Recover the public key from the signature
    signature = {"r": transaction["r"], "s": transaction["s"], "v": transaction["v"]}
    print(dir(Account))
    # exit()

    public_key = Account.recover_message(encoded_tx, signature=signature)
    print(public_key)

    # Print the uncompressed public key
    uncompressed_public_key = Account.convert_to_uncompressed_public_key(public_key)
    print("Recovered public key:", uncompressed_public_key.hex())

    print_colour(target.isComplete())

    # assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
