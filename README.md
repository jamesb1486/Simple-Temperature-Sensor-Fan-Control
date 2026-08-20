# Simple-Temperature-Sensor-Fan-Control
This is a simple but effective raspberry Pi Pico temperature sensor fan controller.

I have used this fan controller on a few projects that required active cooling.
________________________________________________________________________________________

Parts Needed

1. Raspberry Pi Pico
2. 2x MOSFET Switch Driver Module, DC 5V-36V 15A
3. Temperature Sensor:
   - Creality-style 100k NTC thermistor, or
   - DS18B20 digital temperature Sensor
4. 100k ohm Resistor (NTC thermistor version only) 
5. 12v 30 amp power supply
6. 5v Step down converter

[Raspberry Pi Pico](https://www.amazon.com/Raspberry-Pi-Pico/dp/B09KVB8LVR/ref=sr_1_1?crid=1XHY1XV093O4M&dib=eyJ2IjoiMSJ9.KhN-eo1QUief6dgXnlRewOD_5s_2kVFK-6pw5wXpUodNQVbIlckdR02yi6cR9Sg_BYXCIKOeg-5rRf0kVPtR-00xl0HF7jn6HqhXZzmVTqjeOJdnD_ep-k6rldBNb_QblhpAgPj0-ScpRSSNoXy-L7VPGMau7bK1a9iPrvFJmGWQwJxuSyFNoxEZua9-PcgRmSRfYMPTkXv9sBo9cz71kiapwsOsZzopDrvodLmvJ_g.svO7Rn5HoZjw09cC_z0irVLf9-0_SoNNLFxKB6CafvA&dib_tag=se&keywords=raspberry+pi+pico&qid=1787243675&sprefix=raspberry+pi+pico%2Caps%2C277&sr=8-1)

[MOSFET Switch Driver Module](https://www.amazon.com/MateIJS-Control-Compatible-Arduino-Raspberry/dp/B0DX2KCZHL/ref=sr_1_3?crid=1098PVDE7VI0Y&dib=eyJ2IjoiMSJ9.E9SQ9M8ePaFU2VKAldSm6w.dvDomMb5uBNV7Jm7_atJXIYY9SFruHuHKS6ZeNKpaXc&dib_tag=se&keywords=B0Dx2kczhl+Mosfet&qid=1787241375&sprefix=b0dx2kczhl+mosfe%2Caps%2C498&sr=8-3)

[Creality Thermistor](https://www.amazon.com/Creality-Original-3D-Thermistor-Replacement/dp/B0BJJQGC17/ref=sr_1_1?crid=16WL3X8RL9ZOD&dib=eyJ2IjoiMSJ9.vcwHXwvTHSoBG-flEEpa63VQ7sba_rD-0oqznLsT93v6--qunzdEHoSmPyiV_ORtoFVx9ZcwTvdxOkj11C4XnHcw6fOGOXA9QQZEvfCthy7BIqN3njGkU-ObPO3hzxLbxrQwLNuqHELmvbBuCG4p7rVn09VMlHK1JIndux5FpdqPkAuIs84m0pq-5ZVdphz4JIC9bx4ZhKzz2iufgNzExIc-TufUjEJqEZQxlslhQbE.2LgPWcbzaxBcFaR4Nuge2aMXb4JOQbsKX3mdREZ0J7A&dib_tag=se&keywords=creality+thermistor&qid=1787249374&sprefix=creality+thermisto%2Caps%2C268&sr=8-1)

[Temperature Sensor Module](https://www.amazon.com/BOJACK-Temperature-Waterproof-Stainless-Raspberry/dp/B09NVWNGLQ/ref=sr_1_1?crid=3H3SZ1BE2FXTM&dib=eyJ2IjoiMSJ9.-bYFStbANNzH_Z59FVSTqZAucB0Q5q-ZYopfw7iiU0elEEN9lpa5ZYrszSiP5sGhmc9PBS9Kz_e0t3w6tQ5UK7HCldIb9d7xAN88TCJJRMnqATKbeH7fr5Dm9hBMAi-hFA7buXeH_cEGF3W0-b5vNxMnh-HFwziR0JsVvFzDC0qLmJBobN0hU-uSlpuOupmxPsIdWuAT4FWlrb1Jt6Kbs20JXtfEtnWq5NIWafheD1c.WXjQqk5iPsmjBoSMktqW7g07J3Zp3ixlYOcj9xah9Eo&dib_tag=se&keywords=raspberry+pi+temperature+sensor&qid=1787243316&sprefix=raspberry+pi+temperature+senso%2Caps%2C245&sr=8-1)

[100kohm Resistor](https://www.amazon.com/EDGELEC-Resistor-Tolerance-Multiple-Resistance/dp/B07QK9793W/ref=sr_1_1_sspa?crid=3IZ4J10EEYF1P&dib=eyJ2IjoiMSJ9.yHjzlMVxuH3oRABVLngA1efr-nYUveIUbDE_DHHVXs_lGVj-AqY_6TBetvdJHsSC62pfRgJZJzo2-mq6yr1ncTuqZxywBzElR50FekiRU8BoBVC6Puq5fhhI9q7uDr6wfOUBgMUlgKJS3T-8O8LJPUxSwsT6wJhS-5LPQXvcX2wMqplkE2V-Bh9RwkHAtq6ET24lngYytvDs87FC36yoV7wz5BToSMp942CLannVoAM.NzF2-7XWdlq4Xi-S8mYFChy4vq_XFhEOWXCgNPbgaHc&dib_tag=se&keywords=100k%2Bohm&qid=1787244843&sprefix=100k%2Bohm%2Caps%2C221&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)

[12v 30amp PSU](https://www.amazon.com/ALITOVE-Universal-Regulated-Switching-Transformer/dp/B06XJVYDDW/ref=sr_1_3?crid=33KTMYODFITA9&dib=eyJ2IjoiMSJ9.QB9-bUMS1NGDNfUvXBX7vypAE3C6srPVtm799ewHuL2Cr4jo4uDP-9dJmuFvvvCYF4_m-9EzuUr_Pn3WZiQUDzKJjWQgI1noYMY9b_OpMDG-NE88nzEUt5CPCy_vPceM3UEN1qB45B2ry7nqLC1K3j1lq2BuMTyXDOIQxZ6T2RJswovw_5_IB79PbhffqADRKmyevEY8R9fVfvnF7KtzUzDHXYCupzKJnNhy6iDXn8Q.aja4sfo2eZ_7L-r5eO9SxCu00qpK2B50zbi9lfXx_LY&dib_tag=se&keywords=12%2Bv%2B30%2Bamp%2BPSU&qid=1787243811&sprefix=12%2Bv%2B30%2Bamp%2Bpsu%2Caps%2C223&sr=8-3&th=1)

[5v step down converter Regulator](https://www.amazon.com/eleUniverse-DC-Step-Down-Converter/dp/B0GGGN73DB/ref=sr_1_6?crid=117AAYUYMLJH9&dib=eyJ2IjoiMSJ9.mu-WE_Vpqeye--wNsQxvRO7ReCOCK9tLlosc9AJL0SrxRMnarFzKepC3EvDgrE6f9ko5kN-AVlTrcmJCyxu3U0V_ZxRvOdYG2Djm6abyRiUUQRRbEmsuR26bD1s3_j-qbWuAEDanxn-gByJHI2BrHfDZ1wI_fcDk5tgdxOr2vFfHGu0iDfwmpa5W8JnOvBlbs7qufXuknLVTlblGgANwUKg14yXKk_jLS-QWTdfjVk8.UQCqi08t6W7IGeTjz3T1LIOOZId9f_YPcUi6_eZuxvU&dib_tag=se&keywords=5v%2B5amp%2Bstep%2Bdown%2Bregulator&qid=1787243907&sprefix=5v%2B5amp%2Bstep%2Bdown%2Bregulator%2Caps%2C220&sr=8-6&th=1)
_______________________________________________________________________________________________________________________________________________________________________________________________________________

## Program Selection
**Creality-style 100k NTC thermistor:** Use `main.py`

**DS18B20 digital temperature sensor:** Use `main_ds18b20.py`

## How It Works

The controller uses a Raspberry Pi Pico running MicroPython to monitor
temperature and control two 12V cooling fans using PWM (Pulse Width Modulation).

One fan is used for intake and the second fan is used for exhaust. The intake
fan begins cooling first. If the enclosure temperature continues to rise, the
exhaust fan activates to increase airflow through the enclosure.

The method used to read temperature depends on which sensor is installed.

### 100K NTC Thermistor

When using a Creality-style 100K NTC thermistor with `main.py`, the basic
temperature sensing path is:

    100K NTC Thermistor -> Voltage Divider -> Pico ADC -> Temperature Calculation

The thermistor changes resistance as temperature changes. The Pico measures
the resulting voltage through its ADC and the program calculates the
thermistor resistance and temperature.

### DS18B20 Digital Temperature Sensor

When using a DS18B20 temperature sensor with `main_ds18b20.py`, the basic
temperature sensing path is:

    DS18B20 -> 1-Wire GPIO -> Digital Temperature Reading

The DS18B20 measures temperature internally and communicates the digital
temperature reading directly to the Pico. Because of this, the DS18B20 does
not require the ADC voltage divider or thermistor resistance calculations.

### Fan Control Path

Regardless of which temperature sensor is used, the resulting temperature
reading is passed to the same basic cooling control system:

    Temperature -> Control Logic -> PWM Outputs -> MOSFET Drivers -> 12V Fans

The Pico does not power the fans directly. Each fan is powered from the 12V
power supply through a MOSFET driver module.

The Pico provides low-voltage PWM control signals to the MOSFET drivers,
allowing the program to independently control the speed of the intake and
exhaust fans.

The intake fan is activated first at the initial cooling threshold. As
temperature increases, the controller increases the intake fan speed and
then activates the exhaust fan. At the highest temperature threshold, both
fans operate at full power.

This staged approach provides airflow when needed without requiring both
fans to operate at full speed continuously.

## Reading the Thermistor

GPIO26 is ADC0 on the Raspberry Pi Pico.

MicroPython reads the ADC using:

    raw = thermistor.read_u16()

`read_u16()` returns an unsigned 16-bit value ranging from 0 to 65535.

Although the RP2040 ADC hardware is 12-bit, MicroPython scales the ADC reading to the 16-bit range used by its ADC API.

The ADC reading is used to calculate the resistance of the thermistor. The resistance is then converted into temperature using the Beta equation for an NTC thermistor.

The thermistor values used in the program are:

    R0 = 100000
    T0 = 25 + 273.15
    BETA = 3950

R0 represents the thermistor's nominal resistance of 100k ohms at 25°C.

T0 converts the 25°C reference temperature into Kelvin for use in the temperature calculation.

BETA describes the temperature/resistance curve of the thermistor.

## Why Average Multiple Samples?

ADC readings naturally contain some noise. PWM switching, wiring, the power supply, and the ADC itself can cause small variations between consecutive measurements.

Instead of making a cooling decision from a single ADC reading, the controller takes 10 samples and averages them.

    total = 0
    samples = 10

    for i in range(samples):
        total += thermistor.read_u16()
        sleep(0.1)

    raw = total // samples

Each reading is taken approximately 0.1 seconds apart.

The readings are added together and divided by the number of samples to produce one averaged ADC value.

This gives the controller a more stable temperature measurement and reduces the chance of changing fan speed because of a single abnormal ADC reading.

## Fan Control

The Raspberry Pi Pico cannot supply the voltage or current required by the 12V fans.

Instead, two GPIO pins generate PWM signals which control separate MOSFET driver modules.

The intake fan is controlled by GPIO15:

    intake_fan = PWM(Pin(15))
    intake_fan.freq(1000)

The exhaust fan is controlled by GPIO14:

    exhaust_fan = PWM(Pin(14))
    exhaust_fan.freq(1000)

The MOSFET modules switch the 12V power supplied to the fans. The Pico only supplies the 3.3V logic signal used to control the MOSFET modules.

This allows the Pico to independently control both fans without attempting to power the motors directly.

## PWM Duty Cycle

PWM controls fan speed by rapidly switching power on and off. The percentage of time the output remains on during each cycle is called the duty cycle.

For example:

    0%   = Fan off
    25%  = Low speed
    50%  = Medium speed
    75%  = High speed
    100% = Full power

MicroPython's `duty_u16()` function accepts values from 0 to 65535.

The program converts a percentage into that range:

    duty = int(percent * 65535 / 100)

For example, 75% duty cycle is approximately:

    49151

That value is then sent to the PWM output using:

    fan.duty_u16(duty)

## Why 1 kHz PWM?

I experimentally tested several PWM frequencies with the 12V radiator fans.

At 1 kHz:

- 25% operated but produced noticeable audible noise.
- 50% operated with less audible noise.
- 75% produced strong airflow without noticeable PWM noise.
- 100% provided maximum airflow.

I also tested 20 kHz. With this particular fan and MOSFET controller, the motor would not reliably operate at the lower duty cycles and effectively only operated at 100%.

Because of those results, I selected 1 kHz and use 75% and 100% as the primary operating speeds.

This is specific to the fans and MOSFET drivers used in this project. Different DC motors and driver modules may behave differently.

## Intake and Exhaust Cooling Strategy

The intake and exhaust fans intentionally do not start at the same time.

The intake fan begins operating first to push cooler outside air into the enclosure.

If the temperature continues to rise, the intake fan increases to full power and the exhaust fan turns on to actively pull hot air out of the enclosure.

The current cooling stages are:

    Temperature <= 82°F
    Intake:  OFF
    Exhaust: OFF

    Temperature >= 85°F
    Intake:  75%
    Exhaust: OFF

    Temperature >= 95°F
    Intake:  100%
    Exhaust: 75%

    Temperature >= 105°F
    Intake:  100%
    Exhaust: 100%

This provides progressive cooling instead of immediately running both fans at full power.

## Why Use Hysteresis?

The controller uses hysteresis to prevent rapid fan cycling around a temperature threshold.

Without hysteresis, a temperature hovering around 85°F could cause this:

    84.9°F -> OFF
    85.0°F -> ON
    84.9°F -> OFF
    85.0°F -> ON

Instead, the intake fan turns on when the temperature reaches 85°F but does not turn back off until the temperature falls to 82°F.

For example:

    85°F -> Intake turns ON
    84°F -> Intake remains ON
    83°F -> Intake remains ON
    82°F -> Intake turns OFF

This prevents the fan from rapidly cycling on and off because of small temperature fluctuations.

## Fail-Safe Behavior

Cooling is treated as the safer state if the temperature sensor produces an invalid ADC reading.

If the thermistor becomes disconnected, a wire fails, or the ADC returns an invalid value, the program commands both fans to 100%.

    if raw == 0 or raw >= 65535:
        set_intake(100)
        set_exhaust(100)

The basic fail-safe philosophy is:

    If temperature cannot be reliably determined, assume maximum cooling is required.

This is especially important when the controller is operating unattended. A temperature sensor failure should result in maximum cooling rather than silently disabling the cooling system.
