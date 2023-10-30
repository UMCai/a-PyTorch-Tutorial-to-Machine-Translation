from utils import *

DATA_FOLDER_PATH = r"C:\MyCode\Dataset\Transformer_Data"


# this function have bug on wget, 
# this means that the data can not be download properly from the provided url.
# to solve this problem, simply download the url, 
# and put all zipped files into DATA_FOLDER_PATH/tar files folder to activate the rest of the code.

download_data(data_folder=DATA_FOLDER_PATH)

prepare_data(data_folder=DATA_FOLDER_PATH,
             euro_parl=True,
             common_crawl=True,
             news_commentary=True,
             min_length=3,
             max_length=150,
             max_length_ratio=2.,
             retain_case=True)
