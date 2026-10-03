"""CUE Split Tracks — Split a single audio file into tracks using a CUE sheet."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='cue_split_tracks',
        description='Split a single audio file into tracks using a CUE sheet.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('CUE Split Tracks')
    print('One image + CUE into per-track files.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
