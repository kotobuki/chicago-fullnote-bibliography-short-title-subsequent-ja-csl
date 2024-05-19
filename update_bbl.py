import re
import sys
import shutil


def update_bbl_content(content):
    # 日本語文字の後の単一スペースに \mbox{ } を挿入
    # Unicode範囲を考慮し、日本語（漢字、ひらがな、カタカナ）、及び全角記号を含む文字を対象とする
    content = re.sub(
        r"([\u3000-\u303F\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF]) ([\u3000-\u303F\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF])",
        r"\1\\mbox{ }\2",
        content,
    )

    # `\cslcitation` 内の `』、` を `』` に置換
    content = re.sub(r"(\\cslcitation\{[^}]*\}.*?『[^』]*)(』)、", r"\1\2", content, flags=re.DOTALL)

    # `\cslcitation` 内の `」『` を `」、『` に置換
    content = re.sub(r"(\\cslcitation\{[^}]*\}.*?)」『", r"\1」、『", content, flags=re.DOTALL)

    # `\cslcitation` 内の `」、{翻訳者名}：訳` を `」{翻訳者名}：訳` に置換
    content = re.sub(r"(\\cslcitation\{[^}]*\}.*?)」、([^」]*：訳)", r"\1」\2", content, flags=re.DOTALL)

    # `\cslcitation` 内の `：監訳：訳` を `：監訳` に置換
    content = re.sub(r"(\\cslcitation\{[^}]*\}.*?)：監訳：訳", r"\1：監訳", content, flags=re.DOTALL)

    # `\bibitem` 内の `\url{}` を `\texttt{}` で囲む
    content = re.sub(
        r"(\\bibitem\{[^}]*\}.*?)(\\url\{([^}]*)\})",
        lambda match: match.group(1) + r"\texttt{" + match.group(2) + "}",
        content,
        flags=re.DOTALL,
    )

    # `\bibitem` 内の `：監訳：翻訳` を `：監訳` に置換
    content = re.sub(r"(\\bibitem\{[^}]*\}.*?)(：監訳)：翻訳", r"\1\2", content, flags=re.DOTALL)

    return content


def process_bbl_file(filename):
    # ファイルを読み込む
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    # 内容を更新
    updated_content = update_bbl_content(content)

    # オリジナルのファイルをバックアップ
    shutil.copy(filename, filename + ".org")

    # 更新された内容をファイルに書き込む
    with open(filename, "w", encoding="utf-8") as file:
        file.write(updated_content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 update_bbl.py filename.bbl")
        sys.exit(1)

    filename = sys.argv[1]
    process_bbl_file(filename)
