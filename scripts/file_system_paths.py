import os

# get project root
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))
)

# define preprocessing paths
RAW_DATA_PATH = os.path.join(
    PROJECT_ROOT, 'data', '1_raw'
)
PROCESSED_DATA_PATH = os.path.join(
    PROJECT_ROOT, 'data', '2_processed'
)
PREPARED_DATA_PATH = os.path.join(
    PROJECT_ROOT, 'data', '3_model_path'
)

# constants for the project
real_names = ['history_id', 'runtime', 'set1', 'set2', 'set3']
for i in range(21):
    real_names.append(f'tag{i+1}')