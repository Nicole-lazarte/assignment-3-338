import heapq
import random
import timeit
import matplotlib.pyplot as plt

# Inefficient implementation
def insert_into_priority_queue(queue, item):
    heapq.heappush(queue, item)

def extract_from_priority_queue(queue):
    return heapq.heappop(queue)

# Efficient implementation
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        index = len(self.queue)
        self.queue.append(item)
        while index > 0:
            parent = (index - 1) // 2
            if self.queue[parent] < item:
                self.queue[index] = self.queue[parent]
                index = parent
            else:
                break
        self.queue[index] = item

    def extract(self):
        if not self.queue:
            raise IndexError('Queue is empty')
        item = self.queue[0]
        last_item = self.queue.pop()
        if self.queue:
            self.queue[0] = last_item
            index = 0
            while True:
                left_child = (index * 2) + 1
                right_child = (index * 2) + 2
                if left_child < len(self.queue) and self.queue[left_child] > self.queue[index]:
                    largest_child = left_child
                else:
                    largest_child = index
                if right_child < len(self.queue) and self.queue[right_child] > self.queue[largest_child]:
                    largest_child = right_child
                if largest_child == index:
                    break
                self.queue[index] = self.queue[largest_child]
                index = largest_child
            self.queue[index] = last_item
        return item

# Insertion experiment
def experiment_insertion():
    heap_insertion_times = []
    heapq_insertion_times = []
    for i in range(100, 1001, 100):
        binary_heap = PriorityQueue()
        heapq_heap = []
        for j in range(i):
            item = random.randint(0, 100000)
            start_time = timeit.default_timer()
            binary_heap.insert(item)
            end_time = timeit.default_timer()
            heap_insertion_times.append(end_time - start_time)
            start_time = timeit.default_timer()
            heapq.heappush(heapq_heap, item)
            end_time = timeit.default_timer()
            heapq_insertion_times.append(end_time - start_time)
        print(f"Number of elements: {i}")
        print(f"Binary Heap Insertion Time: {min(heap_insertion_times)} seconds")
        print(f"Heapq Insertion Time: {min(heapq_insertion_times)} seconds")

    plt.hist(heap_insertion_times, bins=20, alpha=0.5, label='Binary Heap')
    plt.hist(heapq_insertion_times, bins=20, alpha=0.5, label='Heapq')
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Insertion into Priority Queue')
    plt.show()

# Extraction experiment
def experiment_extraction():
    heap_extraction_times = []
    heapq_extraction_times = []
    for i in range(100, 1001, 100):
        binary_heap = PriorityQueue()
        heapq_heap = []
        for j in range(i):
            item = random.randint(0, 100000)
            binary_heap.insert(item)
            heapq.heappush(heapq_heap, item)

        start_time = timeit.default_timer()
        for j in range(i):
            binary_heap.extract()
        end_time = timeit.default_timer()
        heap_extraction_times.append(end_time - start_time)

        start_time = timeit.default_timer()
       
