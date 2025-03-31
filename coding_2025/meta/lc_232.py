'''
http://leetcode.com/problems/implement-queue-using-stacks/description/
🔧 push(x)
Time Complexity: O(1)

Why: Adding an element to the end of a Python list (append) takes constant time.

🔧 pop()
Time Complexity: Amortized O(1)
Worst-case: O(n)

Why:

If output stack is not empty, popping from it is O(1).

If output is empty, all elements from input are moved to output, which takes O(n) time only once for every n pushes.

Each element is moved from input to output only once, so across n operations, the total cost is O(n), resulting in amortized O(1) per operation.

🔧 peek()
Time Complexity: Amortized O(1)
Worst-case: O(n)

Why: Same reason as pop(). The transfer from input to output only happens once per element. Peeking the last element of a list is O(1).

🔧 empty()
Time Complexity: O(1)

Why: Simply checks if both stacks are empty using a logical and on two list checks.


'''

class MyQueue:

    def __init__(self):
        # Two stacks:
        # 'input' is used for enqueue (push) operations
        # 'output' is used for dequeue (pop/peek) operations
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        # Always push to the input stack
        self.input.append(x)

    def pop(self) -> int:
        # Ensure the output stack has the correct order
        self.peek()
        # Pop from the output stack (front of the queue)
        return self.output.pop()

    def peek(self) -> int:
        # If output stack is empty, move all elements from input to output
        # This reverses the order, making the oldest element accessible on top of output
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        # Return the element at the front of the queue
        return self.output[-1]

    def empty(self) -> bool:
        # Queue is empty only when both stacks are empty
        return not self.output and not self.input
