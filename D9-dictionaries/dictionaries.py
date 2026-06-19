# Read the size of each family group (K)
k = int(input())

# Read the unordered list of room numbers and convert them to integers
room_numbers = list(map(int, input().split()))

# Create a unique set of room numbers
unique_rooms = set(room_numbers)

# Apply the mathematical formula to find the Captain's room
# (Sum of unique rooms multiplied by K) - (Sum of all rooms in the list)
# The difference must be divided by (K - 1) to isolate the unique number.
captains_room = (sum(unique_rooms) * k - sum(room_numbers)) // (k - 1)

# Output the result
print(captains_room)
