board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'

def make_board(string):
    brett = []
    liste = list(string)
    for i in range(int((len(string)**(1/2)))):
        rad = []
        for j in range(i * int(len(string)**(1/2)), (i+1) * int(len(string)**(1/2))):
            if liste[j] == ".":
                rad.append(None)
            else:
                rad.append(liste[j])
        brett.append(rad)
    return brett

def get_piece(brett, x, y):
    rad = brett[-y]
    brikke = rad[x-1]
    return brikke

def get_legal_moves(brett, x, y):
    mulige = []
    rad = brett[-y]
    print(rad)
    brikke = str(rad[x-1])
    print(brikke)
    if brikke == "P":
        venn = ["P", "K", "B", None]
        rad = brett[-y-1]
        if rad[x] not in venn:
            trekk = str(str(x+1) + "," + str(y+1))
            mulige.append(trekk)
        if rad[x-2] not in venn:
            trekk = str(str(x-1) + "," + str(y+1))
            mulige.append(trekk)
        if rad[x-1] == None:
            trekk = str(str(x) + "," + str(y+1))
            mulige.append(trekk)
            if y == 2:
                rad = brett[-y-2]
                if rad[x-1] == None:
                    trekk = str(str(x) + "," + str(y+2))
                    mulige.append(trekk)
    elif brikke == "p":
        venn = ["r", "k", "n", "p", None]
        rad = brett[1-y]
        if rad[x] not in venn:
            trekk = str(str(x+1) + "," + str(y-1))
            mulige.append(trekk)
        if rad[x-2] not in venn:
            trekk = str(str(x-1) + "," + str(y-1))
            mulige.append(trekk)
        if rad[x-1] == None:
            trekk = str(str(x) + "," + str(y-1))
            mulige.append(trekk)
            if y == 4:
                rad = brett[2-y]
                if rad[x-1] == None:
                    trekk = str(str(x) + "," + str(y-2))
                    mulige.append(trekk)
        
    return mulige
                
                
                

brett = make_board(board_string_1)
brikke = get_piece(brett, 2, 5)
mulige = get_legal_moves(brett, 2, 4)
print(brett)
print(brikke)
print(mulige)
        
