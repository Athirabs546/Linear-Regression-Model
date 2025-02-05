class LinearRegression:
    def __init__(self):
        self.m = None
        self.c = None

    def fit(self,X,y):
        n=len(X)
        sum_x=sum(X)
        sum_y=sum(y)
        sum_x_squared = sum(x ** 2 for x in X)
        sum_xy = sum(X[i] * y[i] for i in range(n))

        # Calculate slope (m) and intercept (c)
        self.m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        self.c = (sum_y - self.m * sum_x) / n

    def predict(self,X):
        y=self.m*X+self.c
        return y
    