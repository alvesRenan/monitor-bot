from logger import Log
from threading import Thread
from time import sleep

from kubernetes import client, config


class MonitorTask:

    def __init__(self, mercurio_bot, chat_id, app_name) -> None:
        self.CONFIG = config.load_incluster_config()
        self.CLI = client.CoreV1Api()
        self.STATUS = 'Stopped'

        self.MERCURIO = mercurio_bot
        self.CHAT_ID = chat_id
        self.APP_NAME = app_name
    
    def run(self):
        Thread( target=self.monitor_task ).start()

    def check_status(self):
        pods = self.CLI.list_pod_for_all_namespaces(watch=False)

        for pod in pods.items:
            if pod.metadata.labels.get('app') == self.APP_NAME:
                return pod.status.phase
        
        return None

    def monitor_task(self) -> None:
        erro_notification_sent = False

        while True:
            NEW_STATUS = self.check_status()
            Log().log(f'Status atual da aplicação {self.APP_NAME}: {NEW_STATUS}')

            if self.STATUS == None:
                if not erro_notification_sent:
                    monitor_status_text = 'Não foi possível checar o status da aplicação, ela pode ter caído ou está sendo atualizada.'
                    self.MERCURIO.send_message(self.CHAT_ID, monitor_status_text)

                    erro_notification_sent = True
                

            if NEW_STATUS != self.STATUS:
                monitor_status_text = f'O estado da aplicação {self.APP_NAME} mudou, o atual estado é: {NEW_STATUS}.'
                self.MERCURIO.send_message(self.CHAT_ID, monitor_status_text)

                erro_notification_sent = False

            
            self.STATUS = NEW_STATUS
            
            sleep(1)