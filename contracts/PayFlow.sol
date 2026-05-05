// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PayFlow {

    mapping(string => int256) public balances;

    function updateBalance(string memory user, int256 amount) public {
        balances[user] += amount;
    }

    function getBalance(string memory user) public view returns (int256) {
        return balances[user];
    }
}