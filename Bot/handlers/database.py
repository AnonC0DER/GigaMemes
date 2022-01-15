import psycopg2 as pgs
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
######################################### DATABASE 

# Connect to database and create the table

# You may need to use CREATE DATABASE dbname; before you create connection
## Get values from .env file
conn = pgs.connect(
    host=os.getenv('BOT_DB_HOST'),
    database=os.getenv('DATABASE'),
    user=os.getenv('BOT_DB_USER'),
    password=os.getenv('BOT_DB_PASSWORD'),
)

# create gigadb and its columns if they don't exists
create_table = '''
    CREATE TABLE IF NOT EXISTS gigadb (
        UserID INT NOT NULL,
        UserToken VARCHAR(450) NOT NULL,
        
        UNIQUE (UserID)
    );
'''

cur = conn.cursor()
cur.execute(create_table)
conn.commit()
cur.close()


######################################### Functions
def Get_token_from_db(id):
    query = f'''SELECT usertoken FROM gigadb WHERE userid={id};'''
    cur = conn.cursor()
    cur.execute(query)
    Get_result = cur.fetchone()
    cur.close()

    try:
        result = Get_result[0]
        return result
    except:
        result = None
        return result


def Add_new_token(id, token):
    '''Save user chat ID and token in database'''
    # Insert values into gigadb table
    insert_into_table = f'''
    INSERT INTO gigadb (UserID, UserToken)
    VALUES ({id}, '{token}');
    '''

    cur = conn.cursor()
    cur.execute(insert_into_table, ('gigadb',))
    conn.commit()
    cur.close()
        

def Update_token(id, token):
    '''Update token value for existing column'''
    # Update column query
    Update_column = f'''
    UPDATE gigadb
    SET usertoken = '{token}'
    WHERE userid = {id};
    '''

    cur = conn.cursor()
    cur.execute(Update_column)
    conn.commit()
    cur.close()




# Add_new_token(667, 'oolpl')
# print(Get_token_from_db(667))