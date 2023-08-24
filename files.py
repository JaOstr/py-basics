with open(r'd:\lrn\py\basics\pi_digits.txt') as f:
    #contents = f.read()
    #print(contents)
    for line in f:
        print('Line: ' + line.rstrip()) 
