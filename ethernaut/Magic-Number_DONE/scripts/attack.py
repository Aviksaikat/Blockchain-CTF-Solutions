#!/usr/bin/python3
from brownie import MagicNum, DeployBytecode, Contract, interface
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        magic_num, _ = deploy()
        contract_address = magic_num.address
        _, attacker = get_account()
    else:
        magic_num = MagicNum.at(contract_address)

    deploy_byte_code = DeployBytecode.deploy({"from": attacker})
    deploy_byte_code.deployByteCode(
        "0x608060405234801561001057600080fd5b50600a8061001f6000396000f3fe602A60405260206040F3",
        # 0x600a600c600039600a6000f3602a60405260206040f3,
        {"from": attacker},
    )

    print(
        f"{green}Deployed Attack Contract Address: {red}{deploy_byte_code.addr()}{reset}"
    )

    # exit(-1)

    magic_num.setSolver(deploy_byte_code.addr(), {"from": attacker})

    print(f"{green}Solver Address: {red}{magic_num.solver()}{reset}")

    assert magic_num.solver() == deploy_byte_code.addr()

    attack_contract = interface.ICheckNum(deploy_byte_code.addr())

    assert attack_contract.whatIsTheMeaningOfLife() == 42

    print(
        f"{green}The Magic No. is: {red}{attack_contract.whatIsTheMeaningOfLife()}{reset}"
    )


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()
