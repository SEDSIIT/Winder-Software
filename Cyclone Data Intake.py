import os
import json

file = open("guistuff\\guiOut.json")
fileTwo = open("guistuff\\tempLayers\\layers.json")
data= json.load(file)
dataTwo = json.load(fileTwo)

tubeThickness = data["tubeWall"]
tubeId = data["tubeID"]
tubeLength = data["tubeLength"]
towWidth = data["towWide"]
towThickness = data["towThick"]

numLayers = data["numLayers"]

layers = []

for x in range(numLayers):
    layer = dataTwo["layer "+str(x)]

    if layer["windType"]=="hoop":
        if(x+1)==numLayers:
            windLayer={
                "windType": "hoop",
                "terminal": True
            }
            layers.append(windLayer)
        else:
            windLayer={
                "windType": "hoop",
                "terminal": False
            }
            layers.append(windLayer)
    else:
        windLayer={
            "windType": "helical",
            "windAngle": layer["windAngle"],
            "patternNumber": layer["patternNum"],
            "skipIndex": layer["skipIndex"],
            "lockDegrees": layer["lockAngle"],
            "leadInMM": layer["leadInMM"],
            "leadOutDegrees": layer["leadOutAngle"],
            "skipInitialNearLock": layer["skipInitalNearLock"]
        }
        layers.append(windLayer)


dictionary = {
    "layers": layers,
    "mandrelParameters": {
        "diameter": data["tubeID"],
        "windLength": data["tubeLength"]
    },
    "towParameters": {
        "width": data["towWide"],
        "thickness": data["towThick"]
    },
    "defaultFeedRate": 8000
}

json_object = json.dumps(dictionary, indent=4)

with open("tube.wind", "w") as outfile:
    outfile.write(json_object)

os.system('cmd /c "npm run cli -- plan -o tube.gcode tube.wind"')
