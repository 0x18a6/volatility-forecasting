
from giza_actions.task import task

@task(name='Join and Preprocessing')
def loading_and_preprocessing():
    """
    Loads, preprocess and merges datasets for further analysis.

    Returns: pd.DataFrame: The processed dataframe after merging and cleaning
    """

    df_main = daily_price_dateset_manipulation()
    apy_df = apy_dateset_manipulation()
    tvl_df = tvl_dataset_manipulation()