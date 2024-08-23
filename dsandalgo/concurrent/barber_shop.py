import threading
import time
import random
import queue

class BarberShop:
    def __init__(self, num_chairs):
        self.num_chairs = num_chairs
        self.waiting_customers = queue.Queue(num_chairs)
        self.barber_ready = threading.Condition()

    def getHairCut(self, customer_id):
        print(f"Customer {customer_id} is getting a haircut.")
        time.sleep(random.uniform(0.5, 1.0))  # Simulate the time it takes to get a haircut

    def cutHair(self):
        while True:
            with self.barber_ready:
                if self.waiting_customers.empty():
                    print("Barber is sleeping...")
                    self.barber_ready.wait()  # Barber sleeps if no customers are waiting
                customer_id = self.waiting_customers.get()

            print("Barber is cutting hair.")
            self.getHairCut(customer_id)  # Simulate haircut

            time.sleep(random.uniform(1.0, 2.0))  # Simulate the time it takes to cut hair

    def customer_arrives(self, customer_id):
        if not self.waiting_customers.full():
            self.waiting_customers.put(customer_id)
            print(f"Customer {customer_id} is waiting. ({self.waiting_customers.qsize()} waiting)")

            with self.barber_ready:
                self.barber_ready.notify_all()  # Wake up the barber if necessary

        else:
            print(f"Customer {customer_id} leaves the shop because it is full.")

def barber_thread(brabeshop):
    brabeshop.cutHair()

def customer_thread(brabeshop, customer_id):
    brabeshop.customer_arrives(customer_id)


def main():
    num_chairs = 3
    barbershop = BarberShop(num_chairs)

    #Start the braber thread
    threading.Thread(target=barber_thread, args=(barbershop,)).start()

    #Start customer thread
    for i in range(10):
        threading.Thread(target=customer_thread, args=(barbershop,i)).start()
        time.sleep(random.uniform(0.1,0.5)) #Customer arrive at random intervals

if __name__ == "__main__":
    main()