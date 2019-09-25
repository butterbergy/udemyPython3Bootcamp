def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

beat_gen = current_beat()
for i in range(0, 100):
    print(next(beat_gen))
