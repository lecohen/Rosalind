#Jack did this part for me 
Look_Up=[]

To_Parse=['UUU F      CUU L      AUU I      GUU V']
To_Parse.append('UUC F      CUC L      AUC I      GUC V')
To_Parse.append('UUA L      CUA L      AUA I      GUA V')
To_Parse.append('UUG L      CUG L      AUG M      GUG V')
To_Parse.append('UCU S      CCU P      ACU T      GCU A')
To_Parse.append('UCC S      CCC P      ACC T      GCC A')
To_Parse.append('UCA S      CCA P      ACA T      GCA A')
To_Parse.append('UCG S      CCG P      ACG T      GCG A')
To_Parse.append('UAU Y      CAU H      AAU N      GAU D')
To_Parse.append('UAC Y      CAC H      AAC N      GAC D')
To_Parse.append('UAA Stop   CAA Q      AAA K      GAA E')
To_Parse.append('UAG Stop   CAG Q      AAG K      GAG E')
To_Parse.append('UGU C      CGU R      AGU S      GGU G')
To_Parse.append('UGC C      CGC R      AGC S      GGC G')
To_Parse.append('UGA Stop   CGA R      AGA R      GGA G')
To_Parse.append('UGG W      CGG R      AGG R      GGG G' )

for i in To_Parse:
    Split=[]
    n=0
    while n<len(i):
        while i[n]==' ':
            n+=1
        m=n
        while m<len(i) and i[m]!=' ':
            m+=1
        Split.append(i[n:m])
        n=m+1
    for i in range(int(len(Split)/2)):
        Look_Up.append([Split[i*2],Split[i*2+1]])
#Up to here

rna_string = 'AUGCAAUGCCUCGAGACAAAGCCGUGGGAAACCACUCGGCGCCUCAGCAGUGUCAGAUGCUCACGCUCUACGGGCAUUACGCAAGCUGGUAUUGCGUGGGCGCGAACCCUUCCGAGUCCUAGUACCCAUUCCGGUCCAGUAAAGGAAUCUAUGAGCGCCGAGACUAGAGGGCGACAGAUUAUUCAUUGGAGGUCUUACUCUGAACAGGCGCGUCUGCAUAGAAAUUGUAUCGAAUUGAAACGUAGCCAUAUAGUGUUUAAUCCGUGCGGCAGUUCUUGCGGGGACGAGGGACUAAAAUGUUACUGCACUAUGCAGAGCCGAAUGGCAGUCUAUCAGGUUCUCAUUCUAUCGCUGCUCCUGACCCGUAACGAAUGUCAAGCCGAAGCACGAGCUAUAGAUCCCUUCACUGCGCGUAAGACGAGUAGCCUAGUGCGUCCAUGGACCCAACUUCCCUACCUGCACUAUCAUUAUAAUCUUUCGAUACAUAACUCACUCGUAGGUGGCGUCGCAGAUUCAGUCUGCGUGCUGCCGUCUUGCUGGGACGAGGCUCUAUGCUUGCCGUCAGUCAGGGUACAGGAGAUUUUUAUAGUUUACAGAAUUGGCUUGCGUUAUUAUCGGGCCCGGAUUCCGAGCCCCUACAGGAUAUAUGGACUCCUCACGAAGUGUUACUUAAUAGGCCAUCACCUCCUGGUCCAGGCCUUUUUCGAAAUAUAUAGGUCUGCCGGUCAUAGUUACUUUGCGGGUACCCAUCUCGCAAUAUUCUUGCUCGGGAGGCCUAUGAUAGAACCCGCAAGAGUGAACAAACGUGCAAAGGGCCAUCGGGGUGUCUCCGCUCUGUCGCGGGCAGCCGAGUCCGUUAAAUUUACCUCGCCUCAAAAUCUUCCGAGCCGAAAAAUGUAUCGUCAAUCGAGGCAAGGCUAUCCGCAAAAUCAACUAACAAACGACGGGCGUUUGGUGCGGGAAGGUGUGUCAUUACCCCAUCGAAUCGCCCGUCAAAAGGGCUAUAAGGGCUUCCACUGUGGGCCGACGUGGACACUAGGCGAGCUGUGUGCGCUUUCUCGUGGGGAGGGGUACGUCGUGAAUCUGCUUAGUUACGACCUGAUGGGACACGACAUUAGCAGAGCCUCUGUAAGCUCGACGACCAUCGUAAGGAGUACGGACGUAGCGCUCCUGUACAUAGAAGACAUAUCCCUCUGUUGCCGCGUGCAGGACUACGGCGCUGCUCUCCAAACGAAGAGAGUGGGUAAGUCGCAAUCAGAAAUAGACGUAAUUAUGACAAACAGUCUACCAUACCCCUAUCAUUUCUACUUCCGUAACGUCUCGUCCUCUCUGAUAGAUUCGUUUAUGGGACAUGUAGAUUUCCACCAACUAGCCGGGUAUAAUACGAGUGUCGGCCUAGACCUGCUGGACGCAUUGGACAGGCGACUUAUAAACCGACGUACCUUAAAUGUAUCUAUUAGCAAUAUCAGAACGUGGUCUUCGAAGGUGAAAGCAGUAAGCUUCAGCGAAAACGUAAGGGUCCGUGUGCCGUCCUCUGGUCCUAUGACGCCUGGGUUUUUGAUCGUUUUGAGGUUUAAUGACAAGGGUCAAUUUGCACUUAGUAGAGGCGCCUACUACAUUCAGAAGAGGCUUAGAACUCGUUUGAUAGCCUCGAUAGCGAGGAGCCACUCAGGUUCACGGGGACAUGACUAUCACGGUGAAAAAUACCGUGACGAGGAUGUGUGCGGAUUUCCCGGAGCGUCUCCUCGAAGACCCCGGACGCUUUGUUUUAGUUUACAUGGUUGUGAGAUCCCCGAGGGUGGUAAGUCGCUUGCUUGUCUAUUGCCUUGUGCGGGGCCUGGACUUCGGUCGCGCGCUUCCCGUCCUAAUCGGGACUGUACUAGAGCAGAUGGAACUAUAACUCCUUCUGUGCUACUUUUCAGAUGUCCCUCUCGUGCGCACACACUUUAUCAACGUUCAGUUUCAUUAUCCGCCUCACUCAUACGUGAGACUUUGGCCGUCUGUAUGGACCAUAUGUGCCCGCAUUCGUAUGUAACAUUCCAUCGGUUGAGCCUAGGCUUGUUCGGUCUUCGUCCUGAAUGGUGUCCGGGUUAUUAUGUACAUAGUUCGGCUCCGUGCCUUGUCAUCUUCGAGAACUCGAUUUCCCACACGUCUAAGGCCAAUCGCUUCCCUCUCGCAGCGAUCCCCUUGGCCAGCCCUGCGUCCCGAGCAUGUAAACUUUGGGAUCCGACGAACAAGAUCGAUUGGCGUAACCCGGCCCAAAACCUCUCCAGCCUUGAGCGACUCAUAACAUGGAGUCCAGGACACUCUCUCUUGGUAGCCCGCCACUUAACUUUUUAUGCGCGAAUUCGAGGCCUGCGACUCAUGCUGUGUUUUUCUUCGCUACGCACAUACAAAGCUAUGGCUAUGUCCAUAUUGCUUUGCGCGUGUUGUUCGAGGGCCCAGGACACAGUUAUACAAUUCCACGUCCCAAAGUCCCUCGGUACCAAUAGACCUGUACGGACAUUUCACCCAUUAGGCCUUUAUCCAAUCGCCAGUAACCCCCUAUGCGCGGCCGUACCACUGGAUACGGCUCUCUCUGGGGUUGCUUGGCUUCGUUUGAGAUACGAAGGAAACUUGCCUUGCUAUCUAGACCGCAGGAAUUUUUUAAGUAUCAGUAGACCGAGCUCGACUACCGAAUGGCAAGUAGAGGGCCCUUCAGCAGCAAGCUACGUCGUGCCGGGUAGUAACAUGGGCAUUCAGCCUCGCUCGGAUGAUGUGGUAUAUCUUCGACCAUUGCGACGUUGCUCUAUGCACCAGGGCCUGCUUGCGUCACAGUACCGAUUGCUGCCUAGGUCAUACUAUUGGCGUGUGGUACUGGUACAGCGUCGAGUUAAUGGAUGUAUUACGUGUACCCUGAGGCGCUGGCAUGGUAUGAGUGUGCGAUCAGAAAAGGUUCUCAUAUGUAUCCGGCGGGCAGGAAUGCGUCCUGACUGCCCACCGGUCAGCGCUCCCAGUGCCGGAAGUCCAGGCGCGCAGACGAUACCGUACUUCAUGAACCUGCGUUUUAAUGACGUGCAGAUCCGCAAAUCCACCACUGUUCGCGCAGUUAGGGUUGAUAAUAUCUAUAUUGGCUCUGGGACUAACUUGUUCCGGGUAGAAACCGCAUGGCAAUUAUGUGGAUUAAAGGGCCGAGUAGAAGUGAUUCCUGUCGCGACGUUGAGCGGCCGUUCAUUCAUCUUAUUCGUCACGUUCUCUGUUAUUAGUGAGAAUCAAAUGGGCAAAGGCUGGGUCGAGCACUUGAAAAAAAUUAAUCCCUUAAAACUGACCCGAGAUCUGUGUCCAUCGCAACCCUACUUUCGUGUCGAUUGGCGAAACUCUGAGACCUUCACGCGGAACCGUUUGGCAAGUCAUCGCGAAAAUUCCAUCUCGCUUGGGGCCUUUCAGGUAAGGGAUGACGAAGUGUCUUCGACAAAACCGAGCUCAAAUGAAACAAGAUACAGCGCGGUAGCGAGAUCAUUCCGAUCAUCAAGAUUUCAAAGAGGUAUACGACUAUCUCUACGUCAGUAUGGCCGAAUCAUAUGUGAAGGGUUGAGAUACAACAAAUGGUUACGUUGCGCCAUGGCGUUGGAGAAUAUUGGUUUGCUCCUUAGCAUAAUAAUUUCGUUACUGCAACAAAAGGGCCGACUCUCCUGUUACGUAACAAACAUAUUCACCACCCCCCCACCCGCGUAUGUUCCCUGGAUCCGACUAGCAUUUCUCACUCAUGUCUCGUUAACUGGGGAUUGGUGCAGAGGUGAAUACAUCUACACUGUCGGUAUUCUAGGGGUGCGCUCGAGAACCCAUUAUAGAACCACGUGCUUAGACUCGUUUUUACCGAGUACUCUUCGGGCAGUUGAUGGGAUCCGGGAGUUACGCCGGGGGCUUGCGGCUUCAAAAGUUACAGGUCGCGAGUGCAGCACAUUAUUUAUAACCCAGCGACAUCAAACUACCAUCGAUCAAGACACUGACCAAAGUCAGCAACCUAUCGGGGGAGUAGAUCAUCACAAAGAAGAGUGUAUGCAGUUAGUACUUAAGCUGAAUUGGAGUGUGGCCCGUUUAUGGUACAUUGCCGUUCGACGUUUAUACCCGUGUAAUUCCAAUCCGUGUCAUUCAUUCUCCACGAGGUGUGAAGAGAAUCCCAUGAAUUCCUUAUCCCAGCGUCUAGUAGACCCGCGUCCCAAUGGAUCACCGGGAAUUAUCCUCGAACUUAACAGGGACACAUGCUUGGGACCACAAGAAUAUAUGGGCAGUACCGCCCAUGUUCACACCUAUGGUUUGUUAUUAGACGAACACGGCUUUGAGGUGUCUCUUGGGCUAACAUCAUGUAACCCCCUGUUAAAUUACGGAGAGGCAAUUGGCUGGGAUCAUCUUGACACUAUCGCGCCAACCGUGAAACAAGCUCUACUCGGCGCUUUCGAUGGGCUUUCGAGCAGUCACCUCCGGCCACGGGCUUUGGCGAUUAUAGCAUCGUCAUUCACUAAGGUGAUUUGCCUGAACGAUGUGUGGUCGUGGAAACUCAAUGUGAUGUUACACCGAUUUCCACUAAGUCGGGCGUCGCUACAAGACCAGACACGAGGUUCCGUGCGCAAAGUGAACGGAAGGUAUCAGACAGGCCAAUUCCAUACGUAUCCAAAAAGACUUAGAGGCGAUGCGAUAGCGCUCACUAGUAAUUGUGUUCCGGGCCGCUGGCUAGCGGCCCACAAUAGAGUCCAUGCGACAAAGCUAGCGAGGCGUCGAUGCCAACAACCUCUCUCUGUAAGUGUAUUAACUACAAUCAUGACCUCUCUACACUUUACGGCGGUAACAUGUGUCUUCGGCAGAGACGAAGUACCUCCGCUAGGGCGUCGACACUCUGGCAUUUAUGACACGUCAGGGUUCGGCCUCUUCGGGGCGCAAGGUCAGAGGUCUGAGGUAGUAACGUGCUCAAAAAUUCUUCUAUUUGCGGUGAGAGUCAGCUACGGCCAAUCUGCCAUGAAAGAGCGCCGCUGGAUAUUAAUGCGGUCAAAUUGGAGCAAAAUCUUACUGCAGUUCCCUUGCCUUUAUAGAAACUGGGCUUCCACCGAUCGAGUCCAGGUUAGAAUCGGGUGUACUGCCUCCACUACCCCGGGCGGCACUGACGUGUAUGCAUCGUGUCCAUUGGGAUCGGGAUUGUUGAGAGUGGCAAGGCCUCCCAGCUCCCUGUCAGUGAGCUGUAAACAUGUCUCCUGUCGGCACGCGGCAAACUACUGUAUCGAUCAGACCCAAAUCUUGGCACGGAUGGAUUUCAAGGACAGUCGACACGGGACUGUUACAGGUUUUCACAGUAUAAGGCUGUGGCAGGCGCAAUCGUCCCGGUUUUGGAAAUUUCCGUUCACCAUCUUAUGUUUAUUAUAUGCCGAUAAACGACCUCAAGCGAACGGAUGGGGCACGCCGCACAAGAGAUUUUUUAAAUCAUCUCAUAGGGCGGGCCGGUUCGGCACGUUUGCUGAGUCCGAAUUAAACAGGAGGUUCGCAAGCCAAGUUUGCAUAAUAAUAUCCAACAUUUCCCCACGACAGAGCACCAUGCGUUGGGGAAUGACAACGAAUUUCUCUGAGUCGGACCCAUCUAGAAUUAGUCAAUUGUGGAUCUUUAAUUGGGUUAGACUGAAGGAAUAUCAUCUCCUGCUUACGUUUCCCAAGGGAACUCUGUUAAUGCUGGAGCUUAUGCAACGUGAUUCAUGGAACACAUAUUCGUUCACGCACGUAACAAUAUAUUACCGCAUGCUUUUAACUUCGAGAUUAGUAGAAAUUAUCCAAGUGCUUAGUUACGCUUGGGCGCCAUUUCUUCGUGUUGCUAUCGCAGCAGGACUAGUAUCUCCUGUGGGAUUGUCCGCAUCCUGCAGUCUACAUGGUAGCGAGGGCGGUCAACACCCAAGUCACAAGCCUAAUCUGCACCUCUGCCCGCCAUGGUACUCUUAUCUCCCACAUCAGGACUACGCAGUCAAAGUCGCUCUAAGAAUAUUGGGAAUGUCACGUGAUAUUGUAAUGACCUGGGUCUCUGGAAUGCGACUAACAUCUGAAGAGCCUCCGGUGCUCGUGCUAAGCGGAGCGAGCAAUAGAGGACUGCCUGUAUCCUCACCUGGCCGCAUUUCCCAGAAUCCCUUGCGCGAAAGUCUAAGAUAUUCCCCGGAAGCACGCAAAACACUGUGCGCCCCCCUGUAUGAGAUCCGCAGCCGUCUCCGCUGCCACAUGCGAGCACCUUCGCCAUAUUUUAAUGACCGGGGUUUAGAUGCCCAGACAAAGCCGGUAACGCGUCUGUCUGGGCUUCCAAUAUGUGGCAGUGGAAACAUCUUUGUAGGCGUCGCACAAUUAACACCACGUCGUCUUGGCGACAAUAGCGGAUCUCGGGCCGGUACAAAGCAAAUGAGUGCGAGUGGGUCAUACCGCCGUGCGGUCGGUUGUAAUAAGUGUCUGUUCCAACUUAGUGUAGUUAAGAUGCCCACAGAAUGUGUCAUAUCUUUUAACGCGGCUCGUGUGAGGAACUGGGGUCAGCCCCAAGCACUGAUGCAUUUGGCGGGCAUUCAAAGACCCGGCAAAACGGGACUUGAUCUACUUAAUGAGAUACGGUGUAUGCUUUGGAGAUUUUCCAUGGCAGGAGUGCAAUCAUCAGGCGCAAAAUCGCAUUUUAGAUUAUCCAAUUGGCAACUGCGCAUUACACGGCAGUUCCUUCCAUAUCCGGGGGGUGUCCGGGCAGCAGUGUAUUCAAAGCCUGUAUACGAGCCAUCCAUGGCUCCCUGGUGCCAAGGACAUCCCAGUGGACUCUCCAUCAUCGUGGUACUCGGAGAGGCAGUCGCGACCCGGGCGUUACCCAGCUCCCUUUCAUCGCUGUUUCUUUGGUCACUAUGGCGACCGGGCAACUAUAUUGCUAUGGGUAAACGUGCGGGUGGCCCGCCUGCGUACCGUUGUUCUGGGCGUUGGCUCCUAGGCCGGCGUGACGAUUUAGCAUUGUGGGUUUUCGAGCGUUGGGCUAAAUCAUGUCCCAGACGCAAGACUUACUCAUAUGUAGAGGGAUCGCGCGGCGACCUGUUGCGGACCUCGUGCGCAGCCGACCUCGGCGGGGAAUACGGGGGAUCCAACCUCUUGAUGGUGCUUCGGUCUCAGGACCUCGUUAAACCUCAUAUCAAGGCCAGAGUGAAGUUAUGCCAUCCCCAACGGUGCACUAGUGCGCAGUCGAGUGCAUGGAGACAACAGACAGUGCCCAACAAGACGGUUAGUCCGAAUUCCCUUUGUAUAACCAUACAGAGAUUCUCCGCUCCUUACACGGCCUGCCCUCAAGCAUUAAUAAUGGCAUCAACAAAGUCUGGAUCAGCUAUUGAUGUACGAAGGCAUAGCUCGGUAACCAGUAGAAUCCGCGCUACUGGUCGAGUAAUAAAGACAAAAAUCGGCAGUGCUGUGCCCAUUCCCGUAAUUAGCACUCUGCAUCGACCGGCGCCAAACACGAUCCAUUCACCAUUUCAUCAUCACGCGCCCGCCGACCGCGUUCGAGCUAUGUUUCUUCCCCCUGCGUUUCGCAGUCCAUGUAGUGAGGGCGUAAUCAUGAUUGUAUUUACCAGAUGCCUCAAUGCUAUGUUCCGCCUUAGUUGCAAACGUCGCCAUUCCCUGCAUAGUAACGGCCUGCACAAACGCGGAACACUCCCAUUGGUAUCACUGAACAAAUGCGGCGCUUGGAUUUUCCCCCUGGUCAACUCCUGCACUAACGCCGAAUAUUGCGCGGUUCACUGUCGCAUGUUUGGCAAAUCGCAAGGCUCUCGUGUAACUGGCCUGACUGGGUCCCCGCAAGUAAUCCUUAGAAACUAUCGAGGCAAUUACUUGAAAUUAGGGUGGACAAAGGUUUUGCAUCAGGUUGUCGGGACCCAAGGAGCAAUUCUCAGUCGACUACAUCUAGUACGCCGACAGAACAUGUCCGAAUCAUAUUUGUUUGGGUGUAAAUGUGCGGGGACGCGAUCAGCCCACUGGUGUUACGCGGAAAUGGUUUUUUUACCAUUGUGGACACGUAGGCCUUAUCGGCAGAAGCUACUACUCUCUUCAGGCCUCCCCAUACUACGCGGGACACACGAGUGGCCUUGCGACCUGGUCGAGGGGGUGGUGGUGACUUUAAAAUCUCGCAGGGUACGUGAACCUAAGAUACGCAGCUACAGAAUACUACCGUAUGGCAGUAAAAUUGAGCAGGCCAGGGGUCCUGCGACUGUACUGAUCCUAGGUCGCAACAGUGUAACCAAAGGUGGGAUGUGCAACGUACUGGCACUAAAUCCUGGCUCAGCACGAAGAACACGUAAGAGUAAGGCUCUGCUCACCCAGCUAUCAUGGAGACUGAUCAGCAAUUCUCCAAGCUCCCCAGCGCACAGACCAAUUUCUGCACGCACUCUCUUUGAACGGGGAGACAAUUAUAUUCGGAACACUAAGAGUAGACAAUGGUGCAUCUUGGCAGAUCAAUUGCGUAUCACCCAGGGGUACCUAUCUAAAGGCGGGGGCUUUAUUCUAGCGUGUCGGACAUUAUCUCCCCCAUUUGACGCUUCGCUGUUAUAUGCGGAAUUGAGGGUCUGCUAUCCACGAGCGAAGUUAGCCCAUUGGUGUGUAUCGCCACGUCGGCUAAAACUCGUGAAGACUCUUCCCCAUUUCUUGUAUUUGAACAAUGACGUACGGGCAACCACUGGUUAG'

def protein_string(rna_string):
    output = ''
    codon_position = 0
    #He also added: Threshold=0
    while codon_position * 3 < len(rna_string):
        codon = rna_string[codon_position * 3: codon_position*3 + 3]
        #if ((3*codon_position)/len(rna_string))>=Threshold*0.05:
            #print (Threshold*5,'%')
            #while ((3*codon_position)/len(rna_string))>=Threshold*0.05:
                #Threshold+=1
        index = 0
        while Look_Up[index][0] != codon:
            index+=1
        if Look_Up[index][1]!='Stop':
            output += Look_Up[index][1]
        codon_position += 1
    return output


print(protein_string(rna_string))      








