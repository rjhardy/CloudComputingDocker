import os
import re
from collections import Counter
import socket

def read_text_files():
    # Get a list of all text files in /home/data
    files = [f for f in os.listdir('/home/data') if f.endswith('.txt')]
    word_count = 0
    word_counts = {}
    top_words = {}
    for file in files:
        # Read the contents of each text file
        with open(f'/home/data/{file}', 'r') as f:
            content = f.read()
            # Split the contents into words
            content = ''.join(c if c.isalnum() or c.isspace() else ' ' if c == '\u2014' else '' for c in content)
            words = content.lower().split()
            # Count the number of words in each file
            word_counts[file] = len(words)
            word_count += len(words)
            word_counts2 = Counter(words)
            if(file == "IF.txt"):
                top_words[file] = word_counts2.most_common(3)
    return files, word_counts, word_count, top_words

def get_ip_address():
    # Get the IP address of the machine
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def write_to_file(files, word_counts, word_count, top_words, ip_address):
    # Write the results to a text file
    with open('/home/output/result.txt', 'w') as f:
        f.write('List of text files:\n')
        for file in files:
            f.write(f'- {file}\n')
        f.write('\n')
        f.write('Word count in each file:\n')
        for file, count in word_counts.items():
            f.write(f'- {file}: {count} words\n')
        f.write('\n')
        f.write(f'Top 3 words in IF.txt:\n')
        for file, words in top_words.items():
            f.write(f'- {file}:\n')
            for word, count in words:
                f.write(f' - {word}: {count} times\n')
        f.write('\n')
        f.write(f'Grand total: {word_count} words\n')
        f.write('\n')
        f.write(f'IP address: {ip_address}\n')

def print_file():
    # Read the results of the results.txt file
    with open('/home/output/result.txt', 'r') as f:
        content = f.read()
        print (content)

files, word_counts, word_count, top_words = read_text_files()
ip_address = get_ip_address()
write_to_file(files, word_counts, word_count, top_words, ip_address)
print_file()