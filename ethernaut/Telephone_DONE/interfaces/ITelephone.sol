// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface Telephone {
    function changeOwner(address _address) external;

    function owner() external view returns (address payable);
}
