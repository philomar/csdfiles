nia = [('mark','GHA22222'),
       ('wisdom','GHA33333'),
       ('wisdom','GHA77777'),
       ('SAVIOUR','GHA44444'),
       ('philip','GHA55555')]

mtn = [('mark', '0558195329', 'GHA22222'),
       ('wisdom', '0247550338', 'GHA33333'),
       ('SAVIOUR', '0244156677', 'GHA44444'),
       ('philip', '0248809923', 'GHA55555'),
       ('fred', '0248809924', 'GHA66666')]

vodafone = [
       ('wisdom', '0207550338', 'GHA33333'),
       ('wisdom', '0207550339', 'GHA77777'),
       ('SAVIOUR', '0204156677', 'GHA44444'),
       ('philip', '0208809923', 'GHA22222')]

nca = []

rejected = []

telcos = [mtn, vodafone]

rusers = {}

for telco in telcos:

    for ru in telco:
        (na, pn, gc) = ru
        found = False

        for vu in nia:
            if gc == vu[1]:
                if na == vu[0]:
                    if not gc in rusers.keys():
                        nuser = {
                            'name': na,    
                            'ghana card': gc,
                            'numbers': [pn]
                        }
                        nca.append(nuser)
                        rusers[gc] = nca.index(nuser)
                    else:
                        nca[rusers[gc]]['numbers'].append(pn)
                    
                    print('Successfully added ', na, ' to NCA records')
                else:
                    rejected.append({
                        'name': na,
                        'ghana card': gc,
                        'numbers': pn
                        
                    })
                    print('Inconsistent Ghana card number \nUser: ', na, ' records rejected')
                found = True
                break
            else:
                found = False
                
        if not found:
            print('No user with name: ', na)

print('Successful Registrations\n\n')
for ru in nca:    
    print(ru, end="\n\n")


print('Failed Registrations\n\n')
for ru in rejected:    
    print(ru, end="\n\n")
