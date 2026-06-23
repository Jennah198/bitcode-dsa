n = int(input())
stamps = set()

for _ in range(n):
    stamps.add(input().strip())
    # input().strip() reads a line of text from the user and removes any accidental spaces at the beginning and the end

print(len(stamps))

# In-Place Methods vs. Returning a Copy in Python

# 1. In-Place Modification (Mutable Objects)
# -->Definition: Changes the existing data directly in memory without creating a new object.
# -->Return Value: Always returns None.Example: set.add(), list.append(), list.sort().
# -->Risk: Assigning the result to a variable (e.g., x = x.append(1)) destroys your data because the variable becomes None.

# 2. Returning a Copy (Immutable Objects)
# -->Definition: Leaves the original data untouched and creates a brand-new object with the modifications.
# -->Return Value: Returns the newly created data.
# -->Example: string.replace(), string.upper(), tuple.

# 3. Summary Rule
# If a Python method changes the original object directly, it returns nothing (None). If it leaves the original object alone, it returns a new copy.