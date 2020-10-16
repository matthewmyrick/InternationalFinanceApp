from tkinter import ttk, Entry

class Widgets():
    def ComboBox(self, tab, data, default, rows, columns, padx, pady):
        '''
        This function serves as an easy access widget for the Combobox
        '''
        # create Combobox object inside of tab
        comboBox = ttk.Combobox(tab)
        # Set Values inside of combobox
        comboBox['values'] = data
        try:
            # Set the default value for the Combobox
            comboBox.current(data.index(default))
        except:
            # Set the default value for the Combobox
            comboBox.current(default)
        # Make Combobox unchangable
        comboBox.state(["readonly"])
        # Create teh grid
        comboBox.grid(row=rows, column=columns, padx=padx, pady=pady)
        return comboBox

    def Entry(self, tab, default, state, row, column, padx, pady):
        '''
        This function serves as an easy access widget for the Entry
        '''
        # Create Entry Widget
        entry = Entry(tab)
        entry.insert(1, default)
        entry.configure(state=state)
        entry.grid(row=row, column=column, padx=padx, pady=pady)
        return entry


