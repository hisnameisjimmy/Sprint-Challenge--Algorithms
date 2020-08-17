#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear, O(n). This is just a single while loop, with no nested loops. All the additional N's inside the while loop condition don't have a legible impact on time/space complexity. So the input size proportionally increases the speed/slowness of the algorithm.

b) Nested loops! Quadratic time: O(n^2). This is inception. The speed of the algorithm, slows down dramatically based on input size.

c) This is a constant, 0(1). The size of the input has no affect on space or speed. 

## Exercise II

def egg_dropper(n):
    # n = number of floors
    # f = breaking point floor
    # iterate through all the floors, starting from the lowest, and drop an egg until it breaks, once it breaks, return that value
    # Runtime complexity would be Linear, 0(n)

