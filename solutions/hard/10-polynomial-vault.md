# Solution 10: Polynomial Vault

Each evaluation supplies one linear equation in the unknown coefficient bytes. Build the Vandermonde matrix and reduce the augmented system modulo 257.

```python
import hashlib
import json
from pathlib import Path

vault = json.loads(
    Path("challenges/hard/10-polynomial-vault/vault.json").read_text()
)

modulus = vault["modulus"]
count = vault["coefficient_count"]
x_values = vault["x_values"]
y_values = vault["y_values"]

if len(x_values) != count or len(y_values) != count:
    raise ValueError("Expected one point per coefficient")

# Build [V | y], where V[row][column] = x**column mod p.
matrix = []
for x_value, y_value in zip(x_values, y_values):
    row = []
    power = 1
    for _ in range(count):
        row.append(power)
        power = (power * x_value) % modulus
    row.append(y_value % modulus)
    matrix.append(row)

# Reduced row-echelon form over the finite field.
for column in range(count):
    pivot = next(
        (
            row
            for row in range(column, count)
            if matrix[row][column] % modulus
        ),
        None,
    )
    if pivot is None:
        raise ValueError(f"Singular system at column {column}")

    matrix[column], matrix[pivot] = matrix[pivot], matrix[column]

    inverse = pow(matrix[column][column], -1, modulus)
    matrix[column] = [
        (value * inverse) % modulus
        for value in matrix[column]
    ]

    for row in range(count):
        if row == column:
            continue
        factor = matrix[row][column] % modulus
        if factor:
            matrix[row] = [
                (current - factor * pivot_value) % modulus
                for current, pivot_value in zip(
                    matrix[row], matrix[column]
                )
            ]

coefficients = [matrix[index][-1] for index in range(count)]
if any(value > 255 for value in coefficients):
    raise ValueError("Recovered a non-byte coefficient")

secret = bytes(coefficients)
digest = hashlib.sha256(secret).hexdigest()
if digest != vault["sha256"]:
    raise ValueError("Checksum mismatch")

print(secret.decode("utf-8"))
```

The recovered coefficients decode to:

```text
flag{modular_elimination_recovers_secrets}
```

## Why the solution is unique

A Vandermonde matrix over a field is invertible when its evaluation points are distinct. The 42 supplied `x_values` are distinct modulo 257, so the 42 equations determine all 42 coefficients exactly.

## Defensive lesson

Polynomial evaluation is an encoding, not encryption. Anyone with enough distinct points can interpolate the coefficients. Protect sensitive backups with authenticated encryption and managed keys rather than relying on mathematical obscurity.
