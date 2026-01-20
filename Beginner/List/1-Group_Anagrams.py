words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = {}

for i in words:
    key = "".join(sorted(i))    # sort letters
    if key not in result:
        result[key] = []
    result[key].append(i)

print(list(result.values()))
