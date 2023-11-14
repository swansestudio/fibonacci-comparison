# Fibonacci Optimization Comparison

## History

The Fibonacci numbers were first described in Indian mathematics, as early as **200 BC** in work by Pingala on enumerating possible patterns of *Sanskrit poetry* formed from syllables of two lengths. They were named after the Italian mathematician Leonardo of Pisa, also known as Fibonacci, who introduced the sequence to Western European mathematics in his 1202 book Liber Abaci.

## Contents

The following code snippets in JavaScript and Python demonstrate the performance difference between a standard recursive Fibonacci calculation and an optimized version using memoization (caching).


1. **Recursive Fibonacci**: A simple recursive function to calculate the Fibonacci sequence. While this approach is straightforward, it has a high computational cost for larger input values (> 40-50).

2. **Memoized Fibonacci**: An optimized version of the recursive Fibonacci function that utilizes a cache to store previously calculated values, significantly reducing the computational time for larger input values.

These examples serve as a practical demonstration of how memoization can optimize the performance of algorithms that involve repeated computations. By comparing the execution times of both functions, one can clearly see the benefits of using memoization in recursive algorithms.

In addition, by comparing the execution times between JavaScript(on Node.js) and Python, we can observe the differences in performance between these two languages when executing greedy algorithms.

## Results

The following results were obtained from running the code snippets:

**JavaScript Execution Times**:
- Recursive Fibonacci of 40: 1.492 sec
- Memoized Fibonacci: 0.245 ms

**Python Execution Times**:
- Recursive Fibonacci: 45.542296 sec
- Memoized Fibonacci: 0.043 ms


## Usage

To run the code, simply copy the contents of the file into your JavaScript or Python environment and execute it. The code will output the 50th Fibonacci number and the time taken to compute it for both the recursive and memoized versions.


