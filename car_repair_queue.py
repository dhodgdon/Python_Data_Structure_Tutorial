import time
import random

class Car_Repair_Queue:
    def __init__(self):
        self.queue = []
    
    def __len__(self):
        return len(self.queue)
    
    def __iter__(self):
        yield from self.queue

    def enqueue(self, value):
        print(f"{value} was added")
        self.queue.append(value)

    def dequeue(self):
        start_time = time.time()
        print(f"Servicing {self.queue[0]}'s car")
        time.sleep(random.randrange(1,4))
        if time.time() - start_time >= 2:
            print(f"{self.queue[0]} received the discount")
        else:
            print(f"{self.queue[0]} did not receive the discount")
        return self.queue.pop(0)
    
car_repair_shop_queue = Car_Repair_Queue()

car_repair_shop_queue.enqueue("Customer 1")
car_repair_shop_queue.enqueue("Customer 2")
car_repair_shop_queue.enqueue("Customer 3")
car_repair_shop_queue.enqueue("Customer 4")
car_repair_shop_queue.enqueue("Customer 5")
car_repair_shop_queue.enqueue("Customer 6")
car_repair_shop_queue.enqueue("Customer 7")
car_repair_shop_queue.enqueue("Customer 8")
car_repair_shop_queue.enqueue("Customer 9")
car_repair_shop_queue.enqueue("Customer 10")
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
car_repair_shop_queue.dequeue()
