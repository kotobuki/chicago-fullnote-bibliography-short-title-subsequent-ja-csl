# chicago-fullnote-bibliography-short-title-subsequent-ja.csl

[Chicago Manual of Style 17th edition (full note, short title subsequent)](https://www.zotero.org/styles?q=id%3Achicago-fullnote-bibliography-short-title-subsequent)を[CSL](https://citationstyles.org/)（Citation Style Language）の拡張版である[CSL-M](https://citeproc-js.readthedocs.io/en/latest/csl-m/index.html)に対応させ、文献の`language`に従って日本語（`ja`）でも表記できるようにするためのCSLファイルです。

## オリジナル版からの変更点

- 英文における`, `と`. `の代わりに`、`と`。`を使う
- 書籍名や雑誌名をイタリックにする代わりに`『`と`』`で囲む
- 書籍名や論文名の前に登場する、日本語では不要な`、`（例：著者名`、`『書籍名』）を省略する

## 使い方

- [Jurism](https://juris-m.github.io/)にインポートして使う
- [Pandoc](https://pandoc.org/)およびそのフィルター[citeproc-js-based-replacer](https://github.com/kotobuki/citeproc-js-based-replacer)と組み合わせて使う

## 例

```json
[
  {
    "id": "morgan2022philosophy",
    "author": [
      {
        "family": "Morgan",
        "given": "Casey"
      },
      {
        "family": "Patrov",
        "given": "Alexei"
      }
    ],
    "citation-key": "morgan2022philosophy",
    "event-place": "Chicago, IL",
    "issued": {
      "date-parts": [[2022]]
    },
    "language": "en>ja",
    "note": "alt-title: 自由意志の哲学\nalt-translator: 鈴木||真紀\nalt-issued: 2023\nalt-publisher-place: 東京\nalt-publisher: 城南大学出版会",
    "publisher": "Global Academic Press",
    "publisher-place": "Chicago, IL",
    "title": "The Philosophy of Free Will",
    "type": "book"
  }
]
```

`Note` Casey Morgan and Alexei Patrov, *The Philosophy of Free Will* (Chicago, IL: Global Academic Press, 2022).〔『自由意志の哲学』訳：鈴木真紀（東京：城南大学出版会、2023）。〕

`Bibliography entry` Morgan, Casey, and Alexei Patrov. *The Philosophy of Free Will*. Chicago, IL: Global Academic Press, 2022. 〔『自由意志の哲学』訳：鈴木真紀、東京：城南大学出版会、2023。〕

注：これは架空の文献です。
