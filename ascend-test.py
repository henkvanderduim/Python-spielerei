# import libraries
import pyarrow.parquet as pq
import s3fs

# Instantiate s3fs with Ascend Configuration
s3 = s3fs.S3FileSystem(
    key="<Ascend Access Key>",
    secret="<Ascend Secret Key>",
    client_kwargs={"endpoint_url": "https://s3.ascend.io"},
    config_kwargs={"s3": {"addressing_style": "virtual"}},
)

# Read in Data from Parquet Files
pandas_dataframe = (
    pq.ParquetDataset("s3://trial/ACME/NYC_Taxi/Weather", filesystem=s3)
    .read_pandas()
    .to_pandas()
)
