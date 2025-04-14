
import mysql.connector

def run_sql_script(cursor, script_path):
    with open(script_path, 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            command = command.strip()
            if command:
                cursor.execute(command)

def main():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        cursor = connection.cursor()
        run_sql_script(cursor, 'schema/zoom_bot_schema.sql')
        connection.commit()
        print("✅ Database and tables created successfully.")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
