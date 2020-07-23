from Resource.ui_Search_main import Ui_MainWindow
from PyQt5.Qt import *
from Function.loadData import get_data_from_aliyun
import sys


class SearchPane(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle('搜索内容')
        self.setupUi(self)
        # 获得领域数据
        df_cate = get_data_from_aliyun(user='sheep431', password='xssxyby198566', db='novel',
                                       host='sheep431.mysql.rds.aliyuncs.com',
                                       sql='SELECT distinct fCategory FROM wuxia ')
        list_cate = [x[0] for x in df_cate.values.tolist()]
        item = QTreeWidgetItem()
        items = [item.setText(list_cate.index(x),x) for x in list_cate]
        self.treeWidget.addTopLevelItems(items)
        # # 获得作品数据
        # df_works = get_data_from_aliyun(user='sheep431', password='xssxyby198566', db='novel',
        #                                 host='sheep431.mysql.rds.aliyuncs.com',
        #                                 sql='SELECT distinct fWorkName FROM wuxia ')
        # list_works = df_works.values.tolist()
        # self.comboBox_works.addItems([x[0] for x in list_works])
        # # 获得作者数据
        # df_author = get_data_from_aliyun(user='sheep431', password='xssxyby198566', db='novel',
        #                                  host='sheep431.mysql.rds.aliyuncs.com',
        #                                  sql='SELECT distinct fAuthor FROM wuxia ')
        # list_author = df_author.values.tolist()
        # self.comboBox_author.addItems([x[0] for x in list_author])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # QWidget控件的父子关系()
    window = SearchPane()
    # window = QWidget()

    window.show()

    sys.exit(app.exec_())
