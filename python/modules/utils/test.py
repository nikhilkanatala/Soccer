import pyodbc

# Get connection details from Azure Portal
server = 'nkanatala.database.windows.net'
database = 'development'
username = 'nkanatala'
password = 'Julius@1298'
driver = '{ODBC Driver 17 for SQL Server}'

# Construct connection string
conn_str = f'DRIVER={driver};SERVER=tcp:{server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

# Connect to the database
with pyodbc.connect(conn_str) as conn:
    with conn.cursor() as cursor:
        # Execute a query
        cursor.execute("SELECT TOP 3 * FROM sys.objects")

        # Fetch results
        rows = cursor.fetchall()
        for row in rows:
            print(row)