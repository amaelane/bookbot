import sys

# read the context of text file f, defined in with function
def get_book_text(f):
    file_contents = f.read()
    return file_contents

# process the contents of the book text
def get_num_words():
    # get the contents from the  get_book_text function
    contents = get_book_text(f)
    # split the contents string into a list
    words = contents.split()
    # find the length of the list
    num_words = len(words)
    # print the output as a f-string
    print(f"Found {num_words} total words")

# define how to sort list of dictionaries created in next function
def sort_on(dict):
	return dict["num"]

# get character count
def get_num_characters():
	print("--------- Character Count -------")
	# set blank dictionary
	character_dict = {}
	# set blank list
	char_num = []
	# call get_book_text funtion
	contents = get_book_text(f)
	# convert contents to lowercase
	low_string = contents.lower()
	# count how many times a character occurs
	for chara in low_string:
		if chara in character_dict:
			character_dict[chara] += 1
		else:
			character_dict[chara] = 1
	#return print(character_dict)
	# convert dictionary to dictionaries
	for char, num in character_dict.items():
		char_num_dicts = { 
			"char" : char ,
			"num" : num
			}
		# add dictionary to list only if the character is alphanumeric
		if char.isalpha():
			char_num.append(char_num_dicts)
			#print(char_num)
	# sort the dictionaries by number value in decending order (reverse=True)
	char_num.sort(reverse=True, key=sort_on)
	for value in char_num:
		char_value = value["char"]
		num_value = value["num"]
		print(f"{char_value}: {num_value}")

# open the file using a relative path and get word count/character count
with open(sys.argv[1]) as f:
    get_num_words()

with open(sys.argv[1]) as f:
	get_num_characters()
