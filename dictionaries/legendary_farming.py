legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
flag = True

while flag:
    input_line = input().split()

    for i in range(0, len(input_line), 2):
        quantity = int(input_line[i])
        material = input_line[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                key_materials[material] -= 250
                flag = False
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")

for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")