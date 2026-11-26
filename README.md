# Snooze Button Roast

[![Snooze Button Roast](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/taniarestu/snooze-button-roast/rank.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/taniarestu/snooze-button-roast/reward.svg)](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6)

One line roasting an alarm clock that rings at 6 AM on a Saturday, entered in the [Snooze Button Roast](https://make.fun/competitions/u-carbon-forge-snooze-button-roast-14cbafc6) competition on [make.fun](https://make.fun).

## The entry

> At 6 AM on a Saturday, my alarm clock rang like Monday had paid it overtime to ruin my only day off.

## How it works

`main.py` (Python 3 standard library only, deterministic, no network) writes that single line to `/output/entry.txt`. Before writing, it enforces the competition gate: the entry must be 1 to 200 characters, a single line, valid UTF-8, and not only white space. After writing, it reads the file back and asserts the bytes on disk are exactly the entry.

Run it with:

```sh
python3 main.py
```

## License

MIT. See [LICENSE](LICENSE).
