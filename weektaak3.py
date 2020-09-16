seq = 'ACTGACTGACTG'

aminozuurbad = ('D', 'E', 'F', 'L', 'S', 'Y', 'W', 'P', 'H', 'Q', 'R', 'I', 'N', 'K', 'V')

#tel lengte en hoeveelheid actg
#if elif en dan pas else
aantal_a = seq.count('A')
aantal_c = seq.count('C')
aantal_g = seq.count('G')
aantal_t = seq.count('T')
aantal_totaal = (aantal_a) + (aantal_c) + (aantal_g) + (aantal_t)
print('Total base amount mRna sequence 1: ' + str(aantal_totaal))
print('Total lenght of sequence 1: ')
print(len(seq))
if len(seq) == aantal_totaal:
    print('Sequence 1 is a mRna')
else:
    print('Sequence 1 is an eggwhitesequence!')
    aantal_d = seq.count('D')
    aantal_e = seq.count('E')
    aantal_r = seq.count('R')
    aantal_k = seq.count('K')
    print('Amount of D: ' + str(aantal_d))
    print('Amount of E: ' + str(aantal_e))
    print('Amount of R: ' + str(aantal_r))
    print('Amount of K: ' + str(aantal_k))
    aantal_de = (aantal_d) + (aantal_e)
    aantal_kr = (aantal_k) + (aantal_r)
    aantal_netto = (aantal_de) - (aantal_kr)
    print('Net charge: ' + str(aantal_netto))
    
print('--------------------------------------------------')
#----------------------------------------------------------------------------------------------#
seq2 = 'DEFLSYWRKRIRNAKQDD'
aantal_a2 = seq2.count('A')
aantal_c2 = seq2.count('C')
aantal_g2 = seq2.count('G')
aantal_t2 = seq2.count('T')
aantal_totaal2 = (aantal_a2) + (aantal_c2) + (aantal_g2) + (aantal_t2)
print('Total base amount mRna sequence 2: ' + str(aantal_totaal2))
print('Total lenght of sequence 2: ')
print(len(seq2))
if len(seq) == aantal_totaal2:
    print('Sequence 2 is a mRna')
else:
    print('Sequence 2 is an eggwhitesequence!')
    aantal_d2 = seq2.count('D')
    aantal_e2 = seq2.count('E')
    aantal_r2 = seq2.count('R')
    aantal_k2 = seq2.count('K')
    print('Amount of D: ' + str(aantal_d2))
    print('Amount of E: ' + str(aantal_e2))
    print('Amount of R: ' + str(aantal_r2))
    print('Amount of K: ' + str(aantal_k2))
    aantal_de2 = (aantal_d2) + (aantal_e2)
    aantal_kr2 = (aantal_k2) + (aantal_r2)
    aantal_netto2 = (aantal_de2) - (aantal_kr2)
    print('Net charge: ' + str(aantal_netto2))

print('--------------------------------------------------')
print('Total lenght of sequence 1: ')
print(len(seq))
print('Total lenght of sequence 2: ')
print(len(seq2))
