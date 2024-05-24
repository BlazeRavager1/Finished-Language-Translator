from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import ttk

root = Tk()

root.geometry("1080x600")
root.title("Language Translater")

language = list(LANGUAGES.values())
language_codes = list(LANGUAGES.keys())

label_title = Label(root, text="LANGUAGE TRANSLATOR")
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label=Label(root,text="Enter Text")
label.place(relx=0.1, rely=0.2,anchor=W)

cb1 = ttk.Combobox(state='readonly', values=language, width=22)
cb1.place(relx=0.3,rely=0.2,anchor=W)
cb1.set("english")

ta1 = Text(root, height=11, wrap=WORD, width=60)
ta1.place(relx=0.02,rely=0.5,anchor=W)

label1=Label(root,text="Output")
label1.place(relx=0.7, rely=0.2,anchor=E)

cb2 = ttk.Combobox(state='readonly', values=language, width=22)
cb2.place(relx=0.9,rely=0.2,anchor=E)
cb2.set("Select Output Language")

ta2 = Text(root, wrap=WORD, width=60, height=11)
ta2.place(relx=0.98,rely=0.5,anchor=E)

def Translate():
    translator = Translator()
    src_lang = language_codes[language.index(cb1.get())]
    dest_lang = language_codes[language.index(cb2.get())]
    translated = translator.translate(text=ta1.get(1.0,END), dest=dest_lang, src=src_lang)
    ta2.delete(1.0,END)
    ta2.insert(END, translated.text)

btn = Button(text='Translate', command=Translate)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()

"""
I had to change the code and remove the fonts and colors since they interfered with the code, run 
pip install -U googletrans==4.0.0-rc1 for the code to work properly
DIfferent than other projects for this reason.
"""