from giza_datasets import DatasetsHub, DatasetsLoader

import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

TOKEN_NAME = "WETH" # Choose one of the available tokens in the main dataset.
LOADER = DatasetsLoader()

def calculate_lagged_correlations(df, target_token, lag_days=15, n=10):
    """
    Calculates the correlation between the lagged prices of various tokens and the price of a target token.

    Parameters:
    - df: DataFrame containing 'date', 'token' and 'price' columns.
    - target_token: The token whose price is to be compared against others.
    - lag_days: The number of days of la to apply when calculating the correlation.
    - n: the maximum number of tokens with the highest correlation in return.

    Returns:
    - List of tokens sorted by their correlation with the target token, in descending order, limited to the top n tokens.
    """
    df.sort_values(by='date', inplace=True)
    pivoted_df = df.pivot(index='date', columns='token', values='price')
    lagged_df = pivoted_df.shift(periods=lag_days)
    target_series = pivoted_df[target_token]

    correlations = {}

    for token in lagged_df.columns:
        if token != target_token:  # Skip comparing the target token with itself
            valid_indices = target_series.notna() & lagged_df[token].notna()
            corr = target_series[valid_indices].corr(lagged_df[token][valid_indices])
            correlations[token] = corr

    sorted_tokens = sorted(correlations, key=correlations.get, reverse=True)[:n]
    
    return sorted_tokens

def daily_price_dateset_manipulation():
    """
    Manipulates and prepares the daily price dataset for modeling, including lagged correlation calculation and feature engineering.
    
    Returns:
    - df_final: The final DataFrame ready for modeling.
    """
    daily_token_prices = LOADER.load('tokens-daily-prices-mcap-volume')
    print(daily_token_prices.head)
    df = daily_token_prices.to_pandas()
    correlations = calculate_lagged_correlations(df, target_token=TOKEN_NAME)

def apy_dateset_manipulation():
    """
    Manipulates the APY dataset to focus on specific tokens and reshape it for easier analysis.

    Returns:
    - apy_df_token: The manipulated APY dataFrame
    """

def tvl_dataset_manipulation():
    """
    Manipulates the TVL dataset to focus on specific projects and tokens, reshaping it for analysis.

    Returns:
    - tvl_df: The manipulated TVL DataFrame
    """