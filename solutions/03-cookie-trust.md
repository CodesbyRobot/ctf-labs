# Solution: Cookie Trust

The service stores the role directly in a client-controlled cookie and accepts the value without integrity checks. Replace `role=guest` with `role=admin`, then request `/admin`.

Against the included localhost service:

```bash
curl -s -H 'Cookie: role=admin' http://127.0.0.1:8000/admin
```

The returned flag changes on each run unless the organizer sets `CTF_FLAG`.

## Defensive fix

Do not use an unsigned client value as the authorization source. Keep roles in server-side session state, or use a correctly signed token and still validate authorization on every protected action.
