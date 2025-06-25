import json
import pyttsx3
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self, recipe_json_path):
        # Load JSON file
        with open(recipe_json_path, "r", encoding="utf-8") as f:
            self.recipe = json.load(f)

        # If wrapped inside "recipe" key, unwrap it
        if "recipe" in self.recipe:
            self.recipe = self.recipe["recipe"]

        self.steps = self.recipe["steps"]
        self.index = 0
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        print(f"🗣️ Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_command(self):
        with sr.Microphone() as source:
            self.speak("I'm listening...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"🎤 You said: {command}")
            return command
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            self.speak("Speech recognition service is unavailable.")
            return ""

    def start_cooking(self):
        self.speak("Let's begin cooking!")

        while self.index < len(self.steps):
            step = self.steps[self.index]["step_text"]
            self.speak(f"Step {self.index + 1}: {step}")

            while True:
                command = self.listen_command()

                if "next" in command:
                    self.index += 1
                    break
                elif "repeat" in command:
                    self.speak(f"Repeating: {step}")
                elif "how long" in command:
                    duration = self.steps[self.index].get("duration_seconds", 0)
                    if duration and duration > 0:
                        minutes = duration // 60
                        seconds = duration % 60
                        if minutes > 0:
                            self.speak(f"This step takes about {minutes} minute(s) and {seconds} seconds.")
                        else:
                            self.speak(f"This step takes about {seconds} seconds.")
                    else:
                        self.speak("No specific time mentioned for this step.")
                elif "ingredients" in command:
                    ingredients = self.recipe.get("ingredients", [])
                    self.speak("You will need: " + ", ".join(ingredients))
                else:
                    self.speak("Please say: next, repeat, how long, or ingredients.")

        self.speak("🎉 You're done! Enjoy your meal.")
