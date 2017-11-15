
class Range_filter():

    def __init__(self,range_min_max): #Initialize the class
        self.range_min = range_min_max[0]
        self.range_max = range_min_max[1]

    def update(self,input_scan): #takes in an array of length N
        """Applies the range_filter to input_scan array and returns
        the array of same length. Range_filter filters out the values
        that are not in the range of [range_min,range_max] and replaces them.

        parameters
        ----------
        input_scan: an array of length N of float values representing the
        distance measurements.

        Returns
        -------
        output: an array of same length N as input_scan after applying
        range filter.

        """
        output =[]
        for i in range(len(input_scan)):
            if input_scan[i] < self.range_min:
                output.append(self.range_min)
            elif input_scan[i] > self.range_max:
                output.append(self.range_max)
            else:
                output.append(input_scan[i])
        return output #return the updated scan array
