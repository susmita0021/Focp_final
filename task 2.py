from statistics import mean
print("Swallow speed Analysis: Version '1.0'")
i=1
count=1+i
eu_reading_KPH=[]
uk_reading_MPH=[]
while True:
    reading=input("Enter the next reading: ")#ask user to enter the input.
    if reading=="":
        break
    elif reading[0]=="U" or reading[0]=="u":#it takes the reading in upper and lower case.
        uk_reading_MPH.append(float(reading[1:]))#append function is used to add single item in list.
        eu_reading_KPH.append(float(reading[1:])*1.60934)
    elif reading[0]=="E" or reading[0]=="e":#it takes the reading in upper and lower case.
        eu_reading_KPH.append(float(reading[1:]))
        uk_reading_MPH.append(float(reading[1:])*0.621371)
    elif reading[0:]!="U" or reading[0:]!="u"and reading[0:]!="E" or reading[0:]!="e":#checks the condition and gives the output accordingly.
        print("Wrong input!!")
print(count,"Reading analysed")        
print(f"Max speed: {max(eu_reading_KPH):.1f} MPH,{max(uk_reading_MPH):.1f} KPH")#string formatting is used.
print(f"Min speed: {min(eu_reading_KPH):.1f} MPH,{min(uk_reading_MPH):.1f} KPH")
print(f"Avg speed: {min(eu_reading_KPH)/len(eu_reading_KPH):.1f} MPH,{sum(uk_reading_MPH)/len(uk_reading_MPH):.1f} KPH")
print(type(eu_reading_KPH[0]))

