import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



behavior_steve = 'not-set'
voice_steve = 'not-set'
steve = pyttsx3.init('sapi5')
steve.setProperty('volume', 1)
voices = steve.getProperty('voices')
search_words = ['search', 'wikipedia', 'tell about']
wish_words = ['hello', 'hi', 'hai']
open_words = ['open', 'show']

def speak(str, rate):
    steve.setProperty('volume', 1)
    steve.setProperty('rate', rate)
    steve.say(str)
    steve.runAndWait()


def wishing():
    hour = datetime.datetime.now().hour
    print(hour)
    if hour < 12 and hour > 0:
        speak('hello! a very fresh and good morning!!', 100)
    elif hour > 12 and hour < 16:
        speak('hello!, good afternoon', 150)
    elif hour > 16 and hour < 23:
        speak('hello!good evening', 200)
    speak("i'm your voice assistant, here are some things that you need to do", 180)

def full_setting():
    voice_setting = input('voice of assistant(1=male, 2=female): ')
    while int(voice_setting) >= 3:
        voice_setting = input('voice of assistant(1=male, 2=female): ')
        if int(voice_setting) >= 3:
            speak('please select the aplied one', 134)

    if int(voice_setting) == 1:
        steve.setProperty('voice', voices[0].id)
        print('your assistant voice is as male')
        speak('voice set', 140)
    elif int(voice_setting) == 2:
        steve.setProperty('voice', voices[1].id)
        print('your assistant voice is as female')
        speak('voice set', 150)

    behavior = input('how should assistant behave with you(1=little angry; 2= happy all the time): ')
    if int(behavior) >= 3:
        speak('please select option as told', 200)
    while int(behavior) >= 3:
        behavior = input('how should assistant behave with you(1=little angry; 2= happy all the time): ')

        if int(behavior) >= 3:
            speak('please select option as told', 200)
    if int(behavior) == 1:
        print('your assistant is a bit angry')
    elif int(behavior) == 2:
        print('your assistant is happy all the time')


wishing()
full_setting()
speak('everything set all ready to go!!', 150)
speak('let me introduce myself!!', 130)
speak('''
im your voice assistant!! call me steve!!,
im not going to talk like other assistants!!
im fully different from others!!,
i am created by a developer named srikar!!,
now give me your first command!!
''', 170)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening to your first command!!')
        audi = r.listen(source)
        r.pause_threshold = 1

    try:
        text = r.recognize_google(audi)
        speak('okk!', 100)
        print('ok you said: {}'.format(text))
    except Exception as e:
        print("Say that again please...")
        speak('sorry!!', 160)
        return "None"
    return text

if __name__ == '__main__':
    while True:
        textllr = takeCommand().lower()
        if wish_words[0] in str(textllr) or wish_words[1] in str(textllr) or wish_words[2] in str(textllr):
            print('hehe!! hello!!')
            speak('hello!! have a great day', 150)
        elif search_words[0] in str(textllr) or search_words[1] in str(textllr) or search_words[2] in str(textllr):
            speak('okayyy!! searching for your query!!', 100)
            speak('Searching Wikipedia...',140)
            if search_words[0] in str(textllr):
                textllr = textllr.replace(search_words[0], "")
            elif search_words[1] in str(textllr):
                textllr = textllr.replace(search_words[1], "")
            elif search_words[2] in str(textllr):
                textllr = textllr.replace(search_words[2],"")
            results = wikipedia.summary(textllr, sentences=2)
            speak("According to Wikipedia", 180)
            print(results)
            speak(results, 140)
        elif 'exit' in str(textllr):
            speak('ok!! thanks for your great time!!have a good day bye!!', 170)
            print('bye!!')
            exit('self exit')
        elif str(open_words[0]) in textllr or open_words[1] in textllr:
            speak("opening please wait!! stay in line please wait!!", 150)
            if 'google' in textllr:
                webbrowser.open_new('google.com')
            elif 'youtube' in textllr:
                webbrowser.open_new('youtube.com')
        else:
            speak("sorry i don't understant!! i'm still a learning once sorry!!", 200)
