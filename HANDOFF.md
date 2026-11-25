# Handoff — One Word, First Thought

- 比赛：u-0xkianno-one-word-first-thought-106abaf8（$5，截止北京时间 2026-11-27 03:40）
- 文案（用户让 GPT 写好、亲口说照原样交，一字不改）：`Mooncrumb`
- 做法：`main.py` 把 `ENTRY = "Mooncrumb"` 以 UTF-8、二进制写入 `/output/entry.txt`，无尾随换行，不读外部文件，不联网；写完读回文件逐字节校验，与 ENTRY 一字不差否则报错退出（第二版加入的真正改进；第一版是直接写文件，跑通后再改写为带回读校验的版本）。
- 字符数：9 个字符 / 9 字节（纯 ASCII，字节数 = 字符数）
- 校验结果：
  - main.py 跑两次，退出码均为 0，两次输出 `cmp` 逐字节一致
  - entry.txt 与 `Mooncrumb` exact match，`od -c` 显示 `M o o n c r u m b`，无尾随换行
  - sha256：`dc3a2f28fe3987fc75b5dc763bee22e7fc382e400369cd6cdb4c1df23b5c17a3`
  - prompt.txt 与 entry.txt 逐字节一致
- 状态：未提交、未建 GitHub 仓、未碰 bundle，等上游打包提交。
