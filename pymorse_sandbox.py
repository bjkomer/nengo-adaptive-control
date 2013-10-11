import pymorse
import time

torque_out = { "data":[ { "component":"segment_1",
                          "force":[ 0, 0, 0 ],
                          "torque":[ 0, 0, 0 ] },
                        { "component":"segment_2",
                          "force":[ 0, 0, 0 ],
                          "torque":[ 0, 0, 0] } ] }

def odom_reading( odom ):
  print( odom )

with pymorse.Morse() as sim:
  #print( dir(sim) )
  #print( sim.get_stream_port(sim.streams()[0]) )
  #print( dir(sim.arm.torque) )

  sim.arm.odom.subscribe( odom_reading )

  torque_out['data'][0]['torque'][0] = 2
  torque_out['data'][1]['torque'][0] = 5
  sim.arm.torque.publish( torque_out )

  time.sleep(0.1)
