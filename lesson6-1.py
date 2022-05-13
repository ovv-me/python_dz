# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    _colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for color, s_time in self._colors.items():
            print(f"TrafficLight включил '{color}' "
                  f"на {s_time} секунд")
            sleep(s_time)
            print("Смена цвета")


traffic = TrafficLight()
traffic.running()
