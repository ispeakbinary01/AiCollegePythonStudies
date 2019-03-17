def suma_kolokviumi(new_list):
    sum_list = []
    
    for i in range(len(new_list)):
        sum_dict = {}
        sum_dict["indeks"] = new_list[i]["indeks"]
        sum_dict["predmet"] = new_list[i]["predmet"]
        sum_dict["Vkupno od kolokviumi"] = new_list[i]["Kolokvium 1"] + new_list[i]["Kolokvium 2"]
        sum_list.append(sum_dict)    
    
    return sum_list


n = int(input())
rezultati = []
for i in range(0, n):
    r = {}
    brojIndex = int(input())
    brojPoeni1 = int(input())
    brojPoeni2 = int(input())
    r["indeks"] = brojIndex
    r["predmet"] = "Vestacka Intelegencija"
    r["Kolokvium 1"] = brojPoeni1
    r["Kolokvium 2"] = brojPoeni2
    print("ADDING RESULTS======", r)
    rezultati.append(r)
    print("RESULT ADDED!!")

print("NORMAL RESULTS {}".format(rezultati))
print(" SUM RESULTS ============ {}".format(suma_kolokviumi(rezultati)))
