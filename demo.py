from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time
import math
mc = MyCobot(PI_PORT, PI_BAUD)

speed = 20

#mc.send_angles([0, 0, 0, 0, 0, 0], 20)
#time.sleep(6)

#mc.release_all_servos()
#time.sleep(6)
print(mc.get_coords())
print(mc.get_angles())

#mc.send_coords([200, 200, 160, 0, 0, 0], 30, 1)
mc.set_gripper_value(100, 25)
time.sleep(1)

#mc.send_angles([54.58, -49.92, -89.73, 55.72, 0, 9.66], 20)
#time.sleep(5)

#mc.set_gripper_value(30, 25)
#time.sleep(1)

mc.send_coords([180, 150, 140, -180, 0, -45], speed, 1)
time.sleep(5)

mc.send_coords([180, 150, 95, -180, 0, -45], speed, 1)
time.sleep(4)
mc.set_gripper_value(3, 25)
time.sleep(2)

mc.send_coords([180, 150, 200, -180, 0, -45], speed, 1)
time.sleep(3)

mc.send_coords([240, -10, 200, -180, 0, 180], speed, 1)
time.sleep(5)

mc.send_coords([240, -10, 105, -180, 0, 180], speed, 1)
time.sleep(4)
mc.set_gripper_value(10, 25)
time.sleep(1)



