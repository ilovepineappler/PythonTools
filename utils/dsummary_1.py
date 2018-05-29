def raw_data(file):
    line_counter = 0
    data_header = []
    data_list1 = []
    with open("insurance.csv", "r") as customer_data:
        while True:
            data = customer_data.readline()
            if not data:
                break
            if line_counter == 0:
                data_header = data.strip().split(",")
            else:
                data_list1.append(data.strip().split(","))
            line_counter += 1
    return data_header, data_list1

def making_dataset(file):
    dataset = {}
    key, data_list2 = raw_data(file)
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if(i == 0 or 2 or 6):
            vali = numeric_values(i,data_list2)  
            dataset.setdefault(key[i], vali)
        else:
            vali = nominal_values(i,data_list2)
            dataset.setdefault(key[i], vali)
    return dataset

def numeric_values(num,data_list):    
    results={}
    lst1=[(n[num]) for n in data_list]
    results.setdefault('max',max(lst1))
    results.setdefault('min',min(lst1))
    return results

def nominal_values(num,data_list):
    results={}
    lst2=[str1[num] for str1 in data_list]    
    for str2 in lst2:
        results.setdefault(str2,lst2.count(str2))    
    return results
    
if __name__== "__main__":
    dataset = making_dataset("insurance.csv")
    print dataset
    
