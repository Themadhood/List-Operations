
import random
import time
import logging

#logging.basicConfig(level=logging.DEBUG)
random.seed(31337)


def bubble_sort(list_to_sort):

    comparisons = 0

    last_unsorted_index = len(list_to_sort)-1
    swaps_occurred = True
    
    logging.debug(f"Bubble sort initial state: {list_to_sort}")

    # perform bubble passes until the first time we don't have to swap anything
    # worst-case scenario, this will be when we're down to just one item left
    while swaps_occurred:

        swaps_occurred = False
        
        logging.debug(f"Bubble sort pass on indexs up to {last_unsorted_index}")
        logging.debug(f"Pass initial state: {list_to_sort}")

        for i in range(last_unsorted_index):

            left_i = i
            right_i = i + 1

            # if the adjacent pair of values is out of order, swap them
            comparisons += 1
            if list_to_sort[left_i] > list_to_sort[right_i]:
                swap(list_to_sort,left_i,right_i)
                swaps_occurred = True
                logging.debug(f"{list_to_sort[left_i]}@{left_i} and {list_to_sort[right_i]}@{right_i} swapped")
                logging.debug(f"New list state: {list_to_sort}")
            else:
                logging.debug(f"{list_to_sort[left_i]}@{left_i} and {list_to_sort[right_i]}@{right_i} not swapped")

        # we've put the biggest remaining value at last_unsorted_index,
        # so we need to move it back by one
        last_unsorted_index -= 1
    
    logging.debug(f"No swaps performed last loop, final list state: {list_to_sort}")
    
    return comparisons



def selection_sort(list_to_sort):
    comparisons = 0
    # go through array
    for i in range(len(list_to_sort)):
      
        # Find the minimum # in remaining unsorted array
        SS_MinIdex = i
        for j in range(i+1, len(list_to_sort)):
            comparisons += 1
            if list_to_sort[SS_MinIdex] > list_to_sort[j]:
                SS_MinIdex = j
              
        # Swap the found minimum with the first
        list_to_sort[i], list_to_sort[SS_MinIdex] = list_to_sort[SS_MinIdex], list_to_sort[i]
    
    return comparisons



def quick_sort(list_to_sort,start=0,stop=None):

    comparisons = 0

    # initialize stop to the last valid index
    if stop is None:
        stop = len(list_to_sort) - 1

    logging.debug(f"List state: {list_to_sort}")
    logging.debug(f"Sorting from {start} to {stop} inclusive")

    # base case
    if stop-start <= 0:
        logging.debug("Base case")
        return comparisons
    # recursive case
    else:
        logging.debug("Recursive case")
        pivot_index = stop
        pivot = list_to_sort[pivot_index]
        logging.debug(f"Pivot value: {pivot}")

        left_index = start # "black arrow"
        right_index = pivot_index - 1 # "red arrow"

        # until the arrows cross
        while left_index <= right_index:

            comparisons += 1
            if list_to_sort[left_index] <= pivot:
                logging.debug(f"value at {left_index} is {list_to_sort[left_index]}, stays")
                left_index += 1
            else:
                logging.debug(f"value at {left_index} is {list_to_sort[left_index]}, greater than pivot, swapped with position {right_index}")
                swap(list_to_sort,left_index,right_index)
                right_index -= 1

        swap(list_to_sort,left_index,pivot_index)        

        logging.debug("Making recursive calls")
        l_comps = quick_sort(list_to_sort,start,left_index-1)
        r_comps = quick_sort(list_to_sort,left_index+1,stop)
        comparisons += l_comps
        comparisons += r_comps

        return comparisons



def merge_sort(list_to_sort):
    #TODO: Implement function
    comparisons = 1
    if len(list_to_sort) > 1:
        
         # Finding the mid of the array
        MS_mid = len(list_to_sort)//2
  
        # Dividing the array
        logging.debug("Making recursive calls")
        MS_Left = list_to_sort[:MS_mid]
        MS_Right = list_to_sort[MS_mid:]
  
        # Sorting the first half
        comparisons += merge_sort(MS_Left)
        
        # Sorting the second half
        comparisons += merge_sort(MS_Right)
  
        i=0
        j=0
        k=0
  
        # Copy data from temp arrays
        while i < len(MS_Left) and j < len(MS_Right):
            comparisons += 1
            if MS_Left[i] < MS_Right[j]:
                list_to_sort[k] = MS_Left[i]
                i += 1
            else:
                list_to_sort[k] = MS_Right[j]
                j += 1
            k += 1

        #duble check
        while i < len(MS_Left):
            list_to_sort[k] = MS_Left[i]
            i += 1
            k += 1
  
        while j < len(MS_Right):
            list_to_sort[k] = MS_Right[j]
            j += 1
            k += 1

    return comparisons
    

    
def swap(the_list,i,j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp



def generate_random_list(n=10,min_val=0,max_val=100):
    my_list = list()
    for i in range(n):
        my_list.append(random.randint(min_val,max_val))
    return my_list



def test_algo(algo,num_lists=100,list_size=100,min_val=0,max_val=100):
    for i in range(num_lists):
        random_list = generate_random_list(list_size,min_val,max_val)
        answer = sorted(random_list)
        algo(random_list)
        try:
            assert random_list == answer
        except AssertionError:
            print("Test failed.")
            print("Correct sort:")
            print(answer)
            print("Algorithm output:")
            print(random_list)



def compare_algos(algos,list_size,min_val=0,max_val=100,num_lists=100):
    
    # prepare random lists
    lists = []
    for i in range(num_lists):
        lists.append(generate_random_list(list_size,min_val,max_val))
    
    print(f"Comparing {len(algos)} sorting algorithms on {num_lists} random lists of size {list_size} with values from {min_val} to {max_val}")
    
    algo_comps = dict()
    algo_times = dict()
    
    for algo in algos:

        algo_func = algos[algo]
        all_comparisons = []
        all_times = []
        
        for i in range(len(lists)):
        
            next_list = lists[i][:]
            
            logging.info(f"Testing {algo} on list {i}...")
                
            start_time = time.time()
            comparisons = algo_func(next_list)
            end_time = time.time()
            all_comparisons.append(comparisons)
            all_times.append(end_time-start_time)
        
        algo_comps[algo] = sum(all_comparisons)/len(all_comparisons)
        algo_times[algo] = sum(all_times)/len(all_times)
    
    print(f"Sort,Comps,Time")
    for algo in algos:
        print(f"{algo},{algo_comps[algo]},{algo_times[algo]}")



if __name__ == "__main__":

    algos = dict()
    algos["Bubble sort"] = bubble_sort
    algos["Selection sort"] = selection_sort
    algos["Quick sort"] = quick_sort
    algos["Merge sort"] = merge_sort
    
    for algo in algos:
        print()
        print()
        print()
        print(f"Testing {algo}...")
        test_algo(algos[algo])
    
    compare_algos(algos,list_size=10)
    
