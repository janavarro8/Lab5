import Heap, random

def file_reader():
    try:
        heap_list = []
        file = open("tester.txt", "r")
        line = file.read().split(",")

        for num in line:
            heap_list.append(num)

        heap_list = list(map(int, heap_list))
        return heap_list
    except FileNotFoundError:
        print("I'm sorry, but the file cannot be found.")
        print("Please place the file in the folder with the program and label it 'tester' with .txt extension and start the program again.")
        print("Goodbye.")
        sys.exit()

def heap_sort(heap_list):
    h = Heap.Heap()
    i = len(heap_list) // 2 - 1
    while i >= 0:
        h.percolate_down(i, heap_list, len(heap_list))
        i = i - 1

    i = len(heap_list) - 1
    while i > 0:
        temp = heap_list[0]
        heap_list[0] = heap_list[i]
        heap_list[i] = temp
        h.percolate_down(0, heap_list, i)
        i = i - 1

def test_method():
    h = Heap.Heap()
    random_test = random.sample(range(0, 100), 10)
    print(random_test, "\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    for num in random_test:
        h.insert(num)
        print("Heap array: %s\n" % h.heap_array)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    print("The min-heap with this set of numbers is:\n", h.heap_array)

def main():
    print("Testing the following generated list: ")
    test_method()
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")

    print("Testing the following hard coded list")
    hard_coded_list = random.sample(range(0, 100), 10)
    print("\nList before sorting:\n", hard_coded_list)
    heap_sort(hard_coded_list)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    print("Hard-coded list after sorting: \n", hard_coded_list)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")

    print("\n_-_-_-_Reading the file now_-_-_-_-")
    read_list = file_reader()
    print("\nThe list before heap-sort:\n ", read_list)
    heap_sort(read_list)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    print("The list after heap-sort \n", read_list)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")

main()