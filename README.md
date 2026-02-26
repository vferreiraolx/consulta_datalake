# Trino Connection Script# Trino Connection Script



This script connects to a Trino datalake using PyHive.This script connects to a Trino datalake using PyHive.



## Prerequisites## Prerequisites



- Python 3.13 or higher- Python 3.13 or higher

- PyHive library (install with `pip install -r requirements.txt`)- PyHive library (install with `pip install -r requirements.txt`)



## Setup## Setup



1. Copy `.env.example` to `.env` and fill in your actual connection details and credentials.1. Copy `.env.example` to `.env` and fill in your actual connection details and credentials.

2. Ensure `.env` is added to `.gitignore` to prevent committing sensitive information.2. Ensure `.env` is added to `.gitignore` to prevent committing sensitive information.



## Usage## Usage



Set the environment variables for connection (or use the .env file):Set the environment variables for connection (or use the .env file):



- `TRINO_HOST`: Hostname of the Trino server (default: https://trino-gateway.dataeng.bigdata.olxbr.io)- `TRINO_HOST`: Hostname of the Trino server (default: localhost)

- `TRINO_PORT`: Port of the Trino server (default: 443)- `TRINO_PORT`: Port of the Trino server (default: 8080)

- `TRINO_USER`: Username for authentication (without @olxbr.com)- `TRINO_USER`: Username for authentication

- `TRINO_PASSWORD`: Password for authentication- `TRINO_PASSWORD`: Password for authentication

- `TRINO_CATALOG`: Catalog to use (default: hive)- `TRINO_CATALOG`: Catalog to use (default: default)

- `TRINO_SCHEMA`: Schema to use (default: default)- `TRINO_SCHEMA`: Schema to use (default: default)



Run the script:Run the script:



```bash```bash

python connect_trino.pypython connect_trino.py

``````



The script will attempt to connect and run a test query.The script will attempt to connect and run a test query.



## Notes## Notes



- Credentials are read from environment variables or .env file to avoid hard-coding.- Credentials are read from environment variables or .env file to avoid hard-coding.

- For the OLX datalake, use appropriate host and credentials as per the documentation.- For the OLX datalake, use appropriate host and credentials as per the documentation.



## Troubleshooting## Troubleshooting



- Ensure environment variables are set or .env file is present.- Ensure environment variables are set or .env file is present.

- Check network connectivity to the Trino server.- Check network connectivity to the Trino server.

- Verify credentials are correct.- Verify credentials are correct.