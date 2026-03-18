class BMW:
    def start(self):
        return "El BMW arranca con suavidad."

    def stop(self):
        retur "El BMW se detiene de forma elegante."


class Ferrari:
    def start(self):
        return "El Ferrari ruge al arrancar."

    def stop(self):
        return "El Ferrari frena con potencia."


def test_drive(car):
    print(car.start())
    print(car.stop())


bmw = BMW()
ferrari = Ferrari()

test_drive(bmw)
test_drive(ferrari)
