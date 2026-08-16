# Challenge 7: Orbital Reuse

A synthetic incident report was protected with repeating-key XOR. The author reused a short uppercase ASCII key, so the ciphertext leaks more structure than intended.

## Goal

Recover the flag in the form `flag{...}` from [`cipher.hex`](cipher.hex).

## Known facts

- The plaintext begins exactly with `Incident report:`.
- The key contains only uppercase ASCII letters.
- The key is shorter than 12 bytes and repeats from byte zero.
- The artifact is hexadecimal text representing the raw ciphertext bytes.

## Suggested tools

Python's standard library is enough. Convert the hex text to bytes, use the known plaintext to expose part of the keystream, identify its shortest repeating period, and decrypt the full report.

## Scope

This is an offline, synthetic cryptography exercise. It does not require a service, account, or network target.

## Lesson

Repeating-key XOR is vulnerable when an attacker knows or can guess part of the plaintext. A repeated keystream is not a substitute for authenticated encryption with a unique nonce.
