#!/usr/bin/python3
from brownie import CaptureTheEther, NicknameChallenge, web3
from brownie.convert import to_bytes
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        capute_the_eth, nick_name, _ = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    # print(capute_the_eth.address, nick_name.address)
    # exit()
    print_colour(capute_the_eth.nicknameOf(attacker)[0])

    nickname = to_bytes("jadu".encode().hex(), "bytes")
    """
    for bytes32 the ans is gven by brownie is 
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00jadu'

    but the solidity compiler doesn't read the value like this(maybe)

    so that's why the next step is to convery the above into
    b'jadu\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
     
    """
    bytes_value = bytes(nickname) + b"\x00" * (32 - len(nickname))

    # print(bytes_value)

    tx = capute_the_eth.setNickname(bytes_value, {"from": attacker})
    tx.wait(1)

    print_colour(capute_the_eth.nicknameOf(attacker)[0])

    assert capute_the_eth.nicknameOf(attacker)[0] != 0


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()
