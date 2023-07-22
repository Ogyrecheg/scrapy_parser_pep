import csv
import datetime as dt
from collections import defaultdict
from typing import Dict, List, Tuple, Union

from scrapy import item
from scrapy.exceptions import DropItem

from .constants import BASE_DIR, DATETIME_FORMAT, FILE_NAME, OUTPUT_DIR


class PepParsePipeline:
    def open_spider(self, spider) -> None:
        """Фиксируем время старта паука."""

        self.status_sum: Dict[str, int] = defaultdict(int)
        self.start_time: str = dt.datetime.now().strftime(DATETIME_FORMAT)

    def process_item(self, item: item, spider) -> item:
        """Подсчитываем количество статусов."""

        if not item['status']:
            raise DropItem('Статус отсутствует!')
        self.status_sum[item['status']] += 1

        return item

    def close_spider(self, spider) -> None:
        """Формируем csv файл с результатами парсинга."""

        results: List[Tuple[str, Union[str, int]]] = [('Cтатус', 'Количество')]
        for status in self.status_sum:
            results.append((status, self.status_sum[status]))
        results.append(('Total', sum(self.status_sum.values())))

        results_dir = BASE_DIR / OUTPUT_DIR
        results_dir.mkdir(exist_ok=True)
        file_name = f'{FILE_NAME}_{self.start_time}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
