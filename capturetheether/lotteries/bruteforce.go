package main;
import (
    "crypto/sha3"
    "encoding/hex"
    "fmt"
    "math/big"
)

var answerHash = "0xDB81B4D58595FBBBB592D3661A34CDCA14D7AB379441400CBFA1B78BC447C365" // Replace with your answer hash
var i = big.NewInt(0)

for {
    hash := sha3.Sum256(i.Bytes())
    if hex.EncodeToString(hash[:]) == answerHash {
        fmt.Println(hex.EncodeToString(hash[:]))
        break
    }
    i.Add(i, big.NewInt(1))
}

fmt.Println(i.String()) // Print the value of i as a string
