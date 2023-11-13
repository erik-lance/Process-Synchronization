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


print("Input the following with spaces in between e.g.: 1 5 9")
print("n - the number of slots inside the fitting room")
print("b - number of blue threads")
print("g - number of green threads") 

n_slots, b_threads, g_threads = input().split()

n_slots = int(n_slots)
b_threads = int(b_threads)
g_threads = int(g_threads)

