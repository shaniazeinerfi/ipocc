    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to fetch.
    # table_id = "your-project.your_dataset.your_table_name"

    table = client.get_table(table_id)  # API request

    print(
        "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
    )  
