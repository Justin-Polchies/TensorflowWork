import os
import glob
from sklearn.model_selection import train_test_split
import shutil

from my_untils import split_data



if __name__ =="__main__":

    path_to_data = "C:\\Users\\shank\\Desktop\\USM School\\Programming\\backupcoding files\\GTSRB-GermanTrafficSigns\\Train"
    path_to_save_train = "C:\\Users\\shank\\Desktop\\USM School\\Programming\\backupcoding files\\GTSRB-GermanTrafficSigns\\training_data\\train"
    path_to_save_val = "C:\\Users\\shank\\Desktop\\USM School\\Programming\\backupcoding files\\GTSRB-GermanTrafficSigns\\training_data\\val"
    split_data(path_to_data, path_to_save_train = path_to_save_train, path_to_save_val = path_to_save_val)