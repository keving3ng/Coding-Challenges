''' Major Scales
Jan 17 2018
https://www.reddit.com/r/dailyprogrammer/comments/7hhyin/20171204_challenge_343_easy_major_scales/

Example Input:
Enter a scale: C
Enter a note: Do
> C, Do -> C

Scales:
C, C#, D, D#, E, F, F#, G, G#, A, A#, B
Notes:
Do, Re, Mi, Fa, So, La, Ti
'''


solfege = {"Do":0, "Re":2, "Mi":4, "Fa":5, "So":7, "La":9, "Ti":11}
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def major_scale(sc, no):
	return notes[(int(solfege.get(no)) + int(notes.index(sc))) % len(notes)]

if __name__ == "__main__":
	scale_name = 0
	note_name = 0

	while scale_name != -1:
		scale_name = str(input("Enter a scale: "))
		note_name = str(input("Enter a note: "))

		print (scale_name,",", note_name," -> ", major_scale(scale_name, note_name))
