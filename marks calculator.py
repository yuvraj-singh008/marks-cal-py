# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:48:38 2024

@author: Win
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice
root = Tk()
root.title("LAWRENCE SCHOOL SANAWAR MARKS CALCULATOR")
root.geometry("1920x1080")
root.configure(bg = "red")

subjects = ["ENGLISH - 301", "SST", "SCIENCE", "MATHS - 041", "PSYCHOLOGY - 037", "PHYSICAL EDUCATION - 048", "ARTS - 049", "SCULPTURE - 051", "BUSINESS STUDIES - 054", "ACCOUNTANCY - 055", "ENTREPRENEURSHIP - 066", "IP - 065", "COMPUTER SCIENCE - 083"]

logo = ImageTk.PhotoImage(Image.open("picture2.png"))
limg1 = Label(root, image = logo, bg = "white")
limg1.place(relx = 0.5, rely = 0.08, anchor = CENTER)

l1 = Label(root, text = "Enter roll number", fg="black", bg = "red", font=("Bahnschrift Light Condensed", 15))
textbox1 = Entry(root)
l1.place(relx = 0.2, rely = 0.2, anchor = CENTER)
textbox1.place(relx = 0.2, rely = 0.23, anchor = CENTER)

l2 = Label(root, text = "Enter name", fg="black", bg = "red", font=("Bahnschrift Light Condensed", 15))
textbox2 = Entry(root)
l2.place(relx = 0.5, rely = 0.2, anchor = CENTER)
textbox2.place(relx = 0.5, rely = 0.23, anchor = CENTER)

l3 = Label(root, text = "choose subject      and      enter marks" ,fg="black", bg = "red", font=("Bahnschrift Light Condensed", 15))
dd = ttk.Combobox(root, state = "readonly", values = subjects)
l3.place(relx = 0.8, rely = 0.2, anchor = CENTER)
dd.place(relx = 0.73, rely = 0.23, anchor = CENTER)
textbox3 = Entry(root)
textbox3.place(relx = 0.87, rely = 0.23, anchor = CENTER)
l4 = Label(root, text = " : " ,fg="black", bg = "red", font=("Bahnschrift Light Condensed", 15))
l4.place(relx = 0.8, rely = 0.23, anchor = CENTER)

rollno = textbox1.get()
name = textbox2.get()
marks = textbox3.get()
subject = dd.get()

names = []
rollnumber = []
engl = []
sstt = []
psycc = []
scie = []
mathss = []
phyed = []
artss = []
scul = []
bstt = []
acco = []
ipp = []
entop = []
cscc = []
total = []
percent = []
engbest3 = []

eng = ''
sst = ''
sci = ''
psy = ''
phed = ''
art = ''
math = ''
scu = ''
bst = ''
acc =''
ento = ''
ip = ''
csc = ''

def calculate():
    global eng
    global sst
    global sci
    global psy
    global phed
    global art
    global math
    global scu
    global bst
    global acc
    global ento
    global ip
    global csc
    if subject == "ENGLISH - 301":
        eng = marks
    elif subject == "SST":
        sst = marks
    elif subject == "SCIENCE":
        sci = marks
    elif subject == "PSYCHOLOGY - 037":
        psy = marks
    elif subject == "PHYSICAL EDUCATION - 048":
        phed = marks
    elif subject == "ARTS - 049":
        art = marks
    elif subject == "MATHS - 041":
        math = marks
    elif subject == "SCULPTURE - 051":
        scu = marks
    elif subject == "BUSINESS STUDIES - 054":
        bst = marks
    elif subject == "ACCOUNTANCY - 055":
        acc = marks
    elif subject == "ENTREPRENEURSHIP - 066":
        ento = marks
    elif subject == "IP - 065":
        ip = marks
    elif subject == "COMPUTER SCIENCE - 083":
        csc = marks
    else:
        print("choose subject")
        
    summarks = eng+sst+psy+sci+math+phed+art+scu+bst+acc+ip+ento+csc
    print(summarks)
    percentage = summarks/500*100
    
    names.append(name)
    rollnumber.append(rollno)
    engl.append(eng)
    sstt.append(sst)
    psycc.append(psy)
    scie.append(sci)
    mathss.append(math)
    phyed.append(phed)
    artss.append(art)
    scul.append(scu)
    bstt.append(bst)
    acco.append(acc)
    ipp.append(ip)
    entop.append(ento)
    cscc.append(csc)
    total.append(summarks)
    percent.append(percentage)
    engbest3.append()
    
        
    table = ttk.Treeview(window, columns = ('names', 'rollnumber', 'engl', 'sstt', 'psycc', 'scie', 'mathss', 'phyed', 'artss', 'scul', 'bstt', 'acco', 'ipp', 'entop', 'cscc', 'total', 'percent', 'engbest3'), show = 'headings')
    table.heading('names', text = 'NAME')
    table.heading('rollnumber', text = 'ROLLNO')
    table.heading('engl', text = 'ENG')
    table.heading('sstt', text = 'SST')
    table.heading('scie', text = 'SCI')
    table.heading('mathss', text = 'MATHS')
    table.heading('phyed', text = 'PHED')
    table.heading('artss', text = 'ART')
    table.heading('scul', text = 'SCU')
    table.heading('bstt', text = 'BST')
    table.heading('acco', text = 'ACC')
    table.heading('ipp', text = 'IP')
    table.heading('entop', text = 'ENTO')
    table.heading('cscc', text = 'CSC')
    table.heading('psycc', text = 'PSY')
    table.heading('total', text = 'TOTAL')
    table.heading('percent', text = '%')
    table.heading('engbest3', text = 'ENG+BEST 3')
    
    table.place(relx = 0.5, rely = 0.5, anchor = CENTER, fill = 'both', expand = True)
    
    '''for i in range(100):
    	first = choice(first_names)
    	last = choice(last_names)
    	email = f'{first[0]}{last}@email.com'
    	data = (first, last, email)
    	table.insert(parent = '', index = 0, values = data)'''

btn = Button(root, text = "SUBMIT", command = calculate)
btn.place(relx = 0.5,rely = 0.3, anchor = CENTER)
root.mainloop()