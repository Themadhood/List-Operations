__Program__     = "LstOperations.ListLenManipulate"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")



def RemoveLstsGreaterThanMax(lstOfLst,maxLen=0,error=False):
    lstTmp = lstOfLst.copy()
    try:
        #remove groups greater than max size
        if maxLen > 0:
            for lst in lstTmp:
                if len(lst) > maxLen:
                    lstOfLst.remove(lst)

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","RemoveLstsGreaterThanMax",
                           f"failed to remove lists greater than {maxLen}",
                           e],"Functions")


def RemoveLstsLessThanMin(lstOfLst,minLen=0,error=False):
    lstTmp = lstOfLst.copy()
    try:
        #remove groups greater than max size
        if minLen > 0:
            for lst in lstTmp:
                if len(lst) < minLen:
                    print(lst,minLen)
                    lstOfLst.remove(lst)

    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","RemoveLstsLessThanMin",
                           f"failed to remove lists less than {minLen}",
                           e],"Functions")

















