
voti = [15,25,18,28,26,30,24,28]

voti_24_plus = [ x for x in voti if x > 24 ] # list comprehension

voti_24_lambda = list(map(lambda voto : voto - 2, voti))

print(voti_24_lambda)
