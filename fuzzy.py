# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon June 4 11:32:17 2023

@author: ashfaqmahmud
"""
def getMembershipTemp(temperature):
    degree = {}
    
    if temperature < 0 or temperature > 58:
        degree["cold"] = 0
        degree["warm"] = 0
        degree["hot"] = 0
    
    elif temperature <=25:
        degree["cold"] = 1
        degree["warm"] = 0
        degree["hot"] = 0
    
    elif temperature>10 and temperature<=25:
        degree["cold"] = float((25-temperature)/(15))
        degree["warm"] = float((temperature-10)/(15))
        degree["hot"] = 0
    
    elif temperature>25 and temperature<35:
        degree["cold"] = 0
        degree["warm"] = 1
        degree["hot"] = 0
        
    elif temperature>=35 and temperature<=45:
        degree["cold"] = 0
        degree["warm"] = float((45-temperature)/(10))
        degree["hot"] = float((temperature-35)/(10))
        
    elif temperature >45 and temperature <= 58:
      degree["cold"] = 0
      degree["warm"] = 0
      degree["hot"] = 1
        
    return degree

def getMembershipHum(humidity):
    degree = {}
    
    if humidity < 0 or humidity > 100:
        degree["low"] = 0
        degree["high"] = 0
        
    
    elif humidity <=40:
        degree["low"] = 1
        degree["high"] = 0
    
    elif humidity>40 and humidity<=60: 
        degree["low"] = float((60-humidity)/(20))
        degree["high"] = float((humidity-40)/(20))
        
    elif humidity > 60 and humidity <= 100:
        degree["low"] = 0
        degree["high"] = 1
        
    return degree




def ruleEvalationAssessment(temperature,humidity):
    
    
    cold=max(temperature["cold"],humidity["high"])
    warm=min(temperature["warm"],humidity["high"])
    hot=max(temperature["hot"],min(temperature["warm"],humidity["low"]))
    
    
    return cold,warm,hot
    


def defuzzificationAssessment(m,c,h ):
    
    val1=0
    val2=0
    l=0
    while(l<=100):
        if(l<=20):
           val1+=float(m*l)
           val2+=float(m)
        
        elif l>=30 and l<=40:
              val1+=float(c*l)
              val2+=c
        elif l>=50 and l<=58:
            val1+=float(h*l)
            val2+=h
        l+=5
    cog=float(val1/val2)
    return cog


#input
#temperature, humidity = 30, 60
temperature=float(input("Temperature:"))
humidity=float(input("humidity:"))

fuzzyTemp=getMembershipTemp(temperature)
fuzzyHum=getMembershipHum(humidity)

print(fuzzyTemp)
print(fuzzyHum)


cold,warm,hot = ruleEvalationAssessment(fuzzyTemp,fuzzyHum)
print(cold,warm,hot)


conAssessment = defuzzificationAssessment(cold,warm,hot)
print("Fuzzified Continuous Assessment: ",conAssessment)