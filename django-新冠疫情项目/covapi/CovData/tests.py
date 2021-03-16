from django.test import TestCase
from .read_csv import ReadCsv


# Create your tests here.
class GetFileDataTest(TestCase):
    def test_get_data(self):
        file = ReadCsv("死亡比例")
        labels = ['境外输入', '孝感', '宜昌', '荆州', '黄冈', '十堰', '鄂州', '仙桃', '黄石', '武汉', '襄阳', '荆门', '天门', '潜江', '恩施州', '神农架', '随州', '咸宁']
        data = ['0.00', '3.67', '3.97', '3.29', '4.30', '1.19', '4.23', '3.83', '3.84', '7.69', '3.40', '4.42', '3.02', '4.55', '2.78', '0.00', '3.44', '1.79']
        self.assertEqual(file.labels, labels)
        self.assertEqual(file.data, data)
