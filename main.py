import threading
import random

# Constraints

# 1. There are only n slots inside the fitting room of a department store. 
#    Thus, there can only be at most n persons inside the fitting room at a time.

# 2. There cannot be a mix of blue and green in the fitting room at the same time.
#    Thus, there can only be at most n blue threads or at most n green threads inside
#    the fitting room at a time.

# 3. The solution should not result in deadlock.

# 4. The solution should not result in starvation. For example, blue threads cannot 
#    forever be blocked from entering the fitting room if green threads are lining up to enter as well.

# Task: Coordinate between blue and green threads.

VERBOSE = True

n_prompt = ""
b_prompt = ""
g_prompt = ""

if VERBOSE:
    print("Process Synchronization Project for CSOPESY")
    print("Input the following: ")
    print("     n - the number of slots inside the fitting room")
    print("     b - number of blue threads")
    print("     g - number of green threads")
    print("----------------------------------------------")

    n_prompt = "n: "
    b_prompt = "b: "
    g_prompt = "g: "

n_slots = input(n_prompt)
b_threads = input(b_prompt)
g_threads = input(g_prompt)

n_slots = int(n_slots)
b_threads = int(b_threads)
g_threads = int(g_threads)

# Semaphores
n_sem = threading.Semaphore(n_slots)
b_sem = threading.Semaphore(n_slots)
g_sem = threading.Semaphore(n_slots)

threads: list[threading.Thread] = []

def enter_fitting_room(thread_id, color):
    """This enters a thread into the fitting room.

    Args:
        thread_id (int): id of the thread
        color (string): type of thread (blue or green)
    """
    pass

def exit_fitting_room(thread_id, color):
    """This exits a thread from the fitting room.

    Args:
        thread_id (int): id of the thread
        color (string): type of thread (blue or green)
    """
    pass

def create_thread(color, sleep=0):
    """This constructs a thread that will enter the fitting room.

    Args:
        color (string): type of thread (blue or green)
        sleep (int, optional): Changes the time the thread sleeps. Defaults to 0.
    
    Returns:
        thread: the thread that will enter the fitting room
    """
    new_thread = threading.Thread(target=run_thread, args=(len(threads), color))
    return new_thread
    
def run_thread(thread_id, color):
    """This runs the thread.

    Args:
        thread_id (int): id of the thread
        color (string): type of thread (blue or green)
    """
    enter_fitting_room(thread_id, color)
    exit_fitting_room(thread_id, color)

def simulate_fitting_room(n, b, g, random=None):
    """This simulates the fitting room.

    Args:
        n (int): number of slots inside the fitting room
        b (int): number of blue threads
        g (int): number of green threads
        random (int): seed for randomizing how the threads enter
    """
    random.seed(random)

    # Randomly create threads based on the seed
    # and the number of blue and green threads
    total_threads = b + g
    added_blue = 0
    added_green = 0

    for i in range(total_threads):
        if added_blue == b:
            threads.append(create_thread("green"))
            added_green += 1
        elif added_green == g:
            threads.append(create_thread("blue"))
            added_blue += 1
        else:
            if random.randint(0, 1) == 0:
                threads.append(create_thread("blue"))
                added_blue += 1
            else:
                threads.append(create_thread("green"))
                added_green += 1

    pass


if __name__ == "__main__":
    simulate_fitting_room(n_slots, b_threads, g_threads, random=11)