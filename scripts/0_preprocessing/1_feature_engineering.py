import os
import sys
import warnings
import pandas as pd

# append additional paths
FILE_SYSTEM_PATH = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))
)
sys.path.append(FILE_SYSTEM_PATH)
from file_system_paths import *

# ignore warnings
warnings.filterwarnings('ignore')

# extract parameter for data preparation
set_name = sys.argv[1]

# step 1 - load the dataset
data_name = f'{set_name}.csv'
data = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, data_name))

# step 2 - if it is the train set, calculate max runtime. 
# If not, load it
if set_name == 'train':
    max_runtime = pd.DataFrame(
        data.groupby(['history_id'])['runtime'].max().values,
        columns=['max_runtime'],
        index=data.groupby(['history_id'])['runtime'].max().index
    )

    # save a copy
    if not os.path.isdir(PREPARED_DATA_PATH):
        os.makedirs(PREPARED_DATA_PATH)

    max_runtime.to_csv(
        os.path.join(PREPARED_DATA_PATH, 'max_runtime.csv')
    )
else:

    max_runtime = pd.read_csv(
        os.path.join(PREPARED_DATA_PATH, 'max_runtime.csv'),
        index_col='history_id'
    )

# step 3 - calculate failure class
def create_failure_class(row: pd.DataFrame,
                         data: pd.DataFrame) -> int:
    """
    create a failure class
    1 - the plant will fail in the next 50 cycles
    0 - the plant will not fail in the next 50 cycles

    Parameters
    ----------
    row : pd.DataFrame
        dataframe row
    data : pd.DataFrame
        grouped dataset with the maximum runtime

    Returns
    -------
    int
        failure class
    """
    # business threshold
    FORECAST_WINDOW = 50

    # get the maxium runtime of that specific history id
    max_runtime_id = data.loc[row['history_id'], 'max_runtime']

    if row['runtime'] + FORECAST_WINDOW > max_runtime_id:
        return 1
    else:
        return 0

data['categ'] = data.apply(create_failure_class, data=max_runtime, axis=1)

# step 4 - calculate the RUL
# calculate the rul
data['rul'] = 0
for id in max_runtime.index:

    # extract the maximum runtime by index
    max_runtime_id = max_runtime.loc[id, 'max_runtime']

    # calculate the rlu
    data.loc[data.history_id==id, 'rul'] = max_runtime_id - data.loc[data.history_id==id, 'runtime']

# step 5 - drop useless features
useless = ['set1', 'set2', 'history_id']
data.drop(useless, axis=1, inplace=True)

# step 6 - save both regression and classification datasets
regression_data = data.drop(['categ'], axis=1)

regression_data.to_csv(
    os.path.join(PREPARED_DATA_PATH, f'{set_name}_regression.csv'),
    index=False
)

classification_data = data.drop(['rul'], axis=1)

classification_data.to_csv(
    os.path.join(PREPARED_DATA_PATH, f'{set_name}_classification.csv'),
    index=False
)