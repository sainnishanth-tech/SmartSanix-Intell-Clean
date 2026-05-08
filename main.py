from machine import Pin, ADC, I2C
import time
from vl53l0x import VL53L0X

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

tof = VL53L0X(i2c)

mq135 = ADC(Pin(34))
mq135.atten(ADC.ATTN_11DB)

ir_sensor = Pin(27, Pin.IN)

water_sensor = ADC(Pin(35))
water_sensor.atten(ADC.ATTN_11DB)

sos_button = Pin(14, Pin.IN, Pin.PULL_UP)

buzzer = Pin(26, Pin.OUT)

buzzer.off()

GAS_THRESHOLD = 2500
WATER_THRESHOLD = 1000
DISTANCE_THRESHOLD = 800

occupied = False
occupancy_counter = 0

restock_counter = 0
restock_required = False

water_counter = 0
water_low = False

cleaning_counter = 0
cleaning_required = False

usage_count = 0
previous_occupied = False

last_alert_time = 0
ALERT_COOLDOWN = 5

def average_adc(adc, samples=5):

    total = 0

    for _ in range(samples):
        total += adc.read()
        time.sleep(0.02)

    return total // samples

def trigger_buzzer():

    global last_alert_time

    current_time = time.time()

    if current_time - last_alert_time > ALERT_COOLDOWN:

        buzzer.on()

        time.sleep(0.3)

        buzzer.off()

        last_alert_time = current_time

print("================================")
print(" SMARTSAN+ SYSTEM STARTED ")
print("================================")

while True:

    distance = tof.read()

    if distance < DISTANCE_THRESHOLD:

        occupancy_counter += 1

    else:

        occupancy_counter = 0

    if occupancy_counter >= 3:
        occupied = True
    else:
        occupied = False

    if occupied and not previous_occupied:
        usage_count += 1

    previous_occupied = occupied

    gas_value = average_adc(mq135)

    if gas_value > GAS_THRESHOLD:

        cleaning_counter += 1

    else:

        cleaning_counter = 0

    if cleaning_counter >= 3:
        cleaning_required = True
    else:
        cleaning_required = False

    if ir_sensor.value() == 1:

        restock_counter += 1

    else:

        restock_counter = 0

    if restock_counter >= 3:
        restock_required = True
    else:
        restock_required = False

    water_value = average_adc(water_sensor)

    if water_value < WATER_THRESHOLD:

        water_counter += 1

    else:

        water_counter = 0

    if water_counter >= 3:
        water_low = True
    else:
        water_low = False

    sos_alert = False

    if sos_button.value() == 0:

        time.sleep(0.05)

        if sos_button.value() == 0:
            sos_alert = True

    if (
        cleaning_required or
        restock_required or
        water_low or
        sos_alert
    ):
        trigger_buzzer()

    else:
        buzzer.off()

    print("\n================================")

    if occupied:
        print("STATUS: OCCUPIED")
    else:
        print("STATUS: VACANT")

    print("Distance:", distance, "mm")

    print("Gas Value:", gas_value)

    if cleaning_required:
        print("🚨 CLEANING REQUIRED")

    print("Water Value:", water_value)

    if restock_required:
        print("🚨 RESTOCK REQUIRED")
    else:
        print("Stock Available")

    if water_low:
        print("🚨 WATER REFILL REQUIRED")
    else:
        print("Water OK")

    if sos_alert:
        print("🚨 EMERGENCY SOS ALERT")

    print("Usage Count:", usage_count)

    time.sleep(1)
