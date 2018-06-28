# <Xiao Shan shanx015>
# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.

import sys

def main():
#creating empty table
    originalkey="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    table=[]
    count=0
    line=''
#check key length
    if len(sys.argv[4]) < 3:
        print('The encryption key needs to be more than 3 characters.')
    else:
#construct and print vigenere table
        while count<len(sys.argv[4]):
            found = 0
            for i in range(0,len(originalkey)):
                if originalkey[i] == sys.argv[4][count] and found == 0:
                    line = originalkey[i:]+originalkey[0:i]
                    table += [line]
                    found = 1
            count+=1
#check operation
    #
    if sys.argv[1] == '-e':
        #check if file exist
        fileexist1=False
        try:
            infile = open(sys.argv[2],"r")
            fileexist1=True
        except:
            print("The plain text file does not exist in the directory, please double check if name was entered correctly.")
        #if file exist, encrypt the plain text file to the outfile
        #steps for encrption
        if fileexist1==True:
            infile = open(sys.argv[2],"r")
            outfile = open(sys.argv[3],'w')
            xs=infile.readlines()
            counter=0
            for j in range(0,len(xs)): #j line
                outline=''
                for k in xs[j]: # k word
                    if counter==len(sys.argv[4]):
                        counter=0
                    for p in range(0,len(originalkey)):
                        if originalkey[p]==k:
                            outletter=table[counter][p]
                            outline+=outletter
                    counter+=1
                outfile.write(outline)
            print('\n'+'encoded: '+ outline + '\n')
            print(table)
            print('\n')
            infile.close()
            outfile.close()
    elif sys.argv[1] == '-d':
        fileexist2=False
        try:
            infile = open(sys.argv[2],"r")
            fileexist2=True
        except:
            print("The encrypted file does not exist in the directory, please double check if name was entered correctly.")
        #if file exist, encrypt the plain text file to the outfile
        #steps for encrption
        if fileexist2==True:
            infile = open(sys.argv[2],"r")
            outfile = open(sys.argv[3],'w')
            ps=infile.readlines()
            counter=0
            for j in range(0,len(ps)): #j line
                outline=''
                for k in ps[j]: # k word
                    if counter==len(sys.argv[4]):
                        counter=0
                    for p in range(0,len(originalkey)):
                        if table[counter][p]==k:
                            outletter=originalkey[p]
                            outline+=outletter
                    counter+=1
                outfile.write(outline)
            print('\n'+'decoded: '+ outline + '\n')
            print(table)
            print('\n')
            infile.close()
            outfile.close()
    else:
        print('Please enter -e for encrypting or -d for decrypting.')

if __name__ == '__main__':
    main()
