# Magic Number

<https://www.ethervm.io/>

- **PUSH1** 2A -> 42, push1 -> uint8, hex(42) -> 2A
- **PUSH1** 40 -> memory location 40

- **MSTORE** => syntax : [offset|value] -> top of stack = offset i.e. 40 & next item value i.e. 40 -> 2A.
MSTORE -> save the val

**stack is empty**

- as uint takes 32 bytes we have to pass the size
- **PUSH1** 20 -> length of the value; hex(32) -> 20
- **PUSH1** 40

- **RETURN** => syntax: [offset|length] -> top of stack -> offset i.e. memory location 40.
length i.e. 32 bytes -> 20
- **RETURN**

## Clean version

```c
command  -> opt code
PUSH1 2A -> 60 2A -> 602A
PUSH1 40 -> 60 40 -> 6040
MSTORE   -> 52    -> 52
PUSH1 20 -> 60 20 -> 6020
PUSH1 40 -> 60 40 -> 6040
RETURN   -> F3    -> F3
```

- final -> `602A60405260206040F3`

## Byte Code from remix IDE

```c
000 PUSH1 80
002 PUSH1 40
004 MSTORE
005 CALLVALUE
006 DUP1
007 ISZERO
008 PUSH2 0010
011 JUMPI
012 PUSH1 00
014 DUP1
015 REVERT
016 JUMPDEST
017 POP
018 PUSH1 b6 -> lenght of data
020 DUP1
021 PUSH2 001f
024 PUSH1 00
026 CODECOPY
027 PUSH1 00
029 RETURN
030 INVALID
```

### opt code of the above byte code

- original data

```c
0x608060405234801561001057600080fd5b5060b68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060285760003560e01c8063650500c114602d575b600080fd5b60336047565b604051603e91906067565b60405180910390f35b6000602a905090565b6000819050919050565b6061816050565b82525050565b6000602082019050607a6000830184605a565b9291505056fea2646970667358221220b95b89112dd01fca19270d4995891d7851c4a5bf62ec76e6781ecc44bb7be0ed64736f6c63430008110033
```

- As before retruning everything after the return will be copied to the block chain. As INVALID cmd is `fe` in opt code so the part after that will have to be removed. So now the opt code will look something like

```c
0x608060405234801561001057600080fd5b5060b68061001f6000396000f3fe
```

- But here we can only send of size 10 opt code. So we have to change the `b6` part so it should be. As `0a` -> `10` in int.

```c
0x608060405234801561001057600080fd5b5060 b6 8061001f6000396000f3fe
0x608060405234801561001057600080fd5b5060 0a 8061001f6000396000f3fe
0x608060405234801561001057600080fd5b50600a8061001f6000396000f3fe
```

- After that we have to add the 10 optcodes of data we derived earlier i.e. `602A60405260206040F3`. So the final byte code is

```c
0x608060405234801561001057600080fd5b50600a8061001f6000396000f3fe602A60405260206040F3
```

- another payload

```c
0x600a600c600039600a6000f3602a60405260206040f3
```
