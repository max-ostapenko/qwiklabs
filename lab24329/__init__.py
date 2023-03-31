import pulumi
from pulumi_google_native.storage import v1 as storage
from pulumi_google_native.sqladmin import v1beta4 as sql


def main():
    # Creates a new Cloud SQL instance.
    instance = sql.Instance(
        "lab-instance",
        name="qwiklabs-demo",
        database_version=sql.InstanceDatabaseVersion.MYSQL57,
        settings={
            "tier": "db-n1-standard-1",
        },
    )

    # Create a GCS bucket
    bucket = storage.Bucket("lab-bucket")

    # upload start_station_name.csv to bucket
    storage.BucketObject(
        "start_station_name",
        name="start_station_name.csv",
        bucket=bucket.name,
        source=pulumi.FileAsset("./lab24329/start_station_name.csv"),
    )

    # upload end_station_name.csv to bucket
    storage.BucketObject(
        "end_station_name",
        name="end_station_name.csv",
        bucket=bucket.name,
        source=pulumi.FileAsset("./lab24329/end_station_name.csv"),
    )

    # create Cloud SQL database
    sql.Database("lab-database", instance=instance.name, name="bike")
