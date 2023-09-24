class Directory:
  def __init__(self, parent, name):
    self.parent = parent
    self.child = []
    self.name = name
    self.files = []
    self.size = 0

  def create_sizes(self):
    self.size = sum([file.size for file in self.files]) + sum([directory.create_sizes() for directory in self.child])
    return self.size

  def get_sizes(self):
    self.create_sizes()
    sizes = [self.size]
    for directory in self.child:
      sizes += directory.get_sizes()
    return sizes
class File:

  def __init__(self, size, name, location):
    self.size = size
    self.name = name
    self.location = location


input = open("input.txt")
text = input.read().split("\n")

root = Directory(None, "/")
current = root

for x in range(len(text)):
  command = text[x].split()
  if command[0] == "$":
    if command[1] == "cd":
      if command[2] != '..':
        for i in current.child:
          if i.name == command[2]:
            current = i
      elif command[2] == "/":
        current = root
      else:
        current = current.parent

  elif command[0] != "dir":
    new_file = File(int(command[0]), command[1], current)
    current.files.append(new_file)
  else:
    new_dir = Directory(current, command[1])
    current.child.append(new_dir)

sizes = root.get_sizes()

print(sum([size for size in sorted(sizes) if size<= 100000]))
free_space = 70000000 - sorted(sizes)[-1]
print([size for size in sorted(sizes) if size >= (30000000 - free_space)][0])
