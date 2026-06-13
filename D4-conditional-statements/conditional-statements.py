import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n>=2 or n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n>=6 or n <= 20:
    print("Weird")
elif n % 2 == 0 and n <= 20:
    print("Not Weird")


# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     n = int(input().strip())
    
#     # Condition 1: If n is odd
#     if n % 2 != 0:
#         print("Weird")
        
#     # Condition 2: If n is even and in the inclusive range of 2 to 5
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
        
#     # Condition 3: If n is even and in the inclusive range of 6 to 20
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
        
#     # Condition 4: If n is even and greater than 20
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")
