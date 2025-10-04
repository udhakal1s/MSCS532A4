# Umesh Dhakal
# MSCS532A4
# Priority Queue implementation using Max-Heap

import heapq

class Task:
    def __init__(self, taskID, priority):
        self.taskID = taskID
        self.priority = priority
    def __lt__(self, other):   # for max-heap, invert comparison
        return self.priority > other.priority
    def __repr__(self):
        return f"Task(ID={self.taskID}, Priority={self.priority})"

# Priority Queue
class PriorityQueue:
    def __init__(self):
        self.arraylist = []
    # adding new new task
    def insert(self, task):
        heapq.heappush(self.arraylist, task)
 
    def extract_max(self):
        return heapq.heappop(self.arraylist) if self.arraylist else None
    # increase priority of an existing task
    def increase_key(self, taskID, newpriority):
        for task in self.arraylist:
            if task.taskID == taskID:
                task.priority = newpriority
                heapq.heapify(self.arraylist)
                break
  
    def is_empty(self):
        return len(self.arraylist) == 0

pq = PriorityQueue()
pq.insert(Task(1, 3))
pq.insert(Task(2, 5))
pq.insert(Task(3, 1))
pq.insert(Task(4, 4))

print("priority queue:", pq.arraylist)
print("extracting max :", pq.extract_max())
print("queue after extrcting max:", pq.arraylist)
pq.increase_key(3, 6)
print("queue after increasing priority of task 3:", pq.arraylist)

