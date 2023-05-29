// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface CoinFlip {
    function flip(bool _guess) external returns (bool);

    function consecutiveWins() external returns (uint);
    // function winCount() external returns (uint);
}
