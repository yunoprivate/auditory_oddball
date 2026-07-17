import csv
import datetime
from pathlib import Path

def csv_writer(folder: str, logs: list, id: str=''):
    '''csvファイルに書き込み
    
    folder: csvファイルのフォルダー
    logs: データ (list型)
    

    '''

    if not logs:
        return
    
    today = datetime.date.today()
    time = f'{today.year}_{today.month}_{today.day}'
    filename = time + f'_{id}'

    Path(folder).mkdir(exist_ok=True)

    for i, log in enumerate(logs):
        with open(f'{folder}/{filename}{i}.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=log[0].keys())
            writer.writeheader()
            writer.writerows(log)
