# CSE-3313--HW02
This is the coding assignment for Homework 2 for CSE3313 (Introduction to Signal Processing) 


## Purpose
In this coding assignment, our purpose is to see how sinusoids of specific frequencies lead to specific sounds.

### Process
* We write a python program to produce an audio file of the 24 notes from lines 1 and 3 from twinkle.pdf
* The first note is C<sub>5</sub> (key number 52), the other notes will be relative to this note.
* For each of the other notes, we need to find its approximate frequency which will be an offset of the key A<sub>4</sub> (key number 49). The formula for this is *f = 440 x 2<sup>(keyNumber-49)/12</sup>*

