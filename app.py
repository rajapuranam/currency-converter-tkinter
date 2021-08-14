from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import currency_data as cd

win = Tk()
win.title('Currency Converter')
win.geometry("500x500")

def convert(temp=None):
	global frm, to, rate, fcd, tcd
	global frm_amt, to_amt, show_result, sepe

	fc = from_entry.get().upper().strip()
	tc = to_entry.get().upper().strip()
	amt = amt_entry.get().upper().strip()

	if not fc.isalpha() or not tc.isalpha():
		messagebox.showwarning("WARNING!", "Please fill the FROM and TO fields.")
		return 

	if fc == tc:
		from_entry.delete(0, 'end')
		to_entry.delete(0, 'end')
		messagebox.showwarning("WARNING!", "Both FROM and TO currencies are same.\nPlease provide different currencies to convert.")
		return

	if not amt.replace('.', '', 1).isdigit():
		amt_entry.delete(0, 'end')
		messagebox.showwarning("WARNING!", "Please provide valid amount to convert.")
		return

	if frm == fc and to == tc:
		amt = float(amt)
	else:
		convert_btn.config(text="Please wait...")
		frm, to = fc, tc
		amt = float(amt)
		result = cd.get_exchange_rate(fc, tc)
		convert_btn.config(text="Convert")

		if not result:
			messagebox.showwarning("WARNING!", "Couldn't fetch results.\nPlease provide valid information.")
			return 
		
		rate, fcd, tcd = result
	
	frm_amt.config(text = f'{fcd["currencySymbol"]} {amt:.2f}')
	to_amt.config(text = f'{tcd["currencySymbol"]} {(rate*amt):.2f}')
	sepe.config(text = '=')
	show_result.config(text = f'{fcd["currencyName"]} to {tcd["currencyName"]}')

frm, to, fcd, tcd = '', '', '', ''
rate = 0

# Create Tabs
my_notebook = ttk.Notebook(win)
my_notebook.pack(pady=5, padx=5)

convert_frame = Frame(my_notebook, width=480, height=480)
currency_frame = Frame(my_notebook, width=480, height=480)

convert_frame.pack(fill="both", expand=1)
currency_frame.pack(fill="both", expand=1)

my_notebook.add(convert_frame, text="Convert")
my_notebook.add(currency_frame, text="Currencies")

# Convert Tab
take_input = LabelFrame(convert_frame, text='')
take_input.pack(pady=30)

from_curr = Label(take_input, text='From Currency: ', font=("Bell MT", 14))
from_curr.grid(row=0, column = 0, pady=10, padx=10)
from_entry = Entry(take_input, font=("Bell MT", 14))
from_entry.grid(row=0, column = 1, pady=10, padx=10)

to_curr = Label(take_input, text='To Currency: ', font=("Bell MT", 14))
to_curr.grid(row=1, column = 0, pady=10, padx=10)
to_entry = Entry(take_input, font=("Bell MT", 14))
to_entry.grid(row=1, column = 1, pady=10, padx=10)

amt_convert = Label(take_input, text='Amount to convert: ', font=("Bell MT", 14))
amt_convert.grid(row=2, column = 0, pady=10, padx=10)
amt_entry = Entry(take_input, font=("Bell MT", 14))
amt_entry.grid(row=2, column = 1, pady=10, padx=10)

convert_btn = Button(convert_frame, text="Convert", command=convert, font=("Bell MT", 12), padx=20)
convert_btn.pack()
convert_btn.bind('<Return>', convert)

show_result = LabelFrame(convert_frame, text='', font=("Bell MT", 14))
show_result.pack(pady=20)
frm_amt = Label(show_result, text='', font=("Bell MT", 18))
frm_amt.grid(row=0, column = 0, pady=20, padx=40)
sepe = Label(show_result, text='Enter Currency IDs and Amount\nto convert.', font=("Bell MT", 14))
sepe.grid(row=0, column = 1, pady=20, padx=0)
to_amt = Label(show_result, text='', font=("Bell MT", 18))
to_amt.grid(row=0, column = 2, pady=20, padx=40)

# Currencies Tab
Label(currency_frame, text="", width=70).pack()
Label(currency_frame, text='CURRENCIES', font=("Bell MT", 18)).pack(pady=10)

currency_details = cd.get_currency_details()
currency_details.sort(key=lambda item: item['country'])

frame_list_scrollbar = Frame(currency_frame)

scrollbar = Scrollbar(frame_list_scrollbar, orient=VERTICAL)
curr_list = Listbox(frame_list_scrollbar, yscrollcommand = scrollbar.set, width=100, height=100, font=("Bell MT", 13) )

scrollbar.config(command=curr_list.yview)
scrollbar.pack(side=RIGHT, fill=Y)

curr_list.pack(pady=15)

frame_list_scrollbar.pack()

for ind, item in enumerate(currency_details):
	curr_list.insert(END, f"  Country  : {item['country']}")
	curr_list.insert(END, f"  Currency: {item['currency']}")
	curr_list.insert(END, '\n')

Label(currency_frame, text="", height=70).pack()

win.mainloop()
