### 1. What is the base case of your reverse function?

If the length of the parameter is less than or equal to one, it will be reversed.


### 2. What is the base case of your is_palindrome?

The base case of the is_palindrome function is when the length of the string is 0 or 1 (len(s) <= 1). It returns True.

### 3. What happens if you remove the base case?

If you remove the base case, the function will keep calling itself without stopping. Eventually, Python will give a RecursionError because the maximum recursion depth is exceeded.
