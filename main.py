from lr import LinearRegression

x=[1,2,3,4,5,6,7,8,9,10]
y=[3,6,9,12,15,18,21,24,27,30]

model=LinearRegression()
model.fit(x,y)
print(model.m)    #slope
print(model.c)    #intercept
s=model.predict(15)
print(f"result is {s}")