#Counts the number of words in a given text

def word_count():
  try:
    with open("books/frankenstein.txt","r") as f:
      file_contents = f.read()
      word_count = len(file_contents.split())
      return word_count
  except FileNotFoundError:
    print("File not found...")
  except Exception as e:
    print(f"An error occurred: {e}")


#Counts the number of each character

def char_count():
  try:
    char_count = {}
    with open("books/frankenstein.txt","r") as f:
      file_contents = f.read().lower()

      for char in file_contents:
        if char.isalpha():
          if char in char_count:
            char_count[char] += 1
          else:
            char_count[char] = 1

    return char_count
  except FileNotFoundError:
    print("File not found...")
  except Exception as e:
    print(f"An error occurred: {e}")


def main():
  print("--- Begin report of books/frankenstein.txt ---")
  total_words = word_count()
  if total_words is not None:
    print(f"{word_count()} words found in the document")
    print("")

  char_count_dict = char_count()
  if char_count_dict:
    for char in sorted(char_count_dict):
      print(f"The '{char}' character was found {char_count_dict[char]} times")

  print("--- End report ---")


main()