__Program__     = "LstOperations.CantBeInSameLst"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")



def ItemWithItem(lst,item,itemWith,error=False):
    try:
        if item in lst and itemWith in lst:
            return True
            
    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","RemoveLstsGreaterThanMax",
                           f"failed to remove lists greater than {maxLen}",
                           e],"Functions")
    return False


def RemoveItemWithItem(lstOfLst,item,itemWith,error=False):
    lstTmp = lstOfLst.copy()
    try:
        while lstTmp > []:
            lst = lstTmp.pop()
            if ItemWithItem(lst,item,itemWith,error):
                lstOfLst.remove(lst)

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","RemoveLstsGreaterThanMax",
                           f"failed to remove lists greater than {maxLen}",
                           e],"Functions")

if __name__ == "__main__":
    L = [[1, 3],[1, 2],[2, 3]]
    
    RemoveItemWithItem(L,1,2,error=True)

    for l in L:
        print(l)











