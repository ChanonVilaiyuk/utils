# read text file
import os
import sys

def readSetting(configFile) : 
    lines = []
    config = dict()

    # read file as line
    if os.path.exists(configFile) : 
        f = open(configFile)
        lines = f.readlines()
        f.close()

    for eachLine in lines : 
        if not '#' in eachLine : 
            if ':' in eachLine : 
                # separate from ':'
                elements = eachLine.split(':')

                # first element and remove space
                key = elements[0].replace(' ', '')

                # value and remove space
                value = elements[1].replace(' ', '')

                # update dict
                config.update({key: value})


    return config


def getKeyString(openKey, closeKey, inputText) : 

    strEles = inputText.split(openKey)
    keys = []

    for each in strEles : 
        key = str()
        for eachChar in each : 
            if not eachChar == closeKey : 
                key = '%s%s' % (key, eachChar)
                
            else : 
                keys.append(key)
                break


    return keys
