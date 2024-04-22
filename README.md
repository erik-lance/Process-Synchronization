# Process-Synchronization
Project 2 requirement for CSOPESY (Operating Systems)

## Instructions
Create a solution that will manage the number of people inside a department store fitting room. Here are some constraints:
- There are only n slots inside the fitting room of a department store. Thus, there can only be at most n persons inside the fitting room at a time.
- There cannot be a mix of blue and green in the fitting room at the same time. Thus, there can only be at most n blue threads or at most n green threads inside the fitting room at a time.
- The solution should not result in deadlock.
- The solution should not result in starvation. For example, blue threads cannot forever be blocked from entering the fitting room if green threads are lining up to enter as well.

**Task: Coordinate between blue and green threads.**

## Input
The program accepts three inputs from the user.

* n – the number of slots inside the fitting room
* b – number of blue threads
* g – number of green threads

## Output
The output of the program should be a simulation that includes the following:

* When a blue thread is the first to enter an empty fitting room, the thread should print the string “Blue only.”
* When a green thread is the first to enter an empty fitting room, the thread should print the string “Green only.”
* When a thread enters the fitting room, the thread should print its thread ID and color (i.e., blue or green).
* When a thread is the last to exit the fitting room, the thread should print the string “Empty fitting room.”
