#include <bits/stdc++.h>
using namespace std;

// Method to determine pager faults using FIFO
int getPageFaults(int pages[], int n, int frames)
{
    // To denote the current page set, we use an unordered_set.
    // It will help to have a quick check
    // The availability of the page in the set.

    unordered_set <int> set;
    // The code will store the pages in FIFO technique
    queue <int> indexes;
    
    // Stating from the first page
    int countPageFaults = 0;

    for (int i=0; i < n; i++)
    {
        // Checking the capacity to hold more pages
        if (set.size() < frames)
        {
            // if the page is absent, insert it into the set
            // the condition represents page fault
            if (set.find(pages[i])==set.end())
            {
                set.insert(pages[i]);
                // increment the conter for page fault
                countPageFaults++;
            
                // Push the current page into the queue
                indexes.push(pages[i]);
            }
        }

    // If the queue is full, we need to remove one page through FIFO
    // The topmost page from the queue will be removed
    // Now insert the current page to meet the demand
        else
        {
            // Check if the page in demand is not already present in the queue
            if (set.find(pages[i]) == set.end())
            {
                // Remove the first page from the queue
                int val = indexes.front();
                indexes.pop();
                
                // Pop the index page
                set.erase(val);
                
                // Push the current page in the queue
                set.insert(pages[i]);
                indexes.push(pages[i]);
                
                // Increment page faults
                countPageFaults++;
            }
        }
    }

    return countPageFaults;
}

// Driver code
int main()
{
    int pages[] = {4, 1, 2, 4, 5};
    int n = sizeof(pages)/sizeof(pages[0]);
    int frames = 4;

    cout << "Page Faults: " << getPageFaults(pages, n, frames);

    return 0;
}
