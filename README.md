# Messagator
Messagator is a multithreaded application which provides a GUI to set parameters such as contact name, source language and destination language to fetch messages from Whatsapp and performs Translation and Text to Speech operations on it.

## Threads
It uses two threads created using the Threading module
1. Interface Thread - This thread runs the GUI interface built using tkinter which allows us to set contact name , source language and destination language.
2. Message THread - This runs runs the selenium configured with chrome driver to extract the messages from Whatsappweb

## Preview
![image](https://user-images.githubusercontent.com/75805927/210992848-091b095e-1e8a-4a1f-9a6f-dbc1da2ea5b4.png)
