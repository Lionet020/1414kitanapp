def is_js_or_css_url(url):
    return url.endswith(".js") or url.endswith(".css")

def merge_blocks(input_filename, output_filename):
    blocks = {}  # ブロックごとの内容を保持する辞書

    with open(input_filename, 'r') as input_file:
        current_block = None
        current_content = []

        for line in input_file:
            if line.startswith("********** "):
                if current_block is not None:
                    # ブロックの終わりを処理して内容を辞書に追加
                    blocks[current_block] = current_content

                current_block = line.strip()  # ブロックのラベルを取得
                current_content = []  # 新しいブロックの内容を初期化
            else:
                current_content.append(line.strip())  # 行をブロックの内容に追加

        if current_block is not None:
            blocks[current_block] = current_content

    with open(output_filename, 'w') as output_file:
        for block, content in blocks.items():
            # ブロックのラベルがURLであり、拡張子が.jsか.cssの場合のみマージ
            if block.startswith("********** ") and is_js_or_css_url(block[12:]):
                output_file.write(block + '\n')  # ブロックのラベルを出力

                unique_content = set(content)  # ユニークな内容にするためにセットに変換
                for line in unique_content:
                    output_file.write(line + '\n')  # ユニークな内容を出力

                output_file.write('\n')  # ブロック間に空行を追加

# インプットファイル名とアウトプットファイル名を指定してプログラムを実行
input_filename = "input.txt"
output_filename = "output.txt"
merge_blocks(input_filename, output_filename)
