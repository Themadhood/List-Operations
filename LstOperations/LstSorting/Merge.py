#program:       LstOperations.LstSorting.Merge
#purpose:       sorts list
#progamer:      Themadhood Pequot 5/13/2022

def Merge(list_to_sort):
    if len(list_to_sort) > 1:
        
         # Finding the mid of the array
        mid = len(list_to_sort)//2
  
        # Dividing the array
        Left = list_to_sort[:mid]
        Right = list_to_sort[mid:]
  
        # Sorting the first half
        merge_sort(Left)
        
        # Sorting the second half
        merge_sort(Right)
  
        i=0
        j=0
        k=0
  
        # Copy data from temp arrays
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                list_to_sort[k] = Left[i]
                i += 1
            else:
                list_to_sort[k] = Right[j]
                j += 1
            k += 1

        #duble check
        while i < len(Left):
            list_to_sort[k] = Left[i]
            i += 1
            k += 1
  
        while j < len(Right):
            list_to_sort[k] = Right[j]
            j += 1
            k += 1

    return list_to_sort



if __name__ == "__main__":
    lst = [9,4,5,6,7,3,2,8,1]
    ms = merge_sort(lst)
    print(ms)

    











