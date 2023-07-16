import tkinter

# window
window = tkinter.Tk()
window.title("BMI")
window.minsize(width=450, height=300)

# label
my_label = tkinter.Label(text="Enter your weight (kg)")
my_label.pack()

# entry
mystring = tkinter.StringVar(window)
my_entry = tkinter.Entry(window,textvariable = mystring,width=15,fg="blue",bd=3,selectbackground='violet')
my_entry.pack()

# label
my_label_2 = tkinter.Label(text="Enter your height (cm)")
my_label_2.pack()

# entry
mystring_height = tkinter.StringVar(window)
my_entry_2 = tkinter.Entry(window,textvariable=mystring_height,width=15,fg="blue",selectbackground="violet")
my_entry_2.pack()


def getvalue():
    a=float(mystring.get())
    b=float(mystring_height.get())
    indeks = (float(a) / float(b*b))* 10000
    indeks = round(indeks,2)
    result_indeks=bmı(indeks)
    my_label_3.config(text=result_indeks)

def bmı(indeks):
    result_indeks = "Your BMI is : {}.You are ".format(indeks)
    if indeks <= 18.5:
        result_indeks += "underweight"
    elif 18.5 < indeks <= 24.9:
        result_indeks += "normal"
    elif 24.9 < indeks <= 29.9:
        result_indeks += "overweight "
    elif 29.9 <= indeks <= 34.9:
        result_indeks += "obese"
    else:
        result_indeks += "extremely obese"

    return result_indeks

# button
my_button = tkinter.Button(window,text='Submit',fg='White',bg= 'dark green',height = 1, width = 10,command=getvalue)
my_button.pack()

#label
my_label_3 = tkinter.Label()
my_label_3.pack()




window.mainloop()
