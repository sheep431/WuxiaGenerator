from source.login_ui import Ui_Form
from PyQt5.Qt import *

class LoginPane(QWidget, Ui_Form):
    show_register_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        movie = QMovie("./source/login_top_bg.gif")
        movie.setScaledSize(QSize(539, 170))
        self.label.setMovie(movie)
        movie.start()