# Author: PCL 2/3/23


def ordered_count(inp):
    #empty list for final return of the function and its tuples
    sums = []
    #dictionary of all possible letters, numbers, and spaces for checking letters of the string against
    dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0, " ": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    #splitting the inputted string into a list of its individual characters
    characters = [*inp]
    #for loop that checks for every letter, number, and space and adds +1 to the dictionary of that character if it is present
    for letters in characters:
        if letters == "a":
            dict["a"] += 1
        if letters == "b":
            dict["b"] += 1
        if letters == "c":
            dict["c"] += 1
        if letters == "d":
            dict["d"] += 1
        if letters == "e":
            dict["e"] += 1
        if letters == "f":
            dict["f"] += 1
        if letters == "g":
            dict["g"] += 1
        if letters == "h":
            dict["h"] += 1
        if letters == "i":
            dict["i"] += 1
        if letters == "j":
            dict["j"] += 1
        if letters == "k":
            dict["k"] += 1
        if letters == "l":
            dict["l"] += 1
        if letters == "m":
            dict["m"] += 1
        if letters == "n":
            dict["n"] += 1
        if letters == "o":
            dict["o"] += 1
        if letters == "p":
            dict["p"] += 1
        if letters == "q":
            dict["q"] += 1
        if letters == "r":
            dict["r"] += 1
        if letters == "s":
            dict["s"] += 1
        if letters == "t":
            dict["t"] += 1
        if letters == "u":
            dict["u"] += 1
        if letters == "v":
            dict["v"] += 1
        if letters == "w":
            dict["w"] += 1
        if letters == "x":
            dict["x"] += 1
        if letters == "y":
            dict["y"] += 1
        if letters == "z":
            dict["z"] += 1
        if letters == "A":
            dict["A"] += 1
        if letters == "B":
            dict["B"] += 1
        if letters == "C":
            dict["C"] += 1
        if letters == "D":
            dict["D"] += 1
        if letters == "E":
            dict["E"] += 1
        if letters == "F":
            dict["F"] += 1
        if letters == "G":
            dict["G"] += 1
        if letters == "H":
            dict["H"] += 1
        if letters == "I":
            dict["I"] += 1
        if letters == "J":
            dict["J"] += 1
        if letters == "K":
            dict["K"] += 1
        if letters == "L":
            dict["L"] += 1
        if letters == "M":
            dict["M"] += 1
        if letters == "N":
            dict["N"] += 1
        if letters == "O":
            dict["O"] += 1
        if letters == "P":
            dict["P"] += 1
        if letters == "Q":
            dict["Q"] += 1
        if letters == "R":
            dict["R"] += 1
        if letters == "S":
            dict["S"] += 1
        if letters == "T":
            dict["T"] += 1
        if letters == "U":
            dict["T"] += 1
        if letters == "V":
            dict["V"] += 1
        if letters == "W":
            dict["W"] += 1
        if letters == "X":
            dict["X"] += 1
        if letters == "Y":
            dict["Y"] += 1
        if letters == "Z":
            dict["Z"] += 1
        if letters == " ":
            dict[" "] += 1
        if letters == "0":
            dict["0"] += 1
        if letters == "1":
            dict["1"] += 1
        if letters == "2":
            dict["2"] += 1
        if letters == "3":
            dict["3"] += 1
        if letters == "4":
            dict["4"] += 1
        if letters == "5":
            dict["5"] += 1
        if letters == "6":
            dict["6"] += 1
        if letters == "7":
            dict["7"] += 1
        if letters == "8":
            dict["8"] += 1
        if letters == "9":
            dict["9"] += 1
    #for every dictionary term that now has a count greater than zero it is turned into a tuple and added to a list ALPHABETICALLY
    for k,v in dict.items():
        if (v > 0):
            tup = (k, v)
            sums.append(tup)
    return(sums)

print(ordered_count("Code Wars"))