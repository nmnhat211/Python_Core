#Add & append
a = [70, 20, 30, 40, 50, 60, 60]
dup_items = set()
uniq_items = []
for i in a:
    if i not in dup_items:
        uniq_items.append(i)
        dup_items.add(i)
print(uniq_items)
print(dup_items)
