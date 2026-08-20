from machine import ADC, Pin, PWM
from time import sleep
import math

thermistor = ADC(Pin(26))

VCC = 3.3
R_FIXED = 100000
R0 = 100000
T0 = 25 + 273.15
BETA = 3950


# Fan PWM Setup

intake_fan = PWM(Pin(15))
exhaust_fan = PWM(Pin(14))

intake_fan.freq(1000)
exhaust_fan.freq(1000)

intake_percent = 0
exhaust_percent = 0


def set_intake(percent):
    global intake_percent

    duty = int(percent * 65535 / 100)
    intake_fan.duty_u16(duty)

    intake_percent = percent


def set_exhaust(percent):
    global exhaust_percent

    duty = int(percent * 65535 / 100)
    exhaust_fan.duty_u16(duty)

    exhaust_percent = percent


def read_average():
    total = 0
    samples = 10

    for i in range(samples):
        total += thermistor.read_u16()
        sleep(0.1)

    return total // samples


# Start Fans Off

set_intake(0)
set_exhaust(0)


# Main Loop

while True:

    raw = read_average()

    if raw == 0 or raw >= 65535:
        print("Thermistor fault - both fans forced to 100%")

        set_intake(100)
        set_exhaust(100)

        sleep(1)
        continue

    voltage = raw * VCC / 65535

    resistance = R_FIXED * raw / (65535 - raw)

    temperature_k = 1 / (
        (1 / T0) +
        (1 / BETA) * math.log(resistance / R0)
    )

    temperature_c = temperature_k - 273.15
    temperature_f = temperature_c * 9 / 5 + 32


    # Fan Control

    if temperature_f >= 105:
        set_intake(100)
        set_exhaust(100)

    elif temperature_f >= 95:
        set_intake(100)
        set_exhaust(75)

    elif temperature_f >= 85:
        set_intake(75)
        set_exhaust(0)

    elif temperature_f <= 82:
        set_intake(0)
        set_exhaust(0)


    print(
        "Temp:", round(temperature_f, 1), "F",
        "| Resistance:", round(resistance / 1000, 1), "kOhm",
        "| Intake:", intake_percent, "%",
        "| Exhaust:", exhaust_percent, "%"
    )

    sleep(1)
