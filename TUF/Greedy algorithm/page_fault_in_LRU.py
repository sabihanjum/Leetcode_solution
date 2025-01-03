"""In operating systems that use paging for memory management, page replacement algorithm is needed to decide which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page.

Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults using Least Recently Used (LRU) Algorithm. 

Note:- Before solving this example revising the OS LRU cache mechanism is recommended."""

class Solution:
    def pageFaults(self, N, C, pages):
        # Initialize an empty list to represent the cache
        arr = []
        
        # Counter to keep track of page faults
        page_fault = 0
        
        # Iterate through each page request
        for i in pages:
            # If the page is not in the cache, it's a page fault
            if i not in arr:
                # If the cache is full (size equals capacity C)
                if len(arr) == C:
                    # Remove the least recently used (first) page
                    arr.pop(0)
                
                # Add the new page to the cache
                arr.append(i)
                
                # Increment the page fault counter
                page_fault += 1
            else:
                # If the page is already in the cache (hit),
                # remove it to update its position as most recently used
                arr.remove(i)
                arr.append(i)
        
        # Return the total number of page faults
        return page_fault
