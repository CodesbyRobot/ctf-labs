# Challenge 5: Correlation Chain

A local training environment produced three synthetic logs: authentication, application access, and DNS activity. Several sessions are harmless decoys.

## Goal

Recover the flag in the form `flag{...}`.

Find the single session that meets all of these conditions:

1. A failed login is followed by a successful login from the same source within 60 seconds.
2. The session accesses `/export`.
3. The session queries `part-4.training.invalid`.

After finding the session, collect its `fragment` values from all three logs and order them by timestamp.

## Files

- [`auth.log`](auth.log)
- [`app.log`](app.log)
- [`dns.log`](dns.log)

## Boundaries

The IP addresses use documentation-only ranges, and `.invalid` is a reserved non-resolving domain. Analyze only the supplied files; no network access is needed.

## Lesson

A single event may look ordinary. Correlation across identity, time, source, and session context can reveal the full sequence.
