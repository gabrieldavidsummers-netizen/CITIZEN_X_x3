import random
import sqlite3
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock

# --- SECTION 1: SOVEREIGN CONSTANTS ---
SIG = "13579"
FOUNDATION = 135792468
PILLARS = {"1": 609, "2": 5150, "3": 1978, "4": 666, "5": 3092}

VARIANT_MAP = {
    '0':['0','o','O','⁰'],'1':['1','¹'],'2':['2','²'],
    '3':['3','³'],'4':['4','⁴'],'5':['5','⁵'],
    '6':['6','⁶'],'7':['7','⁷'],'8':['8','⁸'],'9':['9','⁹']
}
REVERSE_MAP = {char: num for num, chars in VARIANT_MAP.items() for char in chars}

# --- SECTION 2: THE DATABASE LEXICON ---
def load_lexicon_from_db():
    db_path = "lexicon.db"
    word_list = []
    
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT word FROM vault")
            rows = cursor.fetchall()
            word_list = [row[0].lower().strip() for row in rows if row[0]]
            conn.close()
        except Exception as e:
            print(f"DATABASE_ERROR: {e}")
    
    if not word_list:
        word_list = ["citizen", "x", "sovereign", "engine", "forge"]

    random.seed(13579) # The Genetic Seed
    unique = sorted(list(set(word_list)))
    shuffled = list(unique)
    random.shuffle(shuffled)
    
    # Range 10000-99999 ensures 5-digit IDs to match your signature format
    id_pool = random.sample(range(10000, 99999), len(shuffled))
    
    lex = {str(id_val): word for id_val, word in zip(id_pool, shuffled)}
    rev_lex = {word: str(id_val) for id_val, word in zip(id_pool, shuffled)}
    return lex, rev_lex

LEXICON, REVERSE_LEXICON = load_lexicon_from_db()

# --- SECTION 3: CORE TRANSFORMATION ---
def encrypt_to_psi(plaintext, pillar_key="1"):
    shift = PILLARS.get(pillar_key, 609)
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

def decrypt_from_psi(psi_string, pillar_key="1"):
    shift = PILLARS.get(pillar_key, 609)
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

# --- SECTION 4: INTERFACE ---
class CitizenXApp(App):
    def build(self):
        self.title = "CITIZEN_X"
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # PSI-SIGNATURE FEED
        self.status_label = Label(
            text="[ CITIZEN_X : SIG-13579 ]", 
            color=(0, 1, 0, 1), 
            size_hint_y=None, height=50, font_size='22sp'
        )
        layout.add_widget(self.status_label)
        
        # KEYBOARD_FLOW FIX: input_type='text' and keyboard_suggestions=True
        # multiline=True and use_bubble enable full Android keyboard features
        self.input_box = TextInput(
            background_color=(0.1, 0.1, 0.1, 1), 
            foreground_color=(1, 1, 1, 1), 
            font_size='18sp',
            hint_text="[ FEED_COMMANDS_HERE ]",
            input_type='text',
            keyboard_suggestions=True,
            use_bubble=True,
            multiline=True
        )
        layout.add_widget(self.input_box)
        
        btn_box = BoxLayout(size_hint_y=None, height=70, spacing=10)
        btn_enc = Button(text="ENCRYPT", background_color=(0.1, 0.5, 0.1, 1), font_size='18sp')
        btn_enc.bind(on_press=lambda x: self.process(True))
        btn_dec = Button(text="DECRYPT", background_color=(0.5, 0.1, 0.1, 1), font_size='18sp')
        btn_dec.bind(on_press=lambda x: self.process(False))
        
        btn_box.add_widget(btn_enc)
        btn_box.add_widget(btn_dec)
        layout.add_widget(btn_box)

        # Automatic Numerical Feed: Pulses the status bar every 2 seconds
        Clock.schedule_interval(self.auto_pulse, 2.0)
        return layout

    def auto_pulse(self, dt):
        words = ["sovereign", "engine", "citizen", "negentropy", "frequency"]
        pulse_word = random.choice(words)
        self.status_label.text = f"[ {encrypt_to_psi(pulse_word)} ]"

    def process(self, encrypt):
        text = self.input_box.text
        if text:
            self.input_box.text = encrypt_to_psi(text) if encrypt else decrypt_from_psi(text)

if __name__ == "__main__":
    CitizenXApp().run()
            
