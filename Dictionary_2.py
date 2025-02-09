#setting the scores
scores={'alice':88,'bob':92,'charlie':85,'Diana':95,'eve':90}

#Finding the maximum
print(f"The person with the Highest score is: {max(scores,key=scores.get)}")

#Finding the lowest
print(f"The person with the lowest score is: {min(scores,key=scores.get)}")