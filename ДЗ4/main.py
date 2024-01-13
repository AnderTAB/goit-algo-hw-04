import timeit
import random

from radix_sort import radix_sort
from timsort import timSort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == '__main__':
    data_small = [random.randint(0, 1000) for _ in range(1000)]
    data_medium = [random.randint(0, 10000) for _ in range(10000)]
    data_large = [random.randint(0, 100000) for _ in range(100000)]
    
    
    time_small_radix = timeit.timeit(lambda: radix_sort(data_small[:]), number=10)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=10)
    time_small_timsort_s = timeit.timeit(lambda: data_small[:].sort(), number=10)
    time_small_timSort = timeit.timeit(lambda: timSort(data_small[:]), number=10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
        
    time_medium_radix = timeit.timeit(lambda: radix_sort(data_medium[:]), number=10)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=10)
    time_medium_timsort_s = timeit.timeit(lambda: data_medium[:].sort(), number=10)
    time_medium_timSort = timeit.timeit(lambda: timSort(data_medium[:]), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    
    # time_large_radix = timeit.timeit(lambda: radix_sort(data_large[:]), number=10)
    # time_large_timsort = timeit.timeit(lambda: sorted(data_large[:]), number=10)
    # time_large_timsort_s = timeit.timeit(lambda: data_large[:].sort(), number=10)
    # time_large_timSort = timeit.timeit(lambda: timSort(data_large[:]), number=10)
    # time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large[:]), number=10)
    # time_large_merge = timeit.timeit(lambda: merge_sort(data_large[:]), number=10)
    
    # print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time large data': <20}")
    # print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
    # print(f"{'| Radix sort': <20} | {time_small_radix:<20.5f} | {time_medium_radix:<20.5f} | {time_large_radix:<20.5f}")
    # print(f"{'| Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f} | {time_large_timsort:<20.5f}")
    # print(f"{'| Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f} | {time_large_timsort_s:<20.5f}")
    # print(f"{'| timSort': <20} | {time_small_timSort:<20.5f} | {time_medium_timSort:<20.5f} | {time_large_timSort:<20.5f}")
    # print(f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f} | {time_large_insertion:<20.5f}")
    # print(f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f} | {time_large_merge:<20.5f}")
    print(f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(f"{'| **Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f}")
    print(f"{'| timSort': <20} | {time_small_timSort:<20.5f} | {time_medium_timSort:<20.5f}")
    print(f"{'| **Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}")
    print(f"{'| Radix sort': <20} | {time_small_radix:<20.5f} | {time_medium_radix:<20.5f}")
    print(f"{'| **Tim sort sorted': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}")
    print(f"{'| **Tim sort sort': <20} | {time_small_timsort_s:<20.5f} | {time_medium_timsort_s:<20.5f}")


# timSort - знайшов реалізацію в інтернеті вирішив перевірити ефективність до кучі