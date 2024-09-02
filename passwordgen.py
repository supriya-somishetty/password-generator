from tkinter import *
import string
import random

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    passwordField.delete(0, END)  # Clear the field before inserting a new password

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
def center_window(root, width=500, height=400):
    # Get the screen's width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate x and y coordinates for the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the geometry of the window with the calculated values
    root.geometry(f'{width}x{height}+{x}+{y}')

root=Tk()
center_window(root, 500, 400)
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.pack(pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.pack(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.pack(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.pack(pady=5)

lengthLabel=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.pack(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.pack(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.pack(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.pack(pady=10)

root.mainloop()
