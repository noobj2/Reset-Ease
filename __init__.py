from aqt import mw
from aqt.utils import showInfo, askUser, getText, tooltip
from aqt.qt import *

def ResetEase():
    user_ease = getText("Enter Ease")[0]
    if user_ease:
        try:
            if int(user_ease) < 130:
                tooltip("Minimum ease is 130%", period=5000)
                user_ease = 130
            anki_ease =int(user_ease) * 10
        except ValueError:
            showInfo("Ease should be a number.")
            ResetEase()
            return
    else:
        user_ease = 250
        anki_ease = 2500
    reset = askUser("This action can't be undone. Reset all cards Ease to {}%?".format(user_ease))
    if reset:
        mw.col.db.execute("update cards set factor = ?", anki_ease)
        # show a message box
        showInfo("Ease has been reset to {}%.".format(user_ease))
    else:
        pass


action = QAction("Reset &Ease", mw)
action.triggered.connect(ResetEase)
mw.form.menuTools.addAction(action)
