import random
import sqlite3
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard

SIG = "13579"
FOUNDATION = 135792468
PILLARS = {
    "Pillar 1": 609,
    "Pillar 2": 5150,
    "Pillar 3": 1978,
    "Pillar 4": 666,
    "Pillar 5": 3092
}

VARIANT_MAP = {
    '0': ['0', 'o', 'O', '⁰'], '1': ['1', '¹'], '2': ['2', '²'],
    '3': ['3', '³'], '4': ['4', '⁴'], '5': ['5', '⁵'],
    '6': ['6', '⁶'], '7': ['7', '⁷'], '8': ['8', '⁸'], '9': ['9', '⁹']
}
REVERSE_MAP = {char: num for num, chars in VARIANT_MAP.items() for char in chars}


def load_lexicon_from_db():
    db_path = "lexicon.db"
    word_list = []
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT word FROM vault")
            word_list = [row[0].lower().strip() for row in cursor.fetchall() if row[0]]
            conn.close()
        except:
            pass
    if not word_list:
        word_list = ["citizen", "x", "sovereign", "engine", "forge"]
    random.seed(13579)
    unique = sorted(list(set(word_list)))
    shuffled = list(unique)
    random.shuffle(shuffled)
    id_pool = random.sample(range(10000, 99999), len(shuffled))
    lex = {str(id_val): word for id_val, word in zip(id_pool, shuffled)}
    rev_lex = {word: str(id_val) for id_val, word in zip(id_pool, shuffled)}
    return lex, rev_lex


LEXICON, REVERSE_LEXICON = load_lexicon_from_db()


def encrypt_to_psi(plaintext, pillar_name="Pillar 1"):
    shift = PILLARS.get(pillar_name, 609)
    output = []
    for word in plaintext.lower().split():
        token_id = REVERSE_LEXICON.get(word)
        if token_id:
            val = str(FOUNDATION + shift + int(token_id))
            alien = "".join(random.choice(VARIANT_MAP[c]) for c in val)
            output.append(f"{SIG}{alien}")
        else:
            output.append(f"[{word}]")
    return " ".join(output)


def decrypt_from_psi(psi_string, pillar_name="Pillar 1"):
    shift = PILLARS.get(pillar_name, 609)
    decoded = []
    for token in psi_string.split():
        if token.startswith(SIG):
            try:
                raw_nums = "".join(REVERSE_MAP.get(c, c) for c in token[len(SIG):])
                target_id = str(int(raw_nums) - FOUNDATION - shift)
                word = LEXICON.get(target_id, "???")
                decoded.append(word.upper())
            except:
                decoded.append("ERR")
        else:
            decoded.append(token.upper())
    return " ".join(decoded)


# Custom TextInput that detects horizontal swipes
class GestureTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._touch_start = None
        self._touch_end = None
        self._swipe_threshold = 50  # pixels

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._touch_start = touch.pos
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        # allow normal text selection and scrolling behavior
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if self._touch_start and self.collide_point(*touch.pos):
            self._touch_end = touch.pos
            dx = self._touch_end[0] - self._touch_start[0]
            dy = self._touch_end[1] - self._touch_start[1]
            # horizontal swipe detection
            if abs(dx) > self._swipe_threshold and abs(dx) > abs(dy):
                # dispatch a custom event to parent to process
                if dx > 0:
                    # swipe right -> encrypt
                    self.parent.parent.process(True)
                else:
                    # swipe left -> decrypt
                    self.parent.parent.process(False)
                # prevent the swipe from producing extra text selection
                self._touch_start = None
                self._touch_end = None
                return True
        return super().on_touch_up(touch)


class CitizenXApp(App):
    def build(self):
        self.title = "CITIZEN_X"
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.status_label = Label(text="[ CITIZEN_X : SIG-13579 ]", color=(0, 1, 0, 1),
                                  size_hint_y=None, height=50, font_size='22sp')
        layout.add_widget(self.status_label)
        self.pillar_selector = Spinner(text='Pillar 1', values=list(PILLARS.keys()),
                                       size_hint=(1, None), height=50)
        layout.add_widget(self.pillar_selector)

        # use GestureTextInput for swipe handling
        self.input_box = GestureTextInput(background_color=(0.1, 0.1, 0.1, 1),
                                          foreground_color=(1, 1, 1, 1),
                                          font_size='18sp', multiline=True)
        layout.add_widget(self.input_box)

        btn_box = BoxLayout(size_hint_y=None, height=70, spacing=10)
        btn_enc = Button(text="ENCRYPT", background_color=(0.1, 0.5, 0.1, 1))
        btn_enc.bind(on_press=lambda x: self.process(True))
        btn_dec = Button(text="DECRYPT", background_color=(0.5, 0.1, 0.1, 1))
        btn_dec.bind(on_press=lambda x: self.process(False))
        btn_copy = Button(text="COPY", background_color=(0.2, 0.2, 0.6, 1))
        btn_copy.bind(on_press=lambda x: self.copy_to_clipboard())

        btn_box.add_widget(btn_enc)
        btn_box.add_widget(btn_dec)
        btn_box.add_widget(btn_copy)
        layout.add_widget(btn_box)

        Clock.schedule_interval(self.auto_pulse, 3.0)
        return layout

    def auto_pulse(self, dt):
        try:
            self.status_label.text = f"[ {encrypt_to_psi('sovereign', self.pillar_selector.text)} ]"
        except Exception:
            # keep status stable if pillar_selector not yet ready
            pass

    def process(self, encrypt):
        if self.input_box.text:
            # convert and replace in place
            if encrypt:
                result = encrypt_to_psi(self.input_box.text, self.pillar_selector.text)
            else:
                result = decrypt_from_psi(self.input_box.text, self.pillar_selector.text)
            self.input_box.text = result
            # auto-copy the result to clipboard as requested
            Clipboard.copy(result)
            # update status to indicate copy
            self.status_label.text = "[ COPIED ]"

    def copy_to_clipboard(self):
        text = self.input_box.text or ""
        Clipboard.copy(text)
        self.status_label.text = "[ COPIED ]"


if __name__ == "__main__":
    CitizenXApp().run()
