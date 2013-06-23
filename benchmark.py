import bogo

seq_file = open("output.sequences", "r")
TEST_SIZE = 1000

pairs = []
for i in range(TEST_SIZE):
	pair = seq_file.readline().strip()
	pairs.append(pair.split())


import time

old_time = time.time()
wrong_count = 0
for pair in pairs:
	result = bogo.process_word(pair[0])
	if result != pair[1]:
		wrong_count += 1
		print(pair, result)

running_time = time.time() - old_time

print("Number of wrong entries: " + str(wrong_count) + "/" + str(TEST_SIZE))
print("Speed: " + str(TEST_SIZE / running_time) + "tests/second")
print("Test time: " + str(running_time))
