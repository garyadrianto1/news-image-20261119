# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/garyadrianto1/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/garyadrianto1/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-page newspaper front page summing up Thursday 19 November 2026's world news in a single 1024×1024 image: 36 stories — 3 illustrated leads (the first Trump–Xi–Putin three-way summit in Shenzhen, GTA VI launch day, the World Court's genocide ruling on Myanmar), 10 medium stories, a world map with numbered pins, and 23 one-liners. Every story happened or was first reported on that Thursday, and a DATE CHECK box lists what was deliberately left out (18 November news) and what had not happened yet. The page was rendered with Python + PIL from a hand-drawn flat-vector layout (no photos, no AI-generated imagery); the entry program simply copies the finished image to `/output/entry.png`, validating its PNG magic, size, and dimensions first.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=m1ceh0z1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
