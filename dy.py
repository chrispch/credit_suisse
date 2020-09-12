# setup (dynamic programming):
# array where indices represent the target sum
# contains an array of solutions (empty array means no soln)
# finding solutions for a given target sum (recursion):
# 1) check if target smaller than all values in given set; if
# so, no solution exists, return [None] to show that target sum has
# been checked and no solution exists
# furthermore, check if target is larger than sum of all values in given set, if
# so, no solution exists (ditto above)
# 2) check if exact match to target exists in given set, if so
# shortest solution is already reached
# 3) else, means that target is larger than all of values in given
# set, and requires multiple levels of summing (recursion)
# hence, add the largest value in given set (attempt at smallest
# solution), and find shortest solution for memory[target - largest_value]
# 4) if no solution exists, try again with the next largest value
# in given set

# assumptions:
# - more than one possible solution; but only one solution is expected to be returned
# - smallest set of indices of numbers refers to the smallest number of items in the set, not the numerical sum
# of the indices in the set (ie. [10, 11] is smaller than [1, 2, 3], [1,2] and [3,4] and of equivalent size)
# - all numbers in the given list are greater than or equal to zero

# limits:
# - computer does not run out of memory to store dynamic programming sub-solutions
# - as data structure used relies on using indices to represent target sum, negative numbers are not supported
#   - supporting negative numbers will require a switch to dictionaries for data structure

class find_smallest_combi:

    # Prepares input for subsequent processing
    def prep_input(self, target, input_list):
        # remove any numbers which are already bigger than the target
        return list(filter(lambda x: x <= target, input_list))

    # Checks
    def is_equal_to_target(self, target, input_list):
        # If there are any numbers equal to the target, solution is already found
        filtered = list(filter(lambda x: x == target, input_list))
        if len(filtered) > 0:
            return [filtered[0]]
        return []

    def is_target_too_small(self, target, input_list):
        # If there are no numbers in the input list that are less than the target, no solution is possible
        return len(list(filter(lambda x: x <= target, input_list))) == 0

    def is_target_too_big(self, target, input_list):
        # If target is larger than the sum of all numbers in the input list, no solution is possible
        return sum(input_list) < target

    # Recursion

    # get shortest solution for given target
    def solve(self, target, input_list):
        print("attempting to solve: " + str(target))
        # print(self.memory)
        # (1) check if solution exists
        if not self.is_target_too_big(target, input_list) and not self.is_target_too_small(target, input_list):
            # (2) check for exact match
            if self.is_equal_to_target(target, input_list) != []:
                print("there is a value in input list that is equal to target")
                # save solution to memory if one exists
                self.memory[target] = self.is_equal_to_target(target, input_list)
            else: 
                # (3) attempt to find a solution
                for value in input_list:
                    print("iterating through possible sub-solutions to find best solution for "
                          + str(target))
                    new_target = target - value
                    if new_target > 0:
                        print("attempting " + str(value) + "+" + str(new_target))
                        if self.memory[new_target] == []:
                            # attempt to solve sub-solution if not attempted before
                            sub_list = input_list.copy()
                            sub_list.remove(value)
                            self.solve(target - value, sub_list)
                        if self.memory[new_target] != None:
                            # if sub-solution exists, solution is found; 
                            # save if it is a better solution
                            print("sub-solution already exists for " + str(new_target))
                            print(self.memory[new_target])
                            save = self.memory[new_target].copy()
                            save.append(value)
                            if self.memory[target] == [] or self.memory[target] == None:
                                print("solution found for " + str(target))
                                print(save)
                                self.memory[target] = save
                            elif len(self.memory[target]) > len(save):
                                print("solution found for " + str(target))
                                print(save)
                                self.memory[target] = save
                        else:
                            print("the sub-solution " + str(value) 
                            + "+" + str(new_target) + " does not exist for " + str(target))
                    else:
                        print("invalid. new target is negative")
                if self.memory[target] == None:        
                    # if no sub-solutions exist, no solutions exist
                    print("no solution exists for: " + str(target) + " because no sub-solutions exist")
            
                return
        else:
            # if no solution exists, save to memory and return
            print("no solution exists for: " + str(target))
            self.memory[target] = None
            return

    # Helper functions
    def convert_values_to_indices(self, input_list, original_list):
        converted = []
        for i in range(len(original_list)):
            if original_list[i] in input_list:
                converted.append(original_list.index(original_list[i]))
                # necessary if there are duplicate values as .index() 
                # function only returns the first index of found value
                original_list[i] = None 
        return converted

    # Gets smallest combi when class instance is initialized
    def __init__(self, target, input_list):
        original_list = input_list
        # prepare input
        input_list = self.prep_input(target, input_list)
  
        # setup dynamic programming
        # memory will be target + 1 elements long instead for convenience when accessing
        # indices (memory[0] is not used)
        self.memory = [[]] * (target + 1) 
        self.solve(target, input_list)
        answer = self.memory[target]
        print(self.memory)
        if answer == None:
            print("There is no solution")
        elif answer == []:
            print("An error has occurred")
        else:
            print("The solution is: " 
                + str(self.convert_values_to_indices(answer, original_list)))
                
if __name__ == "__main__":
    print("main")
    input_list = [0, 1, 1, 2, 6, 3, 17, 82, 23, 234]
    target = 40
    soln = find_smallest_combi(target, input_list)
    print(soln)
