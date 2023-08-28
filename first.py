import tkinter as tk
from tkinter import ttk
import math

class AreaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("通用面积计算器")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="请选择图形类型：").pack()
        self.shape_var = tk.StringVar()
        self.shape_combobox = ttk.Combobox(self.root, textvariable=self.shape_var, values=["正方形", "长方形", "三角形", "圆形"])
        self.shape_combobox.pack()
        self.shape_combobox.bind("<<ComboboxSelected>>", self.on_shape_selected)

        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack()

        self.create_input_fields()

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack()

        self.calculate_button = ttk.Button(self.root, text="计算面积", command=self.calculate_area)
        self.calculate_button.pack()