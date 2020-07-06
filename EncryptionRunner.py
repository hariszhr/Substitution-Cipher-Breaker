try:
    from tkinter import *
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'tkinter']) # install pkg
    subprocess.check_call(["python", '-m', 'pip', 'install',"--upgrade", 'tkinter']) # upgrade pkg
    from tkinter import *

from string import ascii_lowercase
from string import ascii_uppercase

def textfield_print(field,text):
    field.delete('1.0', END)
    field.insert(INSERT,text)
    return

def EncryptButtonPressed():

    button.config(state='disabled', text='Wait...')
    button.update()

    try:
        pt = plainText.get('1.0', END).strip()
        k = KeyText.get('1.0', END).strip()
        clean_pt = ''
        clean_k = ''

        # Clean plain text
        for c in pt:
            if (c in ascii_uppercase or c in ascii_lowercase):
                clean_pt = clean_pt + c.upper()
        # Clean key
        for c in k:
            if (c in ascii_uppercase or c in ascii_lowercase):
                clean_k = clean_k + c.upper()

        # if plain text is empty..
        if (len(clean_pt) is 0):
            textfield_print(CipherText, 'ERROR - current plain text: ' + clean_pt + '\nPlain text is empty')
            CipherText.config(highlightbackground='red')
            return
        # if key length is not equal to 26
        elif len(clean_k) != 26:
            textfield_print(CipherText, 'ERROR - current key: ' + clean_k + '\nKey must be 26 chars long')
            CipherText.config(highlightbackground='red')
            return
        else:
            dict = {}
            for c in clean_k:
                dict[c] = 'blah'
            if (len(dict) < 26):
                textfield_print(CipherText,
                                'ERROR - current key: ' + clean_k + '\nEvery character in key must be unique')
                CipherText.config(highlightbackground='red')
                return
            else:
                print('plain text:', clean_pt)
                print('key:', clean_k)

                # Encryption
                d = {}
                defualt = Alphabets.get('1.0', END).strip()
                idx = 0
                for c in defualt:
                    d[c] = clean_k[idx]
                    idx = idx + 1

                ciphertext = ''
                for c in clean_pt:
                    ciphertext = ciphertext + d[c]

                textfield_print(CipherText, ciphertext)
                CipherText.config(highlightbackground='green')
                return
    finally:
        button.config(state='active', text='Encrypt')
        button.update()

root= Tk()
baseWidth=int(root.winfo_screenwidth()/2);
baseHeight=int(root.winfo_screenheight()/1.5);

root.resizable(False, False)
root.title("Substitution Cipher")
root.geometry(str(baseWidth)+"x"+str(baseHeight))

Label(root, text="Plain Text: ").grid(row=0,sticky=NW,pady=(5,5))
plainText = Text(root)
plainText.config(wrap=WORD, height=10, highlightbackground='black')
plainText.grid(row=0,column=1,pady=(5,5))

Label(root, text="").grid(row=1)

Alphabets= Text(root, height= 1)
Alphabets.grid(row=2, column=1, sticky=NW,pady=(5,5))
Alphabets.insert('insert','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Alphabets.config(state=DISABLED)

Label(root, text="Enter Key: ").grid(row=3, sticky=NW,pady=(5,5))
KeyText= Text(root, height=1, width=26, highlightbackground= 'black')
KeyText.grid(row=3,column=1, sticky=NW,pady=(5,5))

button= Button(root, text="Encrypt", height=3)
button.grid(row=4, columnspan=2,pady=(5,5))
button.config(command= EncryptButtonPressed)

Label(root, text="Cipher Text: ").grid(row=5, sticky=NW,pady=(5,5))
CipherText= Text(root, height=10, highlightbackground= 'black')
CipherText.grid(row=5,column=1)

root.mainloop()