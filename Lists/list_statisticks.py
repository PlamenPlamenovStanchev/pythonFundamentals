number = int(input())
positives = []
negatives = []
for current_number in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)} Sum of negatives: {sum(negatives)}")