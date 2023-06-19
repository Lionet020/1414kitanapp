def launch_tool(tool_path):
    current_dir = os.getcwd()  # 現在のカレントディレクトリを保存

    tool_dir = os.path.dirname(tool_path)  # ツールのディレクトリパスを取得
    os.chdir(tool_dir)  # カレントディレクトリをツールのディレクトリに変更

    file_extension = os.path.splitext(tool_path)[1].lower()
    if file_extension in [".py", ".pyw"]:
        os.system(f'pythonw {tool_path}')  # Pythonスクリプトを実行
    elif file_extension == ".pl":
        os.system(f'perl {tool_path}')  # Perlスクリプトを実行
    elif file_extension in [".xlsx", ".xlsm", ".txt"]:
        os.startfile(tool_path)  # エクセルファイルやテキストファイルを開く
    else:
        messagebox.showwarning("エラー", "サポートされていないファイル形式です。")

    os.chdir(current_dir)  # カレントディレクトリを元に戻す

