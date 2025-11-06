# Task class representing individual tasks
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    
    def __lt__(self, other):
        # Max-heap (higher priority first)
        return self.priority > other.priority

# Priority Queue class using a binary heap
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def insert(self, task):
        self.heap.append(task)  # Add task at the end
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_task = self.heap.pop()
        self._bubble_down(0)
        return max_task

    def _bubble_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def is_empty(self):
        return len(self.heap) == 0

# Example usage
pq = PriorityQueue()
pq.insert(Task(1, 3, 1, 10))
pq.insert(Task(2, 5, 2, 5))
pq.insert(Task(3, 1, 3, 7))

print("Extracting tasks by priority:")
while not pq.is_empty():
    task = pq.extract_max()
    print(f"Task ID: {task.task_id}, Priority: {task.priority}, Arrival Time: {task.arrival_time}, Deadline: {task.deadline}")
