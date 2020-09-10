# Write your code here
DNA = input()
RNA=''
flag='T'
for i in DNA:
    if i not in ['G','C','A','T']:
        print('Invalid Input') 
        flag='F'
        break
    else:
            if i=='G':
                RNA+='C'
            elif i=='C':
                RNA+='G'
            elif i=='T':
                RNA+='A'
            elif i=='A':
                RNA+='U'
if flag=='T':
    print(RNA)
