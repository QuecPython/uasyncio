from usr.uasyncio.core import create_task, sleep, sleep_ms, run
from machine import Pin


async def blink(led, period_ms, name=''):
    while True:
        led.write(1)
        print('led on: {}'.format(name))
        await sleep_ms(period_ms)
        led.write(0)
        print('led off: {}'.format(name))
        await sleep_ms(period_ms)


async def main(led1, led2):
    create_task(blink(led1, 700, 'led1'))
    create_task(blink(led2, 400, 'led2'))
    sleep(10)


if __name__ == '__main__':
    # Running
    run(
        main(
            Pin(Pin.GPIO1, Pin.OUT, Pin.PULL_DISABLE, 0),  # led1
            Pin(Pin.GPIO2, Pin.OUT, Pin.PULL_DISABLE, 0)   # led2
        )
    )
