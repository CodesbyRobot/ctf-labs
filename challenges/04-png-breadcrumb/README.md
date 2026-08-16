# Challenge 4: PNG Breadcrumb

A harmless image was copied from a training workstation. The visible pixels are not the whole story.

## Goal

Inspect [`evidence.png`](evidence.png) and recover the `flag{...}` value.

## Clues

- PNG files are made of named chunks.
- Some chunks store human-readable metadata.
- Image editors, metadata tools, `strings`, or a small parser may help.

## Rebuild the artifact

```bash
make rebuild-png
```

The build script uses only Python's standard library and documents exactly how the synthetic evidence was created.
