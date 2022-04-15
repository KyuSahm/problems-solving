
#fffrrroooggg -> fffrrroooggg
#ffffrogrogrog -> all kill
#frogfrogffrogrfrogogg -> g
def get_next_char(c):
	if (c == 'f'):
		return 'r'
	elif (c == 'r'):
		return 'o'
	elif (c == 'o'):
		return 'g'
	elif (c == 'g'):
		return 'f'

def remove_frog(s):
	answer = ""
	temp = ""
	next_char = 'f'
	found = False
	for i in range(0, len(s)):
		if s[i] == next_char:
			temp += s[i]
			if next_char == "g":
				temp = ""
				found = True
			next_char = get_next_char(next_char)
		else:
			if s[i] == "f":
				answer += temp
				temp = s[i]
				next_char = "r"
			else:
				answer += temp
				answer += s[i]
				temp = ""
				next_char = "f"

	if answer == "":
		return "all kill"
	elif not found:
		return answer
	else:
		return remove_frog(answer)

if __name__ == '__main__':	
	str = input()
	str_len = len(str)	
	print(remove_frog(str))