from blockchain import Blockchain

if __name__ == "__main__":
    
    my_blockchain = Blockchain()

    print("\n" + "="*50)
    print("ADDING BLOCKS:")
    my_blockchain.add_block(data={"sender": "Alice", "receiver": "Bob", "amount": 50})
    my_blockchain.add_block(data="Second data block")
    my_blockchain.add_block(data={"note": "Final payment"})

    print("\n" + "="*50)
    print("FULL BLOCKCHAIN CONTENT:")
    for block in my_blockchain.chain:
        print(block)
        print("-"*20)

    print("\n" + "="*50)
    print("CHAIN VALIDATION CHECK (Initial):")
    if my_blockchain.is_chain_valid():
        print("The Blockchain is VALID and secured.")
    else:
        print("The Blockchain is INVALID.")
        
    print("\n" + "="*50)
    print("TAMPERING TEST:")
    my_blockchain.chain[2].data = {"note": "MALICIOUSLY CHANGED DATA"}
    
    
    print("Block 2 data has been tampered with (data changed, hash not re-mined).")

    print("Re-validating chain after tampering:")
    if my_blockchain.is_chain_valid():
        print("The Blockchain is VALID (ERROR!)")
    else:
        print("The Blockchain is INVALID, Tampering Detected.")