#!/usr/bin/env python

def main():
    code=open(r"/home/peppocola/Scrivania/file").read()
    dayfivepartone(code)
    dayfiveparttwo(code)

def dayfivepartone(code):
    stack=[]
    stack.append(code[0])
    for i in range (1, len(code)):
        if code[i]==code[i].upper():
            if stack and code[i].lower()==stack[-1]:
                stack.pop()
            else:
                stack.append(code[i])
        elif stack and code[i].upper()==stack[-1]:
                stack.pop()
        else:
            stack.append(code[i])
    return(len(stack))

def dayfiveparttwo(code):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    dicty={}
    for i in alphabet:
        newcode=code.replace(i, "").replace(i.upper(), "")
        dicty[i]=dayfivepartone(newcode)
    print(minvalue(dicty))

def minvalue(dicty):
    miny=None
    for key in dicty.keys():
        if miny is None or dicty[key]<miny:
           miny=dicty[key]
    return miny

if __name__ == '__main__':
    main()
