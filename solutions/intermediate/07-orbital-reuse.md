# Solution 7: Orbital Reuse

The known plaintext reveals the beginning of the keystream because repeating-key XOR satisfies:

```text
key_byte = ciphertext_byte XOR plaintext_byte
```

Use the known report prefix, then look for the shortest repeating period in the recovered keystream.

```python
from pathlib import Path

ciphertext = bytes.fromhex(
    Path("challenges/intermediate/07-orbital-reuse/cipher.hex")
    .read_text()
    .strip()
)
known = b"Incident report:"

keystream_sample = bytes(
    encrypted ^ plain
    for encrypted, plain in zip(ciphertext, known)
)

key = None
for length in range(1, 12):
    if all(
        keystream_sample[index] == keystream_sample[index % length]
        for index in range(len(keystream_sample))
    ):
        candidate = keystream_sample[:length]
        if candidate.isalpha() and candidate.isupper():
            key = candidate
            break

if key is None:
    raise RuntimeError("No repeating uppercase key found")

plaintext = bytes(
    byte ^ key[index % len(key)]
    for index, byte in enumerate(ciphertext)
)

print("key:", key.decode())
print(plaintext.decode())
```

The shortest valid key is:

```text
ORBITAL
```

The decrypted report contains:

```text
flag{repeating_xor_needs_random_keys}
```

## Defensive lesson

A repeated XOR key exposes relationships between plaintext and ciphertext. Use a reviewed authenticated-encryption construction, generate nonces as required by that construction, and never reuse a keystream.
