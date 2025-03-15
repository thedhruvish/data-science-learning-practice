# Q13. Write a Python program to
# read a text file, count the frequency of each word, and write the 
# results to a new text file
input_file = 'input.txt' 
output_file = 'output.txt'

with open(input_file, 'r') as file:
    text = file.read()

text = text.lower()

words = text.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

with open(output_file, 'w') as output:
    for word, count in word_count.items():
        output.write(f'{word}: {count}\n')

