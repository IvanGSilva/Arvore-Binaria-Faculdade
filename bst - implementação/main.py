import random
from bst import Bst


def generateRandomList(length: int, min_value: int, max_value: int):
  return random.sample(range(min_value, max_value), length)

list = generateRandomList(20, 1, 99)

bst = Bst()

for i in list:
  bst.insertNode(i)

print("digraph g{ \n" + bst.showLinks() + "\n"
      "}")

print("\n"
"order\n")
print(bst.orderTraversal(bst.node))

print("\n"
      "------------------------------------------------------------------\n"
      "\n")

print("\n"
  "post order\n")
print(bst.postOrderTraversal(bst.node))

print("\n"
  "------------------------------------------------------------------\n"
  "\n")

print("\n"
  "pre order\n")
print(bst.preOrderTraversal(bst.node))

print(bst.deleteNode(30))

print(bst.findNode(30))