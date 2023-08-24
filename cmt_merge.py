def merge_blocks(input_filename, output_filename):
    blocks = {}  # ブロックごとの内容を保持する辞書
    current_block = None  # ブロックのラベルを保持する変数
    content = []  # ブロックの内容を保持する変数

    with open(input_filename, 'rb') as input_file:
        for line in input_file:
            line = line.rstrip(b'\r\n')  # 改行コードを削除
            if line.startswith(b"********** "):
                if current_block is not None:
                    blocks[current_block] = content  # ブロックの内容を保存
                current_block = line.decode('utf-8', errors='replace')  # ブロックのラベルを更新
                content = []  # 新しいブロックの内容を初期化
            else:
                content.append(line.decode('utf-8', errors='replace'))  # 行をブロックの内容に追加

        if current_block is not None:
            blocks[current_block] = content  # 最後のブロックの内容を保存

    merged_blocks = {}  # マージ済みのブロックを保持する辞書

    for block, content in blocks.items():
        if block not in merged_blocks:
            merged_blocks[block] = set(content)
        else:
            merged_blocks[block].update(content)  # ユニークな内容をマージ

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for block, content in merged_blocks.items():
            output_file.write(block + '\n')  # ブロックのラベルを出力

            for line in content:
                output_file.write(line + '\n')  # マージ済みの内容を出力

            output_file.write('\n')  # ブロック間に空行を追加

# インプットファイル名とアウトプットファイル名を指定してプログラムを実行
input_filename = "input.txt"
output_filename = "output.txt"
merge_blocks(input_filename, output_filename)
