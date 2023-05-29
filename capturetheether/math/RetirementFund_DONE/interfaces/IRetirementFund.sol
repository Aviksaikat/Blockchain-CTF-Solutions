pragma solidity ^0.4.21;

interface RetirementFundChallengeInterface {
    // function balance(address _contract) external view returns (uint256);
    function withdraw() public;
    function collectPenalty() public;
    function isComplete() external view returns (bool);
}