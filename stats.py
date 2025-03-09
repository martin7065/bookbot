def word_counter(path):
	with open(path) as f:
		file_contents = f.read()
	word_string = file_contents.split()
	word_count = len(word_string)
	return word_count

def letter_counter(path):
	with open(path) as f:
		file_contents = f.read()
	char_counts = {}
	text = file_contents
	text = text.lower()
	for char in text:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def chars_to_sorted_list(char_counts):
	char_list = []
	for char, count in char_counts.items():
		char_list.append({"char":char, "count":count})
		
	def sort_on(dict_item):
		return dict_item["count"]
	
		
	char_list.sort(reverse=True, key=sort_on)
	return char_list

