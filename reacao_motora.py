import caninos_sdk as k9
import time
import random

# Iniciando a Labrador
labrador = k9.Labrador()
# Iniciando o LED
labrador.pin3.enable_gpio(k9.Pin.Direction.OUTPUT, alias="led")
# Iniciando o botao
labrador.pin7.enable_gpio(k9.Pin.Direction.INPUT, alias="button")
# Iniciando o buzzer
labrador.pin5.enable_gpio(k9.Pin.Direction.OUTPUT, alias="buzzer")
def apertar_botao():
    tf = 0
    ti = time.time()
    while True:
        if labrador.button.read()==1:
            tf = time.time()
            labrador.led.low()
            labrador.buzzer.low()
            return tf-ti

    
def iniciar_exp():
    exp = input("Digite:\n1-para experimento motor visual;\n2-para experimento motor auditivo\n3-Sair\n")
    if exp == "1":
        resp = input("Pronto para iniciar?(y/n)")
        if resp == "y":
            print("Iniciando...")
            tempo_espera = random.uniform(1,5)
            time.sleep(tempo_espera)
            labrador.led.high()
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
            t_espera = random.uniform(1,5)
            time.sleep(t_espera)
            labrador.buzzer.high()
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
