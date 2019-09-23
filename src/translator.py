from PyQt5.QtCore import QTranslator
import gettext

class QTranslatorGettext(QTranslator):
    def load(self, domain):
        self.gettext_translator = gettext.translation(domain).gettext

    def translate(self, context, text, disambiguation, n):
        return self.gettext_translator(text)
