# Solution: Encoding Trail

The artifact contains hexadecimal characters, so decode hex first. The result is Base64 text. Decode Base64, then apply ROT13.

```python
import base64
import codecs
from pathlib import Path

value = Path("challenges/01-encoding-trail/artifact.txt").read_text().strip()
layer_2 = bytes.fromhex(value)
layer_1 = base64.b64decode(layer_2).decode()
flag = codecs.decode(layer_1, "rot_13")
print(flag)
```

Flag: `flag{encoding_is_not_encryption}`

## Defensive takeaway

Hex, Base64, and ROT13 can obscure text from a casual glance, but anyone can reverse them without a key.
