package main

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"github.com/ethereum/go-ethereum/accounts/abi/bind"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/rlp"
	"github.com/ethereum/go-ethereum/ethclient"
	"log"
	"strings"
)

func main() {
	client, err := ethclient.Dial("http://localhost:7545")
	if err != nil {
		log.Fatal(err)
	}

	// Contract address
	var contractAddress common.Address

	privateKey, err := crypto.GenerateKey()
	if err != nil {
		log.Fatal(err)
	}

	// We can calculate the address of the resulting smart contract before deploying it, so we will brute force the generation of EOA until the contract they generate with their first NONCE contains the specified word
	counter := 0

	for {
		privateKeyBytes := make([]byte, 32)
		_, err := rand.Read(privateKeyBytes)
		if err != nil {
			log.Fatal(err)
		}
		newKey, err := crypto.ToECDSA(privateKeyBytes)
		if err != nil {
			log.Fatal(err)
		}

		publicKey := newKey.Public()
		publicKeyECDSA, ok := publicKey.(*crypto.ECDSAPublicKey)
		if !ok {
			log.Fatal("cannot assert type: publicKey is not of type *ecdsa.PublicKey")
		}
		fromAddress := crypto.PubkeyToAddress(*publicKeyECDSA)
		nonce, err := client.PendingNonceAt(fromAddress)
		if err != nil {
			log.Fatal(err)
		}
		contractAddressBytes := crypto.CreateAddress(fromAddress, nonce)
		contractAddress = common.BytesToAddress(contractAddressBytes)
		
		fmt.Println(privateKey, contractAddress)

		if strings.Contains(contractAddress.Hex(), "badc0de") {
			fmt.Println("found:", hex.EncodeToString(privateKeyBytes))
			fmt.Println("contract address:", contractAddress.Hex())
			break
		}

		counter += 1

		if counter%1000 == 0 {
			fmt.Printf("Checked %d addresses\n", counter)
		}
	}
}
