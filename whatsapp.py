from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator
from gtts import gTTS
import os
import time
import threading
import queue


# initialisation 
message_queue = queue.Queue()

#GUI 
def interface(message_queue): 
    contact_translation=''
    source=''
    dest=''
    
    def get_messages(contact_name):
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\pyhton\\chromedriver.exe") #opens chromedriver
        driver.maximize_window()
        driver.get("https://web.whatsapp.com/")  #opens whatsapp
        time.sleep(30)

        search_box = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
        search_box.send_keys(contact_name)
        
        wait = WebDriverWait(driver, 10)
        contact_title = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,' +"'" + contact_name +"'"+ ')]')))
        time.sleep(10)
        contact_title.click()
        time.sleep(10)
        messages = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div') #inspect
        
        #the output is in list, so convert it to a queue
        for message in messages:
            message_queue.put(message.text)
    
    def fetch_messages(contact_name):
        message_thread = threading.Thread(target=get_messages, args=[contact_name])
        message_thread.start()
        message_thread.join()
        messagebox.showinfo("Alert", "Messages from "+contact_name+" have been extracted")
        translate_text(source, dest)


    root = Tk()
    root.title('Messagator')
    root.geometry('700x600')

    frame1=Frame(root,width=300,height=400,bg="cyan")
    frame2=Frame(root,width=300,height=400,bg="pink")
    frame3=Frame(root,width=600,height=200,highlightbackground="black",highlightthickness=1)
    frame4=Frame(frame3,width=500,height=150,highlightbackground="black",highlightthickness=1)
    frame5=Frame(frame3,width=100,height=150,highlightbackground="black",highlightthickness=1)
    frame6=Frame(frame3,width=600,height=50,highlightbackground="black",highlightthickness=1)

    #frames
    frame1.grid(row=0,column=0,sticky="nsew")
    frame2.grid(row=0,column=1,sticky="nsew")
    frame3.grid(row=1,column=0,rowspan=2,columnspan=2,sticky="new")
    frame4.grid(row=0,column=0,sticky="nsew")
    frame5.grid(row=0,column=1,sticky="nsew")
    frame6.grid(row=2,column=0,rowspan=2,columnspan=2,sticky="nsew")

    #frame configuration
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    frame3.columnconfigure(0,weight=2)
    frame3.columnconfigure(1,weight=1)

    #text box
    text_box1=Text(frame1,bg="light blue",fg="black",relief="solid")
    text_box2=Text(frame2,bg="greenyellow",fg="black",relief="solid")
    text_box1.grid(row=0,column=0,sticky="nsew")
    text_box2.grid(row=0,column=1,sticky="nsew")
    text_box1.rowconfigure(0,weight=1)
    text_box1.columnconfigure(0,weight=1)
    text_box2.columnconfigure(1,weight=1)
    text_box1.pack(expand=True,fill=BOTH)
    text_box2.pack(expand=True,fill=BOTH)

    #button
    btn=Button(frame5,text="Fetch Messages",bg="light blue",relief='ridge',font=('Helvetica',10,'bold'), command= lambda: fetch_messages(contact_translation))
    btn.grid(row=1,column=0)
    textBox1 = Text(root)
    textBox2 = Text(root)
    #audio converter
    def convert_audio():
        text_info =  textBox2.get("1.0", "end-1c")
        myObj=gTTS(text=text_info,lang='hi',slow=False)               
        myObj.save('SpeechTest.mp3')
        os.system("SpeechTest.mp3")
    photo=PhotoImage(file="C:\\Users\\user\\Desktop\\pyhton\\Speaker.png")
    speakerbtn=Button(frame5,image=photo, command=convert_audio)
    speakerbtn.grid(row=0,column=0,pady=15)
    
    
    def callback(*arg):
        nonlocal contact_translation
        contact_translation=box.get()

    #combo box1
    contact_combotext=tk.StringVar()
    contact_combotext.set('Type or enter Contact')
    names=["Contact1", "Contact2", "Contact3"]
    box=ttk.Combobox(frame6, values=names, textvariable=contact_combotext)
    box.grid(row=0,column=0,sticky="nsew")  
    contact_combotext.trace('w', callback)

    def callback_source(*arg):
        nonlocal source
        source=sbox.get()
    
    #combo box2
    source_language=StringVar()
    source_language.set('Source Language')
    sbox=ttk.Combobox(frame6,textvariable=source_language,state="read-only")
    sbox['values']=("English",
                    "Kannada",
                    "Hindi",
                    "French",
                    "Korean")
    sbox.grid(row=0,column=1,sticky="nsew")
    source_language.trace('w', callback_source)  

    def callback_dest(*arg):
        nonlocal dest
        dest=dbox.get()
        
    #combo box3
    destination_language=StringVar()
    destination_language.set('Destination Language')
    dbox=ttk.Combobox(frame6,textvariable=destination_language,state="read-only")
    dbox['values']=("English",
                    "Kannada",
                    "Hindi",
                    "French",
                    "Korean")
    dbox.grid(row=0,column=2,sticky="nsew")  
    destination_language.trace('w', callback_dest)  
    
    #combo box configuration
    frame6.columnconfigure(0,weight=1)
    frame6.columnconfigure(1,weight=1)
    frame6.columnconfigure(2,weight=1)

    def translate_text(source, dest):
        textBox1.grid(row=0, column=0)
        textBox1.tag_add("l1", "1.0", "1.50")
        textBox1.tag_configure("l1",background = "white",foreground= "red")
        textBox1.tag_add("l2", "2.0", "2.50")
        textBox1.tag_configure("l2",foreground= "blue")


        textBox2.grid(row=0, column=1)
        textBox2.tag_add("l1", "1.0", "1.50")
        textBox2.tag_configure("l1",foreground= "red")
        textBox2.tag_add("l2", "2.0", "2.50")
        textBox2.tag_configure("l2",foreground= "blue")

        while not message_queue.empty():
            #Languages 
            lang_dict = {                                
                "English": "en",
                "Kannada": "kn",
                "Hindi": "hi",
                "French": "fr",
                "Korean": "ko"
            }
            text = message_queue.get()
            textBox1.insert(INSERT, text)
            translator = Translator()
            textTranslated = translator.translate(text, src=lang_dict[source], dest=lang_dict[dest])
            textBox2.insert(INSERT, textTranslated.text+"\n")

    root.call('encoding', 'system', 'utf-8')
    root.mainloop()


thread = threading.Thread(target=interface, args=[message_queue])
thread.start()
thread.join()

print("Terminating applicaton...")          
