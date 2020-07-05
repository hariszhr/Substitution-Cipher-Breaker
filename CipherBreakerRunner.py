try:
    from tkinter import *
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'tkinter']) # install pkg
    subprocess.check_call(["python", '-m', 'pip', 'install',"--upgrade", 'tkinter']) # upgrade pkg
    from tkinter import *

import Algorithm as CB
from string import *

root  = Tk()
CipherTextLabel = Label(root)
PlainTextLabel = Label(root)

KeyLabel = Label(root)
CipherText = Text(root)
Plaintext = Text(root)
Keytext = Text(root)
MaxIterFrame = Frame(root)
MaxIterLabel = Label(MaxIterFrame)
MaxIterations = Text(MaxIterFrame)

RealKeyLabel = Label(root)
RealKeytext = Text(root)

button_run = Button(root)

key='mykey'
key_match=''
cipher_text=''
plain_text=''
error_text=''


def user_interface_setup():
    baseWidth=int(root.winfo_screenwidth()/1.5);
    baseHeight=int(root.winfo_screenheight()/1.5);
    
    root.resizable(False, False)
    root.title("INSE6110 - Substitution Cipher Breaker")
    root.geometry(str(baseWidth)+"x"+str(baseHeight))
    
    CipherTextLabel.config(text="Cipher Text: ")
    CipherTextLabel.grid(row=0, sticky=NW,pady=(5,5))
    CipherText.config(wrap=WORD, height=10, highlightbackground='black')
    CipherText.grid(row=0,column=1,pady=(5,5))

    MaxIterFrame.grid(row=1, sticky=NSEW, pady=(5, 5))
    MaxIterLabel.config(text="Max Iterations")
    MaxIterLabel.grid(row=1, sticky=E, pady=(5, 5))
    MaxIterations.config(height=1, width=10, highlightbackground='black')
    MaxIterations.grid(row=1, column=1, sticky=E, pady=(5, 5))

    button_run.config(text='DECRYPT', command=run_button_handler)
    button_run.grid(row=1, column=1, pady=(5, 5))
    
    PlainTextLabel.config(text="Decrypted Plain Text: ")
    PlainTextLabel.grid(row=2, sticky=NW,pady=(5,5))
    Plaintext.config(wrap=WORD, height=10, highlightbackground='black')
    Plaintext.grid(row=2,column=1,pady=(5,5))
    
    KeyLabel.config(text="key: ")
    KeyLabel.grid(row=3, sticky=NW,pady=(5,5))
    Keytext.config(wrap=WORD, height=2, highlightbackground='black')
    Keytext.grid(row=3,column=1,pady=(5,5))

    RealKeyLabel.config(text="Orig key: ")
    RealKeyLabel.grid(row=4, sticky=NW, pady=(5, 5))
    RealKeytext.config(wrap=WORD, height=2, highlightbackground='black')
    RealKeytext.grid(row=4, column=1, pady=(5, 5))
    
    root.mainloop()

def normalized_orig_key():
    key = RealKeytext.get('1.0', END).strip()
    RealKeytext.config(highlightbackground='black')
    clean_k=''
    if key is '':
        return ''
    for c in key:
        if (c in ascii_uppercase or c in ascii_lowercase):
            clean_k = clean_k + c.upper()
    if len(clean_k) != 26:
        textfield_print(RealKeytext, 'ERROR - current key: ' + clean_k + '\nKey must be 26 chars long')
        RealKeytext.config(highlightbackground='red')
        return ''
    else:
        dict = {}
        for c in clean_k:
            dict[c] = 'blah'
        if len(dict) < 26:
            textfield_print(RealKeytext,
                            'ERROR - current key: ' + clean_k + '\nEvery character in key must be unique')
            RealKeytext.config(highlightbackground='red')
            return ''
    textfield_print(RealKeytext,' '.join(list(clean_k)))
    return clean_k


def decryption():
    global plain_text, error_text, key, key_match  # update globally

    s = MaxIterations.get('1.0',END).strip()
    if not s.isdigit():
        return False
    print('max iterations: ', s)
    plain_text, key, key_match = CB.Start_Algorithm(cipher_text, int(s), normalized_orig_key())
    return True


def validate_cipher_text():
    global cipher_text,error_text
    
    cipher_text = CipherText.get('1.0', END).strip()
    
    if not(cipher_text.isalpha() & cipher_text.isupper()):
        error_text='ERROR: cipher text must be ONLY uppercase alphabets!'
        return False
    else:
        return True


def run_button_handler():
    global button_run,Plaintext,cipher_text,plain_text,error_text,key,Keytext

    button_run.config(state='disabled', text='Wait...')
    button_run.update()

    textfield_print(Plaintext, 'processing... please wait.')

    # try:
    if not validate_cipher_text():
        Plaintext.config(highlightbackground='red')
        Keytext.config(highlightbackground='red')
        textfield_print(Plaintext, error_text)
        textfield_print(Keytext, '')
        button_run.config(state='active', text='DECRYPT')
        return
    else:
        if decryption():
            Plaintext.config(highlightbackground='green')
            Keytext.config(highlightbackground='green')
            textfield_print(Plaintext, plain_text)
            textfield_print(Keytext, ' '.join(key) + ' (Match: ' + key_match + '%)')
            button_run.config(state='active', text='DECRYPT')
        else:
            Plaintext.config(highlightbackground='red')
            Keytext.config(highlightbackground='red')
            textfield_print(Plaintext, 'UNABLE TO DECRYPT')
            textfield_print(Keytext, '')
            button_run.config(state='active', text='DECRYPT')
        return
    # except Exception as e:
    #     textfield_print(Plaintext, 'EXCEPTION OCCURRED\n'+str(e))
    #     button_run.config(state='active', text='DECRYPT')


def textfield_print(field, text):
    field.delete('1.0', END)
    field.insert(INSERT,text)
    return




if __name__ == '__main__':
    user_interface_setup()
    