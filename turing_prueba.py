def calPoints(ops)->int:
    result = 0
    scores=[]
    for i in ops:
        try:
            scores.append(int(i))
        except:
            if i=='C':
                if len(scores)==0:
                    scores=[]
                else:
                    scores.pop()
            elif i=='D':
                scores.append(2*int(scores[-1]))
            elif i=='+':
                operacion=int(scores[-1])+int(scores[-2])
                scores.append(operacion)
            else:
                scores=scores
    
    result = sum(scores)
    return result

if __name__ == '__main__':
    line="5 -2 4 C D 9 + +"
    ops = line.strip().split()
    print(ops)
    #print(calPoints(ops))