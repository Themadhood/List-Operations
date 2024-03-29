#program:       LstOperations.LstSorting.LstOfDcts
#purpose:       sorts a list of dcts
#progamer:      Themadhood Pequot 5/9/2023

_FILE = "LstOperations.LstSorting.LstOfDcts"
_VERSION = "0.0.1"

import Error


def SortLstOfDctsBy(List,orderkey):
    try:
        if len(List) > 1:
            
            # Finding the midle of the array
            middle = len(List)//2
      
            # Dividing the array
            Left = List[:middle]
            Right = List[middle:]
      
            # Sorting the first half
            SortBy(Left,orderkey)
            
            # Sorting the second half
            SortBy(Right,orderkey)
      
            i=j=k=0
      
            # Copy data from temp arrays
            while i < len(Left) and j < len(Right):
                if Left[i][orderkey] < Right[j][orderkey]:
                    List[k] = Left[i]
                    i += 1
                else:
                    List[k] = Right[j]
                    j += 1
                k += 1
            #duble check
            while i < len(Left):
                List[k] = Left[i]
                i += 1
                k += 1
      
            while j < len(Right):
                List[k] = Right[j]
                j += 1
                k += 1

    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","SortLstOfDctsBy",
                           f"failed to sort lst of dcts by {orderkey}",
                           e],"Functions")

    return List

def OrderdLstToDct(List,orderkey,Orderd=False):
    try:
        #Makes sure list is orderd
        if Orderd:
            lst = List.copy()
        else:
            lst = SortBy(List.copy(),orderkey)

    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","OrderdLstToDct",
                           f"failed order lst",e],"Functions")
    dct = dict()

    #removes record from list and adds it to dictonary
    try:
        while lst > []:
            record = lst.pop(0)
            key = record[orderkey]
            try:
                dct[key].append(record)
            except:
                dct.update({key:[record]})

    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","OrderdLstToDct",
                           f"failed convert lst to dct",e],"Functions")

    return dct


if __name__ == "__main__":
    List = [{"A":2,"B":"D"},
            {"A":9,"B":"B"},
            {"A":4,"B":"C"},
            {"A":2,"B":"C"}]
    
    print(List)
    SListA = SortBy(List.copy(),"A")
    print(SListA)
    SListB = SortBy(List.copy(),"B")
    print(SListB)










