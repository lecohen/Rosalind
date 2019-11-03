#want the distinct protein strings that can be translated from s (order doesn't matter)
#example: s = AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
#example output = MLLGSFRLIPKETLIQVAGSSPCNLS, M, MGMTPRLGLESLLE, MTPRLGLESLLE

DNA_codon_dictionary={'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S','TAT':'Y','TAC':'Y','TAA':'Stop','TAG':'Stop','TGT':'C','TGC':'C','TGA':'Stop','TGG':'W','CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
DNA_string='AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
Start_codon='ATG'
#want 4 functions: 1) reference dictionary, 2) find index of start codons, 3) get reverse complement 4) transcribe from start codons 

#1 reference dictionary
def reference_codon_dictionary(DNA_string, DNA_codon_dictionary):
    Output = ''
    n=0
    while n<len(DNA_string):
        codon = DNA_codon_dictionary[DNA_string[n:n+3]]
        if codon == 'Stop':
            return Output
        Output+=codon
        n+=3
    return Output

#2 find index of start codons
def find_start_codons(DNA_string, Start_codon):
    Output = []
    start_position=0
    while start_position <= len(DNA_string)-3:
        codon = DNA_string[start_position:start_position+3]
        if codon ==Start_codon:
            Output.append(start_position)
        start_position +=1
    return Output

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

def distinct_strings(DNA_string, Start_codon, DNA_codon_dictionary):
    start_positions = find_start_codons(DNA_string, Start_codon)
    Output = []
    for start_position in start_positions:
        Codons=reference_codon_dictionary(DNA_string[start_position:], DNA_codon_dictionary)
        if Codons not in Output:
            Output.append(Codons)

    RC=reverse_complement(DNA_string)
    start_positions = find_start_codons(RC, Start_codon)
    for start_position in start_positions:
        Codons=reference_codon_dictionary(RC[start_position:], DNA_codon_dictionary)
        if Codons not in Output:
            Output.append(Codons)
            
    return Output


print(distinct_strings(DNA_string, Start_codon, DNA_codon_dictionary))


