import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def compound(principal, rate, years, additions = 0):
    result = principal
    for x in range(0,years):
        result = result*(1+rate/100) + additions

    return result


def compute_display():

    a = int(entry_field1.get())
    b = int(entry_field2.get())
    c = int(entry_field3.get())

    val = compound(a,b,c)
    val = round(val,2)
   
    result_display.insert(tk.END, val)

def clear_all():
    entry_field1.delete(0,tk.END)
    entry_field2.delete(0,tk.END)
    entry_field3.delete(0,tk.END)
    result_display.delete(1.0,tk.END)

    entry_field1.focus_set()

# creates instance of the Tk  class
window = tk.Tk()

# creates style of this app
style = ThemedStyle(window)
style.set_theme("radiance")

# generate title for window
window.title("Compound Interest Calculator")

# generate default window size
window.geometry("400x400")

# create a label object to be placed within window frame
title = ttk.Label(text = "Compound Interest Calculator", font = ("helvetica", 20), padding=10)
title.grid(column = 0, row = 0, columnspan=4)

###########################################################################################
# principal
text_field1 = ttk.Label(text = "Starting Principal: ", padding=10)
text_field1.grid(column=0,row=1)

entry_field1 = ttk.Entry()
entry_field1.grid(column = 1, row = 1)

# interest rate
text_field2 = ttk.Label(text="Interest Rate: ", padding=10)
text_field2.grid(column = 0, row = 2)

entry_field2 = ttk.Entry()
entry_field2.grid(column=1,row=2)

# years
text_field3 = ttk.Label(text="Years: ", padding=10)
text_field3.grid(column = 0, row = 3)

entry_field3 = ttk.Entry()
entry_field3.grid(column=1,row=3)

# create button to calculate!
button1 = ttk.Button(text = "Calculate!", command=compute_display)
button1.grid(column = 0, row = 4)

# create text field for results
result_display = tk.Text(master=window,height=1,width=15,font = ("helvetica", 20))
result_display.grid(column=1,row=4)

#create button to clear all entries
button2 = ttk.Button(text = "Clear", command = clear_all)
button2.grid(column=0,row=5)


###################################################################################
# method to generate window. needs to be run after methods to modify size and title
window.mainloop()

