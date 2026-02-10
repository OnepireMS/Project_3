from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time

mc = MyCobot(PI_PORT, PI_BAUD)
speed = 20
mode = 1  

cube    = [180, 150, 140, -180, 0, -45]
d20     = [200, 120, 140, -180, 0, -45]
battery = [220,  90, 140, -180, 0, -45]

mc.send_angles([0, 0, 0, 0, 0, 0], speed)
time.sleep(4)


mc.release_all_servos()
time.sleep(0.5)
input("Move arm to POT by hand, then press ENTER to record... ")

pot_coords = mc.get_coords()
mc.focus_all_servos()
time.sleep(1)

print("POT:", pot_coords)

while True:
    print("\n1 = Cube\n2 = D20\n3 = Battery\n0 = Stop")
    choice = input("Sort: ").strip()

    if choice == "0":
        mc.stop()
        break

    if choice == "1":
        obj = cube
    elif choice == "2":
        obj = d20
    elif choice == "3":
        obj = battery
    else:
        print("Invalid.")
        continue
    
    mc.set_gripper_value(70, 25)
    time.sleep(0.5)
    
    mc.send_coords(obj, speed, mode)
    time.sleep(5)
    mc.set_gripper_value(10, 25)
    time.sleep(2)
    
    mc.send_coords(pot_coords, speed, mode)
    time.sleep(5)
    mc.set_gripper_value(70, 25)
    time.sleep(2)
