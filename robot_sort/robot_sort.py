

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # Understand
        # Is this just a damn bubble sort??
        # Code from previous bubble sort
        # swaps = True
        # while swaps:
        #     swaps = False
        #     for i in range(len(arr) - 1):
        #         cur_index = i
        #         next_index = i + 1
        #         if arr[cur_index] > arr[next_index]:
        #             arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
        #             swaps = True
        # Swaps could be the light
        
        # Start with a swap, because by default the item is None
        # This will make the current item 15 (in the test)
        # Turn the light on to indicate that we're running
        # While the light is running
        # if we can move right, move right
        # compare the current item (15) to the next item (41)
        # If the current item's value is greater, swap it with the next value, move forward
        # If the current item's value is less, then move forward
        # Start with
        # Current Item = None
        # Current Position = 0
        # Light is Off
        # self.swap_item()
        # self.move_right()
        # self.set_light_on()
        # After
        # current item = 15
        # current position is 1
        # light is on
        # while self.light_is_on():
        #     # In case this is the end, set the light off
        #     # If we can move right, or left, we'll turn it back on
        #     self.set_light_off()
        #     while self.can_move_right():
        #         # 15 compared to 41, this fails
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.move_right()
        #             self.set_light_on()
        #         # else succeeds, so we move right one position
        #         # We then hit the while loop again and we're still holding 15, but we've moved to the right
        #         else:
        #             self.move_right()
        #     # same same, but opposite direction
        #     while self.can_move_left():
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.move_left()
        #             self.set_light_on()
        #         else:
        #             self.move_left()

        # self.set_light_on()
        # # first swap to move from None to an actual number, or the first loop is dumb
        # self.swap_item()
        # while self.light_is_on():
        #     self.set_light_off()
        #     # Now the current item is 15
        #     print(f'Initial Item: {self._item}')
        #     while self.can_move_right():
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.move_right()
        #             print(f'Right Item: {self._item}')
        #             print(
        #                 f'Right Position & Value: {self._position} - {self._list[self._position]}')
        #             self.set_light_on()
        #         else:
        #             self.move_right()
        #             print(
        #                 f'Right Position & Value: {self._position} - {self._list[self._position]}')

        #     while self.can_move_left():
        #         print(f'Left Item: {self._item}')
        #         print(
        #             f'Left Position & Value: {self._position} - {self._list[self._position]}')
        #         if self.compare_item() == None:
        #             self.swap_item()
        #         else:
        #             self.move_left()
        # self.swap_item()
        # self.set_light_on()
        # print(f'Currently Held Item: {self._item}')
        # while self.light_is_on():
        #     self.set_light_off()
        #     while self.can_move_right():
        #         self.move_right()
        #         print(
        #             f'Currently Held Item: {self._item}')
        #         print(f'Right Position & Value: {self._position} - {self._list[self._position]}')
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.set_light_on()
        #     # Go to the beginning, the beginning is none
        #     print(f'Post Right Loop: {self._list}')
        #     while self.can_move_left():
        #         self.move_left()
        #         if self.compare_item() is None:
        #             self.move_right()
        #             self.swap_item()
        #             print(f'Currently Held Item: {self._item}')
        #             print(f'Left Position & Value: {self._position} - {self._list[self._position]}')
                    
        #     print(f'Post Left Loop: {self._list}')
        

        # To Start, Value is None, which is not a comparable value
        # Swap to get a starting value

        # self.set_light_on()
        # while self.light_is_on():
        #     self.set_light_off()
        #     while self.can_move_right():
        #         self.move_right()
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.set_light_on()
        #         print(f'Currently Held Item: {self._item}')
        #         # print(f'Right Position & Value: {self._position} - {self._list[self._position]}')
        #     while self.can_move_left():
        #         self.move_left()
        #         if self.compare_item() == None:
        #             self.swap_item()
        #             self.set_light_on()
        #         print(f'Currently Held Item: {self._item}')
        #         # print(f'Left Position & Value: {self._position} - {self._list[self._position]}')
        # if self.can_move_right():
        #     self.move_right()
        # else:
        #     self.set_light_off()

        
        # self.set_light_on()
        # while self.light_is_on():
        #     self.swap_item()
        #     self.set_light_off()
        #     while self.can_move_right():
        #         # print(f'Current Item: {self._item}')
        #         self.move_right()
        #         if self.compare_item() == -1:
        #             self.swap_item()
        #             self.set_light_on()
        #             # print(f'Current Item: {self._item} - Compared Item: {self._list[self._position]}')
        #     while self.can_move_left():
        #         self.move_left()
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.set_light_on()
        #         # print(f'Left Position: {self._position} - Left Value: {self._list[self._position]}')
        #     self.swap_item()
            # print(f'Final Position: {self._position} - Final Value: {self._list[self._position]}')

        # swap
        # move right
        # if item is greater, swap, and move right
        # hit the end
        # go back left, will be at position none
        # move right, swap
        # repeat step 3

        self.set_light_on()
        while self.light_is_on():
            print(f'Start: {self._list}')
            self.swap_item()
            self.set_light_off()
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()
            print(f'After Right: {self._list}')
            while self.can_move_left() and self.compare_item() is not None:
                self.move_left()
                if self.compare_item() is None:
                    self.swap_item()
                    self.set_light_on()
            if self.compare_item() is None and self.can_move_right() is False:
                self.swap_item()
            print(f'After Left: {self._list}')
            self.move_right()


        # how can I move the None around where this can make sense?
            
            


    # swaps = True
    # while swaps:
    #     swaps = False
    #     for i in range(len(arr) - 1):
    #         cur_index = i
    #         next_index = i + 1
    #         if arr[cur_index] > arr[next_index]:
    #             arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
    #             swaps = True
        
# Holding None
# [3, 1, 5]
# Swap
# Holding 3
# [None, 1, 5]
# Move right
# Compare
# Swap initially
# You get 

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    l = [9, 4, 3, 6, 2]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
