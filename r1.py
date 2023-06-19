import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import json
import subprocess

def launch_tool(tool_path):
    file_extension = os.path.splitext(tool_path)[1].lower()
    if file_extension in [".py", ".pyw"]:
        subprocess.Popen(['pythonw', tool_path])  # Pythonスクリプトを実行
    elif file_extension == ".pl":
        subprocess.Popen(['perl', tool_path])  # Perlスクリプトを実行
    elif file_extension in [".xlsx", ".xlsm", ".txt"]:
        os.startfile(tool_path)  # エクセルファイルやテキストファイルを開く
    else:
        messagebox.showwarning("エラー", "サポートされていないファイル形式です。")
