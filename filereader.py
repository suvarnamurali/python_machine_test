import re

def get_words(text):
    words = re.findall(r'\w+', text.lower())
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    repeated_words = [word for word, count in word_dict.items() if count > 1]
    return repeated_words

def main():
    file_path = "sample/file.txt"
    output_file_path = "test.txt"  

    with open(file_path, 'r') as file:
        content = file.read()

    repeated_words = get_words(content)
    if repeated_words:
        with open(output_file_path, 'w') as output_file:
            output_file.write("Repeated words list :  \n")
            output_file.write(','.join(repeated_words) + "\n")
        print("Repeated words written to", output_file_path)
    else:
        print("No repeated words found in the file .")

if __name__ == "__main__":
    main()



