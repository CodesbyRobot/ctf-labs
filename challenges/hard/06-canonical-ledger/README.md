# Challenge 6: Canonical Ledger

A local training service writes an append-only JSON Lines audit ledger. Each record stores the SHA-256 digest of a canonical representation of its fields and points to the previous stored digest.

One record's `action` label was changed after its digest was created. Its other fields and stored digest were left untouched.

## Goal

1. Identify the modified record by sequence number.
2. Infer its intended `action` label.
3. Base64-decode the payloads belonging to `flag-part-N` actions and join them in numeric order.
4. Explain why an unkeyed hash chain can reveal this edit but cannot authenticate who created the ledger.

## File

- [`audit.jsonl`](audit.jsonl)

## Digest rules

For each record, build a new object containing exactly these fields:

```text
seq, ts, actor, action, payload, prev
```

Serialize it as UTF-8 JSON with:

- keys sorted alphabetically;
- no spaces between separators;
- standard JSON string escaping.

In Python, the canonical form is equivalent to:

```python
json.dumps(body, sort_keys=True, separators=(",", ":"))
```

The stored `digest` should equal the lowercase hexadecimal SHA-256 digest of that canonical byte string. The first record's `prev` value is 64 zeroes; every later `prev` value should equal the preceding stored digest.

## Constraints

Use only the supplied local file. No service, account, credential, or external network target is involved.

## Lesson

Deterministic serialization matters when verifying structured data. A hash chain can expose inconsistency, but authentication requires a trusted secret, signature, or external anchor.
