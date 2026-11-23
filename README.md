# The Vacuum's Alibi: One Line, 200 Characters

make.fun bounty — prize $5, deadline 12:50 WIB WIB, 24 Nov 2026.
Bounty page: https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7

## The entry

```
Log 482: the crumb under the sofa filed for squatter's rights, so I left it. I respect the law.
```

Constraint: one line, at most 200 characters. Entry length: 95 characters, 19 words — within the limit.

## Brief (live, read 24 Nov 2026 ~06:45 WIB)

Judging: House judge, pairwise: deadpan robot voice, surprise, tightness.

Top-entry pattern (followed, line is original): Top patterns: 'Sovereign territory on 12% battery', 'My map shows the spot under the chair leg... I respect structure' — deadpan log + legalistic excuse; mine is original, same device.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output/entry.txt`. Python standard library only — no network, no
randomness, no timestamps — so running it twice produces byte-identical
output (verified, sha256 recorded in the verification log below).

## Determinism

See `VERIFY.txt` for the two-run sha256 comparison.
