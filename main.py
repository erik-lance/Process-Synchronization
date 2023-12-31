import threading
import time
import random


class FittingRoom:
    """
    Synchronization Technique:
    - Semaphores: Used a BoundedSemaphore (`self.room_sem`) to control access to the fitting room slots.
    - Mutex Lock: Implemented a mutex lock (`self.mutex`) to protect critical sections for atomic operations.
    - Condition Variable: Utilized a condition variable (`self.condition`) for conditional waiting and notification.
    - Thread Synchronization: Implemented waiting and notification mechanisms to coordinate thread access to the fitting room.

    Additional Notes:
    - Debugging prints are provided (commented) for better understanding of thread interactions.
    """

    def __init__(self, n):
        self.n = n
        self.room_sem = threading.BoundedSemaphore(n)
        self.current_color = None
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)

    def enter_room(self, thread_id, color):
        """Makes the thread enter the fitting room. If the room is empty, 
        it will acquire the room semaphore and set the current color. Else,
        logic is provided to make the thread wait for the fitting room to be empty
        again if the current color is not the same as the thread's color.

        Args:
            thread_id (_type_): _description_
            color (_type_): _description_
        """
        # Acquire the lock
        self.condition.acquire()

        # (Optional print) If the current color is not the same as the thread's color, wait for the room to be empty
        if self.current_color is not None and self.current_color != color:
            print(
                f"Thread {thread_id} ({color}) waits as the fitting room is occupied by {self.current_color}."
            )

        # Wait for the room to be empty or for the current color to be the same as the thread's color
        while self.current_color is not None and self.current_color != color:
            self.condition.wait()

        # Release the lock
        self.condition.release()

        # If the room is empty, acquire the room semaphore and set the current color
        if self.room_sem._value == n:
            self.room_sem.acquire()
            self.current_color = color
            print(f"{color.capitalize()} only.")
            # DEBUG
            # print(f"{color.capitalize()} ({thread_id}) enters. {self.room_sem._value} - FIRST TO ENTER")
        else:
            self.room_sem.acquire()
            # DEBUG
            # print(f"{color.capitalize()} ({thread_id}) enters. {self.room_sem._value}")

        with self.mutex:
            if self.current_color is None or self.current_color == color:
                print(
                    f"Thread {thread_id} ({self.current_color}) enters the fitting room."
                )

    def exit_room(self, thread_id, color):
        """Makes the thread exit the fitting room. If the room is empty, 
        it will notify all threads waiting for the fitting room to be empty.
        It also releases the room semaphore.

        Args:
            thread_id (int): number id of the thread
            color (string): color of the thread
        """
        with self.mutex:
            print(f"Thread {thread_id} ({color}) exits the fitting room.")
            self.room_sem.release()
            if self.is_empty():
                print("Empty fitting room.")
                self.current_color = None
                self.condition.notify_all()

    def is_empty(self):
        return self.room_sem._value == self.n


def simulate_fitting_room(n, b, g):
    """This simulates the fitting room problem. It will prepare the threads and shuffle them before starting them.
    It also provides a run thread function that simply enters then exits the room.

    Args:
        n (int): number of slots inside the fitting room
        b (int): number of blue threads
        g (int): number of green threads
    """
    fitting_room = FittingRoom(n)
    threads = []

    def run_thread(thread_id, color):
        fitting_room.enter_room(thread_id, color)
        # time.sleep(0.5) - Uncomment this line to see the effect of threads waiting, entering and exiting the fitting room in a more obvious way
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
    n, b, g = None, None, None

    n = input("Enter the number of slots inside the fitting room: ")
    b = input("Enter the number of blue threads: ")
    g = input("Enter the number of green threads: ")

    # Error Checking
    try:
        n = int(n)
        b = int(b)
        g = int(g)
    except ValueError:
        print("Invalid input. Please enter a valid integer. Stopping...")
        exit()

    simulate_fitting_room(n, b, g)
