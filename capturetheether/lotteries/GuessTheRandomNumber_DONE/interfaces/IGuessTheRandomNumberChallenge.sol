// SPDX-License-Identifier: MIT
pragma solidity ^0.4.21;

interface GuessTheRandomNumberChallenge { 
    function owner() external view returns (address);
    function isComplete() external view returns (bool);

    function guess(uint8 n) public payable;
}