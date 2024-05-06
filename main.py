import argparse

def generate_wordlist(dictionaries, min_length=1, max_length=10):
    wordlist = []
    for dictionary_file in dictionaries:
        with open(dictionary_file, 'r') as file:
            for word in file:
                word = word.strip()
                if min_length <= len(word) <= max_length:
                    wordlist.append(word)
    return wordlist

def save_wordlist(wordlist, output_file):
    with open(output_file, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generate a password wordlist.')
    parser.add_argument('dictionaries', metavar='D', type=str, nargs='+', help='Path(s) to dictionary file(s)')
    parser.add_argument('--output', '-o', type=str, default='wordlist.txt', help='Output file name (default: wordlist.txt)')
    parser.add_argument('--min-length', '-min', type=int, default=6, help='Minimum length of passwords (default: 6)')
    parser.add_argument('--max-length', '-max', type=int, default=10, help='Maximum length of passwords (default: 10)')
    args = parser.parse_args()

    wordlist = generate_wordlist(args.dictionaries, args.min_length, args.max_length)
    save_wordlist(wordlist, args.output)
    print(f"Wordlist generated and saved to {args.output}")

if __name__ == "__main__":
    main()
