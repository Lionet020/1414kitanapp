import re

def remove_prefix(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = [re.sub(r'^\[\d+\]:\s*', '', line) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

# 使い方の例
remove_prefix('your_text_file.txt')
