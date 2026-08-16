# Solution: Log Hunt

Group the requests by source IP and inspect requests to `/internal/export`. `203.0.113.77` makes three such requests within eight seconds. The final URL includes a Base64-encoded `note` value.

```python
import base64
from urllib.parse import parse_qs, urlsplit

path = "/internal/export?format=txt&note=ZmxhZ3tsb2dzX3RlbGxfYV9zdG9yeX0="
note = parse_qs(urlsplit(path).query)["note"][0]
print(base64.b64decode(note).decode())
```

Suspicious client: `203.0.113.77`

Flag: `flag{logs_tell_a_story}`

## Defensive takeaway

Single log lines often look harmless. Correlation by source, endpoint, and time reveals the sequence.
