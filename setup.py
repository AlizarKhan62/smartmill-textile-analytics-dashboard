import snowflake.connector

conn = snowflake.connector.connect(
    user='ALIZARKHAN22',
    password='Qasimsial51214@',  # 👈 Enter your actual Snowflake password
    account='DODLRUL-DZ00212',
    role='ACCOUNTADMIN',
    warehouse='COMPUTE_WH',
    database='SMARTMILL_DB',
    schema='TEXTILE_ANALYTICS'
)

cs = conn.cursor()
cs.execute("SELECT CURRENT_VERSION()")
print(cs.fetchone())
cs.close()
conn.close()
