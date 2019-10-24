#lily's code
DNAstring = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

def count_nucleotides(DNAstring):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for i in range(len(DNAstring)):
        if DNAstring[i] == 'A':
            countA += 1
        elif DNAstring[i] == 'C':
            countC += 1
        elif DNAstring[i] == 'G':
            countG +=1
        else:
            countT +=1
    return countA, countC, countG, countT

print(count_nucleotides(DNAstring))

#jack's code
def count_nucleotides(DNAstring):
    Counts=[0,0,0,0]
    Bases=['A','C','G','T']
    for i in DNAstring:
        n=0
        while n<len(Bases) and Bases[n]!=i:
            n+=1
        if n<len(Bases):
            Counts[n]+=1
        else:
            Position=0
            for j in Counts:
                Position+=j
            print ('Error! Position:'+str(Position))
    return Counts

print(count_nucleotides(DNAstring))

#terry's code

s = 'AGCTTTTCATTCTGACTGCAACGGGCAWATATGTCTCTGTGTGGATTAAAA AAAGAGTGTCTGATAGCAGC'

string_output = str(s.count('A'))+' '+str(s.count('C'))+' '+str(s.count('G'))+' '+str(s.count('T'))

print(string_output)
