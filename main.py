def deco_timing(f):
    import time
    def wrapper(*args):
        start = time.time()
        r = f(*args)
        print '%s seconds' % (time.time() - start)
        return r
    return wrapper

def mergesort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = mergesort(x[:mid])
    z = mergesort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            result += z
            z = []
        else:
            result += y
            y = []
    return result

def bubblesort(lista):
    looping = True
    while looping:
        looping = False
        for i in xrange(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                looping = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def quicksort(lista):
    if lista == []: 
        return []
    else:
        pivot = lista[0]
        lesser = quicksort([x for x in lista[1:] if x <= pivot])
        greater = quicksort([x for x in lista[1:] if x > pivot])
        return lesser + [pivot] + greater

@deco_timing
def executor(f, *args):
    return f(*args)

if __name__ == '__main__':

    import random, sys
    algorithms = {'b': bubblesort, 'm': mergesort, 'q': quicksort}
    if len(sys.argv) == 3:
        numElements = int(sys.argv[2])
        a = random.sample(xrange(9999999), numElements)
        print executor(algorithms[str(sys.argv[1])], a)
    else:
        print 'Usage: '
        print '1st param: \n b: Bubblesort \n m: Mergesort \n q: Quicksort'
        print '2nd param: \n # elements of sample list'
        print 'Example: python main.py m 50000'
    