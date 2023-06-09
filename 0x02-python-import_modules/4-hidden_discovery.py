#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    fichier = dir(hidden_4)
    leng = len(fichier)
    for m in range(0, leng):
        if fichier[m][0:2] != "__":
            print(fichier[m])
