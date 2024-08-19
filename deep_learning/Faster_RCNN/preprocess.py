## Purpose: Take all the xml, annotation, image file name --> convert to a csv to use as training file

import pandas as pd
import xml.etree.ElementTree as ET
import os

columns= ['img_name', 'cell_type', 'x_min', 'x_max', 'y_min', 'y_max']
folder_path = '/Users/rishinigam/t81_588_course/deep_learning/dataset_DL/BCCD_Dataset/BCCD/Annotations'
anotations = os.listdir(folder_path)

rows = []
cnt = 0
for name in anotations:
    if name.endswith('.xml'):
        file_name = name.split('.')[0]
        jpeg_file = file_name + '.jpg'
        file_path = os.path.join(folder_path, name)
        row = []
        parsedXML = ET.parse(file_path)
        for node in parsedXML.getroot().iter('object'):
            cell_type = node.find('name').text
            x_min = int(node.find('bndbox/xmin').text)
            x_max = int(node.find('bndbox/xmax').text)
            y_min = int(node.find('bndbox/ymin').text)
            y_max = int(node.find('bndbox/ymax').text)
            row = [jpeg_file, cell_type, x_min, x_max, y_min, y_max]
            rows.append(row)
            cnt += 1

df = pd.DataFrame(rows, columns=columns)
df_sorted = df.sort_values(by='img_name')
df_sorted.to_csv('/Users/rishinigam/t81_588_course/deep_learning/dataset_DL/BCCD_Dataset/raw_data.csv', index=False)