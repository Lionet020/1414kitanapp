import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import json

def launch_tool(tool_path):
    file_extension = os.path.splitext(tool_path)[1].lower()
    tool_directory = os.path.dirname(tool_path)
    current_directory = os.getcwd()

    try:
        os.chdir(tool_directory)  # Change the current working directory
        if file_extension == ".py" or file_extension == ".pyw":
            os.system(f'python "{tool_path}"')  # Execute Python file
        elif file_extension == ".pl":
            os.system(f'perl "{tool_path}"')  # Execute Perl file
        elif file_extension in [".xlsx", ".xlsm", ".txt"]:
            os.startfile(tool_path)  # Open Excel or text file
        else:
            messagebox.showwarning("エラー", "サポートされていないファイル形式です。")
    finally:
        os.chdir(current_directory)  # Restore the original current working directory

# Rest of the code remains the same...
