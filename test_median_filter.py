import temporal_median_filter

test_cases=[[0., 1., 2., 1., 3.],
            [1., 5., 7., 1., 3.],
            [2., 3., 4., 1., 0.],
            [3., 3., 3., 1., 3.],
            [10., 2., 4., 0., 0.]]

""" test_case for median filter
"""
print("Median filter result:")
print("=====================")
#test_case inputs


D = 3 #The value of D, the number of previous scans to be considered
        #is given as an input by the user through the test case.

median_filter = temporal_median_filter.Median_filter(D)

for each_test in test_cases:
    print(median_filter.update(each_test))
