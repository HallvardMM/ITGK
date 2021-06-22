#øving 7 oppgave 9
"""
Akkorder og toner - løsning
 
Denne oppgaven handler om å lage en metode som tar inn en akkord som argument, og returnerer en liste med alle
akkordtonene.
"""
 
right = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
left = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
 
# Alle dur og moll akkorder som ligger i den venstre delen av kvintsirkelen, frem til 6 b-er.
quint_circle_left = ['F', 'Dm', 'Bb', 'Gm', 'Eb', 'Cm', 'Ab', 'Fm', 'Db', 'Bbm', 'Gb', 'Ebm']
 
major = 4, 3
minor = 3, 4
dim = 3, 3
aug = 4, 4
 
# Mapper akkordsymboler til riktige intervaller.
mood = {'m': minor, '': major, 'dim': dim, 'aug': aug}
 
 
def get_tone_list(chord):
    """ Returnerer rekken med toner som tilsvarer denne akkorden. Dette er for å få akkordtoner som ligger i riktig
    skala. Feks skal man helst få
    >> chord_notes('B') -> ['B', 'D#', 'F#']
    og ikke
    >> chord_notes('B') -> ['B', 'Eb', 'Gb']
    """
    if chord in quint_circle_left:
        return left
    return right
 
 
def get_undertone(chord):
    """ Finner grunntonen, og returnerer tuple på formen: (grunntone, resten) """
    if '#' in chord or 'b' in chord:
        return chord[:2], chord[2:]
    else:
        return chord[0], chord[1:]
 
 
def chord_notes(chord):
    undertone, rest = get_undertone(chord)
 
    # Finner på hvilken side av kvintsirkelen akkorden ligger
    basic_chord = undertone
    if rest in ['', 'm']:
        basic_chord = chord
    tone_list = get_tone_list(basic_chord)
 
    # Finner hvilke to intervaller 2. og 3. tone av akkorden ligger.
    t_1, t_2 = mood[rest]
 
    # Finner indexen til grunntonen i listen med toner.
    undertone_index = tone_list.index(undertone)
 
    # Finner index og tone til den 2. akkordtonen.
    third_index = (undertone_index + t_1) % 12
    third = tone_list[third_index]
 
    # Finner index og tone til den øverste akkordtonen.
    fifth_index = (third_index + t_2) % 12
    fifth = tone_list[fifth_index]
 
    return [undertone, third, fifth]
 
def main():
    print('Skriv akkorden du vil finne grunntonene til.\n"done" når du er ferdig\nmood = {m:minor, "":major, dim:diminished, aug:augmented')
    while True:
        s=str(input("Skriv inn akkord her "))
        if s=="done":
            break
        else:
            print(chord_notes(s))
main()


