"""Installering av pyaudio:
 Installering av pyaudio
Hvis du bruker PyCharm kan du laste ned pyaudio ved å gå til preferences -> project -> project interpreter -> trykk på pluss-tegnet, for å så finne pyaudio og installere det.

Alternativt, på macOS kan man laste ned pyaudio ved å kjøre følgende kommando i terminalen:

$ pip3 install pyaudio
På Windows kan man installere pyaudio ved å kjøre følgende kommando:

$ python -m pip install pyaudio
Hvis dette ikke fungerer, kan pyaudio lastes ned manuelt som et såkalt wheel. Dette ligger tilgjengelig på følgende side: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
De forskjellige filene er for forskjellige Python-versjoner. Velg en som passer med din installasjon av Python, dette kan du se ve å kjøre python --version i terminalen. Filen installeres ved at man åpner en terminal i samme mappe som filen, og kjører python -m pip install filnavn, hvor filnavn er navnet på wheel-filen du lasted ned.
Problemer med innstallering av pyaudio:

Hvis installeringen ikke fungerer for macOS, prøv å kjøre følgende linje i terminalen.

$ brew install portaudio
Her er brew en pakkebehandler som gjør installering av programmer veldig enkelt.
Hvis dette ikke fungerer kan du google, eller lese mer av som står av tips her: https://stackoverflow.com/questions/33851379/pyaudio-installation-on-mac-python-3"""


import pyaudio
import numpy as np
 
p = pyaudio.PyAudio()
  
CONCERT_PITCH = 440  # kammertonen
HALF_INTERVAL = 2**(1 / 12)
C_FREQUENCY = CONCERT_PITCH * HALF_INTERVAL**(-9)
 
 
def play_tone(frequency, duration, volume=0.3):
    """
    Kode funnet på SO: https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
    Se også: http://en.wikipedia.org/wiki/Bit_rate#Audio
    """
    sampling_rate = 44100
    global stream
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)
 
 
def close():
    global stream
    stream.stop_stream()
    stream.close()
    p.terminate()
 
play_tone(440, 4)
 
close()
