#!/usr/bin/python3
import rlp
from brownie import Recovery, SimpleToken
from eth_utils import keccak, to_bytes, to_checksum_address
from scripts.helpful_scripts import get_account


def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.

    # https://ethereum.stackexchange.com/a/761/620
    """
    #! newAddress = keccak256_encode(rlp_encode(sender_address, nonce))
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)


def deploy():
    owner, _ = get_account()
    # st = SimpleToken.deploy("jadu", owner, 100000000, {"from": owner})
    rcv = Recovery.deploy({"from": owner})
    rcv.generateToken("jadu", 100000000, {"from": owner})

    print(f"Contract Deployed to: {rcv.address}")
    genetated_addr = mk_contract_address(rcv.address, 1)
    print(genetated_addr)

    # * sending a whole eth just for testing
    owner.transfer(genetated_addr, "1 ether")

    return genetated_addr, rcv, owner


def main():
    deploy()
