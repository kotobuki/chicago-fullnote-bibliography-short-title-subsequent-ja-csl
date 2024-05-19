# chicago-fullnote-bibliography-short-title-subsequent-ja.csl

[Chicago Manual of Style 17th edition (full note, short title subsequent)](https://www.zotero.org/styles?q=id%3Achicago-fullnote-bibliography-short-title-subsequent)を[CSL](https://citationstyles.org/)（Citation Style Language）の拡張版である[CSL-M](https://citeproc-js.readthedocs.io/en/latest/csl-m/index.html)に対応させ、文献の`language`に従って日本語（`ja`）でも表記できるようにするためのCSLファイルです。

## オリジナル版からの変更点

- 英文における`, `と`. `の代わりに`、`と`。`を使う
- 書籍名や雑誌名をイタリックにする代わりに`『`と`』`で囲む
- 書籍名や論文名の前に登場する、日本語では不要な`、`（例：著者名`、`『書籍名』）を省略する

## 使い方

- LaTeXおよび[citeproc-lua](https://github.com/zepinglee/citeproc-lua)と組み合わせて使う
- [Jurism](https://juris-m.github.io/)にインポートして使う
- [Pandoc](https://pandoc.org/)およびそのフィルター[citeproc-js-based-replacer](https://github.com/kotobuki/citeproc-js-based-replacer)と組み合わせて使う

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

`Note` Casey Morgan、Alexei Patrov『自由意志の哲学』、鈴木真紀：訳（東京:城南大学出版会、2023）。〔*The Philosophy of Free Will* (Chicago, IL: Global Academic Press, 2022).〕

`Bibliography entry` Morgan, Casey、Alexei Patrov『自由意志の哲学』、鈴木真紀：翻訳、東京：城南大学出版会、2023。〔*The Philosophy of Free Will* (Chicago, IL: Global Academic Press, 2022).〕

注：これは架空の文献です。

## 既知の問題

- [　] [citeproc-js](https://github.com/Juris-M/citeproc-js)ベースのツールで使用する際、日本語に翻訳された文献におけるラテン系の著者名等が`given name` `family name`ではなく日本語と同様の`family name` `given name`になってしまう。

## 付録

Zotero、`citeproc-lua`、`chicago-fullnote-bibliography-short-title-subsequent-ja.csl`の組み合わせでは対応できない日本語文献特有の問題として、編著（編集者でもあり著者でもある）や監訳（翻訳の監修者）の取り扱いがあります。これらに対して、（やや）トリッキーな記法とPythonスクリプトの組み合わせにより暫定的に解決することができます。

まず、Zoteroで文献情報を入力する際、必要に応じて以下のようにします。

- 著者のうち一部が編著者の場合、「Author」を選択し、最後の編著者に「：編著」を追加します。例：
  - `(last)` 鈴木
  - `(first)` 真紀：編著

- 監訳者の場合、「Translator」を選択し、最後の監訳者に「：監訳」を追加します。例：
  - `(last)` 鈴木
  - `(first)` 真紀：監訳

入力が完了したら、[Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/)でCSL用のJSONファイルを出力します。

1. （もしまだであれば）Better BibTeX for Zoteroをインストールします。
2. コレクションを右クリックし、「Export Collection...」を選択します。
3. Formatに「Better CSL JSON」を選択し、ファイルを出力します。

そのままだと、監訳者が「鈴木真紀：監訳：翻訳」のようになってしまうだけでなく、次のような問題があります。

- 共通：
  - 書名における区切りなど意図的に入れた半角スペースが無視されてしまう。
- Note（`\cslcitation`タグで始まるセクション）：
  - `』`の後に不要な`、`が入ってしまう。
  - `」、『`になるべきところが`」『` になってしまう（書籍に収録された論文など書籍の一部の場合）。
  - `」{翻訳者名}：訳`となるべきところが `」、{翻訳者名}：訳` になってしまう（翻訳論文の翻訳者の場合）。
- Bibliography entry（`\bibitem`タグで始まるセクション）：
  - `\url`タグで囲まれたURLにタイプライター体が適用されない。

`update_bbl.py`は、`.bbl`ファイルを書き換えてしまうことにより、これらの問題を暫定的に解決します。使い方は次の通りです。

```shell
xelatex example.tex
citeproc-lua example.aux
python3 update_bbl.py example.bbl
xelatex example.tex
```
