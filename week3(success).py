from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time
import math
h = int(0)
k = int(0)
r = int(240)
z = int(180)
mc = MyCobot(PI_PORT, PI_BAUD)

mc.send_angles([0, 0, 0, 0, 0, 0], 20)
time.sleep(6)

number_of_steps = int(input("Give number of steps: "))
for i in range(number_of_steps):
    #tolerance = 4.0     
    #timeout_s = 8.0     
    #poll_dt = 0.2      

    theta = math.radians(360/number_of_steps * i)
    x_coordinates = h + (r * math.cos(theta))
    y_coordinates = k + (r * math.sin(theta))
    mc.send_coords([x_coordinates, y_coordinates, z, 0, 0, 0], 30, 1)
    time.sleep(8)
    #start_t = time.time()
    #while True:
        #current = mc.get_coords()
        #if isinstance(current, (list, tuple)) and len(current) >= 3:  
            #dx = current[0] - x_coordinates
            #dy = current[1] - y_coordinates
            #dz = current[2] - z
         
            #if (dx*dx + dy*dy + dz*dz) ** 0.5 <= tolerance:
                #break

     
        #if time.time() - start_t > timeout_s:
            #print("Timeout: could not reach point", i)
            #break

        #time.sleep(poll_dt)

    

