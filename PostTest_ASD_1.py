def mergerSort(list):
    list_length = len(list)
    if list_length == 1:
        return list

    mid_point = list_length // 2
    ngiri_partition = mergerSort(list[:mid_point])
    nganan_partition = mergerSort(list[mid_point:])
    return merge(ngiri_partition, nganan_partition)

def merge(ngiri, nganan):
    output = []
    i = j = 0
    while i < len(ngiri) and j < len(nganan):
        if isinstance(ngiri[i], str) and isinstance(nganan[j], str):
            if ngiri[i] < nganan[j]:
                output.append(ngiri[i])
                i += 1
            else:
                output.append(nganan[j])
                j += 1
        elif isinstance(ngiri[i], str):
            output.append(ngiri[i])
            i += 1
        elif isinstance(nganan[j], str):
            output.append(nganan[j])
            j += 1
        else:
            if ngiri[i] < nganan[j]:
                output.append(ngiri[i])
                i += 1
            else:
                output.append(nganan[j])
                j += 1
    output.extend(ngiri[i:])
    output.extend(nganan[j:])

    return output

def pisah(listnya):
    for i in listnya:
        tampungan.append(i)

listacak = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
tampungan = []
print("List awal sebelum diurutkan ",listacak)
pisah(listacak)
print("List setelah diurutkan ",tampungan)
sorted_list = mergerSort(tampungan)
print("Hasil akhir list ",sorted_list)