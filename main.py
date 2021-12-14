from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
from cord import *
import numpy as np
import random

a = 2/3

포장마차1 = [[[16, 7], [16, 9], [8, 12]], [[2, 16, 0, 4], [4, 14, -1], [8, 16, -8]], [[8, 14, -3], [8, 4], [16, 7], [8, 14], [8, 16], [4, 21, -12, -8, -3]], [[4, 16, -12, -8, -5]], [[8, 12, -12, -7, -3], [8, 0], [16, 7, -3], [16, 9], [16, 12], [16, 14]], [[2, 16, -8, -5, 0]],
         [[2*a, 14, -13, -10, -5], [16, 0], [8, 2], [16, 4]], [[8, -12], [8, -8], [8, 4, -5], [16, 7, -12], [16, 7], [16, -5], [16, 4], [8, 9]], [[8, -15], [8, 4, -8], [8, 2, -3], [8, 0], [8, -15], [8, -8], [8, 7, -3], [8, 5]], [[8, -10], [8, -7], [8, 7, -3], [8, 5], [8, -10], [16, 4, -7], [16, 2], [16, -3], [8*a, 0]],
         [[8, 4, -12], [16, 7], [16, 7], [16, -8, -5], [8, 4], [16, 2]], [[8, -10], [8, -5], [8, 7, -1], [8, 9]], [[8, 4, -12], [8, -8], [4, -5], [8, 4, -12], [8, 7, -8], [16, 7, -5], [16, 4], [8, 9]], [[8, -15], [8, 4, -8], [16, 2, -3], [16, 0], [8, 0], [8, -8], [16, 4, -3], [16, 5], [16, 7], [16, 5]], [[8, -10], [16, 4, -7], [16, 2], [16, -3], [8, 0], [8, 0, -15], [16, 4, -7], [16, 2], [4, -3]],
         [[8, -12], [8, 0, -8], [4, 0, -5], [8, -12], [8, 0, -8], [8, 4, -5], [8, 7]], [[8, 9, -15], [8, -8], [8, 9, -3], [16, 0], [16, 2]], [[8, -10], [8, -5], [8, 11, -1], [8, 9]], [[8, 7, -8], [16, 4, -5], [16, 7], [16, 0], [8*a, 14]], [[8, 12, -12], [8, -8], [16, 7, -3], [16, 9], [16, 12], [16, 14]], [[8, 16, -15], [16, 12, -7], [16, 12], [16, -3], [8, 9], [16, 9]], [[8, 16, -12], [16, 14, -8], [16, 14], [16, -5], [8*a, 12]],
         [[8, 16, -12], [8, 16, -8], [8, 16, -3], [16, 12], [16, 14]], [[8, -10], [8, -5], [8, -1], [8, 0], [4, -10, -5, -1], [16, 7], [16, 9], [16, 12], [16, 9]], [[8, 16, -12, -8, -5], [16, 16], [8, 16], [16, 12, -12], [16, 14], [8, -12, -8, -5], [16, 16], [16, 16], [8, -8, -5], [16, 12], [16, 14]], [[8, 16, -12, -8, -3], [16, 16], [8*a, 16], [16, 12, -12], [16, 14]], [[8, -10, -7, -3], [16, 12], [16, 12], [8*a, -7, -3], [16, 7]]]
포장마차2 = [[[16, 16, -12, -8, -3], [16, 16], [16, 16], [16, 17], [16, 16], [16, 14], [16, 12, -12], [16, 12]], [[4, -12, -8, -5], [8, -8, -5], [16, 7], [16, 9]], [[16, 16, -12, -8, -3], [16, 16], [16, 16], [16, 17], [16, 16], [16, 14], [16, 12, -12], [16, 14]], [[4, -10, -5, -1], [16, 7, -5, -1], [16, 9], [16, 12], [16, 9]], [[8, 16, -12, -8, -5], [16, 16], [8*a, 16], [16, 12, -12], [16, 14], [8, -12, -8, -5], [16, 16], [16, 16], [8, -8, -5], [16, 12], [16, 14]], [[8, 16, -12, -8, -3], [16, 16], [8*a, 16], [16, 17, -12], [16, 19]], [[4, 21, -10, -7, -3], [4, 19, -7, -3]],
         [[16, 19, -12, -8, -5], [16, 19], [16, 19], [16, 19], [16, 19], [16, 17], [16, 16, -12], [16, 12]], [[4, -12, -7, -3], [8, -7, -3], [16, 9], [16, 12]], [[16, 16, -12, -8, -3], [16, 16], [16, 16], [16, 16], [16, 16], [16, 17], [8, 16]], [[8, -10, -7, -3], [16, 16, -7, -3], [8*a, 14]], [[16, -12, -8, -5], [16, 12], [8, 12], [16, 19], [16, 21], [16, 24], [16, 21]],
         [[8, 28, -8], [8, -5], [8, -1], [8, 19]], [[8, 26, -10], [8, -5], [4, 24, -1]], [[8, 24, -12], [8, -8], [4, -5], [8, -12, -8, -5], [8, 0], [8, 4], [8, 7]], [[8, 9, -12], [8, -7], [8, 9, -3], [16, 0], [16, 2]], [[8, -10], [8, -5], [8, 11, -1], [8, 9]], [[8, 7, -8], [16, 4, -5], [16, 7, 0], [8*a, 14]], [[8, 12, -12], [8, -8], [16, 7, -3], [16, 9], [16, 12], [16, 14]],
         [[8, 16, -12], [16, 12, -7], [16, 12], [16, -3], [8, 9], [16, 9]], [[8, 16, -12], [16, 14, -8], [16, 14], [16, -5], [8*a, 12]], [[8, 16, -12], [8, 16, -8], [8, 16, -3], [16, 12], [16, 14]], [[8, -10], [8, -5], [4, -1], [4, -10, -5, -1], [16, 7], [16, 9], [16, 12], [16, 9]], [[8, 16, -12, -8, -5], [16, 16], [8*a, 16], [16, 12, -12], [16, 14], [8, -12, -8, -5], [16, 16], [16, 16], [8, -8, -5], [16, 12], [16, 14]],
         [[8, 16, -12, -8, -3], [16, 16], [8*a, 16], [16, 12, -12], [16, 14]], [[8, -10, -7, -3], [16, 12], [16, 12], [8*a, -7, -3], [16, 7]], [[16, 16, -12, -8, -3], [16, 16], [16, 16], [16, 17], [16, 16], [16, 14], [16, 12, -12], [16, 12]], [[4, -12, -8, -5], [8, -8, -5], [16, 7], [16, 9]], [[16, 16, -12, -8, -3], [16, 16], [16, 16], [16, 17], [16, 16], [16, 14], [16, 12, -12], [16, 14]], [[4, -10, -5, -1], [16, 7, -5, -1], [16, 9], [16, 12], [16, 9]]]
포장마차3 = [[[8, 16, -12, -8, -5], [16, 16], [8*a, 16], [16, 12, -12], [16, 14], [8, -12, -8, -5], [16, 16], [16, 16], [8, -8, -5], [16, 12], [16, 14]]]
# 두번쩨 마디 할 차레
포장마차 = 포장마차1 + 포장마차2 + 포장마차3

포장마차cord1 = [X, C, Am, C, F, Am, G, C, Am, Dm, C, G, C, Am, Dm, C, F, G, C, Am, F, C, Am, Eb, C, Am, Dm]
포장마차cord2 = [Am, C, Am, G, C, Am, Dm, C, F, Am, Dm, C, Em, G, C, F, G, C, Am, F, C, Am, G, C, Am, Dm, Am, C, Am, G]
포장마차cord3 = [C]
포장마차cord = 포장마차cord1 + 포장마차cord2 + 포장마차cord3

def existIn(list, a):
    try:
        return list.index(a)
    except ValueError:
        return -1

def findNotes(music):
    notes = []
    for i in music:
        for j in i:
            n = j[1:]
            if existIn(notes, n) == -1:
                notes.append(n)
    return notes

def findCordLens(music):
    cordLen = []
    for i in music:
        if existIn(cordLen, len(i)):
            cordLen.append(len(i))
    cordLen.sort()
    return cordLen

def findCordNotes(music, cord):
    cordNotes = []
    for i in range(len(cords)):
        cordNotes.append([])

    for i, c in zip(music, cord):
        for j in i:
            n = j[1:]
            if existIn(cordNotes[cords.index(c)], n) == -1:
                cordNotes[cords.index(c)].append(n)
    return cordNotes

def findvalues(music):
    values = []
    for i in music:
        for j in i:
            if existIn(values, j[0]):
                values.append(j[0])
    return values

def findNoteRootChange(music):
    noteRoot = []
    for i in music:
        for j in i:
            n = j[1:]
            if n[0] >= 0:
                noteRoot.append(n[0])

    noteRootChange = []
    for i1, i2 in zip(noteRoot[:-1], noteRoot[1:]):
        noteRootChange.append(i2 - i1)
    return noteRootChange

def randomChoice(matrix):
    l = matrix.tolist()
    randomList = []
    for i, n in zip(l, range(len(l))):
        randomList += [n] * i
    return random.choice(randomList)

def setCordChain(cord):
    cordChain = np.full((len(cords), len(cords)), 0)
    for i1, i2 in zip(cord[:-1], cord[1:]):
        cordChain[cords.index(i1)][cords.index(i2)] += 1
    return cordChain

def setCordLenChain(music):
    cordLens = findCordLens(music)

    cordLen = []
    for i in music:
        cordLen.append(len(i))

    cordLenChain = np.full((len(cordLens), len(cordLens)), 0)
    for i1, i2 in zip(cordLen[:-1], cordLen[1:]):
        cordLenChain[cordLens.index(i1)][cordLens.index(i2)] += 1
    return cordLenChain

def setNoteChain(music, cord):
    notes = findNotes(music)
    noteChain = np.full((len(cords), len(notes), len(notes)), 0)
    for i, c in zip(music, cord):
        for j1, j2 in zip(i[:-1], i[1:]):
            n1 = j1[1:]
            n2 = j2[1:]
            noteChain[cords.index(c)][notes.index(n1)][notes.index(n2)] += 1
    return noteChain

def setOnlyNoteChain(music):
    notes = findNotes(music)
    onlyNoteChain = np.full((len(notes), len(notes)), 0)
    noteList = []
    for i in music:
        for j in i:
            n = j[1:]
            noteList.append(n)

    for n1, n2 in zip(noteList[:-1], noteList[1:]):
        onlyNoteChain[notes.index(n1)][notes.index(n2)] += 1

    return onlyNoteChain

def setValueChain(music):
    values = findvalues(music)

    value = []
    for i in music:
        for j in i:
            value.append(j[0])

    valueChain = np.full((len(values), len(values)), 0)
    for i1, i2 in zip(value[:-1], value[1:]):
        valueChain[values.index(i1)][values.index(i2)] += 1
    return valueChain

def setBoundaryNoteChain(music, cord):
    notes = findNotes(music)


    boundaryNoteChain = np.full((len(cords), len(cords), len(notes), len(notes)), 0)
    for i1, i2, cnt in zip(music[:-1], music[1:], range(len(music) - 1)):
        n1 = i1[-1][1:]
        n2 = i2[0][1:]
        boundaryNoteChain[cords.index(cord[cnt])][cords.index(cord[cnt+1])][notes.index(n1)][notes.index(n2)] += 1
    return boundaryNoteChain

def setNextNoteChain(music):
    noteRootChanges = list(set(findNoteRootChange(music)))

    nextNoteChain = np.full((len(noteRootChanges), len(noteRootChanges)), 0)
    for i1, i2 in zip(noteRootChanges[:-1], noteRootChanges[1:]):
        nextNoteChain[noteRootChanges.index(i1)][noteRootChanges.index(i2)] += 1
    return nextNoteChain

def composer(music, cord, length=30, startCord=C):
    cordChain = setCordChain(cord)
    cordLenChain = setCordLenChain(music)
    noteChain = setNoteChain(music, cord)
    valueChain = setValueChain(music)
    boundaryNoteChain = setBoundaryNoteChain(music, cord)
    nextNoteChain = setNextNoteChain(music)

    newCord = [startCord]
    for i in range(length - 1):
        newCord.append(cords[randomChoice(cordChain[cords.index(newCord[-1])])])

    cordLens = findCordLens(music)
    newCordLen = [random.choice(cordLens)]
    for i in range(length - 1):
        newCordLen.append(cordLens[randomChoice(cordLenChain[cordLens.index(newCordLen[-1])])])

    values = findvalues(music)
    newValue = [random.choice(values)]
    for i in range(length):
        for j in range(cordLens[i]):
            newValue.append(values[randomChoice(valueChain[values.index(newValue[-1])])])

    notes = findNotes(music)
    cordNotes = findCordNotes(music, cord)
    newNote = [[7]]
    for i in range(length):
        for j in range(newCordLen[i] - 1):
            newNote.append(notes[randomChoice(noteChain[cords.index(newCord[i])][notes.index(newNote[-1])])])
        if i != length - 1:
            #newNote.append(notes[randomChoice(boundaryNoteChain[cords.index(newCord[i])][cords.index(newCord[i+1])][notes.index(newNote[-1])])])
            #newNote.append(random.choice(cordNotes[cords.index(newCord[i+1])]))


            cordNotes = findCordNotes(music, cord)
            priorNoteChange = newNote[-1][0] - newNote[-2][0]
            nowCordNote = []
            for i in cordNotes[cords.index(newCord[i+1])]:
                nowCordNote.append(i)

            nowNote = []
            noteRootChanges = list(set(findNoteRootChange(music)))
            for i in noteRootChanges:
                nowNote.append(i + priorNoteChange)

            for i, cnt in zip(reversed(nowCordNote), range(len(nowCordNote)-1 , -1, -1)):
                if existIn(nowNote, i[0]) == -1:
                    del nowCordNote[cnt]
            newNote.append(random.choice(nowCordNote))





    note = [NoteSeq(), NoteSeq(), NoteSeq(), NoteSeq()]

    for n, v in zip(newNote, newValue):
        size = len(n)
        for k in range(size):
            note[k].append(Note(n[k], octave=5, dur=1 / v))
        for k in range(size, 4):
            note[k].append(Rest(dur=1 / v))

    midi = Midi(number_tracks=1, tempo=120)
    for i in range(4):
        midi.seq_notes(note[i], track=0)
    midi.write('a5.mid')

def marcofComposer(music, length=150):
    noteChain = setOnlyNoteChain(music)
    valueChain = setValueChain(music)

    notes = findNotes(music)
    newNote = [random.choice((notes))]
    for i in range(length):
        newNote.append(notes[randomChoice(noteChain[notes.index(newNote[-1])])])

    values = findvalues(music)
    newValue = [random.choice(values)]
    for i in range(length):
        newValue.append(values[randomChoice(valueChain[values.index(newValue[-1])])])

    note = [NoteSeq(), NoteSeq(), NoteSeq(), NoteSeq()]

    for n, v in zip(newNote, newValue):
        size = len(n)
        for k in range(size):
            note[k].append(Note(n[k], octave=5, dur=1 / v))
        for k in range(size, 4):
            note[k].append(Rest(dur=1 / v))

    midi = Midi(number_tracks=1, tempo=120)
    for i in range(4):
        midi.seq_notes(note[i], track=0)
    midi.write('a7.mid')



done = False
while not done:
    try:
        #composer(포장마차, 포장마차cord, length=15)
        marcofComposer(포장마차, length=150)
    except IndexError:
        continue
    done = True


"""
note = [NoteSeq(), NoteSeq(), NoteSeq(), NoteSeq()]

for i in 포장마차:
    for j in i:
        size = len(j) - 1
        for k in range(size):
            note[k].append(Note(j[k+1], octave=5, dur=1/j[0]))
        for k in range(size, 4):
            note[k].append(Rest(dur=1/j[0]))

midi = Midi(number_tracks=1, tempo=66)
for i in range(4):
    midi.seq_notes(note[i], track=0)
midi.write('포장마차.mid')
"""
