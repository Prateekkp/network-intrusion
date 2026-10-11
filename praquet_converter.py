import polars as pl

pl.read_csv("./dataset/UNSW_NB15_training-set.csv").write_parquet("./dataset/train_full.parquet")

pl.read_csv("./dataset/UNSW_NB15_testing-set.csv").write_parquet("./dataset/test_full.parquet")