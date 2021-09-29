#https://www.codewars.com/kata/57680d0128ed87c94f000bfd

def valid(s,b):#string, board
    m=len(b)
    n=len(b[0])
    stack=[]
    for x in range(n):
        for y in range(m):
            if b[y][x]==s[0]:
                stack.append((y,x))

    while stack:
    y,x,cells=stack[-1]
        for j in range(y-1,y+2):
            for i in range(x-1,x+2):
                if j<0: continue
                if j>=m: continue
                if i<0: continue
                if i>=n: continue
                if (j,i) in stack: continue
                if b[j][i]==s[len(stack)]:
                    stack.append((j,i,))
        #failed pop stack
        stack.pop()
    #failed return False
    return False



#pseudocode
#at every cell if the cell is the last letter of the word return True
#              if the cell is not then continue to next cell
#              if there are no more cells then pop this, then pop the path just checked
