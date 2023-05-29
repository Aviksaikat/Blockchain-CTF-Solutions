use rand::Rng;
use web3::signing::{keccak256, Signature};
use web3::types::{Address, U256};
use web3::transports::Http;

fn main() {
    let address = Address::from_slice(&[0u8; 20]);

    let http = Http::new("http://localhost:8545").unwrap();
    let web3 = web3::Web3::new(http);

    let result = web3.eth().transaction_count(address, None).unwrap();
    println!("Transaction count: {}", result);

    let private_key = keccak256(b"my_private_key");
    let private_key_str = format!("0x{}", hex::encode(private_key));
    let secret_key = web3::signing::SecretKey::from_str(&private_key_str).unwrap();

    let mut rng = rand::thread_rng();
    let nonce: U256 = rng.gen();

    let transaction = web3::types::TransactionRequest {
        from: address,
        to: Some(address),
        nonce: Some(nonce),
        gas_price: None,
        gas: None,
        value: Some(U256::from(100)),
        data: None,
        chain_id: None,
    };

    let signature = web3::signing::sign_transaction(&transaction, &secret_key, &web3).unwrap();
    let (r, s, v) = signature.rsv();

    let recovered_address = web3::signing::recover(&transaction, &signature).unwrap();

    assert_eq!(recovered_address, address);
}
