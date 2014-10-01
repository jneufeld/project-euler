names_file = open('p022_names.txt')

raw_names = names_file.read()
raw_names = raw_names.replace('"', '')
raw_names = raw_names.lower()

unsorted_names = raw_names.split(',')
sorted_names = sorted(unsorted_names)

total_score = 0
for i, name in enumerate(sorted_names):
    position = i + 1
    word_score = 0

    for character in name:
        word_score += ord(character) - 96

    total_score += word_score * position

print total_score
