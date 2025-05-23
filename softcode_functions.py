import time

from sound_functions import sound_device, tone_600
from village.manager import get_task

task = get_task()


def function1():
    task.send_softcode_to_bpod(1)


def function2():
    start_time = time.time()
    sound = tone_600(duration = 1, gain = 0.05)
    sound_device.load(sound)
    end_time = time.time()
    print("load delay: ", end_time - start_time)


def function10():
    # to test overriding outputs
    task.bpod.manual_override_output(("PWM1", 255))  # funciona
    time.sleep(1)
    task.bpod.manual_override_output(("PWM1", 0))  # funciona
    time.sleep(1)
    task.bpod.manual_override_output("Valve1")
    time.sleep(1)
    task.bpod.manual_override_output("Valve1Off")
    time.sleep(1)
    task.bpod.manual_override_output("BNC1High")  # funciona
    time.sleep(1)
    task.bpod.manual_override_output("BNC1Low")  # funciona


def function11():
    # to test overriding inputs
    task.bpod.manual_override_input("Port1In")  # funciona
    time.sleep(1)
    task.bpod.manual_override_input("Port1Out")  # funciona
    time.sleep(1)


def function33():
    start_time = time.time()
    sound_device.play()
    end_time = time.time()
    print("play delay: ", end_time - start_time)
