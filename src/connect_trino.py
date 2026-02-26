from dotenv import load_dotenv
import os
from pyhive import trino

# Load environment variables from .env file
load_dotenv()

# Get connection details from environment variables
host = os.getenv('TRINO_HOST', 'trino-gateway.dataeng.bigdata.olxbr.io')  # Default to the documented host
port = int(os.getenv('TRINO_PORT', '443'))  # Default to the documented port
username = os.getenv('TRINO_USER')
password = os.getenv('TRINO_PASSWORD')

# Check if credentials are provided
if not username or not password:
    raise ValueError("TRINO_USER and TRINO_PASSWORD environment variables must be set.")

# Connect to Trino
try:
    conn = trino.connect(
        host=host,
        port=port,
        protocol='https',
        source='dataeng-trino-api',
        username=username,
        password=password
    )
    print("Connected to Trino successfully.")
    
    # Simple query to test
    cursor = conn.cursor()
    cursor.execute('SELECT 1 as test')
    result = cursor.fetchall()
    print("Test query result:", result)
    
    cursor.close()
    conn.close()
    print("Connection closed.")
except Exception as e:
    print(f"Error connecting to Trino: {e}")