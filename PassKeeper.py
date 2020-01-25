import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter.ttk

# ****** GLOBAL VARIABLES ******

objects = []
window = Tk()
window.withdraw()
window.title('Przechowalnia')


class Logowanie(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('loguj!')
        top.geometry('{}x{}'.format(270, 105))
        top.resizable(width=False, height=False)
        self.l_1 = Label(top, text="DAWAJ HASŁO KMIOCIE!!!!", font=('Courier', 14), justify=CENTER)
        self.l_1.pack()
        self.entry = Entry(top, show='*', width=30)
        self.entry.pack(pady=7)
        self.b_1 = Button(top, text='Zaloguj', command=self.wejdz, font=('Courier', 14))
        self.b_1.pack()

    def wejdz(self):
        self.value = self.entry.get()
        access = 'bombel'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.entry .delete(0, 'end')
            messagebox.showerror('Złe hasło!', 'Złe mówię! Mało szans pozostało Ci, bo: ' + str(5 - self.attempts))


class JuzDodawanie:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def wypisz(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class JuzDysponowanie:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 14))
        self.label_email = Label(self.window, text=dencryptedE, font=('Courier', 14))
        self.label_pass = Label(self.window, text=dencryptedP, font=('Courier', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=2)
        self.label_pass.grid(row=6 + self.i, column=4, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=5, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Usuń', 'Jesteś pewien, że chcesz usunąc konto??')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


# ******* FUNCTIONS *********


def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = JuzDodawanie(window, n, p, m)
    e.wypisz()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Dodane Konto', 'Dodano z powodzeniem, \n' + 'Nazwa: ' + n + '\nEmail: ' + m + '\nPassy: ' + p)
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = JuzDysponowanie(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


# ******* GRAPHICS *********

m = Logowanie(window)

entity_label = Label(window, text='Dodaj konto', font=('Courier', 18))
name_label = Label(window, text='Nazwa: ', font=('Courier', 14))
email_label = Label(window, text='Email: ', font=('Courier', 14))
pass_label = Label(window, text='Passy: ', font=('Courier', 14))
name = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, text='Add Email', command=onsubmit, font=('Courier', 14))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=1, rowspan=15, pady=3, sticky="ew")
tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=3, rowspan=15, pady=3, sticky="ew")

name_label2 = Label(window, text='Nazwa: ', font=('Courier', 14))
email_label2 = Label(window, text='Email: ', font=('Courier', 14))
pass_label2 = Label(window, text='Passy: ', font=('Courier', 14))


tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=1, row=5, rowspan=15, padx=5, sticky="ns")
tkinter.ttk.Separator(window, orient=VERTICAL).grid(column=3, row=5, rowspan=15, padx=5, sticky="ns")

name_label2.grid(row=5)
email_label2.grid(row=5, column=2)
pass_label2.grid(row=5, column=4)

L1 = Label(window, text=' ')
L1.grid( row=0, column=5, padx=2, pady=2, sticky=W)

readfile()

window.mainloop()