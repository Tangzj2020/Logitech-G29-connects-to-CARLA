import pygame
import pygame.joystick
from configparser import ConfigParser

# Collect expert datas via G29
def collect_buffer():
  # initialize steering wheel
  pygame.joystick.init()
  joystick_count = pygame.joystick.get_count()
  if joystick_count > 1:
    raise ValueError("please connect just one joystick")
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  parser = ConfigParser()
  parser.read('wheel_config.ini')
  steer_index = int(parser.get('G29 Racing Wheel', 'steering_wheel'))
  throttle_index = int(parser.get('G29 Racing Wheel', 'throttle'))
  brake_index = int(parser.get('G29 Racing Wheel', 'brake'))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return True

  numAxes = joystick.get_numaxes()
  jsInputs = [float(joystick.get_axis(i)) for i in range(numAxes)]
  control0 = carla.VehicleControl()
  # transform jsInputs to corresponding data spec
  steerCmd = -1.0 * jsInputs[steer_index]
  print("jsinputs[steer_index]:{}".format(jsInputs[steer_index]))
  print("jsinputs[throttle_index]:{}".format(jsInputs[throttle_index]))
  print("jsinputs[brake_index]:{}".format(jsInputs[brake_index]))
  throttleCmd = 1.5 * (-1.0 * jsInputs[throttle_index] + 1.0)
  brakeCmd = 1.5 * (1.0 * jsInputs[brake_index] - 1.0)
  if throttleCmd == 1.5 and brakeCmd == -1.5:
    throttleCmd = 0.0
    brakeCmd = 0.0
  print("steerCmd:{}".format(steerCmd))
  print("throttleCmd:{}".format(throttleCmd))
  print("brakeCmd:{}".format(brakeCmd))
  control0.steer = steerCmd
  control0.brake = brakeCmd
  control0.throttle = throttleCmd
  steer = torch.tensor([steerCmd])
  accel = torch.tensor([throttleCmd]) + torch.tensor([brakeCmd])
  actions = torch.tensor([accel, steer])
  return actions