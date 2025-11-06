# Assignment4
Heap Data Structures: Implementation, Analysis, and Applications
Overview

In this project, I implemented and analyzed two core applications of heap data structures:

Heapsort Algorithm: A sorting algorithm based on binary heaps.

Priority Queue: A data structure that supports efficient insertion and extraction of tasks based on their priority, implemented using a binary heap.

The project demonstrates the practical applications of heaps in real-world scenarios, such as sorting and scheduling tasks with priorities.

Project Structure

The project is divided into the following components:

Heapsort Algorithm:

heapsort.py: Python implementation of the Heapsort algorithm.

heapify(): Function to ensure the heap property is maintained.

heapsort(): Main sorting function that performs sorting using the heap structure.

Priority Queue:

priority_queue.py: Python implementation of a priority queue using a binary heap.

Task Class: Represents individual tasks with properties like task_id, priority, arrival_time, and deadline.

PriorityQueue Class: Implements the priority queue operations, including insert(), extract_max(), and is_empty().

Features
Heapsort Implementation

Sorting Efficiency: Heapsort is an in-place sorting algorithm with O(n log n) time complexity for worst, best, and average cases.

Space Efficiency: Heapsort has O(1) space complexity as it sorts in place without requiring additional memory aside from the input array.

Priority Queue Implementation

Task Management: Tasks are represented as objects, each having a priority and other relevant attributes such as arrival time and deadline.

Max-Heap: The priority queue is implemented using a max-heap, where tasks with higher priority are extracted first.

Operations:

insert(): Adds a new task to the heap.

extract_max(): Removes and returns the task with the highest priority.

is_empty(): Checks if the priority queue is empty.

Time Complexity Analysis
Heapsort

Worst, Best, and Average Case Time Complexity: O(n log n)

Space Complexity: O(1)

Priority Queue

Insert Operation: O(log n)

Extract Max: O(log n)

is_empty: O(1)

How to Run the Code
Prerequisites

Python 3.x or later is required to run the code.

Running Heapsort

To run the Heapsort implementation, simply execute the following code in a Python environment:

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heapsort(arr)
print("Sorted array:", sorted_arr)

Running Priority Queue

To test the priority queue, you can execute the following code:

pq = PriorityQueue()
pq.insert(Task(1, 3, 1, 10))
pq.insert(Task(2, 5, 2, 5))
pq.insert(Task(3, 1, 3, 7))

while not pq.is_empty():
    task = pq.extract_max()
    print(f"Task ID: {task.task_id}, Priority: {task.priority}, Arrival Time: {task.arrival_time}, Deadline: {task.deadline}")

Testing in Online Compilers

You can run both Heapsort and Priority Queue implementations directly in any online Python compiler such as:

Replit

Programiz

OnlineGDB

Simply paste the code into the editor and run it.

Summary of Findings

Heapsort provides efficient O(n log n) time complexity for sorting and is a reliable choice when predictable performance is important. It is particularly useful for scenarios where worst-case time complexity matters, such as real-time systems.

Priority Queue offers an efficient way to manage tasks with different priorities. Using a binary heap ensures that insertions and extractions of tasks are performed in logarithmic time, making it ideal for task scheduling and priority management in real-world applications.

Conclusion

This project helped me understand how heap data structures work and how they can be applied to solve real-world problems, such as efficient sorting and managing tasks based on priority. I also analyzed the time complexities and compared them with other sorting algorithms, such as Quicksort and Merge Sort. The priority queue implementation showed how heaps can be used effectively for managing tasks with varying levels of priority, which can be applied in areas like process scheduling in operating systems.
