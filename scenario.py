from morse.builder import *

arm = Arm('arm')
arm.translate(x=0.0, z=0)
arm.properties(Object = True, Graspable = False, Label = "ROBOT")

driver = ATRV()
driver.translate(x=2.0, y=2.0)

torque = ForceTorque()
# json message format:
#   {"data":[{"component":<str>,"force":[<num>,<num>,<num>],"torque":[<num>,<num>,<num>]},...]}
# e.g.
#   {"data":[{"component":"segment_1","force":[0,0,0],"torque":[1,0,0]},
#            {"component":"segment_2","force":[0,0,0],"torque":[5,0,0]},
#            {"component":"base","force":[0,0,0],"torque":[0,0,0]}]}
torque.level( "multiple" )
odom = Odometry()

arm.append( torque )
arm.append( odom )

semantic = SemanticCamera()
semantic.translate(x=0.2, y=0.3, z=0.9)
semantic.rotate(x=0.25, y=0.0, z=0.0)
semantic.frequency(frequency=30)
arm.append(semantic)

keyboard = Keyboard()
keyboard.properties(Speed=3.0)
driver.append(keyboard)

torque.add_interface( 'socket' )
odom.add_interface( 'socket' )

env = Environment('land-1/trees')
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.0470, 0, 0.7854])
