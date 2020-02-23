
import subprocess
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter.ttk


cos = []

window = Tk()
window.withdraw()
window.title('Przechowalnia')


class Logowanie(object):

    loop = False
    attempts = 0
    haslo = 'okoń'

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('loguj!')
        top.geometry('{}x{}'.format(270, 155))
        top.resizable(width=False, height=False)
        self.l_1 = Label(top, text="DAWAJ HASŁO KMIOCIE!!!!", font=('Courier', 14), justify=CENTER)
        self.l_1.pack(pady=3)
        self.entry = Entry(top, show='*', width=30)
        self.entry.pack(pady=3)
        self.b_1 = Button(top, text='Zaloguj', command=self.wejdz, font=('Courier', 14))
        self.b_1.pack(pady=3)
        self.b_2 = Button(top, text='Zapomniałem hasła', command=self.wejdz, font=('Courier', 14))
        self.b_2.pack(pady=3)

    def wejdz(self):
        self.value = self.entry.get()

        if self.value == self.haslo:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.entry .delete(0, 'end')
            messagebox.showerror('Złe hasło!', 'Złe mówię! Mało szans pozostało Ci, bo: ' + str(5 - self.attempts))

    def zapomnialem(self):
        messagebox.showerror('Ojoj... biedactwo...\nTRZEBA BYŁO MYŚLE WCZEŚNIEJ!!!')


class KodujOdkoduj:

    key = 5

    def __init__(self, master, n, p, e):

        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def koduj(self, ile):
        w_co = ""
        for letter in ile:
            if letter == ' ':
                w_co += ' '
            else:
                w_co += chr(ord(letter) + self.key)
        return w_co

    def odkoduj(self, ile):
        w_co = ""
        for letter in ile:
            if letter == ' ':
                w_co += ' '
            else:
                w_co += chr(ord(letter) - self.key)
        return w_co

class JuzDodawanie(KodujOdkoduj):

    def wypisz(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        wez_n = self.koduj(n)
        wez_e = self.koduj(e)
        wez_p = self.koduj(p)

        f.write(wez_n + ',' + wez_e + ',' + wez_p + ', \n')
        f.close()


class JuzDysponowanie:


    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        a = KodujOdkoduj()

        daj_n = a.odkoduj(self.name)
        daj_e = a.odkoduj(self.email)
        daj_p = a.odkoduj(self.password)

        self.label_nazwa = Label(self.window, text=daj_n, font=('Courier', 14))
        self.label_email = Label(self.window, text=daj_e, font=('Courier', 14))
        self.button_pass = Button(self.window, text=daj_p, font=('Courier', 12), command=lambda: self.kopjuj(daj_p))
        self.button_usun = Button(self.window, text='X', fg='red', command=self.usun)

    def display(self):
        self.label_nazwa.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=2)
        self.button_pass.grid(row=6 + self.i, column=4, sticky=E)
        self.button_usun.grid(row=6 + self.i, column=6, sticky=E, padx=2, pady=2)

    def kopjuj(self, dane):
        kopjowane = 'echo ' + dane.strip() + '|clip'
        return subprocess.check_call(kopjowane, shell=True)

    def usun(self):
        czy_napewno = tkinter.messagebox.askquestion('Usuń', 'Jesteś pewien, że chcesz usunąc konto??')

        if czy_napewno == 'yes':
            for i in cos:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()
            f = open('emails.txt', "w")
            licz = 0
            for line in lines:
                if licz != self.i:
                    f.write(line)
                    licz += 1
                else:
                    licz += 1
                    continue
            f.close()
            wczytuje_plik()

    def destroy(self):
        self.label_nazwa.destroy()
        self.label_email.destroy()
        self.button_pass.destroy()
        self.button_usun.destroy()


# ******* FUNCTIONS *********


def juz_dodane():
    n = name.get()
    p = password.get()
    e = email.get()
    d = JuzDodawanie(window, n, p, e)
    d.wypisz()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Dodawanie konta', 'Dane dodanego konta \n' + 'Nazwa: ' + n + '\nEmail: ' + e + '\nPassy: ' + p)
    wczytuje_plik()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def wczytuje_plik():
    f = open('emails.txt', 'r')
    zlicz = 0

    for line in f:
        wejscie = line.split(',')
        e = JuzDysponowanie(window, wejscie[0], wejscie[1], wejscie[2], zlicz)
        cos.append(e)
        e.display()
        zlicz += 1
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
submit = Button(window, text='Dodaj Email', command=juz_dodane, font=('Courier', 14))

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
L1.grid(row=0, column=5, padx=2, pady=2, sticky=W)

wczytuje_plik()

window.mainloop()



