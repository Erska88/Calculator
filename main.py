from tkinter import *




calculation_temp = ""
calculation_input = ""
calcualtion_result = ""

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "C", "0", "=", "/"
]

count = 0

def click(btn):
    global count
    count += 1
    print(count)

    global calculation_temp
    global calculation_input
    global calcualtion_result

    
    if ((calculation_input.isnumeric() or calculation_input == "") and btn.isnumeric()):
        calculation_input += btn
    elif (calculation_input.isnumeric() and btn in "+-*/="):
        calculation_temp = str(eval(calculation_temp + calculation_input))
        calculation_input = btn
    elif (calculation_input in "+-*/=" and btn.isnumeric()):
        if(calculation_input != "="):
            calculation_temp += calculation_input
        calculation_input = btn
    elif (btn == "="):
        calcualtion_result = str(eval(calculation_temp + calculation_input))
    elif (btn == "C" and calculation_input != ""):
        calculation_input = calculation_input[:-1]
    
    label1.config(text=calculation_temp) # update label text
    label2.config(text=calculation_input) # update label text
    label3.config(text=calcualtion_result) # update label text




# Create the main window
window = Tk()

label1 = Label(window, text=calculation_temp, font=('Ink Free',20,'bold'))
label1.grid(row=0, column=0, columnspan=4)

label2 = Label(window, text=calculation_input, font=('Ink Free',20,'bold'))
label2.grid(row=1, column=0, columnspan=4)

label3 = Label(window, text=calcualtion_result, font=('Ink Free',20,'bold'))
label3.grid(row=2, column=0, columnspan=4)

button_objs = []
for i in range(buttons.__len__()):
    button_objs.append(Button(window, text = buttons[i])) # create button object
    #button_objs[i].config(command=click) # performs calback on "click" - function
    button_objs[i].config(command=lambda btn=buttons[i]:click(btn)) # performs calback on "click" - function
    button_objs[i].config(font=('Ink Free',50,'bold'),bg="blue", fg="white") # background and foreground color
    row = 3 + (i // 4)  # Start buttons from row 3, calculate row based on index
    col = i % 4  # Column is index modulo 4
    button_objs[i].grid(row=row, column=col)



window.mainloop()







# label2 = Label(window, text="This is a simple counter app", font=('Ink Free',15))
# label2.pack()




