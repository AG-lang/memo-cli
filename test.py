names = ["Alice", "BOB", "Charlie"]
search = "bob"

for i, name in enumerate(names, 1):
    if search.lower() == name.lower():
        print(f"第{i}个名字匹配成功：{name}")