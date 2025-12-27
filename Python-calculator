import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        
        # Minimalist color scheme
        self.bg_color = "#1E1E1E"
        self.display_bg = "#2D2D2D"
        self.number_bg = "#3A3A3A"
        self.operator_bg = "#FF9500"
        self.special_bg = "#505050"
        self.text_color = "#FFFFFF"
        
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.current_value = ""
        self.result_value = 0
        self.operation = None
        self.new_operation = True
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root,
            font=("Segoe UI", 32),
            justify="right",
            bg=self.display_bg,
            fg=self.text_color,
            bd=0,
            relief="flat",
            insertbackground=self.text_color
        )
        self.display.pack(fill="both", ipady=30, padx=1, pady=(1, 10))
        self.display.insert(0, "0")
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(expand=True, fill="both", padx=1, pady=1)
        
        # Button layout
        buttons = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '⌫', '=']
        ]
        
        for i, row in enumerate(buttons):
            buttons_frame.grid_rowconfigure(i, weight=1)
            for j, button_text in enumerate(row):
                buttons_frame.grid_columnconfigure(j, weight=1)
                self.create_button(buttons_frame, button_text, i, j)
    
    def create_button(self, parent, text, row, col):
        # Determine button style
        if text in ['/', '*', '-', '+', '=']:
            bg = self.operator_bg
            fg = "#FFFFFF"
            font_weight = "bold"
        elif text in ['C', '±', '%', '⌫']:
            bg = self.special_bg
            fg = "#FFFFFF"
            font_weight = "normal"
        else:
            bg = self.number_bg
            fg = "#FFFFFF"
            font_weight = "normal"
        
        button = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 20, font_weight),
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            bd=0,
            relief="flat",
            command=lambda: self.on_button_click(text)
        )
        
        # Special width for 0 button
        colspan = 2 if text == '0' else 1
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)
    
    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.on_digit_click(button_text)
        elif button_text in ['+', '-', '*', '/', '%']:
            self.on_operator_click(button_text)
        elif button_text == '=':
            self.on_equal_click()
        elif button_text == 'C':
            self.on_clear_click()
        elif button_text == '⌫':
            self.on_backspace_click()
        elif button_text == '±':
            self.on_sign_change_click()
    
    def on_digit_click(self, digit):
        current = self.display.get()
        
        if current == "0" or self.new_operation:
            if digit == '.':
                self.display.delete(0, tk.END)
                self.display.insert(0, "0.")
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, digit)
            self.new_operation = False
        else:
            if digit == '.' and '.' in current:
                return
            self.display.insert(tk.END, digit)
    
    def on_operator_click(self, operator):
        try:
            current = float(self.display.get())
            
            if self.operation and not self.new_operation:
                # Calculate previous operation first
                self.calculate()
            else:
                self.result_value = current
            
            self.operation = operator
            self.new_operation = True
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    
    def on_equal_click(self):
        self.calculate()
        self.operation = None
    
    def calculate(self):
        try:
            current = float(self.display.get())
            
            if self.operation == '+':
                result = self.result_value + current
            elif self.operation == '-':
                result = self.result_value - current
            elif self.operation == '*':
                result = self.result_value * current
            elif self.operation == '/':
                if current == 0:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    self.new_operation = True
                    return
                result = self.result_value / current
            elif self.operation == '%':
                if current == 0:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    self.new_operation = True
                    return
                result = self.result_value % current
            else:
                return
            
            if result == int(result):
                result = int(result)
            
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.result_value = result
            self.new_operation = True
            
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.new_operation = True
    
    def on_clear_click(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")
        self.current_value = ""
        self.result_value = 0
        self.operation = None
        self.new_operation = True
    
    def on_backspace_click(self):
        current = self.display.get()
        if len(current) > 1:
            self.display.delete(len(current) - 1)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
    
    def on_sign_change_click(self):
        try:
            current = float(self.display.get())
            current = -current
            if current == int(current):
                current = int(current)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current))
        except ValueError:
            pass

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
