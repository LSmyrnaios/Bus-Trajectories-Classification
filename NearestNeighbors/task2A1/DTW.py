import sys
import numpy as np
from numpy import shape
from scipy.spatial.distance import squareform
from SupportMethods import HaversineDist


class Dtw(object):
    """K-nearest neighbor classifier using dynamic time warping
    as the distance measure between pairs of time series arrays

    Arguments
    ---------
    n_neighbors : int, optional (default = 5)
        Number of neighbors to use by default for KNN

    max_warping_window : int, optional (default = infinity)
        Maximum warping window allowed by the DTW dynamic
        programming function

    subsample_step : int, optional (default = 1)
        Step size for the timeseries array. By setting subsample_step = 2,
        the timeseries length will be reduced by 50% because every second
        item is skipped. Implemented by x[:, ::subsample_step]
    """

    def __init__(self, n_neighbors=5, max_warping_window_percentage=0.7, subsample_step=1):
        self.n_neighbors = n_neighbors
        if max_warping_window_percentage > 1.0:   # If the percentage given is not a decimal below zero... make it like it.
            max_warping_window_percentage = max_warping_window_percentage/100
        self.max_warping_window_percentage = max_warping_window_percentage
        self.subsample_step = subsample_step


    def _dtw_distance(self, ts_a, ts_b, d=lambda x, y: abs(x - y)):
        """Returns the DTW similarity distance between two 2-D
        timeseries numpy arrays.

        Arguments
        ---------
        ts_a, ts_b : array of shape [n_samples, n_timepoints]
            Two arrays containing n_samples of timeseries data
            whose DTW distance between each sample of A and B
            will be compared

        d : DistanceMetric object (default = abs(x-y))
            the distance measure used for A_i - B_j in the
            DTW dynamic programming function

        Returns
        -------
        DTW distance between A and B
        """

        # Create cost matrix via broadcasting with large int
        ts_a, ts_b = np.array(ts_a), np.array(ts_b)
        M, N = len(ts_a), len(ts_b)

        max_warping_window = int(N*self.max_warping_window_percentage)

        cost = sys.maxint * np.ones((M, N))

        # Wikipedia-s code with our Haversine where needed.
        for i in xrange(0, M):
            for j in xrange(0, N):
                cost[i, j] = float('Inf') #cost[0, j - 1] + HaversineDist.haversine(ts_a[0][1], ts_a[0][2], ts_b[j][1], ts_b[j][2])

        cost[0, 0] = 0  # HaversineDist.haversine(ts_a[0][1], ts_a[0][2], ts_b[0][1], ts_b[0][2])

        # Populate rest of cost matrix within window
        for i in xrange(1, M):
            for j in xrange(max(1, i - max_warping_window), min(N, i + max_warping_window)):
                choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
                cost[i, j] = min(choices) + HaversineDist.haversine(ts_a[i][1], ts_a[i][2], ts_b[j][1], ts_b[j][2])

        # Return DTW distance
        return cost[-1, -1]


    def _dist_matrix(self, x, y):
        """Computes the M x N distance matrix between the training
        dataset and testing dataset (y) using the DTW distance measure

        Arguments
        ---------
        x : array of shape [n_samples, n_timepoints]

        y : array of shape [n_samples, n_timepoints]

        Returns
        -------
        Distance matrix between each item of x and y with
            shape [training_n_samples, testing_n_samples]
        """

        # Compute the distance matrix
        dm_count = 0

        # Compute condensed distance matrix (upper triangle) of pairwise dtw distances
        # when x and y are the same array
        if (np.array_equal(x, y)):
            x_s = shape(x)
            dm = np.zeros((x_s[0] * (x_s[0] - 1)) // 2, dtype=np.double)

            for i in xrange(0, x_s[0] - 1):
                for j in xrange(i + 1, x_s[0]):
                    dm[dm_count] = self._dtw_distance(x[i, ::self.subsample_step], y[j, ::self.subsample_step])
                    dm_count += 1

            # Convert to squareform
            dm = squareform(dm)
            return dm

        # Compute full distance matrix of dtw distances between x and y
        else:
            x_s = np.shape(x)
            y_s = np.shape(y)
            dm = np.zeros((x_s[0], y_s[0]))
            dm_size = x_s[0] * y_s[0]

            for i in xrange(0, x_s[0]):
                for j in xrange(0, y_s[0]):
                    dm[i, j] = self._dtw_distance(x[i, ::self.subsample_step], y[j, ::self.subsample_step])

            return dm


    def fit(self, x, l):
        """Fit the model using x as training data and l as class labels

        Arguments
        ---------
        x : array of shape [n_samples, n_timepoints]
            Training data set for input into KNN classifer

        l : array of shape [n_samples]
            Training labels for input into KNN classifier
        """

        self.x = x
        self.l = l


    def predict(self, x):
        """Predict the class labels or probability estimates for
        the provided data

        Arguments
        ---------
          x : array of shape [n_samples, n_timepoints]
              Array containing the testing data set to be classified

        Returns
        -------
          2 arrays representing:
              (1) the predicted class labels
              (2) the knn label count probability
        """

        dm = self._dist_matrix(x, self.x)

        # # Identify the k nearest neighbors
        # knn_idx = dm.argsort()[:, :self.n_neighbors]
        #
        # # Identify k nearest labels
        # knn_labels = self.l[knn_idx]
        #
        # # Model Label
        # mode_data = mode(knn_labels, axis=1)
        # mode_label = mode_data[0]
        # mode_proba = mode_data[1] / self.n_neighbors
        #
        # return mode_label.ravel(), mode_proba.ravel()
