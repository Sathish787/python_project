sample = ('TV', 'Computer', 'Laptop')
# Tuple is a collection of data objects which is ordered  and immutable (unchangeable)

print(sample)
print(sample[1])

for item in sample:
    print(item)

print('Length of the tuple: ' + str(len(sample)))

for i in range(len(sample)):
    print('index of tuple: ' + str(i))

sample_iter = iter(sample)
print(next(sample_iter))
print(next(sample_iter))
print(next(sample_iter))