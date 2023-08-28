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

    def create_input_fields(self):
        self.input_frame.destroy()
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack()

        self.unit_var = tk.StringVar()
        ttk.Label(self.input_frame, text="请选择长度单位：").pack()
        ttk.Radiobutton(self.input_frame, text="厘米", variable=self.unit_var, value="cm").pack()
        ttk.Radiobutton(self.input_frame, text="英寸", variable=self.unit_var, value="in").pack()

        if self.shape_var.get() == "正方形":
            ttk.Label(self.input_frame, text="边长：").pack()
            self.side_entry = ttk.Entry(self.input_frame)
            self.side_entry.pack()
        elif self.shape_var.get() == "长方形":
            ttk.Label(self.input_frame, text="长度：").pack()
            self.length_entry = ttk.Entry(self.input_frame)
            self.length_entry.pack()

            ttk.Label(self.input_frame, text="宽度：").pack()
            self.width_entry = ttk.Entry(self.input_frame)
            self.width_entry.pack()
        elif self.shape_var.get() == "三角形":
            ttk.Label(self.input_frame, text="底长：").pack()
            self.base_entry = ttk.Entry(self.input_frame)
            self.base_entry.pack()

            ttk.Label(self.input_frame, text="高：").pack()
            self.height_entry = ttk.Entry(self.input_frame)
            self.height_entry.pack()
        elif self.shape_var.get() == "圆形":
            ttk.Label(self.input_frame, text="直径：").pack()
            self.diameter_entry = ttk.Entry(self.input_frame)
            self.diameter_entry.pack()