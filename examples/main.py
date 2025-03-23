import sys
from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QWidget, QFrame, QPushButton, QHBoxLayout, QApplication, QStyleFactory


from QtLayerShell import QLayerShell

            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screens = app.screens()
    
    btn = QPushButton('test')
    widget = QFrame()
    
    ls = QLayerShell(
        widget,
        'test-shell',
        screens[1],
        QLayerShell.Layer.Top,
        QMargins(0, 0, 0, 0),
        exclusiveZone=30,
        exclusiveEdge=QLayerShell.Anchor.Top
    )
    
    widget.move(400, 200)
    widget.setFixedWidth(500)
    widget.setFixedHeight(500)
    widget.setStyleSheet(
        '''QFrame {
            background-color: rgba(30, 30, 30, 0.9);
            border-radius: 10px;
        }
        ''')
    
    ls.show()
    
    sys.exit(app.exec())
    
