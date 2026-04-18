from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime

class VoidApp(App):
    def build(self):
        self.title = "VOID Blackout"
        Window.clearcolor = (0, 0, 0, 1) # Hitam Pekat
        
        root = BoxLayout(orientation='vertical', padding=10, spacing=5)
        
        # Area Chat
        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.chat_logs = BoxLayout(orientation='vertical', size_hint_y=None, spacing=2)
        self.chat_logs.bind(minimum_height=self.chat_logs.setter('height'))
        self.scroll.add_widget(self.chat_logs)
        root.add_widget(self.scroll)
        
        # Input Area
        input_box = BoxLayout(size_hint=(1, 0.1), spacing=5)
        self.txt_input = TextInput(
            hint_text='Ketik pesan...', multiline=False,
            background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )
        self.txt_input.bind(on_text_validate=self.send_msg)
        
        # Tombol SEND Putih Teks Hitam (Estetika B/W)
        btn_send = Button(
            text='SEND', size_hint=(0.2, 1),
            background_normal='', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1),
            bold=True
        )
        btn_send.bind(on_press=self.send_msg)
        
        input_box.add_widget(self.txt_input)
        input_box.add_widget(btn_send)
        root.add_widget(input_box)
        
        # Pesan awal
        self.add_to_ui("SYSTEM", "0", "0", "VOID Protocol Online. AirGate Ready.")
        
        return root

    def add_to_ui(self, nama, l, r, teks):
        waktu = datetime.now().strftime("%d/%m/%y|%H:%M")
        full = f"[{waktu}]_<{nama}_L{l}_R{r}>: {teks}"
        lbl = Label(
            text=full, size_hint_y=None, height=40,
            text_size=(Window.width - 20, None), halign='left', valign='middle'
        )
        self.chat_logs.add_widget(lbl)
        self.scroll.scroll_y = 0

    def send_msg(self, *args):
        if self.txt_input.text.strip():
            # Identitas dummy untuk V1
            self.add_to_ui("Bojja", "3", "16", self.txt_input.text)
            self.txt_input.text = ""

if __name__ == '__main__':
    VoidApp().run()
