# The One-Line Exit

[![Make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/aldy007x/one-line-exit/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/aldy007x/one-line-exit/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

A make.fun bounty entry for "The One-Line Exit": a program that writes
exactly one resignation letter, exactly one line long, to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

The letter is an original one-liner in the voice of a weary office worker
who has finally lost a three-year feud with the office printer — formal
enough to send, funny enough to remember. `main.py` (Python 3.13, stdlib
only, no network, deterministic) holds the line as a plain string constant,
writes it to `entry.txt`, then reads the file back and verifies it is
exactly one non-blank line of 1–140 characters, exiting non-zero on failure.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
