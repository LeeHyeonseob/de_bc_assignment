from pyspark.sql import SparkSession

WAREHOUSE = "s3://iceberg-prac-260814/warehouse/"

def build_spark():
    return (SparkSession.builder
            .appName("IcebergGlueLab")
            .config("spark.jars.packages",
                    "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.7.1,"
                    "org.apache.iceberg:iceberg-aws-bundle:1.7.1")
            .config("spark.sql.extensions",
                    "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
            .config("spark.sql.catalog.glue_catalog",
                    "org.apache.iceberg.spark.SparkCatalog")
            .config("spark.sql.catalog.glue_catalog.catalog-impl",
                    "org.apache.iceberg.aws.glue.GlueCatalog")
            .config("spark.sql.catalog.glue_catalog.io-impl",
                    "org.apache.iceberg.aws.s3.S3FileIO")
            .config("spark.sql.catalog.glue_catalog.client.region", "ap-northeast-2")
            .config("spark.sql.catalog.glue_catalog.warehouse", WAREHOUSE)
            .getOrCreate()
            )

if __name__ == "__main__":
        spark = build_spark()