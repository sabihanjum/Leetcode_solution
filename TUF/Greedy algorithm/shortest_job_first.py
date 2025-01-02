"""Geek is a software engineer. He is assigned with the task of calculating average waiting time of all the processes by following shortest job first policy.

The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next.

Given an array of integers bt of size n. Array bt denotes the burst time of each process. Calculate the average waiting time of all the processes and return the nearest integer which is smaller or equal to the output.

Note: Consider all process are available at time 0."""

class Solution:
    def solve(self, bt):
        # Initialize total time (t) and total waiting time (wt) to 0
        t, wt = 0, 0

        # Sort the burst times in ascending order to minimize average waiting time
        bt.sort()

        # Iterate through each burst time in the sorted list
        for time in bt:
            wt += t  # Add the accumulated total time to the waiting time
            t += time  # Update the total time by adding the current burst time

        # Calculate and return the average waiting time (floor division by number of processes)
        return wt // len(bt)


