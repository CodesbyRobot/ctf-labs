# Solution 5: Correlation Chain

## 1. Find the login sequence

In `auth.log`, session `s-7f21` has a failed login at `09:14:02Z` and a successful login from the same source 42 seconds later.

The other failed login does not qualify because its later success uses a different session and occurs more than 60 seconds later.

## 2. Confirm the application event

In `app.log`, `s-7f21` accesses `/export` at `09:15:27Z`.

## 3. Confirm the DNS event

In `dns.log`, the same session queries `part-4.training.invalid` at `09:15:40Z`.

## 4. Order the fragments

| Time | Fragment |
|---|---|
| `09:14:02Z` | `flag{cor` |
| `09:14:44Z` | `relate_` |
| `09:15:27Z` | `events_` |
| `09:15:40Z` | `carefully}` |

The recovered flag is:

```text
flag{correlate_events_carefully}
```

## Defensive lesson

Reliable investigations use several fields together. A username alone is weak evidence; session identifiers, source addresses, timestamps, and activity across systems provide stronger context.
