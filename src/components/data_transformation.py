import os
import sys
from dataclasses import dataclass

import numpy as numpy
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.Exception import CustomException
from src.logger import logging
from src.utils import save_object


class DataTransformationconfig:
    prepprocessor_obj_file_path=os.path.join('artifact',"preprocessor.pk1")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

        def get_dat_transformer_object(self):
            '''
            this function is responsible for dta transformation
            '''
            try:
                numerical_columns =["writing_score","reading_score"]
                categorical_columns=[
                    "gender",
                    "race_ethnicity",
                    "parental_level_of_education",
                    "lunch",
                    "test_preparation_course",
                ]
                num_pipeline=pipeline(
                    steps=[
                      ("Imputer",SimpleImputer(statergy="medium")), 
                      ("scaler",StandardScaler())
                    ]
                )
                cat_pipeline=pipeline(
                    steps=[
                        ("imputer"),SimpleImputer(statergy="most_frequent"),
                        ("one_hot_encoder",OnehotEncoder()),
                        ("scaler",StandardScaler())
                    ]
                )    
                

                loggomg.info("Numerical columns Standard scaling completed")
                logging.info("Categorical columns One hot encoding completed")
                preprocessor=ColumnTransformer(
                    [
                        ("num_pipeline",num_pipeline,numerical_columns),
                        ("cat_pipeline",cat_pipeline,categorical_columns)
                    ]
                

                )
                return preprocessor
            except Exception as e:   
                raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")

            logging.info("obtaining preprocessing object")

            preprocessing_obj=self.get_data_transform_object()
            target_column_name="math_score"
            numerical_columns= ["writing_score","reading_score"]

            input_feature_train_df=tarin.df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training and test datframes."
            )
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr =- np.c_[
                input_feature_train_arr,
                np.array(target_feature_train_df)
            ]
            test_arr =- np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=-self.data_transformation_config.prepprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.prepprocessor_obj_file_path,
            )
        except:
            pass
