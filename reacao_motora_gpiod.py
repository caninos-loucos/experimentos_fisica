import gpiod
import time
import random
#ESTE CODIGO AINDA NAO ESTA FUNCIONANDO!!!!
# Configurando o chip e as linhas GPIO
# gpiochip{n} onde n vai de 0 a 4
# A labrador possui 5 grupos de GPIO A, B, C, D, E como descrito na wiki
# onde:
# 0 = A
# 1 = B
# 2 = C
# 3 = D
# 4 = E
# Para este exercicio vamos usar o grupo B que corresponde ao gpiochip1

PATH = '/dev/gpiochip1'
chip = gpiod.Chip(PATH)
led_line = 16  # pino 27
button_line = 17  # pino 29
buzzer_line = 10  # pino 31

# Configurando valores ativos e inativos
ACTIVE = gpiod.line.Value.ACTIVE
INACTIVE = gpiod.line.Value.INACTIVE

# Configurando as direçoes INPUT e OUTPUT
INPUT = gpiod.LineSettings(direction=gpiod.line.Direction.INPUT)
OUTPUT = gpiod.LineSettings(direction=gpiod.line.Direction.OUTPUT, output_value=ACTIVE)

# Habilitando e configurando os sensores e atuadores da GPIO
led = gpio.request_lines(PATH, consumer="led", config={led_line, OUTPUT})
button = gpio.request_lines(PATH, consumer="button", config={button_line, INPUT})
buzzer = gpio.request_lines(PATH, consumer="button", config={buzzer_line, OUTPUT})


def apertar_botao():
    ti = time.time()
    while True:
        if button.get_value() == ACTIVE:
            tf = time.time()
            led.set_value(0)
            buzzer.set_value(0)
            return tf - ti

def iniciar_exp():
    exp = input("Digite:\n1-para experimento motor visual;\n2-para experimento motor auditivo\n3-Sair\n")
    if exp == "1":
        resp = input("Pronto para iniciar?(y/n)")
        if resp == "y":
            print("Iniciando...")
            tempo_espera = random.uniform(1, 5)
            time.sleep(tempo_espera)
            led_line.set_value(1)
            tr = apertar_botao()
            print(f"Tempo de resposta: {tr:.4f} ms")
            iniciar_exp()
        elif resp == "n":
            print("Talvez uma outra hora.")
        else:
            print("Digite apenas y para sim e n para nao")
            iniciar_exp()
    elif exp == "2":
        resp2 = input("Pronto para iniciar?(y/n)")
        if resp2 == "y":
            print("Iniciando...")
            t_espera = random.uniform(1, 5)
            time.sleep(t_espera)
            buzzer_line.set_value(1)
            tr = apertar_botao()
            print(f"Tempo de resposta: {tr:.4f} ms")
            iniciar_exp()
        elif resp2 == "n":
            print("Talvez uma outra hora.")
        else:
            print("Digite apenas y para sim e n para nao")
            iniciar_exp()
    else:
        print("Talvez uma outra hora.")

iniciar_exp()
