def reverse_words(str):
    words = str.split()
    words.reverse()

    return " ".join(words)

def __main__():

    str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"

    print("[original str1]\n%s"%str1)
    print("[reversed str1]\n%s"%reverse_words(str1))

    print("[original str2]\n%s"%str2)
    print("[reversed str2]\n%s"%reverse_words(str2))

__main__()
