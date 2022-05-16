def future_lump_sum(r, n, pv):
    ''' 
    TODO: desc 

    Parameters
        r   rate
        n   number of periods
        pv  present value
    '''
    return pv * (1 + r)**n


def present_lump_sum(r, n, fv):
    return fv / (1 + r)**n


def future_annuity(r, n, pmt):
    '''
    Calculate and return the future value of an annuity of pmt
    to be received each period for n periods, invested at the periodic rate r
    '''
    return pmt * ((1+r)**n - 1)/r


if __name__ == '__main__':
    print(future_lump_sum(0.05, 2, 100))
    print(present_lump_sum(0.06, 5, 1000))
    print(future_annuity(0.04, 5, 100))