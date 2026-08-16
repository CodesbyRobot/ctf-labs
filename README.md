# CTF Labs

Beginner-friendly Capture the Flag projects designed for ethical, contained practice. Every challenge runs from local files or a service bound to `127.0.0.1`.

## Ground rules

- Use these labs only on your own computer or in an environment where you have explicit permission.
- Do not redirect the examples toward public hosts, third-party accounts, or real credentials.
- Keep challenge data synthetic. The IP addresses in the logs are documentation-only ranges.
- Treat the solutions as spoilers. Try each challenge first, then compare your approach.

## Challenges

| # | Challenge | Category | Difficulty | Main lesson |
|---|---|---|---|---|
| 1 | [Encoding Trail](challenges/01-encoding-trail/) | Encoding | Easy | Encoding layers are reversible and are not encryption |
| 2 | [Log Hunt](challenges/02-log-hunt/) | Log analysis | Easy | Events become meaningful when correlated by time and source |
| 3 | [Cookie Trust](challenges/03-cookie-trust/) | Web | Easy | Authorization decisions must not trust client-controlled state |
| 4 | [PNG Breadcrumb](challenges/04-png-breadcrumb/) | File forensics | Easy | Metadata can reveal useful evidence |

## Quick start

```bash
git clone https://github.com/CodesbyRobot/ctf-labs.git
cd ctf-labs
make test
```

The repository uses only Python's standard library. Python 3.10 or later is recommended.

Run the web challenge:

```bash
make cookie-trust
```

Then open `http://127.0.0.1:8000` in a browser. Stop the server with `Ctrl+C`.

## Solutions

Spoilers are stored in [`solutions/`](solutions/).

## For educators

These labs work well as short classroom exercises. You may change flags, remove the solution directory from participant copies, or add a lightweight scoreboard. The web challenge creates a fresh flag on each run unless `CTF_FLAG` is set.

## License

MIT. See [LICENSE](LICENSE).
