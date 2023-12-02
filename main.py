import threading
import random
import time

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

rng = random
rng.seed(11)

n_ctr = 0

# Mutex Lock
mutex = threading.Lock()
bg_mutex = threading.Lock()

# Semaphores
b_sem = threading.Semaphore(n_slots)
g_sem = threading.Semaphore(n_slots)

waiting_sem = threading.Semaphore(1)

is_blue_first = False

threads: list[threading.Thread] = []

def enter_fitting_room(thread_id, color):
    """This enters a thread into the fitting room.

    Args:
        thread_id (int): id of the thread
        color (string): type of thread (blue or green)
    """
    string_prompt = f"Thread {thread_id} ({color}) enters the fitting room."
    
    global n_ctr
    global g_threads
    global b_threads

    failsafe = 5
    i = 0
    
    # Start of critical section
    mutex.acquire()

    try:
        # If the opposite color is the first to enter
        if not is_empty():
            if color == "blue":
                mutex.release()
                # Wait until green is empty
                while(g_sem._value != n_slots):
                    print("g_sem._value ", g_sem._value, " != ", n_slots)
                    i+=1
                    if i == failsafe: break
                    pass
                pass
                print(string_prompt)
                b_sem.acquire()
            else:
                mutex.release()
                # Wait until blue is empty
                while(b_sem._value != n_slots):
                    print("b_sem._value ", b_sem._value, " != ", n_slots)
                    i+=1
                    if i == failsafe: break
                    pass
                pass
                print(string_prompt)
                g_sem.acquire()
        else:
            print(f"{color.capitalize()} only.")
            print(string_prompt)
            # n_ctr += 1

            if color == "blue":
                b_sem.acquire()
            else:
                g_sem.acquire()
    except Exception as e:
        print("Error: ", thread_id)
    mutex.release()

def is_empty():
    return b_sem._value == n_slots and g_sem._value == n_slots

def exit_fitting_room(thread_id, color):
    """This exits a thread from the fitting room.

    Args:
        thread_id (int): id of the thread
        color (string): type of thread (blue or green)
    """
    string_prompt = f"Thread {thread_id} ({color}) exits the fitting room."
    print(string_prompt)

    if color == "blue":
        b_sem.release()
    else:
        g_sem.release()
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
    print("Thread: ", thread_id, " - ", color)
    enter_fitting_room(thread_id, color)
    time.sleep(random.uniform(0,3))
    exit_fitting_room(thread_id, color)

def simulate_fitting_room(n, b, g, random=None):
    """This simulates the fitting room.

    Args:
        n (int): number of slots inside the fitting room
        b (int): number of blue threads
        g (int): number of green threads
        random (int): seed for randomizing how the threads enter
    """

    for i in range(b):
        threads.append(create_thread("blue"))

    for i in range(g):
        threads.append(create_thread("green"))

    rng.shuffle(threads)  
    
    for t in threads: t.start()
    for t in threads: t.join()


if __name__ == "__main__":
    simulate_fitting_room(n_slots, b_threads, g_threads, random=11)