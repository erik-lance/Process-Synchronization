import threading
import time
import random


class FittingRoom:
    def __init__(self, n):
        self.n = n
        self.room_sem = threading.BoundedSemaphore(n)
        self.current_color = None
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)

    def enter_room(self, thread_id, color):
        # Acquire the lock
        self.condition.acquire()

        # Wait for the room to be empty or for the current color to be the same as the thread's color
        while self.current_color is not None and self.current_color != color:
            self.condition.wait()

        # Release the lock
        self.condition.release()

        if self.room_sem._value == n:
            self.room_sem.acquire()
            print(f"{color.capitalize()} only.")
        else:
            self.room_sem.acquire()

        with self.mutex:
            if self.current_color is None or self.current_color == color:
                self.current_color = color
                print(
                    f"Thread {thread_id} ({self.current_color}) enters the fitting room."
                )
            else:
                print(
                    f"Thread {thread_id} ({color}) waits as the fitting room is occupied by {self.current_color}."
                )

    def exit_room(self, thread_id, color):
        with self.mutex:
            print(f"Thread {thread_id} ({color}) exits the fitting room.")
            self.room_sem.release()
            if self.is_empty():
                print("Empty fitting room.")
                self.current_color = None
                self.condition.notify(1)

    def is_empty(self):
        return self.room_sem._value == self.n


def simulate_fitting_room(n, b, g):
    fitting_room = FittingRoom(n)
    threads = []

    def run_thread(thread_id, color):
        fitting_room.enter_room(thread_id, color)
        # time.sleep(1)
        fitting_room.exit_room(thread_id, color)

    for i in range(b):
        thread = threading.Thread(target=run_thread, args=(i, "blue"))
        threads.append(thread)

    for i in range(g):
        thread = threading.Thread(target=run_thread, args=(i + b, "green"))
        threads.append(thread)

    random.shuffle(threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    n = int(input("Enter the number of slots inside the fitting room: "))
    b = int(input("Enter the number of blue threads: "))
    g = int(input("Enter the number of green threads: "))

    simulate_fitting_room(n, b, g)
