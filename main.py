import speech_recognition as sr
import pyttsx3
import time
#from time import ctime
import webbrowser
import wikipedia
import random
#import pyaudio
#import pywhatkit

name = "Noob Doob"
listener = sr.Recognizer() # Make a listnening device
engine = pyttsx3.init()
#voices = engine.getProperty("voices")
#engine.setProperty("voices", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(ask = False):
    if ask:
        talk(ask)
    with sr.Microphone() as source: # Source is our microphone
        audio = listener.listen(source)    # Use recognizer to listen to what is said into the microphone
        voice_data = ""
        try:
            voice_data = listener.recognize_google(audio) #
        except sr.unknownValueError:
            talk("Sorry I did not get that")
        except sr.RequestError:
            talk("Sorry, my speech service is down")
        return voice_data.lower()


# These are commands to promt the assisatnat to ntroduce them selfes more prperly
intro_queries_to_check = ["tell me about yourself", "what can you tell me about yourself", "who are you", "what can you do", "what functions do you have", "what services do you provide?"]
# List of known greeting phrases
greetings_to_check = ["hello", "hi", "greetings", "good mornign", "good afternoon", "good day", "hola amigo"]
# list of known websites
urls_to_check = ["athena.itslearning.com/index.aspx", "github.com/GAJ96", "gaj96.github.io/gaj96/index.html", "youtube.com","runalyze.com/dashboard", "DN.se", "svtplay.se", "svt.se"]
# these commands correspond to above urls
website_commands = ["athena", "github", "personal website", "youtube", "runalyze", "dn", "svtplay", "svt"]

# This is the response
def respond(voice_data):

    # IF the assistant is greeted
    if any(greeting in voice_data for greeting in greetings_to_check):
        talk("Oh well " + random.choice(greetings_to_check) + ", you are so nice")

    # Ask their name
    if "what is your name" in voice_data:
        talk("Ah, I thought you knew that already. My name is " + name)

    # Prompt the assistant to introduce its different abilities
    if  any(intro_query in voice_data for intro_query in intro_queries_to_check):
        talk("Yes master. I am your virtual assistant " + name + ". My can do a great many things. Including performing google searches, finding locations of google maps, and sharing my vast library of knowledge as grate as the whole of wikipedia.")

    # What time/date is it?
    if "what time is it" in voice_data:#or "what date is it" #or "what day is it" or "give me todays date" in voice_data:
        talk(time.ctime())

    # Visit pre defined websites in website_commands
    if "website" in voice_data:
        website = ""
        while website not in website_commands:
            website = record_audio(talk("Which website do you wish to visit?"))
            print(website)
            if website in website_commands:
                url = "https://" + urls_to_check[website_commands.index(website)]
                print(website_commands.index(website))
                print(url)
                webbrowser.get().open(url)
                talk("Opening " + website)
            else:
                talk("Yeah I did not get that")
    # Search on google
    if "search" in voice_data:
        search = record_audio(talk("What do you want to search for?"))
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        talk("Here is what I found for " + search)

    # Find location on gmaps
    if "find location" in voice_data:
        location = record_audio(talk("What location do you want me to show you?"))
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        talk("This is the location of " + location)

    # Get wikipedia summary (by changing the method to tomething else, e.g. search you can get different wiki content)
    if "wiki" in voice_data:
        input = record_audio(talk("What topic do you wish to learn more about?"))
        length = ""
        try_count = 0
        while ("short" not in length or "long" not in lenght) and try_count <= 6:
            if try_count == 0:
                length = record_audio(talk("and do you want the long or the short verion?"))
            if try_count in range(1,4):
                length = record_audio(talk("Come again? Did you want the long or the short verion?"))
            if try_count == 4:
                length = record_audio(talk("This really should not be too complicated. You need oly to reply short or long."))
            if try_count == 5:
                length = record_audio(talk("Ok, this is getting far too irritating for me. Do you have vax in your ear or something in that manner? I will ask again. Do you wish for me to tell you the long or the shortened version of my vast knowledge about " + input))
            if try_count == 6:
                length = record_audio(talk("Oh fuck off bloody hell, you really are the most stupidest little shit"))
            if "short" in length:
                talk("Ok, this a shortened version about " + input)
                talk(wikipedia.summary(input, sentences = 3))
            if "long" in length:
                talk("Ok, this is all I know about " + input)
                talk(wikipedia.summary(input))
            if "short" not in length or "long" not in lenght or try_count < 6:
                try_count += 1

#    # Change name
#    if "I would like to change your name" in voice_data:
#        name = record_audio(talk("What name do you wish to give me?"))
#    if "play" in voice_data:
#        youtube = record_audio(talk("What on youtube do you want to play?"))
#        pywhatkit.playonyt(youtube)
#        talk("This is what I found searching " + youtube + " on youtube.")

    # Exit assistant
    if "terminate" in voice_data:
        talk("Ok, I will go to sleep now")
        exit()

    # If the commadn is not programmed into the assistant
    else:
        talk("Come again, I do not think that is part of my reportoar?")


time.sleep(1)
talk("How can I help you?")      # Promt the user
while 1:
    voice_data = record_audio()
    respond(voice_data)
