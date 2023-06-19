import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import json

def launch_tool(tool_path):
    file_extension = os.path.splitext(tool_path)[1].lower()
    if file_extension == ".py":
        os.system(f'python {tool_path}')  # Pythonファイルを実行
    elif file_extension == ".pyw":
        os.system(f'pythonw {tool_path}')  # Pythonwファイルを実行
    elif file_extension == ".pl":
        os.system(f'perl {tool_path}')  # Perlファイルを実行
    elif file_extension in [".xlsx", ".xlsm", ".txt"]:
        os.startfile(tool_path)  # エクセルファイルやテキストファイルを開く
    else:
        messagebox.showwarning("エラー", "サポートされていないファイル形式です。")

def add_tool():
    messagebox.showinfo("ツール選択", "ランチャーに追加したいツールを選択してください")
    tool_path = filedialog.askopenfilename(filetypes=[
        ("Pythonファイル", "*.py"),
        ("Pythonwファイル", "*.pyw"),
        ("Perlファイル", "*.pl"),
        ("Excelファイル", "*.xlsx;*.xlsm"),
        ("テキストファイル", "*.txt")
    ])
    if tool_path:
        messagebox.showinfo("アイコン選択", "表示するアイコンを選択してください")
        icon_path = filedialog.askopenfilename(filetypes=[("アイコンファイル", "*.png")])
        if icon_path:
            tool_name = entry_name.get()
            relative_tool_path = os.path.relpath(tool_path)
            relative_icon_path = os.path.relpath(icon_path)
            tool = {"name": tool_name, "path": relative_tool_path, "icon": relative_icon_path}
            tools.append(tool)
            save_tools()
            refresh_tool_buttons()
            entry_name.delete(0, tk.END)  # 入力欄の内容をクリア

def create_button(tool, row, col):
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), tool["icon"])
    icon = Image.open(icon_path)
    icon = icon.resize((64, 64), Image.ANTIALIAS)  # アイコンのサイズを調整
    icon = ImageTk.PhotoImage(icon)

    button_frame = tk.Frame(tool_frame)
    button_frame.grid(row=row, column=col, padx=10, pady=10)

    button = tk.Button(button_frame, image=icon, compound=tk.TOP, command=lambda path=tool["path"]: launch_tool(path), **button_style)
    button.image = icon  # ガベージコレクションを防ぐために参照を保持
    button.pack()

    label = tk.Label(button_frame, text=tool["name"], **label_style)
    label.pack()

    delete_button = tk.Button(button_frame, text="削除", command=lambda t=tool: delete_tool(t), **delete_button_style)
    delete_button.pack()

def save_tools():
    with open("tools.json", "w") as f:
        json.dump(tools, f)

def load_tools():
    global tools
    try:
        with open("tools.json", "r") as f:
            tools = json.load(f)
    except FileNotFoundError:
        tools = []

def refresh_tool_buttons():
    for widget in tool_frame.winfo_children():
        widget.destroy()

    row = 0
    col = 0
    for tool in tools:
        create_button(tool, row, col)
        col += 1
        if col >= 7:
            col = 0
            row += 1

def main():
    global root, button_style, label_style, tools, entry_name, tool_frame, delete_button_style
    root = tk.Tk()
    root.title("ランチャーツール")

    load_tools()

    # ボタンのスタイル設定
    button_style = {
        "font": ("Arial", 12),
        "bg": "#336699",
        "fg": "white",
        "activebackground": "#5588CC",
        "activeforeground": "white",
        "bd": 0,
        "highlightthickness": 0,
        "relief": tk.FLAT
    }

    # ラベルのスタイル設定
    label_style = {
        "font": ("Arial", 10),
        "fg": "#333333"
    }

    # 削除ボタンのスタイル設定
    delete_button_style = {
        "font": ("Arial", 10),
        "bg": "red",
        "fg": "white",
        "activebackground": "darkred",
        "activeforeground": "white",
        "bd": 0,
        "highlightthickness": 0,
        "relief": tk.FLAT
    }

    # タブを作成
    tab_control = ttk.Notebook(root)
    tab_control.pack(fill=tk.BOTH, expand=1)

    # ツール表示用タブ
    tool_tab = ttk.Frame(tab_control)
    tab_control.add(tool_tab, text="ツール")

    # ツールを表示するフレーム
    tool_frame = tk.Frame(tool_tab)
    tool_frame.pack()

    # ツール追加用タブ
    add_tab = ttk.Frame(tab_control)
    tab_control.add(add_tab, text="ツール追加")

    # ツール名入力欄のラベルとテキストボックス
    label_name = tk.Label(add_tab, text="ツール名:")
    label_name.pack(side=tk.LEFT)
    entry_name = tk.Entry(add_tab, width=20)
    entry_name.pack(side=tk.LEFT)

    # ツール追加ボタン
    add_button = tk.Button(add_tab, text="ツール追加", command=add_tool)
    add_button.pack(side=tk.LEFT, padx=10)

    # 既存のツールボタンを表示
    refresh_tool_buttons()

    root.mainloop()

if __name__ == "__main__":
    main()
