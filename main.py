'''tkinter is used to provide the python user the GUI elements
for the python file using the widgets from tkinter toolkit'''
from tkinter import *
from tkinter import messagebox

'''base64 is used to convert the bytes that have the binary text
data into the ASCII characters'''
import base64


def encryption_text():
    password = code.get() # here we're fetching the password entered by the user
    '''password is basically the unique secret key for the 
    encryption or decryption'''
    if password == "1234": 
        # defining the geometric structure of window
        image_icon = PhotoImage(file="encrypterimage.png")
        screen.iconphoto(False, image_icon)
        screen1 = Toplevel(screen)
        screen1.title("Encrypted Text")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        #block of code for encrypting the text
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text='ENCRYPTED TEXT', font="arial",
              fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encryption", "Please enter the unique secret key")
    else:
        messagebox.showerror("encryption", "Your unique secret key wrong")


def decryption_text():
    password = code.get() # here we're fetching the password entered by the user
    '''password is basically the unique secret key for the 
    encryption or decryption'''
    if password == "1234":
        # defining the geometric structure of window
        screen2 = Toplevel(screen)
        image_icon = PhotoImage(file="encrypterimage.png")
        screen.iconphoto(False, image_icon)
        screen2.title("Decrypted Text")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        #block of code for encrypting the text
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text='DECRYPTED TEXT', font="arial",
              fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white",
                     relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("Encryption", "Please enter the unique secret key")
    else:
        messagebox.showerror("encryption", "Your unique secret key wrong")


def main_screen():
    # specifying th scope of the variables to global
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("618x600")

    image_icon = PhotoImage(file="encrypterimage.png")
    screen.iconphoto(False, image_icon)
    screen.title("Text Encrypter or Decrypter")

    #block of code for resetting the entire window
    def reset_all():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter the text which you want to encrypt",
          fg="black", font=("Rajdhani", 18)).place(x=10, y=10)

    text1 = Text(font="Rajdhani", bg="White", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=600, height=150)

    Label(text="Enter the unique secret key for the encryprion or decryption",
          fg="black", font=("Rajdhani", 16)).place(x=10, y=170)

    code = StringVar()

    Entry(textvariable=code, width=33, bd=0, font=(
        "Rajdhani", 25), show="*").place(x=10, y=200)

    # specifying the design of the buttons
    Button(text="ENCRYPT", height="2", width=40, bg="#ed3833",
           fg="white", bd=0, command=encryption_text).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=40, bg="#00bd56",
           fg="White", bd=0, command=decryption_text).place(x=320, y=250)
    Button(text="RESET ALL", height="2", width=80, bg="#1089ff",
           fg="white", bd=0, command=reset_all).place(x=25, y=300)

    ''' mainloop() is simply a method in the main window that executes what
    we wish to execute in an application,
    As the name implies it will loop forever until the user exits the window
    or waits for any events from the user.
    The mainloop automatically receives events from the window system and
    deliver them to the application widgets.This gets quits when we click
    on the close button.'''
    screen.mainloop()

# end of main screen here
main_screen()
