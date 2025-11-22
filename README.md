#####################################################################################""


for run Use
cd blockchaintp1
then:
python main.py



i wont lie i used AI but i did a lot work by myself too so ,i hope u will like my work
i started working on my own pc then i changed to github you wont see my code starting from scratch
and about this page i didnt know how to explain all the code by myself so used a little bit of AI for organizational purposes
i worked with soheyb fassi 
down you will find mywork 
 ||
_||_
\  /
 \/
 thank you for your time

###################################################################################################################""





# Minimal Blockchain Implementation in Python

This repository presents a concise, functional implementation of a fundamental blockchain using native Python libraries. The project demonstrates core principles including block structure, hashing, Proof-of-Work (PoW), and chain integrity validation.

## Implemented Features

The following features comply with all project requirements, including optional extensions for comprehensive evaluation:

| Feature | Implementation Detail |
|
| **Block Structure** | Includes all required fields: `index`, `timestamp`, `data`, `previous_hash`, `nonce`, and `hash`. |
| **Hashing Algorithm** | Utilizes `hashlib.sha256()` to ensure cryptographic integrity. |
| **Proof-of-Work (PoW)** | Difficulty is set to **4** . The `nonce` is iteratively incremented until the condition is satisfied. |
| **Chain Validation** | The `is_chain_valid()` function verifies block linkage, confirms adherence to PoW difficulty, and detects data tampering. |
| **Mining Time Measurement** | The elapsed time required for the PoW calculation for each block is measured and reported. |
| **Average Nonce Count** | The average `nonce` value across all mined blocks is calculated and displayed. |