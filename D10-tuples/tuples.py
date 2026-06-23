# hash(object, /)
# Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))