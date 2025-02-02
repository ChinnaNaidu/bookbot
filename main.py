def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    words = file_contents.split()
    #print(len(words))
    ans=count_occurence(file_contents)
    #print(ans)
    print_report(file_contents)


def count_occurence(book):
    #Declare a dictionary to store the word count
    book = book.lower()
    word_count = {}
    #Iterate through the book
    for x in book:
        #Check if the word is in the dictionary
        if x in word_count:
            #Increment the count of the word
            word_count[x] += 1
        else:
            #Add the word to the dictionary
            word_count[x] = 1
    return word_count
def print_report(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words in the book: {num_words}")
    alpha ="abcdefghijklmnopqrstuvwxyz"
    word_count = count_occurence(file_contents)
    for i in word_count:    
        if i in alpha:
            print(f"'{i}': {word_count[i]}")
    print("--- End of report --- and Thanks a lot for reading the book")



main()

