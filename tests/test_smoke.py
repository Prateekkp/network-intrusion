from pathlib import Path
import polars as pl


def test_environment_imports():
    """Verify core dependencies are installed and importable."""
    import matplotlib
    import pandas
    import pyarrow
    import sklearn
    import xgboost

    assert True


def test_parquet_datasets_exist():
    """Verify committed parquet datasets exist and are non-empty."""
    train_path = Path("dataset/train_full.parquet")
    test_path = Path("dataset/test_full.parquet")

    assert train_path.exists(), "dataset/train_full.parquet does not exist"
    assert test_path.exists(), "dataset/test_full.parquet does not exist"

    df_train = pl.read_parquet(train_path)
    df_test = pl.read_parquet(test_path)

    assert df_train.height > 0, "Train parquet dataset is empty"
    assert df_test.height > 0, "Test parquet dataset is empty"
