# Data Science Academy

# Importa o módulo `uuid` para gerar identificadores únicos universais
import uuid

# Importa classes relacionadas a data e hora
from datetime import datetime, timedelta

# Importa as classes principais do Airflow para criar DAGs
from airflow import DAG
##
# Importa o operador Python do Airflow para execução de funções Python como tarefas
from airflow.operators.python import PythonOperator

# Define os argumentos padrão da DAG, incluindo o proprietário e a data de início
default_args = {"owner": "Jonas Lomiler",
                "start_date": datetime(2025, 1, 9, 8, 10)}
# Define a DAG do Airflow
with DAG("teste",
         # Define os argumentos padrão da DAG
         default_args=default_args,
         # Define o agendamento da DAG como uma vez por dia
         schedule=timedelta(days=1),
         # Impede a execução retroativa da DAG
         catchup=False,
) as dag:
    # Define a tarefa que faz o streaming de dados
    streaming_task = PythonOperator(task_id="teste", 
                                    python_callable=dsa_stream_dados)




