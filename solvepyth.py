#!/usr/bin/python3
import random
import string
import os

def main():
    X='_'
    Ymul='__'
    print('Welcome to MIND READER')
    print('-------------------------------------------------------------')
    print('Enter your choice')
    print('1:play')
    print('2:Instructions')
    print('3:About')
    print('--------------------------------------------------------------')
    print('Enter choice')
    choice=input()
    start=1
    
    if choice=='1':
        z=random.choice(string.ascii_lowercase)
        os.system('cls' if os.name=='nt' else 'clear')
        k=random.choice(string.ascii_lowercase)
        if choice=='1':
            print('Enter limit to create random number')
            end=int(input())
            for i in range(start,end):
                print(str(i)+":")
        
        print('1:Ready')
        choice=input()
        if choice=='1':
            for i in range(start,end):
                if(i%9==0):
                    print(str(i)+":"+str(z)+"\t")
                else:
                    k=random.choice(string.ascii_lowercase)
                    print(str(i)+":"+str(k)+"\t")
        os.system('cls' if os.name=='nt' else 'clear')
        print('1:show')
        choice=input()
        if choice=='1':
            print('Guessed letter::'+ z)
     
    elif choice=='2':
        print('In the page,Choose any two digit number between 1 to 100, add together both the digits and then subtract total from your original number.When you have the final number click on Ready button and look it up on the chart and find the relevant alphabet.concentrate on the symbol and when you have it clearly in your mind the click on show option and it will show you the alphabet you are thinking off.ex: if you choose 30:3+0=3,30 minus 3 gives answer..')
    elif choice=='3':
        print('Developed by Sharath.M')

if __name__=="__main__":main()

