from matplotlib import pyplot as plt
from tkinter import messagebox, font, ttk, colorchooser
from time_series import time, Tested #data retriving module
from PIL import Image
import tkinter as tk
from requests.exceptions import ConnectionError as error
import request  # refference to my personal class for retrieving data
import os

# colors = {blue: '#00ccff', Purple:'#b5cdff', green:'#7fff80', green:'#17e890',
#           blue:'#00A5F9', blue:'#526EFF', red:#}

if 'graphs' not in [x for x in os.listdir()]:
    os.mkdir('graphs')
else:
    pass

HEIGHT = 600
WIDTH = 600

root = tk.Tk()
root.geometry(f'{HEIGHT}x{WIDTH}')
# root.resizable(False, False)
root.title('Corona Diagnose')
root.iconbitmap('9.bmp')

def Font_style():
    top = tk.Toplevel(root)
    top.geometry('300x300')
    tk.Label(top, text='Style').grid(row=0, column=0)

    #create combobox
    global x
    x = tk.StringVar()
    combobox = ttk.Combobox(top, textvariable=x, values=font.families())
    combobox.grid(row=1, column=1)

    #create label

    tk.Label(top, text='Size').grid(row=2, column=0)
    #create scrollbar
    global scale
    scale = tk.Scale(top)
    scale.grid(row=3, column=1)

    #create label
    tk.Label(top, text='Type').grid(row=4, column=0)
    #create option menu
    global y
    global z
    y = tk.IntVar()
    z = tk.IntVar()
    checkbox = tk.Checkbutton(top, variable=y, text='bold')
    checkbox.grid(row=5, column=1)
    checkbox1 = tk.Checkbutton(top, variable=z, text='italic')
    checkbox1.grid(row=6, column=1)

    def pick():
        color = colorchooser.askcolor()[1]
        label.config(fg=color)

    def change():
        font = [x.get(), scale.get()]
        if y.get() == 1:font.append('bold')
        if z.get() == 1:font.append('italic')
        if y.get() == 0:pass
        if z.get() == 0:pass
        label.config(font=font)

    btn = tk.Button(top,text='Done',command=change).grid(row=7, column=1)
    btn1 = tk.Button(top, text='color', command=pick).grid(row=7, column=2)

def cases_time_series():

    global label
    global frame2
    frame2.place_forget()
    label.place_forget()

    frame2 = tk.Frame(root, bg='#4a4848')
    frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

    label = tk.Label(frame2,font=['Bahnschrift Light', 26, 'bold'],background='grey', fg='white',activebackground='#7fff80')
    label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)

    top = tk.Toplevel()
    initialized = time(top, label)
    initialized.main()
    btn = tk.Button(top, text='Get Date', command=initialized.caller).pack()

# instancing teste meta data class
def test_data():
    global label
    global frame2
    frame2.place_forget()
    label.place_forget()

    frame2 = tk.Frame(root, bg='#4a4848')
    frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

    label = tk.Label(frame2,font=['Bahnschrift Light', 10, 'bold'],background='grey', fg='white',activebackground='#7fff80')
    label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)

    top = tk.Toplevel()
    test = Tested(top, label)
    test.main_window()

    btn = tk.Button(top, text='get', command=test.main_data)
    btn.pack()

# for district data
def district_info():
    global label
    global frame2
    frame2.place_forget()
    label.place_forget()

    frame2 = tk.Frame(root, bg='#4a4848')
    frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

    label = tk.Label(frame2,font=['Bahnschrift Light', 26, 'bold'],background='grey', fg='white',activebackground='#7fff80')
    label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)

    top = tk.Toplevel()

    info = Tested(top, label)
    info.district_gui()




menu = tk.Menu()
root.config(menu=menu)


# file menu
file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Font Style', command=Font_style)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)


# option menu
option_menu = tk.Menu(menu)
menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='District Wise', command=district_info)
option_menu.add_command(label='Tested', command=test_data)
option_menu.add_command(label='Date wise', command=cases_time_series)


# input menu
input_menu = tk.Menu(menu)
menu.add_cascade(label='Input')
input_menu.add_command(label='Save')

img = tk.PhotoImage(file='7.png')
# img1 = tk.PhotoImage(file=f'graphs\\Maharashtra.png')

label2 = tk.Label(root, image=img)
label2.pack()
imag = tk.PhotoImage(file='8.png')


# main windows

def task(string):
    try:
        global label
        global frame2
        frame2.place_forget()
        label.place_forget()
        response = request.Fetcher()

        if len(string.split(' ')) == 1:
        	name = string.capitalize()
        elif len(string.split(' ')) > 1:
        	values_name = []
        	for i in string.split(' '):
        		values_name.append(i.capitalize())
        	name = ' '.join(values_name)

        response.entry = name
        result = response.conclusion()

        frame2 = tk.Frame(root, bg='#4a4848')
        frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)


        label = tk.Label(frame2,text=result,font=['Bahnschrift Light', 26, 'bold'],background='grey', fg='white',activebackground='#7fff80')
        label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)
    except Exception as e:
        label['image'] = imag

class graphs:
    def __init__(self, string):
        self.string = string

        response = request.Fetcher()
        response.entry = self.string
        plt.style.use('seaborn')

        y = [response.confirmed(), response.recovered(), response.deaths()]
        x = [1, 2, 3]
        pct = '%.1f'

        plt.pie(y, labels=['Confirmed', 'Recovered', 'Deaths'], startangle=10, autopct=pct, explode =[0,0.02,0],
            wedgeprops={'linewidth':1.5, 'edgecolor':'#4a4848'})
        
        plt.legend(loc='upper right')
        # plt.tight_layout()
        plt.title(self.string)
        self.path = f'{response.state()}.png'
        plt.savefig(self.path)
    @property
    def final(self):
        size = (560, 460)
        image = Image.open(self.path)
        image.thumbnail(size)
        image.save(self.path)

location = os.getcwd()

def pictures(string):
    try:
        def storage():
            if os.getcwd() == location:
                os.chdir('graphs')
            else:
                pass
            if f"{string}.png" not in [x for x in os.listdir()]:
            	if len(string.split(' ')) == 1:
            		name = string.capitalize()
            	elif len(string.split(' ')) > 1:
            		values_name = []
            		for i in string.split(' '):
            			values_name.append(i.capitalize())
            		name = ' '.join(values_name)
            	g = graphs(name)
            	g.final
            else:
                pass
        storage()

        global label
        global frame2

        frame2.place_forget()
        label.place_forget()
        # print(os.getcwd())

        global p
        p = tk.PhotoImage(file = f'{string}.png')

        frame2 = tk.Frame(root, bg='grey')
        frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

        label = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'], background='red', fg='#00ccff',
                     activebackground='#7fff80', image=p)
        label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)
    except Exception:
        label['text'] == 'Error Ocurred'




frame = tk.Frame(root, bg='#4a4848')
frame.place(relx=0.07, rely=0.210, relwidth=0.85, relheight=0.1)

frame2 = tk.Frame(root, bg='#4a4848')
frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

frame3 = tk.Frame(root, bg='#4a4848')
frame3.place(relx=0.08, rely=0.02, relwidth=0.2725, relheight=0.1)

frame4 = tk.Frame(root, bg='#4a4848')
frame4.place(relx=0.36, rely=0.02, relwidth=0.2725, relheight=0.1)

frame5 = tk.Frame(root, bg='#4a4848')
frame5.place(relx=0.64, rely=0.02, relwidth=0.2725, relheight=0.1)

entry = tk.Entry(frame, font=['Bahnschrift Light Condensed', 27], bd=1, background='grey', foreground='white',
                 relief='groove', selectbackground='#00ccff')
entry.place(relx=0.01, rely=0.091, relwidth=0.65, relheight=0.85)
entry.insert(0, 'type state name here')
entry.selection_from(1)


accept = tk.PhotoImage(file='10.png')
accept2 = tk.PhotoImage(file='11.png')

button = tk.Button(frame, text='Accept', background='#526EFF', activebackground='#7fff80', image=accept,
                   borderwidth=0, relief='raise', overrelief='groove', cursor='hand2', command=lambda: task(entry.get()))
button.place(relx=0.67, rely=0.091, relheight=0.85, relwidth=0.155)

button2 = tk.Button(frame, text='Graph', borderwidth=0, background='#526EFF',command=lambda: pictures(entry.get()),
                    image=accept2, activebackground='#7fff80', relief='groove', overrelief='raise', cursor='hand2')
button2.place(relx=0.835, rely=0.091, relheight=0.85, relwidth=0.155)

f = request.Fetcher()
f.entry = "Total"



label = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'],image=img, fg='#00ccff',
                 activebackground='#7fff80')
label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)
print(os.getcwd())

try:
    def maker():
        os.chdir('graphs')
        global total
        h = graphs(f.entry)
        h.final
        total = tk.PhotoImage(file='Total.png')
    maker()
except error:
    messagebox.showwarning(title= 'Connection Error', message='Check your internet connection')

def function():
    global label_total2
    label_total2 = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'], background='grey', fg='#00ccff',
        image=total, activebackground='#7fff80')
    label_total2.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)

try:
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:
        confirmed_ = executor.submit(f.confirmed).result()
        recovered_ = executor.submit(f.recovered).result()
        deaths_ = executor.submit(f.deaths).result()
        

    button3 = tk.Button(frame4, text=recovered_, border=0, background='#7fff80',
                        activebackground='#7fff80', relief='raise', overrelief='raise', cursor='hand2',
                        command=function, font=['Bahnschrift Light', 25, 'bold'])
    button3.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)

    label_total1 = tk.Label(frame3, text=confirmed_, relief='groove', font=['Bahnschrift Light', 25, 'bold']
                            , background='red')
    label_total1.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)  # confirmed

    label_total3 = tk.Label(frame5, text=deaths_, relief='groove', font=['Bahnschrift Light', 25, 'bold']
                            , background='grey')  # deaths
    label_total3.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)
except error:
    button3 = tk.Button(frame4, border=0, background='#7fff80')
    button3.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)
    label_total1 = tk.Label(frame3, relief='groove', font=['Bahnschrift Light', 25, 'bold']
                            , background='red')
    label_total1.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)  # confirmed

    label_total3 = tk.Label(frame5, relief='groove', font=['Bahnschrift Light', 25, 'bold']
                            , background='grey')  # deaths
    label_total3.place(relx=0.03, rely=0.05, relwidth=0.93, relheight=0.9)
    messagebox.showerror(title='Error', message='Connection Error')


root.mainloop()





