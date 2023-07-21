from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock



class TelaCarregamento(Screen):
    def on_enter(self):
        Clock.schedule_once(self.efeitoFade)

    def efeitoFade(self,dt):
        animacao = Animation(opacity=1, duration=2)
        animacao.start(self.ids.logo_carregamento)
        #animacao.bind(on_complete=self.do_something_after_fade)



class gerenciador_Telas(ScreenManager):
    pass


class appCaixa(MDApp):
    def build(self):
        Window.fullscreen = 'auto'
        return Builder.load_file("telas.kv")


appCaixa().run()