import os

# フォルダ内のファイルを取得
files = os.listdir()
target_files = [filename for filename in files if filename[:2].isdigit() and filename.endswith("_aaa.txt")]

# 検索ワード
search_word = "======================================================"

# ファイルごとに処理
for filename in target_files:
    with open(filename, "r", encoding="utf-8") as file:  # エンコーディングをutf-8に変更
        content = file.read()
        occurrences = content.count(search_word)
        
        # 出力ファイル名
        output_filename = filename[:2] + "_bbb.txt"
        
        # 出力内容
        if occurrences < 4:
            output_content = content
        else:
            output_content = "\n".join(content.split(search_word)[:4])
        
        # 出力ファイルに書き込み
        with open(output_filename, "w", encoding="utf-8") as output_file:  # エンコーディングをutf-8に変更
            output_file.write(output_content)
