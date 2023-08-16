from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock


class TelaVenda(Screen):
    pass



class TelaInicial(Screen):
    def on_enter(self):
        Window.bind(on_keyboard=self.tecla_pressionada)
    def tecla_pressionada(self,*args):
        self.manager.current = "tela_vendsa"

class TelaCarregamento(Screen):
    def on_enter(self):
        Clock.schedule_once(self.efeitoFade)

    def efeitoFade(self,dt):
        animacao = Animation(opacity=1, duration=4 )
        animacao.bind(on_complete=self.change_screen)
        animacao.start(self.ids.logo_carregamento)


    def change_screen(self,*args):
        self.manager.current = "tela_inicial"


class gerenciador_Telas(ScreenManager):
    pass


class appCaixa(MDApp):
    def build(self):
        Window.fullscreen = 'auto'
        return Builder.load_file("telas.kv")


appCaixa().run()