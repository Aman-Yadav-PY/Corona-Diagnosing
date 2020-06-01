import concurrent.futures
from matplotlib import pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter.ttk import *
import request  # refference to my personal class for retrieving data
import concurrent.futures
import os

# colors = {blue: '#00ccff', Purple:'#b5cdff', green:'#7fff80', green:'#17e890',
#           blue:'#00A5F9', blue:'#526EFF', red:#}

if 'graphs' not in [x for x in os.listdir()]:
    os.mkdir('graphs')
else:
    pass

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title('Corona Diagnose')
root.iconbitmap('9.bmp')

img = tk.PhotoImage(file='7.png')
# img1 = tk.PhotoImage(file=f'graphs\\Maharashtra.png')

label2 = tk.Label(root, image=img)
label2.pack()
imag = tk.PhotoImage(file='8.png')



def task(string):
    try:
        global label
        global frame2
        frame2.place_forget()
        label.place_forget()
        response = request.Fetcher()
        response.entry = string
        result = response.conclusion()

        frame2 = tk.Frame(root, bg='#4a4848')
        frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)


        label = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'],text=result, background='grey', fg='white',
                 activebackground='#7fff80')
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
    def storage():
        if os.getcwd() == location:
            os.chdir('graphs')
        else:
            pass
        if f"{string}.png" not in [x for x in os.listdir()]:
            g = graphs(string)
            g.final
        else:
            pass
    storage()

    global label
    global frame2

    frame2.place_forget()
    label.place_forget()
    print(os.getcwd())

    global p
    p = tk.PhotoImage(file = f'{string}.png')

    frame2 = tk.Frame(root, bg='#7fff80')
    frame2.place(relx=0.07, rely=0.34, relwidth=0.85, relheight=0.65)

    label = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'], background='red', fg='#00ccff',
                 activebackground='#7fff80', image=p)
    label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)




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

Style().configure('TButton', command=lambda: graph(entry.get()),
                  cursor='hand2', relief='raise', overrelief='groove', background='#526EFF', activebackground='#7fff80',
                  font='bold')

accept = tk.PhotoImage(file='10.png')
accept2 = tk.PhotoImage(file='11.png')

button = tk.Button(frame, text='Accept', background='#526EFF', activebackground='#7fff80', image=accept,
                   border=0, relief='raise', overrelief='groove', cursor='hand2', command=lambda: task(entry.get()))
button.place(relx=0.67, rely=0.091, relheight=0.85, relwidth=0.155)

button2 = tk.Button(frame, text='Graph', border=0, background='#526EFF',command=lambda: pictures(entry.get()),
                    image=accept2, activebackground='#7fff80', relief='groove', overrelief='raise', cursor='hand2')
button2.place(relx=0.835, rely=0.091, relheight=0.85, relwidth=0.155)

f = request.Fetcher()
f.entry = "Total"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    confirmed_ = executor.submit(f.confirmed).result()
    recovered_ = executor.submit(f.recovered).result()
    deaths_ = executor.submit(f.deaths).result()

label = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'], background='grey', fg='#00ccff',
                 activebackground='#7fff80')
label.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)
print(os.getcwd())

def maker():
    os.chdir('graphs')
    global total
    h = graphs(f.entry)
    h.final
    total = tk.PhotoImage(file='Total.png')
maker()

def function():
    global label_total2
    label_total2 = tk.Label(frame2, font=['Bahnschrift Light', 26, 'bold'], background='grey', fg='#00ccff',
        image=total, activebackground='#7fff80')
    label_total2.place(relx=0.01, rely=0.0135, relwidth=0.98, relheight=0.97)




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

root.mainloop()

