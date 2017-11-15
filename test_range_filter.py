import range_filter

test_cases=[[0., -1., 2., 1., 3.],
            [1., 5., 7., 1., 3.],
            [2., 3., 4., 1., 0.],
            [3., 3., 3., 1., 3.],
            [10., 2., 4., 0., 10000.]]

""" test_case for range_filter

"""
print("Range filter result:")
print("=====================")

range = [0.03,50] # [min_range, max_range]
range_filter = range_filter.Range_filter(range)

for each_test in test_cases:
    print(range_filter.update(each_test))
