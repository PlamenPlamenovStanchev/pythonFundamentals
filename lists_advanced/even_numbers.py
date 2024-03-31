number_list = list(map(int, int(input().split(", "))))
found_indeces_or_no = map(lambda x: x if number_list[x] % 2 == 0 else "no", range(len(number_list)))
even_indeces = list(filter(lambda a: a != "no", found_indeces_or_no))
print(even_indeces)