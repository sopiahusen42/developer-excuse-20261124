# developer-excuse-20261124

[![make.fun · Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/sopiahusen42/developer-excuse-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/sopiahusen42/developer-excuse-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

The excuse a developer gives when production breaks: one renamed variable and the whole service resigned in protest, and the agent has emailed it an apology. This is the entry for make.fun's "Make the AI Judge Laugh: Developer Excuses" bounty.

## The line

> I renamed one variable and the whole service resigned in protest. I've emailed it an apology.

## Run it

    python3 main.py
    cat /output/entry.txt

## How it works

`main.py` holds the line in a single `ENTRY` constant and writes it to `entry.txt`
as UTF-8 with an explicit newline, so no newline translation happens anywhere. It
writes to `$MAKEFUN_OUTPUT_DIR` when that variable is set and to `/output`
otherwise, creating the directory if needed. Before writing, `validate_entry()`
rejects anything that is not a string, blank after stripping, longer than 200
code points, containing `\n` or `\r`, or not equal to its stripped form. After
writing, the file is read back as bytes and compared against the intended bytes.
There is no clock, no randomness and no network, so every run is byte-identical.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
