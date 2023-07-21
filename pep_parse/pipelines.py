import csv
import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from .constants import BASE_DIR, DATETIME_FORMAT, FILE_NAME


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_sum = defaultdict(int)
        self.start_time = dt.datetime.now().strftime(DATETIME_FORMAT)

    def process_item(self, item, spider):
        if item['status']:
            self.status_sum[item['status']] += 1
        else:
            raise DropItem('Статус отсутствует!')

        return item

    def close_spider(self, spider):
        results = [('Cтатус', 'Количество')]
        for status in self.status_sum:
            results.append((status, self.status_sum[status]))
        results.append(('Total', sum(self.status_sum.values())))

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'{FILE_NAME}_{self.start_time}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
