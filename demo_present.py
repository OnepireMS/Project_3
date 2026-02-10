from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time

mc = MyCobot(PI_PORT, PI_BAUD)
speed = 20
mode = 1 
z = 140 

cube    = [180, 150, 95, -180, 0, -45]
d20     = [200, 120, 95, -180, 0, -45]
battery = [220,  90, 95, -180, 0, -45]

mc.send_angles([0, 0, 0, 0, 0, 0], speed)
time.sleep(4)


mc.release_all_servos()
time.sleep(0.5)
input("Move arm to POT by hand, then press ENTER to record... ")

pot_coords = mc.get_coords()
mc.focus_all_servos()
time.sleep(1)

print("POT:", pot_coords)

def at_safe_z(p):
    return [p[0], p[1], z, p[3], p[4], p[5]]

def pick_and_place(obj, pot):
    
    mc.send_coords(at_safe_z(pot), speed, mode)
    time.sleep(4)

    
    mc.send_coords(at_safe_z(obj), speed, mode)
    time.sleep(5)

    
    mc.set_gripper_value(70, 25)   
    time.sleep(1)
    mc.send_coords(obj, speed, mode)
    time.sleep(4)
    mc.set_gripper_value(10, 25)    
    time.sleep(2)
    mc.send_coords(at_safe_z(obj), speed, mode)
    time.sleep(4)

    
    mc.send_coords(at_safe_z(pot), speed, mode)
    time.sleep(5)

    
    mc.send_coords(pot, speed, mode)
    time.sleep(4)
    mc.set_gripper_value(70, 25)   
    time.sleep(2)
    mc.send_coords(at_safe_z(pot), speed, mode)
    time.sleep(4)

while True:
    print("\n1 = Cube\n2 = D20\n3 = Battery\n0 = Stop")
    choice = input("Sort: ").strip()

    if choice == "0":
        mc.stop()
        break
    elif choice == "1":
        pick_and_place(cube, pot_coords)
    elif choice == "2":
        pick_and_place(d20, pot_coords)
    elif choice == "3":
        pick_and_place(battery, pot_coords)
    else:
        print("Invalid.")
