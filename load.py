import re # Regular Expressions
import _thread # Threading
import pygame # The sound starter thingy majingy
import time # Time.sleep for delaying in spaces
pygame.init() # Init
pygame.mixer.init() # Init
class TextToSpeech: # Main Class

    def __init__(self, words_pron_dict:str='cmudict-0.7b.txt'):
        self._l = {}
        self._load_words(words_pron_dict)

    def _load_words(self, words_pron_dict:str):
        with open(words_pron_dict, 'r') as file:
            for line in file:
                if not line.startswith(';;;'):
                    key, val = line.split('  ',2)
                    self._l[key] = re.findall(r"[A-Z]+",val)

    def get_pronunciation(self, str_input):
        list_pron = []
        for word in re.findall(r"[\w']+",str_input.upper()):
            if word in self._l:
                list_pron += self._l[word]
        print(list_pron)
        delay=0
        for pron in list_pron:
            _thread.start_new_thread( TextToSpeech._play_audio, (pron,delay,))
            delay += 0.145
    
    def _play_audio(sound, delay):
        try:
            time.sleep(delay)
            #wf = wave.open("sounds/"+sound+".wav", 'rb')
            prefix = "sounds/"
            suffix = ".wav"
            s = pygame.mixer.Sound(f"{prefix}{sound}{suffix}")
            s.play()
            return
        except:
            pass
    
 
 

if __name__ == '__main__':
    tts = TextToSpeech()
    while True:
        try:
            tts.get_pronunciation(input('Enter a word or phrase: '))
        except:
            exit()
