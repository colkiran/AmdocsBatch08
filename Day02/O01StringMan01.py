
st = "hello world"
print(f"st :{st}")
print(type(st))

print('-' * 40)
print(f"st[0]  :{st[0]}")            # strings are stored like lists(arrays)
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print('-' * 40)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

# reverse indexing
print('-' * 40)
print(f"st[-1]  :{st[-1]}")
print(f"st[-7]  :{st[-7]}")
print(f"st[-11] :{st[-11]}")

# slicing
print('-' * 40)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
# print(f"st[-12] :{st[-12]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# check if a given string is a palindrome
print('-' * 40)
st = "malayalam"
print(f"Palindrome - {st}" if st == st[::-1] else f"Not a Palindrome - {st}")


print('-' * 40)
# st = "hello world"
# print(f"st[0] :{st[0]}")
# # st[0] = "H"
# print(type(st))

st = "abc"
print(dir(st))
