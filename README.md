# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![make.fun rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/konzlodon74-dot/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![make.fun reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun bounty "The Houseplant Out-of-Office"](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047): write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer.

## The line

> Out of office: I'm the fern. No water since March. If I reply, it's a miracle. If I don't, I've composted myself.

113 characters. The fern by the window has been ignored since March; its reply is a miracle, its silence is compost.

## Run

```sh
python3 main.py
```

Prints exactly that one line, deterministically. When run inside the make.fun
sandbox it also writes the same text to `/output/entry.txt`, where the gate
scorer reads it. Python 3 standard library only, no dependencies.
