
## pip install music21
## pip install scipy
## install MuseScore2

from music21 import *

## Note:   http://web.mit.edu/music21/doc/moduleReference/moduleNote.html#music21.note.Note
## A note may be identified by a string.
n = note.Note('C4')
# n.show()          ## show as MusicXML file. (set MuseScore as default)
# n.show('midi')    ## passed to MuseScopre2.

## Play AS Stream:
def play(n):
    s = stream.Stream()
    s.append(n) 
    # s.show('midi')        

    ## Play with pygame's StreamPlayer
    midi.realtime.StreamPlayer(s).play() ## hear it immediately.
# play(n)

## Play an array of notes.
n = [note.Note('C#4'), note.Note('E-4'), note.Note('A4'), note.Note('F4')]
# play(n)

## A note may be identified by an integer which is called a MIDI Number.
# play(note.Note(midi=60))

def note_chromatic():    ## from C4(60) to C5(72), 13 steps
    s = stream.Stream()
    for i in range(60, 73):
        n = note.Note(midi=i)
        print(i, n.nameWithOctave, n.pitch.french)
        s.append(n)
    # midi.realtime.StreamPlayer(s).play()
    s.show('midi')
# note_chromatic()

## transpose(<step>) transform the note to the next step note.
def transpose():
    s = stream.Stream()
    n = note.Note('C4')
    for i in range(13):
        print(n.pitch.midi, n.nameWithOctave, n.pitch.french)
        s.append(n)
        n = n.transpose(1)      ## 1 step
    s.show('midi')
# transpose()

## But we are more familiar with only 8 notes.
midi_numbers = [60, 62, 64, 65, 67, 69, 71, 72]
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
def notes_test():
    s = stream.Stream()
    for i in notes:
        n = note.Note(i)
        print(n.pitch.midi, n.nameWithOctave, n.pitch.french)
        s.append(n)
    # midi.realtime.StreamPlayer(s).play()
    s.show('midi')
# notes_test()

## Chords:
## A chord is composed of multiple notes.
# play(chord.Chord(['C3', 'G#4', 'B5', 'A5']))  ## a list of note names.
# play(chord.Chord('C3 G#4 B5 A5'))             ## a string that contains note names.

## https://en.wikipedia.org/wiki/Chord_names_and_symbols_(popular_music)
## There are a lot of popular commonly defined chords.
def common_chord():
    s = stream.Stream()
    cs = [chord.Chord('c e- g'), chord.Chord('c e g'), chord.Chord('c e g#'), chord.Chord('c e- g-'),
          chord.Chord('c e g b-'), chord.Chord('c e g b'), chord.Chord('c e- g b'),
          chord.Chord('c e- g b-'), chord.Chord('c e g# b'), chord.Chord('c e g# b-'),
          chord.Chord('c e- g- b-'), chord.Chord('c e- g- b--'), chord.Chord('c e g- b-')]
    for c in cs:
        print(c.commonName)
        s.append(c)
    s.show('midi')
# common_chord()

# Quarter Length:
## The quarter length of a note defines the duration sound.
def quarter_len():
    s = stream.Stream()
    q = 0.0
    for _ in range(10):
        q += 0.5
        n = note.Note('C4')
        n.quarterLength = q
        print(n.pitch.french, n.quarterLength)
        s.append(n)
    s.show('midi')
# quarter_len()

## A chord may contains Duration.
def chord_len():
    s = stream.Stream()
    q = 0.0
    for _ in range(10):
        q += 0.5
        c = chord.Chord('A4 C#5 E5', duration=duration.Duration(q))
        print(c.commonName, c.duration)
        s.append(c)
    s.show('midi')
# chord_len()

## A Rest is a space between notes. By default it has the length of 1 quarter.
def rest():
    r = note.Rest()     ## default rest
    print(r.duration.type, r.duration.quarterLength)        ## quarter 1.0
    print(note.Rest(type='half').duration.quarterLength)    ## 2.0
    print(note.Rest(type='whole').duration.quarterLength)   ## 4.0
# rest()

def rest_test():
    s = stream.Stream()
    n = note.Note('C4')
    for i in range(13):
        s.append(n)
        s.append(note.Rest(type='whole'))
        n = n.transpose(1)
    s.show('midi')
# rest_test()

## TitnyNotation:
## http://web.mit.edu/music21/doc/moduleReference/moduleTinyNotation.html
##  - Note names are: a,b,c,d,e,f,g and r for rest.
##  - Flats, sharps, and naturals are notated as #,-, and n.
##  - After the note name, a number may be placed indicating the note length:
##     1 = whole, 2 = half, 4 = quarter, 8 = eighth, 16 = sixteenth
##    If omitted, it is assumed to be the same as the previous note.
def tiny():
    p = converter.parse('tinynotation: g# a2 e- g r a4 f f#2 f')
    # midi.realtime.StreamPlayer(p).play()
    p.show('midi')
# tiny()

## Composing By Programming
def mysong():
    s = stream.Stream()
  
    n1 = note.Note('C4#')
    s.repeatAppend(n1, 3)
    s.append(note.Rest(type='half'))
    
    n2 = note.Note('C4')
    n2.quarterLength = 3.0
    s.repeatAppend(n2, 10)
  
    # midi.realtime.StreamPlayer(s).play()
    s.show('midi')
# mysong()

## Music Scores
## MuseScore comes with sample scores (.mscz) in
##   %USER%\AppData\Local\MuseScore\MuseScore2

## music21 has the 'corpus' module which is a store that contains lot of music scores.
## Once a score is parsed, we can view, transform, and manipulate its components.
def score_test():
    s = corpus.parse('bwv7.7')  ## return a Score
    print(s[0].title)           ## s[0] is the metadata which has 'title' of the score.

    # midi.realtime.StreamPlayer(s).play()
    s.show('midi')
# score_test()

## Ex. Extracting Stream:
def extract():
    s = corpus.parse('bwv323')
    s = s.getElementById('Soprano')
    # s = s.getElementById('Tenor')
    s.show('mid')
# extract()

## Ex. Shiftng Notes.
def shift():
    s = corpus.parse('bwv323')
    s = s.getElementById('Soprano')
    t = stream.Stream()
    for n in s.flat.notes:
        t.append(n.transpose(3))
    t.show('midi')
# shift()

## Ex. Inserting Notes.
def insert():
    s = corpus.parse('bwv323')
    s = s.getElementById('Soprano')
    t = stream.Stream()
    i = 0
    for n in s.flat.notes:
        t.append(n)
        if i % 4 == 0:
            t.append(note.Rest(type='half'))
            # t.append(note.Note('C4'))
        i += 1
    t.show('midi')
# insert()

## The MusicXML file can be opened with MuseScore or Finale Reader
## http://musescore.org/
## http://finalemusic.com/Reader

## Midi File:
def midi_test():
    s = corpus.parse('bwv30.6')
    
    ## Write score to midi file
    fp = s.write('midi', fp='bach1.mid')
    
    ## Read and play midi file
    converter.parse('bach1.mid').show('midi')
# midi_test()   

