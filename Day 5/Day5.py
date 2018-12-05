#!/usr/bin/env python

def main():
    code=open(r"/home/peppocola/Scrivania/file").read().rstrip()
    dayfivepartone(code)
    dayfiveparttwo(code)

def dayfivepartone(code):
    stack=[]
    for i in code:
        if stack:                                                           #if stack is not empty
            if i==i.upper():                                                #if i is uppercase
                if i.lower()==stack[-1]:                                    #if top of stack is i lowercase
                    stack.pop()                                             #remove
                else:                                                       #i is uppercase but the top of the stack isnt i lowercase
                    stack.append(i)                                         
            elif i.upper()==stack[-1]:                                      #it's lowecase, so if i uppercase is the top of the stack
                stack.pop()                                                 #remove
            else:                                                           #lowercase but the top of the stack isnt i uppercase
                stack.append(i)                                             #push
        else:                                                               #if stack is empty
            stack.append(i)                                                 #push
    return(len(stack))

def dayfiveparttwo(code):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    length=[]
    for i in alphabet:                                                      #for every word in the alphabet
        newcode=code.replace(i, "").replace(i.upper(), "")                  #remove that letter lowercase and uppercase
        length.append(dayfivepartone(newcode))                              #put the length of the string after reactions in a list
    print(min(length))

if __name__ == '__main__':
    main()
