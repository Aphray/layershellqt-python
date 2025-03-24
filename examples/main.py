import sys
from PySide6.QtCore import QMargins, Qt
from PySide6.QtWidgets import QWidget, QFrame, QPushButton, QHBoxLayout, QApplication, QStyleFactory


from QtLayerShell import QLayerShell

            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    screens = app.screens()
    
    btn = QPushButton('test')
    
    
    ls = QLayerShell(
        scope='test-shell',
        screen=screens[1],
        layer=QLayerShell.Layer.Top,
        margins=QMargins(0, 0, 500, 0),
        exclusiveZone=30,
        exclusiveEdge=QLayerShell.Anchor.Left
    )
    
    widget = QFrame()
    ls.setWidget(widget)
    
    l = QHBoxLayout()
    l.addWidget(btn)
    widget.setLayout(l)
    
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
    
