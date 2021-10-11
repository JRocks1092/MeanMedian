import pandas as pd

df = pd.read_csv("SOCR-HeightWeight.csv")
Heights = df["Height(Inches)"].tolist()
Weight = df["Weight(Pounds)"].tolist()
Heights.sort()
Weight.sort()


def mean(data):
    sumno = 0
    for i in data:
        sumno += i
    return sumno/len(data)


def median(data):
    medianno = 0.0
    if len(data) % 2 == 0:        
        medianno = mean([
            data[int(len(data)/2-1)],
            data[int(len(data)/2)]
        ])
    else:
        medianno = data[len(data)-1/2]
    return medianno


def mode(data):
    numbers = []
    num = 0.0
    count = 0
    for i in data:
        if i == num:
            count += 1
        else:
            numbers.append([num, count])
            num = i
            count = 1
    lastCount = 0
    lastNo = 0.0
    for i in numbers:
        if i[1] > lastCount:
            lastNo = i[0]
            lastCount = i[1]
    return lastNo


heights_mean = mean(Heights)
heights_mode = mode(Heights)
heights_median = median(Heights)
weights_mean = mean(Weight)
weights_mode = mode(Weight)
weights_median = median(Weight)

print("╔"+"═"*80+"╗")
print("║"+" "*80+"║")
print("║  heights_mean --->   "+str(heights_mean))
print("║"+" "*80+"║")
print("║  heights_mode --->   "+str(heights_mode))
print("║"+" "*80+"║")
print("║  heights_median --->   "+str(heights_median))
print("║"+" "*80+"║")
print("║  weights_mean --->   "+str(weights_mean))
print("║"+" "*80+"║")
print("║  weights_mode --->   "+str(weights_mode))
print("║"+" "*80+"║")
print("║  weights_median --->   "+str(weights_median))
print("║"+" "*80+"║")
print("╚"+"═"*80+"╝")