import json
from threading import Thread
from time import sleep

import requests

from logger import Log


class MonitorAPI:

    def __init__(self, mercurio_bot, chat_id) -> None:
        self.STATUS = 'Stopped'

        self.MERCURIO = mercurio_bot
        self.CHAT_ID = chat_id
    
    def run(self):
        Thread( target=self.monitor_api ).start()

    def monitor_api(self) -> None:
        last_status = 200

        while True:
            try:
                res = json.loads( requests.get('http://test-app:5000/status').text )
                code = res.get('code')
                Log().log(f'Status retornado pela API: {res.text}')

                if last_status != code:
                    if code == 200:
                        text = f'API retornou status {code}'

                    if code != 200:
                        text = f'Error: API retornou status {code}'
                    
                    self.MERCURIO.send_message(self.CHAT_ID, text)
                
                last_status = res.get('code')
                    
            except:
                Log().log(f'Erro ao tentar acessar a API')
            
            sleep(1)