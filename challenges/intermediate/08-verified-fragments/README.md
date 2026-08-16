# Challenge 8: Verified Fragments

A synthetic evidence export was shuffled before it reached the analyst. Some rows are also decoys. The valid rows form one linked chain whose decoded payloads contain a flag.

## Goal

Recover the flag from [`records.jsonl`](records.jsonl).

## Record format

Each JSON line contains:

- `id`: the record identifier
- `previous`: the identifier of the preceding valid record, or `START` for the first record
- `payload_b64`: one Base64-encoded text fragment

A record is valid only when its `id` equals the first 12 hexadecimal characters of:

```text
SHA256(previous + ":" + payload_b64)
```

Start at `START`, verify candidate records before following them, Base64-decode each accepted payload, and concatenate the fragments. The valid chain is unique.

## Suggested tools

Python's `json`, `hashlib`, and `base64` modules are sufficient.

## Scope

All records are synthetic local data. The challenge requires no network access or external target.

## Lesson

Ordering evidence by timestamps or file position alone can be misleading. Verify integrity and provenance before reconstructing a sequence.
