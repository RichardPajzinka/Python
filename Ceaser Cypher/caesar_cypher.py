#cakame na kluc od uzivatela a dalsie data
rot = int(input("zadaj kluc: "))
action = input("ches [s]ifrovat alebo [d]esifrovat: ")
data = input("zadaj text: ")

#budeme to riesit cez ord kedy si znak dame do cisla a to cislo budeme posuvat
if action == "s" or action == "sifrovat":
    #vysledy text do ktoreho budem nahadzovat znaky
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += rot #rotujem do prava taže sifrujem
            #tu mu poviem ze do 94 su znaky ktore viem podporvat a ked sa toto prekroci tak po deleni sa to vrati naspat do toho rangu
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("moja sifra je: {}".format(text))
elif action == "d" or action == "desifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= rot #idem do lava taze desifrujem
            # tu mu poviem ze do 94 su znaky ktore viem podporvat a ked sa toto prekroci tak po deleni sa to vrati naspat do toho rangu
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("odsifrovany text: {}".format(text))
else:
    print("zle si zadal znak")