class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)
        self.percolate_up(len(self.heap_array) - 1)

    def percolate_up(self, node):
        while node > 0:
            parent_node = (node - 1) // 2  # Used to find parent of current node
            if self.heap_array[node] >= self.heap_array[parent_node]:  # Used to check if the max heap is present
                return
            else:  # This is where we need to swap elements to meet property to min-heap
                print("Swapping: %d with %d" % (self.heap_array[parent_node], self.heap_array[node]))
                temp = self.heap_array[node]
                self.heap_array[node] = self.heap_array[parent_node]
                self.heap_array[parent_node] = temp

                node = parent_node

    def percolate_down(self, node, heap_list, size):
        child_index = (2 * node) + 1
        element = heap_list[node]

        while child_index < size:  # Find the max among the node and all the node's children
            max_value, max_index = element, -1
            i = 0

            while i < 2 and i + child_index < size:
                if heap_list[i + child_index] > max_value:
                    max_value = heap_list[i + child_index]
                    max_index = i + child_index
                i = i + 1

            if max_value == element:
                return

            # We will swap the current node index with the max index using a temp variable
            temp = heap_list[node]
            heap_list[node] = heap_list[max_index]
            heap_list[max_index] = temp

            node = max_index
            child_index = 2 * node + 1

    def is_empty(self):
        return len(self.heap_array) == 0

