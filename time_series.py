from request import complete, district_info as di
from tkinter import ttk
import tkinter as tk

class time:

	#calling cases_time_series class
	Complete= complete()

	def __init__(self, master, label):
		self.master = master
		self.label = label
		self.frame = tk.Frame(self.master)
		self.scroller = tk.Scrollbar(self.frame)
		self.scroller.pack(side='right',fill='y', expand=1)

	def main(self):
		self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scroller.set)
		self.listbox.pack()

		#config scroll bar
		self.scroller.config(command=self.listbox.yview)

		for content in self.Complete.date():
			self.listbox.insert('end', content) 

		self.frame.pack()

	# create a method
	def caller(self):
		date = self.listbox.get('anchor')
		Complete = complete()
		data = Complete.response(date)
		result = f"Increase by:\n\tConfirmed : {data[0]}\n\tRecovered : {data[2]}\nDeath : {data[1]}\nTotal:\n\tConfirmed : {data[3]}\n\tRecovered : {data[5]}\nDeath : {data[4]}"
		return self.label.config(text=result)

	def date(self):
		c = complete()
		# creating list
		self.listbox1 = tk.Listbox(self.frame, yscrollcommand=self.scroller.set)
		self.scroller.config(command=self.listbox1.yview)

		# adding all the date at which tested updated cointaining update time also
		for data in c.update_time():
			self.listbox1.insert(0, data)
		self.listbox1.pack()
		self.frame.pack()

	def individuals_records(self):
		Date = self.listbox1.get('anchor')
		c = complete()
		self.label.config(text = c.test(date))



class Tested(time):
	def __init__(self, master, label):
		self.master = master
		self.label = label
		self.frame = tk.Frame(self.master)
		self.scrollbar = tk.Scrollbar(self.frame)
		self.scrollbar.pack(side='right', fill='y', expand=1)
		

	def main_window(self):
		self.listbox = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set)
		self.listbox.pack(fill='y', expand=1)

		for data in time.Complete.update_time():
			self.listbox.insert(0, data)
		self.scrollbar.config(command=self.listbox.yview)

		self.frame.pack()

	def main_data(self):
		date = self.listbox.get('anchor')
		result = time.Complete.test(date)
		self.label.config(text=result)


	def district_gui(self):
		values = di().State()[0]

		# combobox for state
		self.combobox1 = ttk.Combobox(self.master, values = values)
		self.combobox1.set('State')
		self.combobox1.pack()

		def func(event):
			# value for state
			value = self.combobox1.get()
			districts = di().districts(value)
            
            # Another combox for district
			self.combobox = ttk.Combobox(self.master, values = districts)
			self.combobox.set('Districts')
			self.combobox.pack()

			def Date(event):
				# value for district
				value1 = self.combobox.get()
				date_x = di().date(value, value1)

				# Combobox fot dates of data
				self.combobox2 = ttk.Combobox(self.master, values = date_x)
				self.combobox2.set('Date')
				self.combobox2.pack()

				def Data(event):
					# variable for date
					Date = self.combobox2.get()
					result = di().Data(value, value1, Date)

					self.label.config(text = result)

				# bind static date funtion to combobox for retrieving data
				self.combobox2.bind('<Double 1>', Data)

			# binding Date function to the combobox	
			self.combobox.bind('<Double 1>', Date)


		self.combobox1.bind('<Double 1>', func)

		# value for sencond listbox:


if __name__ == '__main__':
	root = tk.Tk()
	label = tk.Label(root)
	date = Tested(root, label)
	date.district_gui()
	label.pack()

	root.mainloop()
