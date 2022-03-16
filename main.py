import os
import re
import openpyxl
import json

import pandas as pd
import xml.etree.ElementTree as ET

def parseXML(file):
    tree = ET.parse(file)

    all_data = {}

    for elem in tree.iter():
      #remove element here if needed
      #for child in list(elem):
        #if child.tag == '{http://www.portalfiscal.inf.br/nfe}det':
          #elem.remove(child)
      obs = elem.tag
      obs = re.findall(r"(?<=}).*", obs)
      obs = str(*obs)
      
      data = elem.text
      if data == None:
        data = "0"

      all_data[obs] = data

    return all_data

def main():
    directory = 'xml'
    output = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if os.path.isfile(f):
            nf = parseXML(f)
            output.append(nf)

    json_object = json.dumps(output)
    df_json = pd.read_json(json_object)
    df_json.to_excel('data.xlsx')

if __name__ == '__main__':
    main()
  