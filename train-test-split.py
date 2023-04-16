import splitfolders

dataset_dir = 'raw_dataset/'

splitfolders.ratio(
    input=dataset_dir,
    output='dataset',
    seed=42,
    ratio=(0.8, 0.2),
    group_prefix=None
)