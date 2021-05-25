if __name__ == '__main__':
    lst=[]
    stud=[]
    marks=[]
    
    for number in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score]) #nested list
        stud.append(name)
        marks.append(score)
    marks=list(set(marks))
    marks.sort()
    marks=marks[1]
    o=[]
    for i in lst:
        if i[1]==marks:
            o.append(i[0])
    o.sort()
    print(*o,sep='\n')
        
    
        
