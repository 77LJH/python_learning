from Case.面向对象案例.data_define import Record
import json
from typing import List


class FileReader:
    def read_data(self, data_path: str) -> List[Record]:
        """
        读取文件的数据，读到的每一条数据都转换为Record对象，将它们封装到list并返回。
        :param data_path: 数据文件路径
        :return: 包含Record对象的列表
        """
        raise NotImplementedError("Subclasses should implement this method.")


class TextFileReader(FileReader):
    def read_data(self, data_path: str) -> List[Record]:
        record_list = []
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                for line in f:
                    data_list = line.strip().split(',')
                    record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                    record_list.append(record)
        except FileNotFoundError:
            print(f"File not found: {data_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return record_list


class JsonFileReader(FileReader):
    def read_data(self, data_path: str) -> List[Record]:
        record_list = []
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                for line in f:
                    data_dict = json.loads(line.strip())
                    record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']),
                                    data_dict['province'])
                    record_list.append(record)
        except FileNotFoundError:
            print(f"File not found: {data_path}")
        except json.JSONDecodeError:
            print(f"JSON decoding error in file: {data_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return record_list
