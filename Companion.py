
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser  # Import the webbrowser module
import pyjokes
import time
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Store the current playing song
current_song = None

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = "good bye"
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'buddy' in command:
                command = command.replace('buddy', '')
                print(command)
    except Exception as e:
        print(e)
    return command

def run_buddy():
    global current_song  # Use a global variable to track the currently playing song
    command = take_command()
    print("You said:", command)
    time.sleep(4)
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
        current_song = song  # Update the current song
    elif 'stop' in command:
        if current_song:
            talk('Stopping the song ' + current_song)
            pywhatkit.stop()  # Stop the currently playing song
            current_song = None  # Reset the current song
        else:
            talk('No song is currently playing.')
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time:", current_time)
        talk('The current time is ' + current_time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%d %B %Y')
        print("Current date:", current_date)
        talk('Today\'s date is ' + current_date)
    elif 'tell' in command:
        query = command.replace('tell', '')
        info = wikipedia.summary(query, sentences=2)
        print("Wikipedia says:", info)
        talk(info)
    elif 'love me' in command:
        print('Yes, I love you, my friend!')
        talk('Yes, I love you, my friend!')
    elif 'date' in command:
        print('Sorry, I have a headache.')
        talk('Oh sorry! I have a headache.')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'how are you' in command:
        print('I am doing good, what about you, my friend?')
        talk('I am doing good, what about you, my friend?')
    elif 'who are your friends' in command:
        print('It\'s you, Alexa, and Siri')
        talk('It\'s you, Alexa, and Siri')
    elif 'how old are you' in command:
        print('That is a ridiculous question; it is giving me a headache.')
        talk('Oh! That is a ridiculous question; it is giving me a headache.')
    elif 'happy' in command:
        talk('Hey, that\'s great to hear! I am happy for you. Wait, I will sing a song for you.')
        pywhatkit.playonyt('Hiriye Hiriye')
    elif 'sad' in command:
        talk('I am sorry to hear that you are feeling sad today. Let me try to make you happy.')
        talk(pyjokes.get_joke())
        talk('I hope you feel better now. Try engaging with your friends and family or do activities that make you happy.')
    elif 'angry' in command:
        talk('Calm down for a while. Take deep breaths and go for a walk.')
        pywhatkit.playonyt('Baby calm down')
    elif 'guilty' in command:
        talk('It\'s fine; don\'t feel so miserable. Things done in the past can\'t be changed, so forgive yourself and avoid repeating the same mistakes.')
    elif 'fear' in command:
        talk('There is nothing to fear. Confidence is the key to success. Everything is possible; it\'s your efforts that matter.')
    elif 'good bye' in command:
        talk('Okay, thank you, see you later.')
        exit(0)
    
    elif ''  in command: 
        import wikipedia as googlescrap
        query =command.replace("jarvis"," ")
        query= command.replace(""," ")
        query=command.replace("google","")
        talk("this what i found!")
        pywhatkit.search(query)
        try:
            result=googlescrap.summary( query,2)
            talk(result)
        except:
            talk('Sorry I am not able to answer!')
       
    
    elif 'who is' in command:
        query = command.replace('who is', '')
        search_url = "https://www.google.com/search?q=" + query
        webbrowser.open(search_url)  # Open the Google search results in the default web browser
           
            
    else:
        print('I couldn\'t understand. Can you please repeat that?')
        talk('I couldn\'t understand. Can you please repeat that?')

initial_message = "Hey, I am your buddy. How are you? What can I do for you?"
talk(initial_message)

while True:
    run_buddy()
 
 
