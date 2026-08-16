# Challenge 3: Cookie Trust

This tiny training service makes an authorization decision using a cookie supplied by the browser.

## Start the service

From the repository root:

```bash
make cookie-trust
```

The server listens only on `127.0.0.1:8000` by default.

## Goal

Retrieve the runtime `flag{...}` from `/admin` without changing the server source code.

## Clues

- Inspect the cookie created for a normal visitor.
- Decide which data is controlled by the client.
- Browser developer tools or `curl` are enough.

## Defensive lesson

A server must verify authorization from trusted server-side state. Client-controlled cookies can carry identifiers, but sensitive claims need integrity protection and server-side validation.
