from Tkinter import *

import EmailSetup

def set_text(text):
    T.delete(1.0,END)
    T.insert(1.0,text)
    return

def input_text(input):
    modify = input.split(",")

def clear_entry(event, entry):
    entry.delete(0, END)

#setting up application window
window = Tk()
window.title("3DRFP_EMAIL_LYONS")
window.geometry("500x300")
window.wm_iconbitmap('')
# background_image=PhotoImage(file="dj.gif")
# background_label =Label(window, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)


#setting up titles and labels
Title = Label(window, text="SendEMail", fg="#383a40", font=("Helvetica",18))
instr1 = Label(window, text= "Enter The Email, Name, and Ticket number", font=("Helvetica", 13))
entInstr1 = Entry(window, fg="#273746", insertwidth="5")

T = Text(window, height=2, width=10)
T.pack(side=TOP, padx=(0,0), pady=(20,0))
T.insert(END, " Email \n Verifier")


#instr2 = Label(window, text= "Enter your working hours", font=("Helvetica", 13))
#entInstr2 = Entry(window, fg="#273746", insertwidth="5")

#allows entry to have a default text
entInstr1.insert(0, 'example@email.com,Name,20123')
#entInstr2.insert(0, 'Ex: 2:30-22:40')
#that gets erased after a mouse click
entInstr1.bind("<Button-1>", lambda event: clear_entry(event, entInstr1))
#entInstr2.bind("<Button-1>", lambda event: clear_entry(event, entInstr2))

#oraganizing the labels
#Title.pack(pady=(50,40))
instr1.pack(pady=(70,0))
entInstr1.pack(fill=X, padx=50)
#instr2.pack(pady=(20,3))
#entInstr2.pack()
#Buttons
sendbtn=Button(window, text="Send", fg="#000000", font=("Helvetica",10), command=lambda : [set_text(EmailSetup.SendEmail(entInstr1.get()))])
sendbtn.config(height=3, width=10)
sendbtn.pack(side=LEFT, padx=(150,6), pady=0)


updatebt=Button(window, text="Update", fg="#000000", font=("Helvetica",10),command=lambda : [prrint()])
updatebt.config(height=3, width=10)
updatebt.pack(side=LEFT )

window.mainloop()
