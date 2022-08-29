#Reverse the list below in-place using an in-place algorithm.
#For extra credit: Reverse the strings at the same time.
#words = ['this' , 'is', 'a', 'sentence', '.']
words = ['this' , 'is', 'a', 'sentence', '.']
def reverse(list):
    list.reverse()
    print(list)
#reverse(words)



def disct():
    a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
    result = {}
    def wordCount(x):
        for x in x.lower().split():
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
        return result
    wordCount(a_text)
    sorted_string = dict(sorted(result.items(), key=lambda item:item[0]))
    print(sorted_string)

#disct()


# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

nums_list = [10,23,45,70,11,15]
target = 70
def linear(list, value):
    for x in range(len(list)):
        if list[x] == value:
            print(f"{value} found in index number {x}")
            return True 
    return -1

#result = linear(nums_list,target)
#print(result)    

# time complexity is O(n) cause it take n time to find the value 