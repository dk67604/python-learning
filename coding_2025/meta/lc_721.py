'''

✅ Time Complexity: O(N * M * log M)
Where:

N is the number of accounts

M is the average number of emails per account
O(N * M) for graph construction
+ O(V + E) for DFS traversal
+ O(M log M) for sorting
⇒ O(N * M + M log M)

✅ Space Complexity: O(N * M)
Graph storage (adjacency list): O(M)

Visited set: O(M)

Recursive DFS call stack: up to O(M) in worst case

Result storage: O(N * M)

'''

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accountList: List[List[str]]) -> List[List[str]]:
        """
        Merges accounts that share common emails using DFS traversal.
        
        :param accountList: List of accounts, where each account consists of a name 
                            and multiple email addresses.
        :return: Merged list of accounts with unique emails sorted alphabetically.
        """
        
        # Step 1: Build an adjacency list (Graph representation)
        adjacent = defaultdict(list)  # Stores connections between emails

        for account in accountList:
            accountFirstEmail = account[1]  # First email in the account
            for j in range(2, len(account)):  # Connect all emails in the account
                accountEmail = account[j]
                # Since emails are bidirectionally connected, add edges in both directions
                adjacent[accountFirstEmail].append(accountEmail)
                adjacent[accountEmail].append(accountFirstEmail)

        # Step 2: Use DFS to find connected components (merged accounts)
        mergedAccounts = []  # Stores the final merged accounts
        visited = set()  # Keeps track of visited emails

        def dfs(mergedAccount: List[str], email: str):
            """
            Depth-First Search (DFS) to collect all connected emails.
            
            :param mergedAccount: The list that stores all emails belonging to one merged account
            :param email: The current email being processed in DFS
            """
            mergedAccount.append(email)  # Add the email to the current account
            visited.add(email)  # Mark email as visited
            
            # Explore all neighboring emails (connected emails)
            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(mergedAccount, neighbor)  # Recursively visit connected emails

        # Step 3: Process each account and merge connected emails
        for account in accountList:
            accountName = account[0]  # Extract account holder's name
            accountFirstEmail = account[1]  # Get the first email in the account

            # If the first email hasn't been visited, start DFS from it
            if accountFirstEmail not in visited:
                mergedAccount = [accountName]  # Start with the account name
                dfs(mergedAccount, accountFirstEmail)  # DFS collects all emails
                mergedAccount[1:] = sorted(mergedAccount[1:])  # Sort emails
                mergedAccounts.append(mergedAccount)  # Store the merged account

        return mergedAccounts
