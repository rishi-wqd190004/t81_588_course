# Task: Split the data based on train, test and validate text file for further training
import pandas as pd

full_csv = f'../dataset_DL/BCCD_Dataset/raw_data.csv'
train_txt = f'../dataset_DL/BCCD_Dataset/BCCD/ImageSets/Main/train.txt'
val_txt = f'../dataset_DL/BCCD_Dataset/BCCD/ImageSets/Main/val.txt'
test_txt = f'../dataset_DL/BCCD_Dataset/BCCD/ImageSets/Main/test.txt'

full = pd.read_csv(full_csv)

def get_fileNames(txt_file_path):
    with open(txt_file_path, 'r') as f:
        filenames = f.read().splitlines()
    return filenames

train_filenames = get_fileNames(train_txt)
val_filenames = get_fileNames(val_txt)
test_filenames = get_fileNames(test_txt)

def filter_by_filenames(df, filenames):
    filenames_with_extension = [fname + '.jpg' for fname in filenames]
    return df[df['img_name'].isin(filenames_with_extension)]

df_train = filter_by_filenames(full, train_filenames)
df_val = filter_by_filenames(full, val_filenames)
df_test = filter_by_filenames(full, test_filenames)

write_path = f'../dataset_DL/BCCD_Dataset/processed_csv/'

df_train.to_csv(write_path + 'train.csv', index=False)
df_val.to_csv(write_path + 'val.csv', index=False)
df_test.to_csv(write_path + 'test.csv', index=False)