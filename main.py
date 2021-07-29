import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
flag = 1

def intro():
    engine.say('Hello, I am Alexa.  How can I help you!')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

            elif 'siri' in command:
                talk('Who is siri?')

            elif 'google' in command:
                talk('Who is Google?')

    except:
        pass

    return command

def run_alexa():
    command = take_command()
    command = command.lower()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)

    elif 'search' in command:
        topic = command.replace('search','')
        info = pywhatkit.search(topic)

    elif 'what is' in command:
        topic = command.replace('what is', '')
        info = wikipedia.summary(topic,1)
        print(info)
        talk(info)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'exit' in command:
        talk('Bye, See you soon!')
        exit(0)

    else:
        talk('Please say the command again!')

intro()
while True:
    run_alexa()