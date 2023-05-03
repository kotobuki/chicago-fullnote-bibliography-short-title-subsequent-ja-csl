# chicago-fullnote-bibliography-short-title-subsequent-ja.csl

[Chicago Manual of Style 17th edition (full note, short title subsequent)](https://www.zotero.org/styles?q=id%3Achicago-fullnote-bibliography-short-title-subsequent)を[CSL](https://citationstyles.org/)（Citation Style Language）の拡張版である[CSL-M](https://citeproc-js.readthedocs.io/en/latest/csl-m/index.html)に対応させ、文献の`language`に従って日本語（`ja`）でも表記できるようにするためのCSLファイルです。

## オリジナル版からの変更点

- 英文における`, `と`. `の代わりに`、`と`。`を使う
- 書籍名や雑誌名をイタリックにする代わりに`『`と`』`で囲む
- 書籍名や論文名の前に登場する、日本語では不要な`、`（例：著者名`、`『書籍名』）を省略する

## 使い方

- [Jurism](https://juris-m.github.io/)にインポートして使う
- [Pandoc](https://pandoc.org/)およびそのフィルター[citeproc-js-based-replacer](https://github.com/kotobuki/citeproc-js-based-replacer)と組み合わせて使う
- LaTeXおよび[citeproc-lua](https://github.com/zepinglee/citeproc-lua)と組み合わせて使う

## 例

```json
[
  {
    "id": "morgan2023jiyu",
    "author": [
      { "family": "Morgan", "given": "Casey" },
      { "family": "Patrov", "given": "Alexei" }
    ],
    "citation-key": "morgan2023jiyu",
    "event-place": "東京",
    "issued": { "date-parts": [[2023]] },
    "language": "ja",
    "original-date": { "date-parts": [[2022]] },
    "original-publisher": "Global Academic Press",
    "original-publisher-place": "Chicago, IL",
    "original-title": "The Philosophy of Free Will",
    "publisher": "城南大学出版会",
    "publisher-place": "東京",
    "title": "自由意志の哲学",
    "translator": [{ "family": "鈴木", "given": "真紀" }],
    "type": "book"
  }
]
```

`Note` Casey Morgan、Alexei Patrov『自由意志の哲学』訳：鈴木真紀（東京:城南大学出版会、2023）。〔*The Philosophy of Free Will* (Chicago, IL: Global Academic Press, 2022).〕

`Bibliography entry` Morgan, Casey、Alexei Patrov『自由意志の哲学』翻訳：鈴木真紀、東京：城南大学出版会、2023。〔*The Philosophy of Free Will* (Chicago, IL: Global Academic Press, 2022).〕

注：これは架空の文献です。

## 既知の問題

- [　] [citeproc-js](https://github.com/Juris-M/citeproc-js)ベースのツールで使用する際、日本語に翻訳された文献におけるラテン系の著者名等が`given name` `family name`ではなく日本語と同様の`family name` `given name`になってしまう。
