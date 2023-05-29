pragma solidity ^0.4.21;

interface TokenWhaleChallengeInterface {
    function balanceOf(address _owner) external view returns (uint256 balance);
    function transfer(address _to, uint256 _value) external returns (bool success);
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success);
    function approve(address _spender, uint256 _value) external returns (bool success);
    function allowance(address _owner, address _spender) external view returns (uint256 remaining);
    function isComplete() external view returns (bool);
    function player() external view returns (address);
    function totalSupply() external view returns (uint256);
    function name() external view returns (string);
    function symbol() external view returns (string);
    function decimals() external view returns (uint8);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}
