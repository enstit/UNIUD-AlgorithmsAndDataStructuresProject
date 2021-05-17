Tutti file sono compatibili con python2, le differenze sono poche e principalment stanno per "print".

Gli output vengono stampati nel terminal ma per comodità hanno la forma di un csv.
Se voglio salvare output gli eseguo in questo modo:

python2 amortizedAnalysis.py > a.csv
python2 amortizedAnalysisWorstCase.py > b.csv
python2 amortizedAnalysisSameInputs.py > c.csv

In teoria il file amortizedAnalysis.py è qullo che bisogna consegnare come il programma per la stima dei tempi di esecuzione, mentre altri possiamo aggiungere nella relazione oppure consegnare tutti quanti.

BST ha due metodi insert e due metodi find. Il metodo iterativo viene usato solo per il calcolo del caso peggiore per non avere "recursion error maximum recursion depth exceeded". Si può usare anche "sys.setrecursionlimit(10**6)" per aumentare "recursion depth" e non usare i metodi iterativi.

