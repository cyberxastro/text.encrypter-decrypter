'''tkinter is used to provide the python user the GUI elements
for the python file using the widgets from tkinter toolkit'''
import base64
import tkinter
from tkinter import *
from tkinter import messagebox
'''CustomTkinter is a python UI-library based on Tkinter, which provides new, modern and fully customizable widgets.'''
import customtkinter
'''base64 is used to convert the bytes that have the binary text
data into the ASCII characters'''


def encryption_text():
    password = code.get()  # here we're fetching the password entered by the user
    '''password is basically the unique secret key for the 
    encryption or decryption'''
    if password == "1234":
        # defining the geometric structure of window
        image_icon = PhotoImage(file="encrypterimage.png")
        screen.iconphoto(False, image_icon)
        screen1 = customtkinter.CTkToplevel(screen)
        screen1.title("Encrypted Text")
        screen1.geometry("400x200")
        screen1.configure(fg_color="#3e1717")

        message = text1.get(1.0, END)
        # block of code for encrypting the text
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        customtkinter.CTkLabel(screen1, text='ENCRYPTED TEXT', font=("Rajdhani",20)).place(x=10, y=0)
        text2 = Text(screen1, font="Rajdhani", bg="#260f0f",fg="Silver",relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encryption", "Please enter the unique secret key")
    else:
        messagebox.showerror("encryption", "Your unique secret key wrong")


def decryption_text():
    password = code.get()  # here we're fetching the password entered by the user
    '''password is basically the unique secret key for the 
    encryption or decryption'''
    if password == "1234":
        # defining the geometric structure of window
        screen2 = customtkinter.CTkToplevel(screen)
        image_icon = PhotoImage(file="encrypterimage.png")
        screen.iconphoto(False, image_icon)
        screen2.title("Decrypted Text")
        screen2.geometry("400x200")
        screen2.configure(fg_color="#173e19")

        message = text1.get(1.0, END)
        # block of code for encrypting the text
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        customtkinter.CTkLabel(screen2, text='DECRYPTED TEXT', font=("Rajdhani",15)).place(x=10, y=0)
        text2 = Text(screen2, font="Rajdhani", bg="#13260f",fg="Silver",relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror(
            "Decryption", "Please enter the unique secret key")
    else:
        messagebox.showerror("decryption", "Your unique secret key wrong")


def main_screen():
    # specifying th scope of the variables to global
    global screen
    global code
    global text1

    screen = customtkinter.CTk()
    screen.geometry("618x380")

    image_icon = PhotoImage(file="encrypterimage.png")
    screen.iconphoto(False, image_icon)
    screen.title("Text Encrypter or Decrypter")

    # block of code for resetting the entire window
    def reset_all():
        code.set("")
        text1.delete(1.0, END)

    label = customtkinter.CTkLabel(screen, font=(
        "Rajdhani", 28), text="Enter the text which you want to encrypt")
    label.place(x=10, y=10)



    frame = customtkinter.CTkFrame(screen, corner_radius=10)
    frame.place(x=10, y=50, width=600, height=100)

    text1 = Text(frame, font="Rajdhani", bg="#2b2b2b",
                 relief=GROOVE, wrap=WORD, bd=0, fg="silver")
    text1.place(x=5, y=5, width=590, height=90)

    label = customtkinter.CTkLabel(screen, font=(
        "Rajdhani", 22), text="Enter the unique secret key for the encryprion or decryption")
    label.place(x=10, y=170)


    code = StringVar()

    Entry(textvariable=code, width=33, bd=0, bg="#2b2b2b", fg="RED", font=(
        "Rajdhani", 25), show="*").place(x=10, y=200)

    # specifying the design of the buttons
    customtkinter.CTkButton(screen, text="ENCRYPT", height=39, width=290,hover_color="red", command=encryption_text).place(x=10, y=250)
    customtkinter.CTkButton(screen, text="DECRYPT", height=39, width=290,hover_color="green",command=decryption_text).place(x=320, y=250)
    customtkinter.CTkButton(screen, text="RESET ALL", height=39, width=290,hover_color="orange",command=reset_all).place(x=10, y=300)
    customtkinter.CTkLabel(screen, text="Appearance mode: ", font=customtkinter.CTkFont(size=15, weight="bold")).place(x=320, y=300)
    customtkinter.CTkOptionMenu(screen, values=["Dark", "System", "Light"], button_hover_color="#1f6aa5",command=change_appearance_mode_event).place(x=470, y=300)

    ''' mainloop() is simply a method in the main window that executes what
    we wish to execute in an application,
    As the name implies it will loop forever until the user exits the window
    or waits for any events from the user.
    The mainloop automatically receives events from the window system and
    deliver them to the application widgets.This gets quits when we click
    on the close button.'''
    screen.mainloop()

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


# end of main screen here
main_screen()
