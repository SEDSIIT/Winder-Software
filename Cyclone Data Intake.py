import os
import numpy
import json

print("Enter the following values in mm.")

tubeThickness = float(input("Enter tube thickness: "))
tubeId = float(input("Enter inner diameter of the tube(also the OD of the mandrel): "))
tubeLength = float(input("Enter tube length: "))
towWidth = float(input("Enter tow width: "))
towThickness = float(input("Enter tow thickness: "))

numLayers = round(tubeThickness / towThickness)

layers = []

x = 0

while(x<numLayers):
    print("Layer ", x+1)
    helOrHoop =input("Is this layer a hoop layer(True or False)? ")
    
    if (helOrHoop.lower()=="true"):
        if(x+1 == numLayers):
            layer = {
                "windType": "hoop",
                "terminal": True
            }
        else:
            layer = {
                "windType": "hoop",
                "terminal": False
            }
    else:
        ang = int(input("Enter wind angle: "))
        patNum = int(input("Enter pattern number: "))
        skipInd = int(input("Enter skip index: "))
        lockDeg = int(input("Enter lock angle: "))
        leadInMM = int(input("Enter lead in length(mm): "))
        leadOutAng = int(input("Enter lead out angle: "))
        SkipIni = bool(input("Skip inital near lock?(True or False): "))
        
        layer = {
            "windType": "helical",
            "windAngle": ang,
            "patternNumber": patNum,
            "skipIndex": skipInd,
            "lockDegrees": lockDeg,
            "leadInMM": leadInMM,
            "leadOutDegrees": leadOutAng,
            "skipInitialNearLock": SkipIni
        }
    
    layers.append(layer)
    x+=1


dictionary = {
    "layers": layers,
    "mandrelParameters": {
        "diameter": tubeId,
        "windLength": tubeLength
    },
    "towParameters": {
        "width": towWidth,
        "thickness": towThickness
    },
    "defaultFeedRate": 8000
}

json_object = json.dumps(dictionary, indent=4)

with open("tube.wind", "w") as outfile:
    outfile.write(json_object)

os.system('cmd /c "npm run cli -- plan -o tube.gcode tube.wind"')
