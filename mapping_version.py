from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QTableWidget,QMessageBox

# QT6
try :
    Dialog = Qt.WindowType.Dialog
    WaitCursor = Qt.CursorShape.WaitCursor
    WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowType.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    NoEditTriggers = QTableWidget.EditTrigger.NoEditTriggers
    SelectRows = QTableWidget.SelectionBehavior.SelectRows
    NoSelection = QTableWidget.SelectionMode.NoSelection
    Warning = QMessageBox.Icon.Warning
    RejectRole = QMessageBox.ButtonRole.RejectRole
    AcceptRole = QMessageBox.ButtonRole.AcceptRole
    Ok = QMessageBox.StandardButton.Ok

# QT5
except :
    Dialog = Qt.Dialog
    WaitCursor = Qt.WaitCursor
    WindowCloseButtonHint = Qt.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
    EditTriggers = QTableWidget.NoEditTriggers
    SelectRows = QTableWidget.SelectRows
    NoSelection = QTableWidget.NoSelection
    Warning = QMessageBox.Warning
    RejectRole = QMessageBox.RejectRole
    AcceptRole = QMessageBox.AcceptRole
    Ok = QMessageBox.Ok
