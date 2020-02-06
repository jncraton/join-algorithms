import random
from collections import OrderedDict
from time import time

def join_nested_loop(left, right):
    """
    Returns matching items in left and right lists using the nested loop join algorithm
    
    >>> list(join_nested_loop([1,2,3],[4,5,6]))
    []
    >>> list(join_nested_loop([1,2],[1,2,3]))
    [(1, 1), (2, 2)]
    >>> list(join_nested_loop([1,2,3],[3,4,5]))
    [(3, 3)]
    """

def join_sort_merge(left, right):
    """
    Returns matching items in left and right lists using the sort-merge join algorithm
    
    >>> list(join_sort_merge([1,2,3],[4,5,6]))
    []
    >>> list(join_sort_merge([1,2],[1,2,3]))
    [(1, 1), (2, 2)]
    >>> list(join_sort_merge([1,2,3],[3,4,5]))
    [(3, 3)]
    """
    
def join_hash(left, right):
    """
    Returns matching items in left and right lists using the hash join algorithm
    
    >>> list(join_hash([1,2,3],[4,5,6]))
    []
    >>> list(join_hash([1,2],[1,2,3]))
    [(1, 1), (2, 2)]
    >>> list(join_hash([1,2,3],[3,4,5]))
    [(3, 3)]
    """

def time_join(join, size):
    """
    Time a join algorithm executing against tables of a given size
    """
    
    random.seed(0)
    left = random.sample(range(size*2), size)
    right = random.sample(range(size*2), size)
    
    t0 = time()
    row_count = sum([1 for row in join(left, right)])
    return (time() - t0) * 1e6

def plot_performance(algorithms, max_size=14):
    """
    Plot runtime performance of join algorithms
    """

    import matplotlib.pyplot as plt
    
    sizes = [2**i for i in range(2,max_size)]

    for join in algorithms:
        times = [time_join(join, size) for size in sizes]
        plt.plot(sizes[:len(times)], times, label=join.__name__)

    plt.title('Performance (runtime vs table size)')
    plt.ylabel('Time (µs)')
    plt.xlabel('Items')
    plt.yscale('log', basey=2)
    plt.xscale('log', basex=2)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_performance([join_nested_loop, join_sort_merge, join_hash])
