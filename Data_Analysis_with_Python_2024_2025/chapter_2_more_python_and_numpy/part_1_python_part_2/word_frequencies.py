#!/usr/bin/env python3

def word_frequencies(filename):
    results = {}
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in results:
                    results[word] += 1
                else:
                    results[word] = 1
    return results

def main():
    pass

if __name__ == "__main__":
    main()

freq = word_frequencies("src/alice.txt")
print(len(freq))
