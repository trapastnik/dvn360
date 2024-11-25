
import os
import mysql.connector
import chardet

def execute_sql_script(database_config, sql_script_path):
    with open(sql_script_path, 'rb') as sql_file:
        raw_data = sql_file.read()
        encoding = chardet.detect(raw_data)['encoding']
        sql_script = raw_data.decode(encoding)

    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Split the script into individual statements and execute them one by one
        statements = sql_script.split(';')
        for statement in statements:
            if statement.strip():
                cursor.execute(statement)

        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error executing SQL script at statement: {statement}\nDetails: {e}")
        return False

def check_consistency(database_config):
    try:
        conn = mysql.connector.connect(**database_config)
        cursor = conn.cursor()

        cursor.execute("CHECK TABLES")
        for result in cursor.fetchall():
            if result[1] == "OK":
                print("The table '{}' is consistent.".format(result[0]))
            else:
                print("The table '{}' is not consistent. Details: {}".format(result[0], result[2]))

        cursor.close()
        conn.close()
    except Exception as e:
        print("Error: ", e)

# Replace these values with your actual MySQL database configuration
database_config = {
    'host': 'localhost',
    'user': 'dvn',
    'password': 'Protivofazaqscgu9',
    'database': 'musicseasi_org.sql'
}

# Replace this path with the actual SQL script file path
sql_script_path = '/Users/a/Desktop/musicseasi_org.sql'

if execute_sql_script(database_config, sql_script_path):
    check_consistency(database_config)