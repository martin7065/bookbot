import sys
from stats import letter_counter, chars_to_sorted_list, word_counter


def main():
	#path = "./books/frankenstein.txt"
	
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	else:
		word_count = word_counter(sys.argv[1])
		char_counts = letter_counter(sys.argv[1])
		sorted_char = chars_to_sorted_list(char_counts)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ----------")
		print(f"Found {word_count} total words")
		print("--------- Character Count -------")
		for char_dict in sorted_char:
			char = char_dict["char"]
			count = char_dict["count"]
			if char.isalpha():
				print(f"{char}: {count}")
		print("============= END ===============")


main()

