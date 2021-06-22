# Eksamen 2017 2a
def file_to_list(filename):
    output=[]
    file=open(filename,'r')
    for line in file:
        line=line.strip()
        liste=line.split('\t')
        liste[2]=float(liste[2])
        output.append(liste)
    file.close()
    return output


#2b
def list_stores(dataList):
    output=[]
    for element in dataList:
        if element[0] not in output:
            output.append(element[0])
    return output

#2c
def sum_prices_stores(dataList,storeList):
    output=[0]*len(storeList)
    for element in storeList:
        for verdi in dataList:
            if element==verdi[0]:
                output.insert(storeList.index(element),output[storeList.index(element)]+verdi[2])
    return output

#2d
def rank_stores(storeList,sumStores):
    output=[]
    copystoreList=[]+storeList
    copysumStores=[]+sumStores
    while len(copystoreList)>0:
        indexen=copysumStores.index(min(copysumStores))
        output.append(copystoreList[index])
        del copystoreList[indexen]
        del copysumStores[indexen]
    return output

                




            
        
