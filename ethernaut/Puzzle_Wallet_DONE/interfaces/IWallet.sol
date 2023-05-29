// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IWallet {
    function admin() external view returns (address);

    function owner() external view returns (address);

    function proposeNewAdmin(address _newAdmin) external;

    function addToWhitelist(address addr) external;

    function deposit() external payable;

    function multicall(bytes[] calldata data) external payable;

    function execute(
        address to,
        uint256 value,
        bytes calldata data
    ) external payable;

    function setMaxBalance(uint256 _maxBalance) external;

    function balances(address addr) external view returns (uint256);

    function balance() external view returns (uint256);
}
