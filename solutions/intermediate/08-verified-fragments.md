# Solution 8: Verified Fragments

Do not follow the `previous` links until each row's identifier has been recomputed. Filtering first removes every decoy and leaves one child for each valid predecessor.

```python
import base64
import hashlib
import json
from pathlib import Path

path = Path("challenges/intermediate/08-verified-fragments/records.jsonl")
records = [json.loads(line) for line in path.read_text().splitlines()]

by_previous = {}
for record in records:
    material = f"{record['previous']}:{record['payload_b64']}".encode()
    expected = hashlib.sha256(material).hexdigest()[:12]
    if record["id"] != expected:
        continue
    by_previous.setdefault(record["previous"], []).append(record)

previous = "START"
fragments = []
seen = set()

while previous in by_previous:
    candidates = by_previous[previous]
    if len(candidates) != 1:
        raise RuntimeError(f"Ambiguous chain after {previous}: {candidates}")

    record = candidates[0]
    if record["id"] in seen:
        raise RuntimeError("Cycle detected")
    seen.add(record["id"])

    fragments.append(
        base64.b64decode(record["payload_b64"], validate=True).decode()
    )
    previous = record["id"]

print("".join(fragments))
```

The verified chain is:

```text
START
  -> 3744a70d9026
  -> 2e21de4572ec
  -> 7aa6cdd5c59d
  -> d3db189113ce
  -> 6dacd88ce891
  -> 87863ae7aa72
  -> 3fc2f99c2ad3
```

The decoded flag is:

```text
flag{linked_records_need_verified_ordering}
```

## Defensive lesson

Integrity metadata is useful only when it is actually checked. In a production evidence pipeline, prefer authenticated records or digital signatures anchored to a trusted key, not unkeyed hashes supplied alongside potentially hostile data.
