from machine import Pin, PWM
from time import sleep
import onewire
import ds18x20

# DS18B20 Setup
sensor_pin = Pin(26)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin))

roms = ds_sensor.scan()

if not roms:
    raise RuntimeError("No DS18B20 temperature sensor found")

sensor = roms[0]

print("DS18B20 found")


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


# Start Fans Off

set_intake(0)
set_exhaust(0)


# Main Loop

while True:

    try:

        # Tell DS18B20 to take a temperature measurement
        ds_sensor.convert_temp()

        # DS18B20 requires time to complete the conversion
        sleep(0.75)

        temperature_c = ds_sensor.read_temp(sensor)

        if temperature_c is None:
            raise RuntimeError("Invalid DS18B20 reading")

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
            "| Intake:", intake_percent, "%",
            "| Exhaust:", exhaust_percent, "%"
        )


    except Exception as error:

        # Fail-safe: if temperature cannot be determined,
        # force maximum cooling.

        print("Temperature sensor fault:", error)
        print("Fans forced to 100%")

        set_intake(100)
        set_exhaust(100)


    sleep(1)
