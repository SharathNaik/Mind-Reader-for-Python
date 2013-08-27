#!/usr/bin/env python

def main():
    X='_'
    Ymul='__'
    print('_______Welcome to MIND READER_____')
    print('-------------------------------------------------------------')
    print('Enter your choice')
    print('1:play')
    print('2:Instructions')
    print('3:About')
    print('----------------------------------------')
    

    choice=input()
    print(choice)
    if (choice=='1'):
        import os
        os.system('cls' if os.name=='nt' else 'clear')
        
        A = [[1,X,2,X,3,X,4,X,5,X,6,X,7,X,8,X,9,Ymul,10,X],
             [11,X,12,X,13,X,14,X,15,X,16,X,17,X,18,Ymul,19,X,20,X],
			 [21,X,22,X,23,X,24,X,25,X,26,X,27,Ymul,28,X,29,X,30,X],
             ]

        print('\n'.join([''.join(['{:1}'.format(item) for item in row])
                         for row in A]))
        
        print('enter 1 to generate a random number')
        comp=input()
        import os
        os.system('cls' if os.name=='nt' else 'clear')
        if(comp=='1'):
            
            import random
            import string
            z=random.choice(string.ascii_lowercase)
        
            for row in A:
                for ix,val in enumerate(row):
                    if val == X:
                        y=random.choice(string.ascii_lowercase)
                        row[ix]=y
                    elif val==Ymul:
                        row[ix]=z
                    
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in A]))
        
        
    elif (choice=='2'):
        print('check the app')
    elif (choice=='3'):
        print('blah blah')
        
    print('-----------------------------------')
    print('1:show the letter')
    final=input()
    if(final=='1'):
        import os
        os.system('cls' if os.name=='nt' else 'clear')
        print('The Guessed letter is ::',z)
    else:
        print('End')
	




if __name__=="__main__":main()
