#author: Franklin

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.clock import Clock, ClockEvent

class AquaTabletApp(App):
    def __init__(self, **kwargs) -> None:
        super(AquaFitApp, self).__init__(**kwargs)
        self.trigger_timer = ClockEvent # type: ClockEvent

    def _go_rest_screen(self) -> None:
        self.root.current = 'telapropaganda'

    def timer_to_rest_screen(self) -> None:
        Clock.unschedule(self.trigger_timer)
        #lambda é necessário para passsar uma função sem argumentos
        self.trigger_timer = Clock.schedule_once(lambda dt: self._go_rest_screen(), 5.0)

if __name__ == '__main__':
    AquaTabletApp().run()


