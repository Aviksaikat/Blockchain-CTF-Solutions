// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface TokenInterface {
    function transfer(address _to, uint _value) external returns (bool);

    function balanceOf(address _address) external view returns (uint balance);
}
