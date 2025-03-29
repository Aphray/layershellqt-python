import sys

from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication, QFrame
from PySide6.QtCore import QMargins
from QtLayerShell import QLayerShell



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    widget = QFrame()
    button = QPushButton()
    button.clicked.connect(lambda: print('Hello!'))
    
    layout = QHBoxLayout()
    layout.addWidget(button)
    
    # widget.setLayout(layout)
    
    widget.setObjectName('Widget')
    widget.setStyleSheet(
        '''
        QFrame#Widget {
            background: rgba(14, 14, 14, 0.05);
            border-radius: 10px;
        }             
        ''')
    
    
    layer = QLayerShell(
        widget,
        'test-shell',
        margins=QMargins(10, 10, 10, 1050),
        exclusiveZone=30,
        exclusiveEdge=QLayerShell.Anchor.Top
    )
    
    layer.show()
    
    print('running')
    sys.exit(app.exec())