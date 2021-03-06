import sys
import Auth_SQL
from PyQt5.QtWidgets import *
from PyQt5 import uic
import inlove
import N2_3_DspecMODIFY



N2_3_DUI = uic.loadUiType("C:/DengDengE/N2_3_D.ui")[0]
class N2_3_DDialog(QDialog, N2_3_DUI):
    def __init__(self,value, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        #label_a 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT name FROM family where id = 'n2_3_D' ")
        text_edit_a = Auth_SQL.cur.fetchone()[0]
        self.label_a.setText(text_edit_a)

        # label_b 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT position FROM family where id = 'n2_3_D' ")
        text_edit_b = Auth_SQL.cur.fetchone()[0]
        self.label_b.setText(text_edit_b)

        # label_c 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT birthday FROM family where id = 'n2_3_D'; ")
        text_edit_c = Auth_SQL.cur.fetchone()[0]
        self.label_c.setText(text_edit_c)

        # label_d 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT special FROM family where id = 'n2_3_D'; ")
        text_edit_d = Auth_SQL.cur.fetchone()[0]
        self.label_d.setText(text_edit_d)

        # label_e 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT tel FROM family where id = 'n2_3_D'; ")
        text_edit_e = Auth_SQL.cur.fetchone()[0]
        self.label_e.setText(text_edit_e)

        # 메모지 수정_ 조회해서 가져오기
        Auth_SQL.cur.execute("SELECT memo FROM family where id = 'n2_3_D'; ")
        text_edit_m = Auth_SQL.cur.fetchone()[0]
        self.plainTextEdit_m.setPlainText(text_edit_m)

    def nachHause_click_open(self):
        self.inLoveopen = inlove.InLove()
        self.inLoveopen.show()
        self.close()

    #spec 수정하는 창 열기
    def N2_3_DspecMODIFY(self):
        self.n2_3_DspecMODIFYopen = N2_3_DspecMODIFY.N2_3_DspecMODIFY_Dialog(self)
        self.n2_3_DspecMODIFYopen.show()
        self.close()



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     N3_4D = N3_4Dialog()
#     N3_4D.show()
#     app.exec_()