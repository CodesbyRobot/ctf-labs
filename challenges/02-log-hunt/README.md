# Challenge 2: Log Hunt

The file [`access.log`](access.log) contains synthetic web access records from a training environment. One client performed an unusual sequence and left a note in the final request.

## Goal

Find:

1. The suspicious client IP address.
2. The hidden `flag{...}` value.

## Clues

- Correlate requests by IP address and timestamp.
- Focus on repeated access to `/internal/export`.
- The `note` query parameter is encoded, not encrypted.

## Safety

All addresses use ranges reserved for documentation. They do not identify real systems.
