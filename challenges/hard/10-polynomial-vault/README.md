# Challenge 10: Polynomial Vault

A synthetic backup system represented a secret message as coefficients of a polynomial over the finite field modulo 257. The coefficient bytes were discarded, but 42 polynomial evaluations remain in [`vault.json`](vault.json).

## Goal

Recover the coefficient bytes in order and submit the resulting `flag{...}` value.

## Encoding model

Let the unknown bytes be `c[0]` through `c[n-1]`. For each stored point `x`, the corresponding value is:

```text
y = c[0] + c[1]x + c[2]x^2 + ... + c[n-1]x^(n-1)  (mod p)
```

The JSON file supplies:

- prime modulus `p = 257`
- the coefficient count
- distinct `x_values`
- matching `y_values`
- a SHA-256 digest of the recovered byte string for validation

Because all `x` coordinates are distinct in the field and the number of points equals the number of coefficients, the system has one solution.

## Suggested approach

Build the Vandermonde matrix and solve the augmented linear system with Gaussian elimination modulo 257. Every recovered coefficient should be in the byte range `0..255`.

## Scope

This is a local, synthetic mathematics and cryptography exercise. It has no service, credential, or external target.

## Lesson

Finite-field equations can be solved exactly without floating-point arithmetic. They also demonstrate why deterministic algebraic encodings alone provide no confidentiality.
