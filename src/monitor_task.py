from time import sleep
from kubernetes import client, config

CONFIG = config.load_incluster_config()
CLI = client.CoreV1Api()
STATUS = 'Running'

def check_status(app_name):
    pods = CLI.list_pod_for_all_namespaces(watch=False)

    for pod in pods.items:
        if pod.metadata.labels.get('app') == app_name:
            return pod.status.phase
    
    return None

def monitor_task(mercurio, id, app_name):
    NEW_STATUS = check_status(app_name)

    if STATUS == None:
        monitor_status_text = f'Aplicação não encontrada'
        mercurio.send_message(id, monitor_status_text)

    if NEW_STATUS != STATUS:
        monitor_status_text = f'O estado da aplicação mudou, o atual estado é: {NEW_STATUS}'
        mercurio.send_message(id, monitor_status_text)

    STATUS = NEW_STATUS
    
    sleep(5)

        
