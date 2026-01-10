import os
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Line, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

# --- PILLAR GEOMETRY ---
PILLARS = {
    "1": 609,
    "2": 5150,
    "3": 1978,
    "4": 666,
    "5": 3092
}

# --- TRUE OBFUSCATED LEXICON ---
# Derived from lexicon.db: 1 is not ¹, 0 is not o.
LEXICON = {
    "corpus": "445¹⁶", "attachment": "7o⁷⁷9", "characterization": "9⁴⁹31", "adopted": "⁷⁹³85", 
    "skilled": "¹5³92", "guns": "88⁶⁶⁹", "operators": "603³⁷", "obtaining": "⁶56O8",
    "formula": "94²⁶⁶", "lycos": "⁵1o⁸3", "gi": "³416²", "sister": "8⁵³8³", "aaa": "¹⁷83⁸",
    "federal": "29⁷38", "milfhunter": "39⁸⁹3", "students": "6³³¹²", "ceremony": "15⁶9⁷",
    "books": "268⁹2", "transformation": "6⁵6⁰1", "collector": "12938", "european": "²⁶⁰⁹7",
    "jazz": "⁴⁵⁶25", "pushed": "8⁴⁵5⁹", "domain": "8⁴²13", "diseases": "⁷2³63", "highways": "⁶88²⁶"
}
REVERSE_LEXICON = {v: k for k, v in LEXICON.items()}

class SovereignEngine(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.active_pillar = "1"
        self.canvas.before.add(Color(0.02, 0.02, 0.02, 1))
        self.canvas.before.add(Rectangle(pos=(0, 0), size=(Window.width, Window.height)))
        
        # Header / Icon Placeholder
        self.header = Label(
            text="[ CITIZEN_X ]\nSOVEREIGN v4.6",
            font_size='18sp',
            color=get_color_from_hex('#00ff41'),
            halign='center',
            size_hint_y=0.15,
            bold=True
        )
        self.add_widget(self.header)

        # Pillar Selection
        self.pillar_box = BoxLayout(size_hint_y=0.1, spacing=5)
        self.pillar_btns = {}
        for p_id in PILLARS.keys():
            btn = Button(
                text=p_id,
                background_normal='',
                background_color=get_color_from_hex('#002200'),
                color=get_color_from_hex('#00ff41')
            )
            btn.bind(on_release=self.set_pillar)
            self.pillar_btns[p_id] = btn
            self.pillar_box.add_widget(btn)
        self.update_pillar_ui()
        self.add_widget(self.pillar_box)

        # Input Area (Optimized for Android Swipe/Glide)
        self.input_field = TextInput(
            hint_text="ENTER_SIGNAL...",
            background_color=(0, 0, 0, 1),
            foreground_color=get_color_from_hex('#00ff41'),
            cursor_color=get_color_from_hex('#00ff41'),
            font_size='14sp',
            size_hint_y=0.25,
            multiline=True,
            auto_indent=False
        )
        self.add_widget(self.input_field)

        # Action Matrix
        self.action_box = BoxLayout(size_hint_y=0.1, spacing=10)
        self.enc_btn = Button(text="ENCRYPT¹", background_color=get_color_from_hex('#004400'))
        self.dec_btn = Button(text="DECRYPT⁰", background_color=get_color_from_hex('#001100'))
        self.enc_btn.bind(on_release=lambda x: self.process('encrypt'))
        self.dec_btn.bind(on_release=lambda x: self.process('decrypt'))
        self.action_box.add_widget(self.enc_btn)
        self.action_box.add_widget(self.dec_btn)
        self.add_widget(self.action_box)

        # Manifest Output
        self.output_label = TextInput(
            text="[IDLE]",
            readonly=True,
            background_color=(0.05, 0.05, 0.05, 1),
            foreground_color=get_color_from_hex('#00ff41'),
            size_hint_y=0.3
        )
        self.add_widget(self.output_label)

        # System Ops
        self.ops_box = BoxLayout(size_hint_y=0.1, spacing=10)
        self.chain_btn = Button(text="CHAIN_TURN", font_size='10sp')
        self.flush_btn = Button(text="FLUSH_MEM", font_size='10sp', color=(1,0,0,1))
        self.chain_btn.bind(on_release=self.chain)
        self.flush_btn.bind(on_release=self.flush)
        self.ops_box.add_widget(self.chain_btn)
        self.ops_box.add_widget(self.flush_btn)
        self.add_widget(self.ops_box)

    def set_pillar(self, instance):
        self.active_pillar = instance.text
        self.update_pillar_ui()

    def update_pillar_ui(self):
        for p_id, btn in self.pillar_btns.items():
            if p_id == self.active_pillar:
                btn.background_color = get_color_from_hex('#00ff41')
                btn.color = (0, 0, 0, 1)
            else:
                btn.background_color = get_color_from_hex('#002200')
                btn.color = get_color_from_hex('#00ff41')

    def process(self, mode):
        text = self.input_field.text.strip().lower()
        if not text: return
        
        if mode == 'encrypt':
            words = re.findall(r'\b[a-z0-9]+\b', text)
            result = [LEXICON.get(w, "[PSI_NULL]") for w in words]
            self.output_label.text = " ".join(result)
        else:
            tokens = text.split()
            result = [REVERSE_LEXICON.get(t, "[PSI_ERR]") for t in tokens]
            self.output_label.text = " ".join(result)

    def chain(self, instance):
        self.input_field.text = self.output_label.text
        self.output_label.text = "[CHAINED]"

    def flush(self, instance):
        self.input_field.text = ""
        self.output_label.text = "[IDLE]"

class SovereignApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return SovereignEngine()

if __name__ == '__main__':
    SovereignApp().run()
