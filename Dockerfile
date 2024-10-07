FROM quay.io/astronomer/astro-runtime:12.1.1

# Add your other necessary dependencies like installing packages here
COPY secret.json /usr/local/airflow/secret.json
