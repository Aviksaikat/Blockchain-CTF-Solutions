#!/usr/bin/python3
from brownie import web3
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

target_hash = "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365"


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

    i = 0
    # ans = web3.keccak(i).hex().upper()
    # uint8 to value ranges 0-255
    for i in range(256):
        if web3.keccak(i).hex() == target_hash:
            break

        i += 1
        # ans = web3.keccak(i).hex().upper()
        # print(web3.keccak(i).hex())
        # exit()
    # print(i)

    print(f"{green}Secret value found: {i}{reset}")

    target.guess(i, {"from": attacker, "value": "1 ether"}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True
    print(f"{green}Assert Passed!!{reset}")


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
