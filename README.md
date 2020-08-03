# Substitution-Cipher-Breaker

This is a fast approach for breaking substitution cipher encryption, taken from following research paper:
https://www.researchgate.net/publication/266714630_A_fast_method_for_cryptanalysis_of_substitution_ciphers


The dictionary used to generate bigram is in ./book.txt

# Run - Encryption:
python3 EncryptionRunner.py

![Alt text](res/encryption.png?raw=true "Generate Encrypted Text using a Key")

# Run - Cipher Breaker:
python3 CipherBreakerRunner.py

![Alt text](res/keybreaker.png?raw=true "Retrive key using plaintext and cipher text, and compare retrieved key with actual key, to check accuracy")

![Alt text](res/consoleoutput.png?raw=true)


