import pyttsx3 as voice
import pygame
pygame.init()
song = ('Song.mp3')
pygame.mixer.music.load(song)

engine = voice.init()
engine.setProperty('rate', 250)
engine.setProperty('volume', 10)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

pygame.mixer.music.play(-1)
engine.say("If there's 14 000604 ways Where it goes wrong, then why play?")
engine.say("If we’ve got one chance to win Make room I'll be goin in, aye")
engine.say("Cause I'm a beast on a mic, Thanos on a mission")
engine.say("Lyrics tryin to get your mind stoned like it’s vision")
engine.say("Kinda like Romanoff, Hawkeye with precision")
engine.say("When I get to going off the greatest shit you'll ever witness like")
engine.say("Tony stark in the suit when I blast fast")
engine.say("I swear that you're invisible to me you can ask drax")
engine.say(" Captain Marvel flying over heads with my last tracks")
engine.say("I don't think you've got the stones to snap back")
engine.setProperty('rate', 100)
engine.setProperty('volume', 100)
engine.say("Oh.")
engine.say("Hi Diva!")
engine.runAndWait()
