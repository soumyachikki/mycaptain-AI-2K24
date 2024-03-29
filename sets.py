# -*- coding: utf-8 -*-
"""sets

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VfXrKOC15pj7z_uVMxpb-Eev974CHS_e
"""

# Define two sets
E = {8,0,6,2,4}
N = {2,4,1,3,5}

# Perform set operations
union_result = E.union(N)
intersection_result = E.intersection(N)
difference_result = E.difference(N)
symmetric_difference_result = E.symmetric_difference(N)

# Print the results
print(f"Union of E and N is {union_result}")
print(f"Intersection of E and N is {intersection_result}")
print(f"Difference of E and N is {difference_result}")
print(f"Symmetric difference of E and N is {symmetric_difference_result}")