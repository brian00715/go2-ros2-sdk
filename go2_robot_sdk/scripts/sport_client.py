import json
from dataclasses import dataclass
from typing import List
from unitree_api.msg import Request

# API Constants
ROBOT_SPORT_API_ID_DAMP = 1001
ROBOT_SPORT_API_ID_BALANCESTAND = 1002
ROBOT_SPORT_API_ID_STOPMOVE = 1003
ROBOT_SPORT_API_ID_STANDUP = 1004
ROBOT_SPORT_API_ID_STANDDOWN = 1005
ROBOT_SPORT_API_ID_RECOVERYSTAND = 1006
ROBOT_SPORT_API_ID_EULER = 1007
ROBOT_SPORT_API_ID_MOVE = 1008
ROBOT_SPORT_API_ID_SIT = 1009
ROBOT_SPORT_API_ID_RISESIT = 1010
ROBOT_SPORT_API_ID_SWITCHGAIT = 1011
ROBOT_SPORT_API_ID_TRIGGER = 1012
ROBOT_SPORT_API_ID_BODYHEIGHT = 1013
ROBOT_SPORT_API_ID_FOOTRAISEHEIGHT = 1014
ROBOT_SPORT_API_ID_SPEEDLEVEL = 1015
ROBOT_SPORT_API_ID_HELLO = 1016
ROBOT_SPORT_API_ID_STRETCH = 1017
ROBOT_SPORT_API_ID_TRAJECTORYFOLLOW = 1018
ROBOT_SPORT_API_ID_CONTINUOUSGAIT = 1019
ROBOT_SPORT_API_ID_CONTENT = 1020
ROBOT_SPORT_API_ID_WALLOW = 1021
ROBOT_SPORT_API_ID_DANCE1 = 1022
ROBOT_SPORT_API_ID_DANCE2 = 1023
ROBOT_SPORT_API_ID_SWITCHJOYSTICK = 1027
ROBOT_SPORT_API_ID_POSE = 1028
ROBOT_SPORT_API_ID_SCRAPE = 1029
ROBOT_SPORT_API_ID_FRONTFLIP = 1030
ROBOT_SPORT_API_ID_FRONTJUMP = 1031
ROBOT_SPORT_API_ID_FRONTPOUNCE = 1032


@dataclass
class PathPoint:
    timeFromStart: float
    x: float
    y: float
    yaw: float
    vx: float
    vy: float
    vyaw: float



class SportClient:
    def damp(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_DAMP
        return req

    def balance_stand(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_BALANCESTAND
        return req

    def stop_move(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_STOPMOVE
        return req

    def stand_up(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_STANDUP
        return req

    def stand_down(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_STANDDOWN
        return req

    def recovery_stand(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_RECOVERYSTAND
        return req

    def euler(self, roll: float, pitch: float, yaw: float) -> Request:
        req = Request()
        req.parameter = json.dumps({"x": roll, "y": pitch, "z": yaw})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_EULER
        return req

    def move(self, vx: float, vy: float, vyaw: float) -> Request:
        req = Request()
        req.parameter = json.dumps({"x": vx, "y": vy, "z": vyaw})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_MOVE
        return req

    def sit(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_SIT
        return req

    def rise_sit(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_RISESIT
        return req

    def switch_gait(self, d: int) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": d})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_SWITCHGAIT
        return req

    def trigger(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_TRIGGER
        return req

    def body_height(self, height: float) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": height})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_BODYHEIGHT
        return req

    def foot_raise_height(self, height: float) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": height})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_FOOTRAISEHEIGHT
        return req

    def speed_level(self, level: int) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": level})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_SPEEDLEVEL
        return req

    def hello(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_HELLO
        return req

    def stretch(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_STRETCH
        return req

    def trajectory_follow(self, path: List[PathPoint]) -> Request:
        req = Request()
        js_path = []
        for point in path[:30]:  # Only process first 30 points
            js_point = {
                "t_from_start": point.timeFromStart,
                "x": point.x,
                "y": point.y,
                "yaw": point.yaw,
                "vx": point.vx,
                "vy": point.vy,
                "vyaw": point.vyaw,
            }
            js_path.append(js_point)
        req.parameter = json.dumps(js_path)
        req.header.identity.api_id = ROBOT_SPORT_API_ID_TRAJECTORYFOLLOW
        return req

    def switch_joystick(self, flag: bool) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": flag})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_SWITCHJOYSTICK
        return req

    def continuous_gait(self, flag: bool) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": flag})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_CONTINUOUSGAIT
        return req

    def wallow(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_WALLOW
        return req

    def content(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_CONTENT
        return req

    def pose(self, flag: bool) -> Request:
        req = Request()
        req.parameter = json.dumps({"data": flag})
        req.header.identity.api_id = ROBOT_SPORT_API_ID_POSE
        return req

    def scrape(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_SCRAPE
        return req

    def front_flip(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_FRONTFLIP
        return req

    def front_jump(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_FRONTJUMP
        return req

    def front_pounce(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_FRONTPOUNCE
        return req

    def dance1(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_DANCE1
        return req

    def dance2(self) -> Request:
        req = Request()
        req.header.identity.api_id = ROBOT_SPORT_API_ID_DANCE2
        return req
