import random, sqlite3, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard

# ANCHORS
SIG = "13579"
FOUNDATION = 135792468
PILLARS = {
    "Pillar 1": 609, 
    "Pillar 2": 5150, 
    "Pillar 3": 1978, 
    "Pillar 4": 666, 
    "Pillar 5": 3092
}

# PSI-LANGUAGE VARIANT MAP
VARIANT_MAP = {
    '0':['0','o','O','⁰'],'1':['1','¹'],'2':['2','²'],
    '3':['3','³'],'4':['4','⁴'],'5':['5','⁵'],
    '6':['6','⁶'],'7':['7','⁷'],'8':['8','⁸'],'9':['9','⁹']
}
REVERSE_MAP = {char: num for num, chars in VARIANT_MAP.items() for char in chars}

def load_lexicon():
    db_path = "lexicon.db"
    word_list = []
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT word FROM vault")
            word_list = [row[0].lower().strip() for row in cursor.fetchall() if row[0]]
            conn.close()
        except: pass
    
    if not word_list: 
        word_list = ["citizen", "x", "sovereign", "engine", "forge"]
    
    random.seed(13579)
    unique = sorted(list(set(word_list)))
    random.shuffle(unique)
    id_pool = random.sample(range(10000, 99999), len(unique))
    
    return {str(i): w for i, w in zip(id_pool, unique)}, {w: str(i) for i, w in zip(id_pool, unique)}

LEXICON, REV_LEXICON = load_lexicon()

class GestureTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.touch_start_x = 0

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.touch_start_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            dx = touch.x - self.touch_start_x
            if abs(dx) > 150:
                # Swipe Right = Encrypt, Swipe Left = Decrypt
                self.parent.parent.process(dx > 0)
                return True
        return super().on_touch_up(touch)

class CitizenXApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        self.status = Label(text="[ ENGINE_ACTIVE : 13579 ]", color=(0, 1, 0, 1), size_hint_y=None, height=50)
        self.pillar = Spinner(text='Pillar 1', values=list(PILLARS.keys()), size_hint_y=None, height=60)
        self.input_box = GestureTextInput(
            background_color=(0.1, 0.1, 0.1, 1), 
            foreground_color=(0, 1, 0, 1), 
            font_size='18sp', 
            multiline=True
        )
        
        btn_box = BoxLayout(size_hint_y=None, height=80, spacing=10)
        for t, c, m in [("ENCRYPT", (0, .4, 0, 1), True), ("DECRYPT", (.4, 0, 0, 1), False), ("COPY", (.2, .2, .5, 1), None)]:
            btn = Button(text=t, background_color=c)
            btn.bind(on_press=lambda x, m=m: self.process(m) if m is not None else self.copy())
            btn_box.add_widget(btn)
        
        layout.add_widget(self.status)
        layout.add_widget(self.pillar)
        layout.add_widget(self.input_box)
        layout.add_widget(btn_box)
        return layout

    def process(self, enc):
        if not self.input_box.text: return
        shift = PILLARS.get(self.pillar.text, 609)
        res = []
        
        if enc:
            for w in self.input_box.text.lower().split():
                tid = REV_LEXICON.get(w)
                if tid:
                    val = str(FOUNDATION + shift + int(tid))
                    res.append(SIG + "".join(random.choice(VARIANT_MAP[c]) for c in val))
                else: res.append(f"[{w}]")
        else:
            for t in self.input_box.text.split():
                if t.startswith(SIG):
                    try:
                        raw = "".join(REVERSE_MAP.get(c, c) for c in t[len(SIG):])
                        target_id = str(int(raw) - FOUNDATION - shift)
                        res.append(LEXICON.get(target_id, "???").upper())
                    except: res.append("ERR")
                else: res.append(t.upper())
        
        self.input_box.text = " ".join(res)
        self.copy()

    def copy(self):
        Clipboard.copy(self.input_box.text)
        self.status.text = "[ RESULT COPIED ]"

if __name__ == "__main__":
    CitizenXApp().run()
        
