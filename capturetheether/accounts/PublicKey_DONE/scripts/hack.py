#!/usr/bin/python3
from brownie import web3
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

from eth_account._utils.signing import to_standard_v
from eth_account._utils.legacy_transactions import (
    serializable_unsigned_transaction_from_dict,
)
from eth_keys.datatypes import Signature

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
        "chainId": "0x01",
        "data": transaction["input"] or b"",
    }

    serialized_tx = serializable_unsigned_transaction_from_dict(tx_dict)
    rec_pub = signature.recover_public_key_from_msg_hash(serialized_tx.hash())
    recovered_address = rec_pub.to_checksum_address()

    # * convert it to bytes so that we can pass it as parameter
    public_key = rec_pub.to_bytes()

    print(f"{green}Recoved public key: {magenta}{rec_pub}{reset}")
    print(f"{green}Targeted address: {magenta}{recovered_address.lower()}{reset}")

    assert rec_pub.to_checksum_address() == transaction["from"]

    tx = target.authenticate(public_key, {"from": attacker})
    tx.wait(1)

    assert target.isComplete() == True
    print_colour(target.isComplete())


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
