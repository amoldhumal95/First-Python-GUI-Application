import os
import pyttsx3                  #pip install pyttsx3
import pythoncom
import datetime                 
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia                    #pip install wikipedia
import smtplib
import webbrowser as wb
import subprocess
from Tkinter import *
#from PIL import ImageTk,Impip listage

########### Initialize Text to audio engine ##############
engine = pyttsx3.init()
alpha = 1
window = Tk()

window.title("Assistant")
window.geometry("512x512")
window.config(bg='black')

####################### Transparent BG ##########################
window.configure(background = "yellow")
window.wm_attributes("-transparentcolor", "yellow")
window.attributes("-alpha", alpha)


###################################

#canvas = Canvas(window,width=512,height=512)
# image = ImageTk.PhotoImage(Image.open("I:/Python Tlinter 4 GUI/1.jpg"))
# canvas.create_image(0,0,anchor=w,image=image)
# canvas.pack()

#################### Buttons Functions #####################
def lowAlpha():
    global window, alpha
    alpha = alpha - 0.05
    window.attributes("-alpha", alpha)
def incAlpha():
    global window, alpha
    alpha = alpha + 0.05
    window.attributes("-alpha", alpha)
def openAi():
    ai()
    window.destroy()

def openPS():
    os.startfile('C:/Program Files/Adobe/Adobe Photoshop CC 2019/Photoshop.exe')
    speak("Opening Photoshop Creative Cloud for you sir ...")
def openFilmora():
    os.startfile('C:/Program Files/Wondershare/Filmora9/Wondershare Filmora9.exe')
    speak("Opening Filmora 9 for you sir...")
def openDolby():
    os.startfile('C:/Program Files (x86)/Dolby Home Theater v4/pcee4l.exe')
    speak("Opening Dolby Home Thetre 4.0 for you sir ... Enjoy most beautiful sound equilizer ...")
def openvsCode():
    os.startfile('C:/Program Files/Microsoft VS Code/Code.exe')
    speak("Opening Visual Studio code for you sir ...")
def openVlc():
    os.startfile('C:/Program Files (x86)/VideoLAN/VLC/vlc.exe')
    speak("Opening VLC music player for you")
def openNV():
    os.startfile('C:/Program Files/NVIDIA Corporation/NVIDIA GeForce Experience/NVIDIA GeForce Experience.exe')
    speak("Opening NVIDIA GeForce Experience for you")
def openChrome():
    os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
    speak("Opening Chrome Web Browser for you...")
def openExcel():
    os.startfile('C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE')
    speak("Opening Microsoft Excel for you...")
def openWord():
    os.startfile('C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE')
    speak("Opening Microsoft Word for you...")
def openPpt():
    os.startfile('C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE')
    speak("Opening Microsoft Power Point for you...")
def openNpp():
    os.startfile('C:/Program Files/Notepadplus/notepadplus.exe')
    speak("Opening Notepad plus plus for you...")
############################ Button ###########################
#ghost = Button(window, text = "GhostMode" , command = lowAlpha).pack(anchor='w')
#alpha = Button(window, text = "Alpha" , command = incAlpha).pack(anchor='w')
ai = Button(window, text="Ai Assistant", command=openAi,bg='black' ,fg='lime', borderwidth=0).pack(anchor='w')
ps = Button(window, text="Photoshop", command=openPS,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
filmora = Button(window, text="Filmora9", command=openFilmora,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
dolby = Button(window, text = "Dolby Home Thetre 4.0", command=openDolby,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
vsCode = Button(window, text = "Visual Studio Code",command = openvsCode,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
vlc = Button(window, text="VLC", command=openVlc,bg='black',fg='lime' , borderwidth=0).pack(anchor='w')
nvidia = Button(window, text="NVidia GeForce 920Mx", command=openNV,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
chrome = Button(window, text = "Chrome", command = openChrome,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
excel= Button(window, text = "MS Excel" , command = openExcel ,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
word= Button(window, text = "MS Word" , command = openWord,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
ppt= Button(window, text = "MS PowerPoint" , command = openPpt ,bg='black',fg='lime', borderwidth=0).pack(anchor='w')
npp= Button(window, text = "Notepad++" , command = openNpp ,bg='black',fg='lime' ,borderwidth=0).pack(anchor='w')









###################################################################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is Hack Like Pro's AI Assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Amol")
    time()
    date()
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour <12:
        greet = "Good Morning!"
    elif hour >= 12 and hour <17:
        greet = "Good Afternoon!"
    elif hour >= 17 and hour <21:
        greet = "Good Evening!"
    else:
        greet = "Go to bed now its too late!"    
    speak(greet)
    speak("Hack Like Pro is at your service. Please tell me how can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        print("say that again please!")
        #speak("say that again please!")

        return "None"

    return query


def sendEmail(to, containt):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amoldhumal95@gmail.com', 'password')
    server.sendmail('amoldhumal95@gmail.com',to, containt)
    server.close()
#####################################################################################################


def ai():
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()  
        
        elif 'date' in query:
            date()
        elif 'offline' in query:
            quit()
        elif 'wikipedia' in query:
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=5)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say")
                containt = takeCommand()
                to = 'ilovuamol@gmail.com'
                sendEmail(to, containt)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'open chrome' in query:
            speak("Opening Chrome Web Browser for you...")
            os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
        elif 'open photoshop' in query:
            speak("Opening Photoshop Creative Cloud for you...")
            os.startfile('C:/Program Files/Adobe/Adobe Photoshop CC 2019/Photoshop.exe')
        elif 'open excel' in query:
            speak("Openinig Microsoft Excel for you")
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE')
        elif 'open notepad' in query:
            speak("Opening Notepad plus plus")
            os.startfile('C:/Program Files/Notepadplus/notepadplus.exe %s')
            
        elif 'search in chrome' in query:
            speak("What should I search for u")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')


window.mainloop()