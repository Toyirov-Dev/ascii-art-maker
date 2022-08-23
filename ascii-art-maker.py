from tkinter import*
from tkinter import messagebox
from tkinter import filedialog,simpledialog
import time
import pyautogui
from random import randint
import os

rname = randint(1,1000)
rns = str(rname)

try:
    import pywhatkit    
except Exception as e:
    os.system("msg * Internetga ulanishni tekshiring!")
    time.sleep(1.5)
    exit()



# Window:
root = Tk()
root.title("Ascii Art Maker ")
root.geometry('250x250')
root.config(bg='#87ceeb')
root.iconbitmap('photos/pencil.ico')


# funktions:
def About():     
    label = messagebox.showinfo("About", "Dastur Toyirov Ziyodullo tomonidan\n 22.08.2202 - sanada yartildi.\n\n Dastur vazifasi: suratlarni  \n Ascii san'atiga convert qilish. \n\nTelegram: @Desperados_partfolio")

def Qollanma():     
    label = messagebox.showinfo("Qo'llanma", "Siz suratlarni ascii san'atiga convert qilish uchun \nBiror bir web-site dan yoki dasturdan foydalanasiz! \nSiz bu dastur orqali ortiqcha web-sahifalarga kirmasdan,\nsuratlaringizni ascii san'atiga convert qilishingiz mumkin,\nva ular 'ascii-arts' faylida text file bo'lib saqlanadi!\n\n-1) 'input'ga suratni manzilini yozing!\n-2) 'convert' tugmasini bosing! \n-3) Dasturdan chiqib, 'ascii-arts' foylini tekshiring!\n\n--> Ascii fayllar nomi random tarzda qo'yiladi!\n--> Dastur Internet bilan ishlaydi!  \n\n Agar sizda suratlar muvoffaqqiyatli\n convert bo'layotgan bo'lsa unda sizni\n tabriklaymiz!\n\n Support: 'About' bo'limida.")


def cmdExit():     
    quit()

def cmdOpen():     
    fd = filedialog.askopenfile(parent = root, mode = 'r')
    t = fd.read()     
    delete(0.0, END)
    insert(0.0, t)

def Convert():
    input_get = Input.get()
    save = 'ascii-arts/' + rns

    try:
        pywhatkit.image_to_ascii_art(input_get, save)
        os.system("msg * ASCII art saqlandi!")
    except Exception as e:
        os.system(" msg * Nimadir xato! Iltimos qayta tekshirib urinib ko'ring")


# Name:
Name = Label(root, text="Ascii Art Maker",
    fg='#8a2be2',
    font=('Times', 20, 'bold'),
    bg='#87ceeb')
Name.place(x=30, y=10)

# tavfsif:
tavfsif = Label(root, text="Suratni manzilini kiriting",
    fg='blue',
    font=('Times', 10, 'bold'),
    bg='#87ceeb')
tavfsif.place(x=50, y=80)

# select image file Input:
Input = Entry(root,
    bg='#e9967a',
    fg='black',
    font=('Times', 10, 'bold'),
    relief=SOLID,
    cursor='hand2',
    width=20)
Input.place(x=53, y=110)

# convert button:
button = Button(root, text='convert',
    bg='#e9967a',
    fg='black',
    font=('Times', 10, 'bold'),
    relief=SOLID,
    cursor='hand2',
    width=20,
    command=Convert)
button.place(x=50, y=180)



# Menu:
asciiMenu = Menu(root)
root.configure(menu=asciiMenu)


helpMenu = Menu(asciiMenu, tearoff = False)
asciiMenu.add_cascade(label='Help', menu = helpMenu)

helpMenu.add_command(label='About', command=About) 
helpMenu.add_command(label="Qo'llanma", command=Qollanma) 
helpMenu.add_separator()
helpMenu.add_command(label='Chiqish', command = cmdExit) 






root.mainloop()