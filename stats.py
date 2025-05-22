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
    print(f"{num_words} words found in the document")

# get character count
def get_num_characters():
	# set blank dictionary
	character_dict = {}
	# call get_book_text funtion
	contents = get_book_text(f)
	# convert contents to lowercase
	low_string = contents.lower()
	for chara in low_string:
		if chara in character_dict:
			character_dict[chara] += 1
		else:
			character_dict[chara] = 1
	return print(character_dict)

# open the file using a relative path and get word count
with open("books/frankenstein.txt") as f:
       	get_num_words()

with open("books/frankenstein.txt") as f:
	get_num_characters()

