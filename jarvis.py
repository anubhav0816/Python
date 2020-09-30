import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

jarvis = pyttsx3.init()
voices = jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[0].id)

def talk(audio):
	jarvis.say(audio)
	jarvis.runAndWait()

def greet():
	cur_time = int(datetime.datetime.now().hour)
	if cur_time >= 0 and cur_time < 12:
		talk("Good Morning!")
	elif cur_time >= 12 and cur_time < 18:
		talk("Good Afternoon!")
	else:
		talk("Good Evening!")
	talk("This is your personal assistant Jarvis. How may I help you!")

def getCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language = 'en-in')
		print(f"You said: {query}\n")
	except Exception as e:
		print("Sorry.. May I beg Your pardon!")
		return "None"
	return query

if __name__ == "__main__":
	greet()
	while True:
		query = getCommand().lower()

		if 'open google' in query:
			webbrowser.open("google.com")
		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
		elif 'open geeksforgeeks' in query:
			webbrowser.open("geeksforgeeks.com")

		elif 'play music' in query:
			music_dir = 'C:\\Manav\\Songs\\MyFavourites'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))
		
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			talk(f"Sir, the time is {strTime}")

		elif 'open code' in query:
			codePath = "C:\\Users\\Manav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

		elif 'go to sleep' in query:
			talk("Going on standby Sir! You can call me anytime")
			break
