import decimal, time
precision = 2
elapsed = 1
while elapsed < 60:
    decimal.setcontext(decimal.Context(prec=precision))
    i = 1
    x = decimal.Decimal(3)
    pi = x
    start = time.time()
    while x > 0:  # taylor series expansion
            x = x * i / ((i + 1) * 4)
            i += 2
            pi += x / i
    elapsed = time.time() - start

    print('In {:6.2f} seconds {:5d} digits of pi is'.format(elapsed, len(str(pi)) - 1), pi)
    precision *= 2
