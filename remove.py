def merge_unique_data(file_path):
    with open(file_path, 'r', encoding='shift-jis') as file:
        lines = file.readlines()

    merged_data = {}
    current_key = None
    current_data = []

    for line in lines:
        if line.startswith('********* http'):
            if current_key is not None:
                merged_data.setdefault(current_key, []).extend(current_data)
            current_key = line.strip()
            current_data = [line.strip()]
        else:
            current_data.append(line.strip())

    if current_key is not None:
        merged_data.setdefault(current_key, []).extend(current_data)

    with open('output.txt', 'w', encoding='shift-jis') as output_file:
        for key, data in merged_data.items():
            unique_data = list(set(data))  # データ部分をユニークにする
            output_file.write(key + '\n')
            output_file.write('\n'.join(unique_data) + '\n\n')

# 使い方の例
merge_unique_data('your_text_file.txt')
