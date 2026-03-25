# Plain-Text Format

The generator accepts a UTF-8 `.txt` file directly.

## Recommended format

```text
标题：女生节心愿礼物抽选
副标题：给你们准备了一点女生节的小惊喜。选一句最像自己的小心思，看看今天落到你手里的，会是哪一份可爱礼物。
提示：轻轻点开一张小卡片，开奖属于你的女生节惊喜。
底部文案：愿今天的快乐不止女生节限定，愿你们被偏爱、被惦记，也一直闪闪发光。

选项：
1. 休闲时刻喜欢打打麻将
2. 喜欢开盲盒
3. 喜欢摸可爱的小猫猫

礼物：
1. 麻将魔方
2. 猫猫情绪盲盒
3. 猫猫情绪盲盒

祝福：
1. 愿你手气和脑力都在线，课业生活都能一把胡。
2. 愿你的惊喜感永远在线，拆开的每一天都有小确幸。
3. 愿你像小猫一样被温柔接住，撒娇自由，快乐也自由。
```

## Faster format

You can also write one entry per line:

```text
标题：女生节心愿礼物抽选

条目：
1. 休闲时刻喜欢打打麻将 | 麻将魔方 | 愿你手气和脑力都在线，课业生活都能一把胡。
2. 喜欢开盲盒 | 猫猫情绪盲盒 | 愿你的惊喜感永远在线，拆开的每一天都有小确幸。
3. 喜欢摸可爱的小猫猫 | 猫猫情绪盲盒
```

If a blessing is omitted, the generator creates a default one automatically.
