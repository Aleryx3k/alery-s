import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.display_var = tk.StringVar(value="0")

        self.display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 24), justify='right')
        self.display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=12)

        self._reset_state()

        # Ряд кнопок (цифры и операции)
        btns = [
            ('7','8','9','/'),
            ('4','5','6','*'),
            ('1','2','3','-'),
            ('0','C','=','+')
        ]

        frame = tk.Frame(root)
        frame.pack()

        for r, row in enumerate(btns):
            row_frame = tk.Frame(frame)
            row_frame.pack(fill=tk.BOTH, expand=True)
            for c, label in enumerate(row):
                btn = tk.Button(row_frame, text=label, font=("Arial", 18),
                                command=lambda l=label: self.on_button(l))
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _reset_state(self):
        self.current_input = ""  # текущее вводимое число как строка
        self.operand1 = None
        self.operator = None
        self.update_display("0")

    def update_display(self, text):
        self.display_var.set(text)

    def on_button(self, label):
        if label.isdigit():
            self.current_input += label
            self.update_display(self.current_input)
        elif label in '+-*/':
            if self.current_input:
                self.operand1 = float(self.current_input)
                self.current_input = ""
            self.operator = label
        elif label == '=':
            if self.operand1 is not None and self.operator and self.current_input:
                operand2 = float(self.current_input)
                try:
                    result = self._compute(self.operand1, operand2, self.operator)
                    self.update_display(str(result))
                    # готовимся к новым вычислениям
                    self.operand1 = None
                    self.operator = None
                    self.current_input = str(result)
                except ZeroDivisionError:
                    self.update_display("Ошибка")
                    self._reset_state()
            # если неполная операция — ничего не делаем
        elif label == 'C':
            self._reset_state()

    def _compute(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError
            return a / b

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()