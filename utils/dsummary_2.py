def fileopen(filenm):
    with open(filenm) as fo:
        lst_1=fo.readlines()
        return lst_1

def transpose(lst_data):
    lst_3= [data.strip().split(',') for data in lst_data]
    zlist=zip(*lst_3)
    return zlist

def numeric_summary(num_list):
    return {'max':max(num_list, key=float), 'min':min(num_list, key=float)}

def nominal_summary(nomi_list):
    d={}
    for nm in nomi_list:
        d.setdefault( nm , nomi_list.count(nm) )
    return d

def do_summary(lst_20, excp_lst):
    d={}
    for i, col_data in enumerate(lst_20):
        try:
            if i in excp_lst:
                raise ValueError
            d.setdefault( lst_20[i][0], numeric_summary(col_data[1:]) )
        except ValueError as ve:
            d.setdefault( lst_20[i][0], nominal_summary(col_data[1:]) )
    return d

if __name__=="__main__":
    l1=fileopen('insurance.csv')
    l2 = transpose(l1)
    print do_summary(l2, [3])