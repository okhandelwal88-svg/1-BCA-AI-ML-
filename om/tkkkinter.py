import tkinter as tk
root= tk.Tk()

selected_option=tk.IntVar()
question1ans=3

question=tk.Label(root,text="Q1 which option allows you to change the order of appereance of the animation?" )
question.pack()
radio_1=tk.Radiobutton(root,text="start",variable=selected_option,value=1)
radio_2=tk.Radiobutton(root,text="delay",variable=selected_option,value=2)
radio_3=tk.Radiobutton(root,text="recorder animation",variable=selected_option,value=3)
radio_1.pack()
radio_2.pack()
radio_3.pack()

def get_selected_value():
    currentselection=selected_option.get()
    print(f"selected answer:{currentselection}")
    if currentselection==question1ans:
        print("correct answer")
    else:
        print("wrong answer")
button=tk.Button(root,text="submit",command=get_selected_value)
button.pack()

selected_option1=tk.IntVar()
question2ans=5
question1=tk.Label(root,text="Q2 largest river in the world?" )
question1.pack()
radio_4=tk.Radiobutton(root,text="ganga",variable=selected_option1,value=4)
radio_5=tk.Radiobutton(root,text="nile",variable=selected_option1,value=5)
radio_6=tk.Radiobutton(root,text="krishna",variable=selected_option1,value=6)
radio_4.pack()
radio_5.pack()
radio_6.pack()

def get_selected_value1():
    currentselection=selected_option1.get()
    print(f"selected answer:{currentselection}")
    if currentselection==question2ans:
        print("correct answer")
    else:
        print("wrong answer")
button1=tk.Button(root,text="submit",command=get_selected_value1)
button1.pack()
root.mainloop()