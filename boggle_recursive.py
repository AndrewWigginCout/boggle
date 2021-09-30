from copy import deepcopy
def valid_recursive(y,x,s,b,depth):
    #print(y,x,s)
    #print(b[y][x])
    print(depth)
    if s=='' or b[y][x]==None:
        return False
    elif b[y][x]==s:
        return True
    elif b[y][x][0]==s[0]:
        m=len(b)
        n=len(b[0])
        #print("line10")
        b2=deepcopy(b)
        b2[y][x]=None
        bool=False
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if j<0: continue
                if j>=m: continue
                if i<0: continue
                if i>=n: continue
                if (j,i)==(y,x): continue
                if valid_recursive(j,i,s[1:],b2,depth+1):
                    #print(y,x,s[1:])
                    return True
    return False
def find_word(b,s):
    m=len(b)
    n=len(b[0])
    for y in range(m):
        for x in range(n):
            if b[y][x]==s[0] and valid_recursive(y,x,s,b,0): return True
    return False
def print_board(b):
    for row in b:
        for cell in row:
            print(cell,end="")
        print('')

if __name__ == "__main__":
    b=[ ["I","L","A","W"],
     ["B","N","G","E"],
    ["I","U","A","O"],
    ["A","S","R","L"] ]
    print_board(b)
    print(find_word("BINGO",b))