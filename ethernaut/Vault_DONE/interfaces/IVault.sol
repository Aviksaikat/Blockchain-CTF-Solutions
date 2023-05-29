//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface Vault {
    function unlock(bytes32 _password) external;

    function locked() external view returns (bool);
}
