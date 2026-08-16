# Solution 6: Canonical Ledger

## 1. Verify the chain and record digests

Run this script from the repository root:

```python
import hashlib
import json
from pathlib import Path

path = Path("challenges/hard/06-canonical-ledger/audit.jsonl")
records = [json.loads(line) for line in path.read_text().splitlines()]
fields = ("seq", "ts", "actor", "action", "payload", "prev")
previous = "0" * 64

for record in records:
    if record["prev"] != previous:
        print(f"sequence {record['seq']}: previous-digest link mismatch")

    body = {field: record[field] for field in fields}
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"))
    computed = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    if computed != record["digest"]:
        print(f"sequence {record['seq']}: digest mismatch")

    previous = record["digest"]
```

The output identifies sequence `5` as the only record whose stored digest does not match its current contents.

## 2. Infer the changed label

The ledger contains `flag-part-1`, `flag-part-2`, and `flag-part-4`. Sequence 5 is an analyst record between parts 2 and 4, and the challenge states that one action label was changed while its payload remained intact. Its intended label is therefore:

```text
flag-part-3
```

## 3. Decode and join the payloads

```python
import base64

parts = {
    1: "ZmxhZ3tjYW5vbmljYWxf",
    2: "anNvbl9hbmRf",
    3: "aGFzaF9jaGFpbnNf",
    4: "bmVlZF9jb250ZXh0fQ==",
}

flag = "".join(base64.b64decode(parts[number]).decode() for number in sorted(parts))
print(flag)
```

The recovered flag is:

```text
flag{canonical_json_and_hash_chains_need_context}
```

## Why the edit is detectable

Changing sequence 5's `action` changes its canonical byte representation. Recomputing SHA-256 therefore produces a value different from the stored digest.

## Why the chain is not authentication

SHA-256 uses no secret. An attacker able to rewrite the ledger could alter a record and recompute that record plus every later digest. A production design needs an HMAC with a protected key, a digital signature, or a trusted external checkpoint. Canonicalization and hashing provide consistency checks, not proof of origin by themselves.
