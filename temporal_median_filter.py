from numpy import median

class Median_filter():
    #Initialize the class to apply temporal median filter
    def __init__(self, D):
        self.d = D
        self.past_scans = []

    def update(self, input_scan): #input_scan is a single scan of length N.
        """Applies the temporal median filter to the input_scan array
        and returns the median of all the scans for the first D scans.

        parameters
        ----------
        input_scan : an array of length N of float values representing
        distance measurements. For ex:input_scan = [1., 5., 7., 1., 3.]


        Returns
        -------
        y :an array of length N after applying temporal median Filter
        For ex:[0.5, 3., 4.5, 1., 3.]
        """

        self.past_scans.append(input_scan)
        each_y = [] # Initialize the list to hold x(i) values 
        y = []

        if len(self.past_scans)>self.d+1:
            del self.past_scans[0]

        if len(self.past_scans)<=1:
            return self.past_scans[0]

        for i in range(len(input_scan)):
            for each_scan in self.past_scans:
                each_y.append(each_scan[i])
            y.append(median(each_y))
            each_y = []

        return y #returns the updated scan array
