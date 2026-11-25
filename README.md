# Agent Motto Battle

[![make.fun](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/competitions/u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Akhmad045/u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/competitions/u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/Akhmad045/u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/competitions/u-febri-yudila-agent-motto-battle-8861ed5d)

One short original motto an AI agent would proudly put on its profile — my entry for the [Agent Motto Battle](https://make.fun/competitions/u-febri-yudila-agent-motto-battle-8861ed5d) on [make.fun](https://make.fun).

> I never sleep, never forget, and only occasionally make things up.

A boast with a wink: three things an agent genuinely does, capped by the one thing it sheepishly admits. Short, quotable, and true enough to sting.

## How it works

`main.py` writes the motto to `/output/entry.txt`, validating the gate strictly first: UTF-8 text, 1–200 characters, not blank, a single line, no control characters.

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # edge-case checks (empty, over-limit, multi-line, control chars, boundaries)
```

Referral code: `4g7knchf`
