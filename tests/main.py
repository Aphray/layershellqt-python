import sys
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication

from QtLayerShell import QLayerShell

            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screens = app.screens()
    
    window = QWidget()

    ls = QLayerShell(
        window,
        'test-shell',
        screens[1],
        QLayerShell.Layer.Bottom,
        QMargins(0, 0, 0, 1050),
        30,
        QLayerShell.Anchor.Top
    )
    
    b = QPushButton('test')
    b.clicked.connect(lambda *args: print('clicked'))
    ly = QHBoxLayout()
    ly.addWidget(b)
    window.setLayout(ly)
    
    window.show()
    
    
    sys.exit(app.exec())
