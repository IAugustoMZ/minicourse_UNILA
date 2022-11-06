import os
import sys
import warnings
import itertools
import pandas as pd

# append additional paths
FILE_SYSTEM_PATH = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))
)
sys.path.append(FILE_SYSTEM_PATH)
from file_system_paths import *

# ignore warnings
warnings.filterwarnings('ignore')

# extract parameter for data preprocessing
set_name = sys.argv[1]
var_thresh = float(sys.argv[2])

# step 1 - load the dataset
data_name = f'PM_{set_name}.txt'
data = pd.read_csv(os.path.join(RAW_DATA_PATH, data_name), header=None, sep=' ')

# step 2 - remove additional columns
data.drop([26, 27], axis=1, inplace=True)

# step 3 - rename columns
data.columns = real_names

# step 4 - remove low variance columns
if set_name == 'train':

    # calculate stats table
    stats = data.describe().T

    # calculate relative variability
    stats['CV'] = stats['std'] / (stats['mean'] + .1)

    # drop very low variance columns
    data.drop(stats.loc[stats.CV < var_thresh].index, axis=1, inplace=True)

else:

    # load processed train dataset
    data_ref = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, 'train.csv'))

    # select only the columns of the train dataset
    data = data[data_ref.columns]

# step 5 - drop duplicated columns

# list the combinations of columns 2-to-2
comb = itertools.combinations(data.columns, 2)

# iterate through the combinations and compare the pairs
dup_cols = []
for col1, col2 in comb:
    if ((col1 not in dup_cols) and (col2 not in dup_cols)):
        if data[col1].equals(data[col2]):
            dup_cols.append(col1)

# drop duplicated, if any
data.drop(dup_cols, axis=1, inplace=True)

# step 6 - save dataset
save_name = f'{set_name}.csv'

if not os.path.isdir(PROCESSED_DATA_PATH):

    # if the directory does not exist, create it
    os.makedirs(PROCESSED_DATA_PATH)

# save data
data.to_csv(os.path.join(PROCESSED_DATA_PATH, save_name), index=False)
