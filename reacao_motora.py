import gpiod
import time
import random
# Configurando o chip e as linhas GPIO
# gpiochip{n} onde n vai de 0 a 4
# A labrador possui 5 grupos de GPIO A, B, C, D, E como descrito na wiki
# onde:
# 0 = A
# 1 = B
# 2 = C
# 3 = D
# 4 = E
# Para este exercicio vamos usar o grupo E e B que corresponde ao gpiochip4 e gpiochip1

chipE = gpiod.chip('/dev/gpiochip4')
chipB = gpiod.chip('/dev/gpiochip1')
led = chipE.get_line(3)  # pino 3
button = chipE.get_line(2)  # pino 5
buzzer = chipB.get_line(18)  # pino 7

ACTIVE = 1
INACTIVE = 0

# Configurando as direçoes INPUT e OUTPUT
INPUT = gpiod.line_request.DIRECTION_INPUT
OUTPUT = gpiod.line_request.DIRECTION_OUTPUT

# Configurando as requisiçoes
config_led = gpiod.line_request()
config_led.consumer = "led"
config_led.request_type = OUTPUT # define a direção do pino como saída
led.request(config_led)

config_button = gpiod.line_request()
config_button.consumer = "button"
config_button.request_type = INPUT # define a direção do pino como entrada
button.request(config_button)

config_buzzer = gpiod.line_request()
config_buzzer.consumer = "buzzer"
config_buzzer.request_type = OUTPUT
buzzer.request(config_buzzer)



def apertar_botao():
    ti = time.time()
    while True:
        if button.get_value() == ACTIVE:
            tf = time.time()
            led.set_value(INACTIVE)
            buzzer.set_value(INACTIVE)
            return tf - ti

def iniciar_exp():
    exp = input("Digite:\n1-para experimento motor visual;\n2-para experimento motor auditivo\n3-Sair\n")
    if exp == "1":
        resp = input("Pronto para iniciar?(y/n)")
        if resp == "y":
            print("Iniciando...")
            tempo_espera = random.uniform(1, 5)
            time.sleep(tempo_espera)
            led.set_value(ACTIVE)
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
            buzzer.set_value(ACTIVE)
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
