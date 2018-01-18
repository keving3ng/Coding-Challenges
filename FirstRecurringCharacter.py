'''First Recurring Character
Jan 17 2018
https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/

Example Input:
ABCDEBC -> B
IKEUNFUVFV -> U
PXLJOUDJVZGQHLBHGXIW -> J
*l1J?)yn%R[}9~1"=k7]9;0[$ -> 1
'''
chars = []
i = 0
cChar = str()

string = input ("Input the string: ")


while chars.count(cChar) == 0:
	chars.append(cChar)
	i += 1
	cChar = string[i]

print (cChar)
