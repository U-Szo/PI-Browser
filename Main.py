import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
import StyleSheets as ss
import SelectAllLineEditClass as sle

class Ui_MainBrowserWindow(object):
	def setupUi(self, MainBrowserWindow):
		MainBrowserWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		MainBrowserWindow.setStyleSheet(ss.main_window_stylesheet)
		MainBrowserWindow.setWindowIcon((QtGui.QIcon("main_window_icons/Logoicon.png")))
		self.central_widget = QtWidgets.QWidget(MainBrowserWindow)
		####################
		##MAIN GRID LAYOUT##
		####################
		self.main_grid_layout = QtWidgets.QGridLayout()
		self.main_grid_layout.setSpacing(0)
		self.main_grid_layout.setContentsMargins(0, 0, 0, 0)
		self.central_widget.setLayout(self.main_grid_layout)

		############
		##TITLEBAR##
		############
		self.title_bar_frame = QtWidgets.QFrame()
		self.title_bar_frame.setFixedHeight(29)
		self.title_bar_frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
		self.title_bar_frame.setStyleSheet(ss.title_bar_frame_stylesheet_window_normal)
		self.title_bar_frame_horizontal_layout = QtWidgets.QHBoxLayout()
		self.title_bar_frame_horizontal_layout.setContentsMargins(4, 0, 0, 0)

		self.title_bar_widgets_names=["deco_button","title_bar_spacer","minimize_button","maximize_button","exit_button"]
		self.title_bar_widgets_stylesheets=[ss.deco_button_stylesheet, ss.minimize_button_stylesheet,
		ss.maximize_button_stylesheet, ss.exit_button_stylesheet_window_normal]
		self.title_bar_widgets_icons=["main_window_icons/DecoButtonicon.png", "main_window_icons/MinimizeButtonicon.png",
		"main_window_icons/MaximizeButtonicon.png", "main_window_icons/ExitButtonicon.png"]
		self.title_bar_widgets_dict,title_bar_loop_counter={},0
		for x in self.title_bar_widgets_names:
			if x == "title_bar_spacer":
				self.title_bar_widgets_dict[x] = QtWidgets.QFrame()
				self.title_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(16777215, 29))
				self.title_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(16777215, 29))
				self.title_bar_frame_horizontal_layout.addWidget(self.title_bar_widgets_dict[x])
			else:
				self.title_bar_widgets_dict[x] = QtWidgets.QPushButton(self.title_bar_frame)
				title_bar_button_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
				self.title_bar_widgets_dict[x].setSizePolicy(title_bar_button_size_policy)
				self.title_bar_widgets_dict[x].setStyleSheet(self.title_bar_widgets_stylesheets[title_bar_loop_counter])
				title_bar_button_icon = QtGui.QIcon()
				title_bar_button_icon.addPixmap(QtGui.QPixmap(self.title_bar_widgets_icons[title_bar_loop_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				self.title_bar_widgets_dict[x].setIcon(title_bar_button_icon)
				if x =="deco_button":
					self.title_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(100, 21))
					self.title_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(100, 21))
					self.title_bar_widgets_dict[x].setIconSize(QtCore.QSize(100, 21))
				else:
					self.title_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(51, 29))
					self.title_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(51, 29))
					if x == "maximize_button":
						self.title_bar_widgets_dict[x].setIconSize(QtCore.QSize(18, 18))
					else:
						self.title_bar_widgets_dict[x].setIconSize(QtCore.QSize(21, 21))
				self.title_bar_frame_horizontal_layout.addWidget(self.title_bar_widgets_dict[x])
				title_bar_loop_counter+=1
		self.title_bar_frame.setLayout(self.title_bar_frame_horizontal_layout)

		##################
		##NAVIGATION BAR##
		##################
		self.nav_frame = QtWidgets.QFrame()
		nav_frame_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		self.nav_frame.setSizePolicy(nav_frame_size_policy)
		self.nav_frame.setMinimumSize(QtCore.QSize(0, 50))
		self.nav_frame.setMaximumSize(QtCore.QSize(16777215, 50))
		self.nav_frame.setStyleSheet(ss.nav_frame_stylesheet)
		self.nav_frame_horizontal_layout = QtWidgets.QHBoxLayout(self.nav_frame)
		self.nav_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)

		#################
		##URL LINE EDIT##
		#################
		self.adress_line_edit = sle.SelectAllLineEdit(self.nav_frame)
		self.adress_line_edit.setMinimumSize(QtCore.QSize(50, 25))
		self.adress_line_edit.setMaximumSize(QtCore.QSize(16777215, 25))
		self.adress_line_edit.setStyleSheet(ss.adress_line_edit_stylesheet)
		self.adress_line_edit.setPlaceholderText("http://...")
		self.adress_line_edit.returnPressed.connect(self.goToNewAdress)

		################
		##BROWSER TABS##
		################
		self.browser_tabs = QtWidgets.QTabWidget()
		self.browser_tabs.setTabsClosable(True)
		self.browser_tabs.setStyleSheet(ss.browser_tabs_stylesheet)
		self.browser_tabs.currentChanged.connect(self.tabChanged)
		self.browser_tabs.tabCloseRequested.connect(self.closeTab)
		self.newTab("http://www.google.com","Google")
		self.browser_tabs_add_button = QtWidgets.QPushButton()
		self.browser_tabs_add_button.setMinimumSize(QtCore.QSize(24, 24))
		self.browser_tabs_add_button.setMaximumSize(QtCore.QSize(24, 24))
		self.browser_tabs_add_button.setText('')
		browser_tabs_add_button_icon = QtGui.QIcon()
		browser_tabs_add_button_icon.addPixmap(QtGui.QPixmap("main_window_icons/TabAddButtonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.browser_tabs_add_button.setIcon(browser_tabs_add_button_icon)
		self.browser_tabs_add_button.setIconSize(QtCore.QSize(23, 23))
		self.browser_tabs_add_button.setStyleSheet(ss.browser_tabs_add_button_stylesheet)
		self.browser_tabs.setCornerWidget(self.browser_tabs_add_button,corner=QtCore.Qt.Corner.BottomRightCorner)
		self.browser_tabs_add_button.clicked.connect(self.addTabButtonClicked)

		###################
		##NAV BAR WIDGETS##
		###################
		nav_spacer_left = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
		self.nav_frame_horizontal_layout.addItem(nav_spacer_left)

		self.nav_bar_widgets_names=["back_button","foward_button","reload_button","home_button"]
		self.nav_bar_widgets_stylesheets=[ss.back_button_stylesheet,ss.foward_button_stylesheet,
		ss.reload_button_stylesheet,ss.home_button_stylesheet]
		self.nav_bar_widgets_icons=["main_window_icons/BackButtonicon.png","main_window_icons/FowardButtonicon.png",
		"main_window_icons/ReloadButtonicon.png","main_window_icons/HomeButtonicon.png"]
		self.nav_bar_widgets_methods=[self.goBackTab,self.goFowardTab,self.reloadTab,self.goHome]
		self.nav_bar_widgets_dict,nav_bar_loop_counter={},0
		for x in self.nav_bar_widgets_names:
			self.nav_bar_widgets_dict[x] = QtWidgets.QPushButton(self.nav_frame)
			self.nav_bar_widgets_dict[x].setStyleSheet(self.nav_bar_widgets_stylesheets[nav_bar_loop_counter])
			nav_bar_button_icon = QtGui.QIcon()
			nav_bar_button_icon.addPixmap(QtGui.QPixmap(self.nav_bar_widgets_icons[nav_bar_loop_counter]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.nav_bar_widgets_dict[x].setIcon(nav_bar_button_icon)
			self.nav_bar_widgets_dict[x].clicked.connect(self.nav_bar_widgets_methods[nav_bar_loop_counter])
			nav_bar_loop_counter+=1
			if x == "reload_button":
				self.nav_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(34, 34))
				self.nav_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(34, 34))
				self.nav_bar_widgets_dict[x].setIconSize(QtCore.QSize(23, 23))
				self.nav_frame_horizontal_layout.addWidget(self.nav_bar_widgets_dict[x])
			elif x == "home_button":
				self.nav_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(25, 25))
				self.nav_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(25, 25))
				self.nav_bar_widgets_dict[x].setIconSize(QtCore.QSize(25, 25))
			else:
				self.nav_bar_widgets_dict[x].setMinimumSize(QtCore.QSize(40, 40))
				self.nav_bar_widgets_dict[x].setMaximumSize(QtCore.QSize(40, 40))
				self.nav_bar_widgets_dict[x].setIconSize(QtCore.QSize(27, 27))
				self.nav_frame_horizontal_layout.addWidget(self.nav_bar_widgets_dict[x])

		self.nav_frame_horizontal_layout.addWidget(self.adress_line_edit)
		self.nav_frame_horizontal_layout.addWidget(self.nav_bar_widgets_dict["home_button"])
		nav_spacer_right = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
		self.nav_frame_horizontal_layout.addItem(nav_spacer_right)

		self.main_grid_layout.addWidget(self.nav_frame,1,0)
		self.main_grid_layout.addWidget(self.title_bar_frame,0,0)
		self.main_grid_layout.addWidget(self.browser_tabs,2,0)

		MainBrowserWindow.setCentralWidget(self.central_widget)
		main_browser_window_size_grip = QtWidgets.QSizeGrip(MainBrowserWindow)
		main_browser_window_size_grip.setStyleSheet("background-color: transparent;\n")

	def newTab(self,newtaburl="",title="New Tab"):
		tab_web_view = QWebEngineView()
		tab_web_view.setUrl(QtCore.QUrl(newtaburl))
		tab_web_view.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
		tab_web_view.urlChanged.connect(self.updateAdress)
		tab_index = self.browser_tabs.addTab(tab_web_view,title)
		tab_web_view.loadFinished.connect(lambda _, tab_index=tab_index, tab_web_view=tab_web_view:self.browser_tabs.setTabText(tab_index, tab_web_view.page().title()))
		self.browser_tabs.setCurrentIndex(tab_index)
	def addTabButtonClicked(self):
		self.newTab()
	def tabChanged(self):
		self.updateAdress(self.browser_tabs.currentWidget().url())
	def closeTab(self,tabindex):
		if self.browser_tabs.count() < 2:
			self.browser_tabs.currentWidget().setUrl(QtCore.QUrl('about:blank'))
		else:
			self.browser_tabs.removeTab(tabindex)
	def goHome(self):
		self.browser_tabs.currentWidget().setUrl(QtCore.QUrl('http://google.com'))
	def goToNewAdress(self):
		new_url = self.adress_line_edit.text()
		if "http://" in new_url:
			pass
		elif "https://" in new_url:
			pass
		elif "." in new_url:
			new_url = "http://"+new_url
		else:
			new_url = new_url.replace(" ","+")
			new_url = "https://www.google.com/search?q="+new_url
		self.browser_tabs.currentWidget().setUrl(QtCore.QUrl(new_url))
	def updateAdress(self, urltoset):
		self.adress_line_edit.setText(urltoset.toString())
	def goBackTab(self):
		self.browser_tabs.currentWidget().back()
	def goFowardTab(self):
		self.browser_tabs.currentWidget().forward()
	def reloadTab(self):
		self.browser_tabs.currentWidget().reload()

class MainBrowserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainBrowserWindow()
        self.setWindowTitle("PI Browser")
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.title_bar_widgets_dict["minimize_button"].clicked.connect(lambda: self.showMinimized())
        self.ui.title_bar_widgets_dict["maximize_button"].clicked.connect(lambda: self.maximizeAndRestore())
        self.ui.title_bar_widgets_dict["exit_button"].clicked.connect(lambda: self.close())
        def moveWindow(event):
            if self.isMaximized():
                return
            else:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
        self.ui.title_bar_widgets_dict["title_bar_spacer"].mouseMoveEvent = moveWindow
    def maximizeAndRestore(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.title_bar_widgets_dict["exit_button"].setStyleSheet(ss.exit_button_stylesheet_window_normal)
            self.ui.title_bar_frame.setStyleSheet(ss.title_bar_frame_stylesheet_window_normal)
        else:
            self.showMaximized()
            self.ui.title_bar_widgets_dict["exit_button"].setStyleSheet(ss.exit_button_stylesheet_window_maximized)
            self.ui.title_bar_frame.setStyleSheet(ss.title_bar_frame_stylesheet_window_maximized)
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def mouseDoubleClickEvent(self, event):
        self.maximizeAndRestore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app_id = 'PI Browser'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    font_id = QtGui.QFontDatabase.addApplicationFont("fonts/Alice-Regular.ttf")
    _fontstr = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
    _font = QtGui.QFont(_fontstr, 10)
    app.setFont(_font)
    main_browser_window = MainBrowserWindow()
    main_browser_window.show()
    sys.exit(app.exec_())