#read the data and split the data into train and test
import os
import sys
sys.path.insert(0, '/Users/sanjana/Documents/sanjana/mlproject')
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#all the inputs will be creating ain another class-data ingestion class
#the __init__(), __repr__(), and __eq__() methods are automatically generated, based on the attributes defined in the class.
@dataclass #directly able to define a class variable
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    
    #all the outputs are stored in this artifact folder
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


#if you have only variables to define dataclass decorator is suggested otherwise use the functions

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        #to read from database
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/StudentsPerformance.csv')
            logging.info("Data read successfully")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

# import os
# import sys
# sys.path.insert(0, '/Users/sanjana/Documents/sanjana/mlproject')
# # sys.path.insert(0, '/Users/sanjana/Documents/sanjana/mlproject/src/exception.py')
# # sys.path.insert(0, './src')
# from src.logger import logging
# from src.exception import CustomException
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass 


# @dataclass
# class DataIngestionConfig:
#     train_data_path:str=os.path.join('artifacts',"train.csv")
#     test_data_path:str=os.path.join('artifacts',"test.csv")
#     raw_data_path:str=os.path.join('artifacts',"raw.csv")      


# class DataIngestion:
#     def __init__(self) :
#         self.ingestion_config = DataIngestionConfig()
    
#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method")
#         try:
#            df = pd.read_csv('notebook\diamonds.csv')
#            logging.info("Data Read as df")
           
#            df = df.drop(["Unnamed: 0"],axis = 1)
#            logging.info("unamed column dropped")      
                
#            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
           
#            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
           
#            logging.info("initialized Train Test Split")
#            train_data,test_data = train_test_split(df,test_size=0.2,random_state=7)
           
#            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
#            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
           
#            logging.info("Train and Test Folders Created...Ingestion DOne")
           
#            return(
#                self.ingestion_config.train_data_path,
#                self.ingestion_config.test_data_path               
#            )
#         except Exception as e:
#             raise CustomException(e,sys)
        
        
# if __name__=='__main__':
#     obj = DataIngestion()
#     train_data,test_data = obj.initiate_data_ingestion()
    