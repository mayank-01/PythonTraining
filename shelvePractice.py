import shelve

# Writing
file = shelve.open("shelf_file")
arr = ["Abcd", "efgh", "ijkl"]
file['arr'] = arr
file.close()

# Reading
file = shelve.open("shelf_file")
print(file['arr'])
file.close()

# Updating
file = shelve.open("shelf_file", writeback=True)

n = int(input("No of values to be added: "))
for _ in range(n):
    file['arr'].append(input())

print(file['arr'])
file.close()
