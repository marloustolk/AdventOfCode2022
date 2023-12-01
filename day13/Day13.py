pairs = open("input13.txt", "r").read().split("\n\n")

def has_list(value):
   return value.find("[")

def get_list(value):
   values = value.split("[")[1].split("]")[0]
   print "value " + str(values.split(",")) + " " + str(len(values))
   if len(values) < 3:
      return []
   else:
      return map(lambda x: int(x), value.split("[")[1].split("]")[0].split(","))

for pair in pairs:
   [first, second] = pair.split("\n")
   print get_list(first)
