# file_path = input()
#
# file_name = file_path.rstrip('\\', 1)
# file_name, file_extension = full_filename.split('.')
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")


file_path = input().split("\\")
filename_and_extension = file_path[-1]
filename, extension = filename_and_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
