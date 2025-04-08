import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.style = ttk.Style("solar")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, pady=(10,0))

        self.create_temperature_tab()
        self.create_weight_tab()
        self.create_length_tab()


    # --- TEMPERATURE TAB ---
    def create_temperature_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Temperature")

        self.temp_direction = True  # True = C → F

        self.temp_label_input = ttk.Label(tab, text="Celsius")
        self.temp_label_input.grid(row=0, column=0, padx=10, pady=10)

        self.temp_entry_input = ttk.Entry(tab, width=20)
        self.temp_entry_input.grid(row=1, column=0, padx=10)

        self.temp_switch_button = ttk.Button(tab, text="⇄", command=self.switch_temp_units, bootstyle=SECONDARY)
        self.temp_switch_button.grid(row=1, column=1, padx=10)

        self.temp_label_output = ttk.Label(tab, text="Fahrenheit")
        self.temp_label_output.grid(row=0, column=2, padx=10, pady=10)

        self.temp_entry_output = ttk.Entry(tab, width=20, state="readonly")
        self.temp_entry_output.grid(row=1, column=2, padx=10)

        convert_btn = ttk.Button(tab, text="Convert", command=self.convert_temperature, bootstyle=SUCCESS)
        convert_btn.grid(row=2, column=0, columnspan=3, pady=10)

    def switch_temp_units(self):
        self.temp_direction = not self.temp_direction
        if self.temp_direction:
            self.temp_label_input.config(text="Celsius")
            self.temp_label_output.config(text="Fahrenheit")
        else:
            self.temp_label_input.config(text="Fahrenheit")
            self.temp_label_output.config(text="Celsius")
        self.clear_entries(self.temp_entry_input, self.temp_entry_output)

    def convert_temperature(self):
        try:
            value = float(self.temp_entry_input.get())
            result = value * 9/5 + 32 if self.temp_direction else (value - 32) * 5/9
            self.set_result(self.temp_entry_output, result)
        except ValueError:
            self.set_result(self.temp_entry_output, "Invalid input")

    # --- WEIGHT TAB ---
    def create_weight_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Weight")

        self.weight_direction = True  # True = Kg → Lbs

        self.weight_label_input = ttk.Label(tab, text="Kilograms")
        self.weight_label_input.grid(row=0, column=0, padx=10, pady=10)

        self.weight_entry_input = ttk.Entry(tab, width=20)
        self.weight_entry_input.grid(row=1, column=0, padx=10)

        self.weight_switch_button = ttk.Button(tab, text="⇄", command=self.switch_weight_units, bootstyle=SECONDARY)
        self.weight_switch_button.grid(row=1, column=1, padx=10)

        self.weight_label_output = ttk.Label(tab, text="Pounds")
        self.weight_label_output.grid(row=0, column=2, padx=10, pady=10)

        self.weight_entry_output = ttk.Entry(tab, width=20, state="readonly")
        self.weight_entry_output.grid(row=1, column=2, padx=10)

        convert_btn = ttk.Button(tab, text="Convert", command=self.convert_weight, bootstyle=SUCCESS)
        convert_btn.grid(row=2, column=0, columnspan=3, pady=10)

    def switch_weight_units(self):
        self.weight_direction = not self.weight_direction
        if self.weight_direction:
            self.weight_label_input.config(text="Kilograms")
            self.weight_label_output.config(text="Pounds")
        else:
            self.weight_label_input.config(text="Pounds")
            self.weight_label_output.config(text="Kilograms")
        self.clear_entries(self.weight_entry_input, self.weight_entry_output)

    def convert_weight(self):
        try:
            value = float(self.weight_entry_input.get())
            result = value * 2.20462 if self.weight_direction else value / 2.20462
            self.set_result(self.weight_entry_output, result)
        except ValueError:
            self.set_result(self.weight_entry_output, "Invalid input")

    # --- LENGTH TAB ---
    def create_length_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Length")

        self.length_direction = True  # True = Meters → Feet

        self.length_label_input = ttk.Label(tab, text="Meters")
        self.length_label_input.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry_input = ttk.Entry(tab, width=20)
        self.length_entry_input.grid(row=1, column=0, padx=10)

        self.length_switch_button = ttk.Button(tab, text="⇄", command=self.switch_length_units, bootstyle=SECONDARY)
        self.length_switch_button.grid(row=1, column=1, padx=10)

        self.length_label_output = ttk.Label(tab, text="Feet")
        self.length_label_output.grid(row=0, column=2, padx=10, pady=10)

        self.length_entry_output = ttk.Entry(tab, width=20, state="readonly")
        self.length_entry_output.grid(row=1, column=2, padx=10)

        convert_btn = ttk.Button(tab, text="Convert", command=self.convert_length, bootstyle=SUCCESS)
        convert_btn.grid(row=2, column=0, columnspan=3, pady=10)

    def switch_length_units(self):
        self.length_direction = not self.length_direction
        if self.length_direction:
            self.length_label_input.config(text="Meters")
            self.length_label_output.config(text="Feet")
        else:
            self.length_label_input.config(text="Feet")
            self.length_label_output.config(text="Meters")
        self.clear_entries(self.length_entry_input, self.length_entry_output)

    def convert_length(self):
        try:
            value = float(self.length_entry_input.get())
            result = value * 3.28084 if self.length_direction else value / 3.28084
            self.set_result(self.length_entry_output, result)
        except ValueError:
            self.set_result(self.length_entry_output, "Invalid input")

    # --- HELPER METHODS ---
    def set_result(self, output_entry, result):
        output_entry.config(state="normal")
        output_entry.delete(0, 'end')
        output_entry.insert(0, f"{result:.2f}" if isinstance(result, float) else result)
        output_entry.config(state="readonly")

    def clear_entries(self, entry1, entry2):
        entry1.delete(0, 'end')
        entry2.config(state="normal")
        entry2.delete(0, 'end')
        entry2.config(state="readonly")


# --- RUN ---
if __name__ == "__main__":
    root = ttk.Window(themename="solar")
    app = UnitConverterApp(root)
    root.mainloop()
