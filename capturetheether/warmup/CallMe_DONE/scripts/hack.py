#!/usr/bin/python3
from brownie import CallMeChallenge
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(target, solved=False):
    if solved:
        print(f"{blue}Is complete: {green}{target.isComplete()}{reset}")
    else:
        print(f"{blue}Is complete: {red}{target.isComplete()}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        _, attacker = get_account()
    else:
        target = CallMeChallenge.at(contract_address)

    # print(target.address)
    print_colour(target, target.isComplete())

    tx = target.callme({"from": attacker})
    tx.wait(1)

    # print(f"{blue}Is complete: {green}{target.isComplete()}{reset}")
    print_colour(target, target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
