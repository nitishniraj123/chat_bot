from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import  *
import pyttsx3 as pp
import speech_recognition as s
import threading
engine=pp.init()
voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)
def speak(word):
    engine.say(word)
    engine.runAndWait()
bot=ChatBot("My Bot")
convo={
    'hello',
    'hi',
    'what is your name ?',
    'My name is Bot , i am created by Nitish',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Darbhanga',
    'In which language you talk',
    'I mostly talk in english'
}
trainer=ListTrainer(bot)
trainer.train(convo)
main=Tk()
main.geometry("500x650")
main.title("My Chat bot")
img=PhotoImage(file="chatbot.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-en')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognised")
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"You : "+ query)
    msgs.insert(END,"bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("vandana",20),command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()
main.bind('<Return>',enter_function)
def repeat():
    while True:
        takeQuery()
t=threading.Thread(target=repeat)
t.start()
main.mainloop()