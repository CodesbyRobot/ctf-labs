# Solution: PNG Breadcrumb

PNG files contain chunks. This image includes a `tEXt` chunk with a `Comment` field. A quick approach on many systems is:

```bash
strings challenges/04-png-breadcrumb/evidence.png | grep 'flag{'
```

A metadata viewer or a small PNG chunk parser finds the same value.

Flag: `flag{metadata_can_talk}`

## Defensive takeaway

Metadata can survive file copying and may expose internal notes, locations, usernames, or other sensitive context. Review and sanitize metadata before publication.
