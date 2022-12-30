from google.cloud import bigquery
import os 
import pandas as pd


'''
  $ pip install --upgrade google-cloud
  $ pip install --upgrade google-cloud-bigquery
  $ pip install --upgrade google-cloud-storage
'''

credentials_path = '/home/druestaples/myfiles/bigquery_practice/bigquery-demo-reference/cogent-density-239117-263a9c7f3ac0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
print(client)


table_id = 'cogent-density-239117.my_dataset_1.mytable-2'
dataset_id = 'cogent-density-239117.my_dataset_1'
# print(client.get_dataset(dataset_id))

# Big Query Public Dataset
# query_job = client.query('''SELECT homeTeamName, awayTeamName, attendance FROM `bigquery-public-data.baseball.schedules` LIMIT 10''')
# x =list(query_job.result())
# print(x)


# Convert table to pandas dataframe
# ds = client.get_dataset(dataset_id)
# query_job = client.query(f'''SELECT * FROM `{table_id}`''')
# df = query_job.to_dataframe()



# SELECT, CREATE, UPDATE, INSERT, DELET

# SELECT ROW
query_job = client.query(f'''SELECT * FROM `{table_id}` LIMIT 10''')
# SELECT COLUMN NAMES
# column_names = client.query(f'''SELECT column_name FROM `cogent-density-239117.my_dataset_1`.INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'mytable-2' ''')
# SELECT column_name FROM `cogent-density-239117.my_dataset_1`.INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'mytable-2'
# movie_selection = 'Hackers'
# query_select = client.query(f'''SELECT * FROM `{table_id}` WHERE movie='{movie_selection}' ''')

# INSERT - Be careful as this will add duplicate fields
# query_insert = client.query(f'''INSERT INTO `{table_id}` VALUES (61, 'The Batman', 0.5, 0.7, 0.2)''')


# UPDATE
# query_select = client.query(f'''SELECT * from `{table_id}`''')
# query_update = client.query(f'''UPDATE `{table_id}` SET movie = 'Loki' WHERE movie = 'The Batman' ''')

# DELETE
# -- DELETE FROM `cogent-density-239117.my_dataset_1.mytable-2` WHERE movie = 'Ex Machina'



if __name__ == '__main__':
    select =list(query_job.result())
    print(select)
    # update = query_insert.result()
    # print(update)
    # columns = list(column_names.result())
    # print(columns)
    # for row in column_names.result():
    #     print(row[0])
    # print(df)
    # qs = list(query_select.result())
    # print(qs)
    # for i in qs:
    #     print(i[1], '\n')
  # qu = query_update.result()
  # for i in qu:
  #   print(i)
