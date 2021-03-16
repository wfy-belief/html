class ReadCsv(object):
    __slots__ = ['labels', 'data', 'dir']

    def __init__(self, directory):
        self.dir = directory
        self.labels = None
        self.data = None
        self.__build()

    def __build(self):
        self.labels = self.__get_labels()
        self.data = self.__get_data()

    def __get_labels(self):
        try:
            with open(f"static/csv/{self.dir}/城市.csv", 'r', encoding='UTF-8') as file:
                labels = file.read().split(',')
                file.close()
            return labels
        except Exception as e:
            print(e)
        return ""

    def __get_data(self):
        try:
            with open(f"static/csv/{self.dir}/数据.csv", 'r', encoding='UTF-8') as file:
                data = file.read().split(',')
                data = list(map(int, data))
                file.close()
            return data
        except Exception as e:
            print(e)
        return ""

    def dump_as_json(self):
        data = {
            'status': '200',
            'labels': self.labels,
            'data': self.data
        }
        return data
