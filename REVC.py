DNAstring = 'AAAACCCGGT'

def reverse_complement(DNAstring):
    output = ''
    n=len(DNAstring)-1 #n is last element of DNAstring - start here and go backwards 
    while n>=0:
        i=DNAstring[n]
        if i == 'A':
           output += 'T'
        elif i == 'C': 
            output += 'G'
        elif i == 'G':
            output += 'C'
        elif i=='T':
            output += 'A'
        else:
            output+='ERROR'
        n-=1 #makes n one smaller to move loop along
    return output
print(reverse_complement(DNAstring))
      
