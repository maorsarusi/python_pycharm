def secret(word):
    ascii_inp = 0
    for i in range(1, 10):
        print(i)
        if i < len(word):
          ascii_inp += ord(word[i])
    return ascii_inp

def main():
    inp = input("Magic word: ")
    if len(inp) <= 3:
        print("")
        return

    ascii_sum = secret(inp)
    ascii_sub = ascii_sum - 846
    if ascii_sub == 20:
        print("Good work you are getting it!")
    else:
        print("")
    return



if __name__ == "__main__":
    main()