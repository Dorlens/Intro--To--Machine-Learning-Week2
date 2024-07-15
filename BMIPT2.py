
"""Extend the previous homework from Week1 #4, with the following additions:
1) create a loop of 10 times, to ask for those 3 pieces of information of 10 different people
2) for each person, run through the  same BMI calculator, store the person's name and BMI in a dictionary
3) as you run through the loop, append each BMI value to a list
4) after the loop is completed, calculate the min, max, mean, standard deviation, variance of the BMI list"""

import statistics


def bmicalc():
    myDic = {}
    bmiList = []

    for i in range(10):
        name = input("What's your name? ")
        weight = float(input("How much you weigh in pounds? "))
        feet = int(input("What's your height in feet? "))
        inches = int(input("whats your reminding inches? "))

        height = feet * 12 + inches # converted height to inches 

        bmi = (weight * 703) / (height **2) # body mass index 
    #Add the name and bmi in a dictionary 
    myDic[name] = bmi
    # add the bmi to a list
    bmiList.append(bmi)

      #calculation 
    minBmi = min(bmiList)
    maxBmi = max(bmiList)
    meanBmi = statistics.mean(bmiList)
    stdDevBmi = statistics.stdev(bmiList)
    varianceBmi = statistics.variance(bmiList)

        #Printed the results 
    print(f"Minimum BMI: {minBmi:.2f}")
    print(f"Maximum BMI: {maxBmi:.2f}")
    print(f"Mean BMI: {meanBmi:.2f}")
    print(f"Standard Deviation of BMI: {stdDevBmi:.2f}")
    print(f"Variance of BMI: {varianceBmi:.2f}")

    #printed each persons Bmi
    print("\nPeoples  BMIs:")
    for name in myDic.items():
        print(f"{name} has a bmi of {bmi}")
bmicalc() 