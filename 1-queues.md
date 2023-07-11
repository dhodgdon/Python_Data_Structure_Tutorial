# Queues

Queues are all around us: standing in line at the grocery store, placing items on a conveyor belt, waiting for your meal at a restaurant. All of these scenarios have one thing in common - each of these involve people/items that are handled in the order in which they arrived/were received, AKA "first come, first served." (The way we say this when talking about data structures is "FIFO," or "First In, First Out.") In Python, we can use queues to do just that - handle items/tasks one at a time, in the order they have been given us. There are a variety of ways to implement queues in Python, but we will be using lists.

## Enqueue/Dequeue 

The two fundamental functions of a queue are `enqueue` and `dequeue`, which entail, respectively, adding an item to the back of the queue and removing an item from the front of the queue. We can use list methods to implement these functions:
 * `.append()` enqueues an item, adding it to the back of the queue
 * `.pop(0)` dequeues an item, removing it from the front of the queue

Here is a simple example of enqueuing three items to a queue and then dequeuing those three items.

```python
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
```

Here is the output from the above code (note that the order the items are dequeued is the same order they were enqueued, or in other words First In First Out):

```python
1
2
3
```

Understanding these functions allows us to utilize queues any time we encounter a software problem requiring items to be handled in a "first come, first served" manner.

## Queues to Prevent Race Conditions

Note: This section assumes that you already have a basic understanding of multiprocessing/multithreading and concurrency. 

Queues can be useful when working with multiple processes/threads to protect against race conditions and ensure data integrity.

Race conditions are when two processes/threads are trying to change data at the same time, resulting in data corruption. The following is a simple example of a race condition in real life:

Bob and Jane are married and handle finances together. At the beginning of the month, Jane realizes that rent has not been paid and opens her renter's online portal to pay it. The problem is that Bob realizes that rent has not been paid and gets on the portal at the same time without communicating with his wife. They pay the rent at the same time, both thinking that rent was due and end up paying double.

This is an example of the danger of race conditions (and not communicating with your spouse). Bob and Jane are like processes who both access data and change it at the same time, resulting in data corruption. Here is an example in programming:

 * Process 1 accesses the variable `age` (`age = 25`).
 * Process 1 is about to increment the variable, but before it can Process 2 accesses the same variable.
 * Process 2 also wants to increment the variable `age`, which is still equal to `25`.
 * Process 1 increments the variable to `age = 26`.
 * Process 2, which still thinks that `age = 25`, also increments the variable to `age = 26`.
 * The problem we have now is that we were expecting `age = 27`, but what we get back is `age = 26`.

One solution to this problem is creating a queue of processes that will allow each process to read and update the variable one at a time as they are dequeued. This way, we avoid all possibility of a race condition.

## Queue Performance

Here are the performance times for the main queue methods using lists in Python:

 * `enqueue` - O(1) performance to add an item to the back of the queue
 * `dequeue` - O(n) performance to remove an item from the front of the queue and update the indices of the rest of the items in the queue
 * `size` - O(1) performance to check the size of a queue
 * `empty` - O(1) performance to check the size of a queue (same as checking `size == 0`)

## Example - Game Night

Here is an example of a game night program using a queue. Each player arrives at the party one at a time and takes turns playing the game in the order they arrived. Each player then leaves the party in the order they arrived.

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def __len__(self):
        return len(self.queue)
    
    def __iter__(self):
        yield from self.queue

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

players = Queue()

players.enqueue('Bob')
players.enqueue('Nancy')
players.enqueue('Jeff')
players.enqueue('Jane')

for player in players:
    print(f"{player} just joined the game.")

print(f"There are {len(players)} players.")

print()

for player in players:
    print(f"It is {player}'s turn.")

print()

for i in range(len(players)):
    print(f"{players.dequeue()} left the game.")

print(f"There are {len(players)} players.")
```
Here are the results when we run the above:
```
Bob just joined the game.
Nancy just joined the game.
Jeff just joined the game.
Jane just joined the game.
There are 4 players.

It is Bob's turn.
It is Nancy's turn.
It is Jeff's turn.
It is Jane's turn.

Bob left the game.
Nancy left the game.
Jeff left the game.
Jane left the game.
There are 0 players.
```

## Problem to Solve : People Waiting at the Car Repair Shop

There is a line of 15 people at the car repair shop waiting for their cars to be repaired. The car shop has a policy that the customer gets a discount if they wait more than 20 minutes after they begin repairing the customer's car. Create a program simulating this car repair shop using a queue that will service each customer's car and then sleep for a random time between 1-3 seconds (each second represents 10 minutes). Display whether the customer received the discount before beginning to work on the next customer's car.

The example output of the program is shown below:
```
Customer 1 was added
Customer 2 was added
Customer 3 was added
Customer 4 was added
Customer 5 was added
Customer 6 was added
Customer 7 was added
Customer 8 was added
Customer 9 was added
Customer 10 was added
Servicing Customer 1's car
Customer 1 received the discount
Servicing Customer 2's car
Customer 2 received the discount
Servicing Customer 3's car
Customer 3 received the discount
Servicing Customer 4's car
Customer 4 received the discount
Servicing Customer 5's car
Customer 5 received the discount
Servicing Customer 6's car
Customer 6 did not receive the discount
Servicing Customer 7's car
Customer 7 did not receive the discount
Servicing Customer 8's car
Customer 8 received the discount
Servicing Customer 9's car
Customer 9 received the discount
Servicing Customer 10's car
Customer 10 received the discount
```

You can check your code with the solution here: [Solution](car_repair_queue.py)

[Back to Welcome Page](0-welcome.md)