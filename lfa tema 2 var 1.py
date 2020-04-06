def star(s):

    if s == '':
        return 'λ'

    if s == 'λ':
        return 'λ'

    if len(s) == 1:
        return s + "*"

    if s[-1] == '*':
        return s

    return "[" + s + "]" + "*"


def product(s1, s2):

    if s1 == '' or s2 == '':
        return ''

    if s1 == 'λ':
        return s2

    if s2 == 'λ':
        return s1

    if '∪' in s1 and (']' not in s1 or s1[::-1].find(']') > s1[::-1].find('∪')):
        s1 = '[' + s1 + ']'

    if '∪' in s2 and (']' not in s2 or s2[::-1].find(']') > s2[::-1].find('∪')):
        s2 = '[' + s2 + ']'

    return s1 + s2


def union(s1, s2):

    if s1 == '':
        return s2

    if s2 == '':
        return s1

    if s1 == s2:
        return s1

    return s1 + "∪" + s2


def locfind(x, l):

    for i in range(len(l)):
        if l[i] == x:
            return i

    return 'false'


def selfmfind(node):

    for i in range(len(d[node][0])):
        if d[node][0][i] == node:
            return d[node][1][i]

    return ''


m = int(input()) # nr muchii
n = int(input()) # nr noduri

q = ['start'] + input().split() + ['fin'] # nodurtile intr-o ordine aleatorie , numele trebuie sa fie diferit de fin sau start

d = {}

for i in range(m):
    s = input().split() # pe rand muchiile, !!!daca exista mai multe muchii de la un nod la altul, trebuie date ca o singura muchie cu valoarea scrisa ca reuniune

    if s[0] not in d.keys():
        d.update({s[0]: [[], [], [s[1]], [s[2]]]}) # d[st][0] -> noduri incidente interioare, d[st][1] -> muchii incidente interioare
                                          # d[st][2] -> noduri incidente exterioare, d[st][3] -> muchii incidente exterioare
    else:
        d[s[0]][2].append(s[1])
        d[s[0]][3].append(s[2])

    if s[1] not in d.keys():
        d.update({s[1]: [[s[0]], [s[2]], [], []]})

    else:
        d[s[1]][0].append(s[0])
        d[s[1]][1].append(s[2])


sinit = input()

d.update({'start': [[], [], [sinit], ['λ']]})
d[sinit][0].append('start')
d[sinit][1].append('λ')

sfin = input().split()

d.update({'fin': [[], [], [], []]})

for i in range(len(sfin)):
    d['fin'][0].append(sfin[i])
    d['fin'][1].append('λ')

    d[sfin[i]][2].append('fin')
    d[sfin[i]][3].append('λ')

eliminated = set() # multimea de noduri eliminate pana la pasul curent

for nod in d.keys():
    if nod != 'fin' and nod != 'start':

        eliminated.add(nod)

        li = len(d[nod][0])
        le = len(d[nod][2])

        for i in range(li): # d[nod][0][i], d[nod][1][i]
            if d[nod][0][i] not in eliminated: # nu iau in calcul nodurile eliminate, incluzand actualul nod

                inaux = d[nod][0][i]
                inauxm = d[nod][1][i]

                for j in range(le): # d[nod][2][j], d[nod][3][j]
                    if d[nod][2][j] not in eliminated:

                        exaux = d[nod][2][j]
                        exauxm = d[nod][3][j]

                        if inaux in d[exaux][0]:
                            poz = locfind(inaux, d[exaux][0])
                            poz2 = locfind(exaux, d[inaux][2])

                            d[exaux][1][poz] = union(d[exaux][1][poz], product(inauxm, product(star(selfmfind(nod)), exauxm)))
                            d[inaux][3][poz2] = d[exaux][1][poz]
                        else:
                            newm = product(inauxm, product(star(selfmfind(nod)), exauxm))

                            d[exaux][0].append(inaux)
                            d[exaux][1].append(newm)

                            d[inaux][2].append(exaux)
                            d[inaux][3].append(newm)

auxfin = d['fin'][1][locfind('start', d['fin'][0])]

i = 0
while i < len(auxfin):
    if auxfin[i] == "∪":

        auxfin = auxfin[:i] + " ∪ " + auxfin[i + 1:]
        i += 3
    else:
        i += 1

print(auxfin)







