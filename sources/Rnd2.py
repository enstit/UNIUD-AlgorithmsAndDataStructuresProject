# Frammento di codice per generare un vettore di stringhe pseudocasuali utilizzando il secondo metodo descritto della consegna 
strings2 = []
for size in sizes:
    q = random.randint(1, size)
    s = (''.join(random.choices(['a', 'b', 'c'], k=q)))

    for i in range(q + 1, size):
        s = s + s[(i - 1) % q + 1]

    strings2.append(s)
    
