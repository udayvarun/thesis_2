import roboticstoolbox as rtb
import swift

def map_to_robot(data):
    env = swift.Swift()
    env.launch(realtime=True)
    panda = rtb.models.Panda()
    env.add(panda)
    dt = 0.01
    while True:
        for q in data:
            panda.q = q
            env.step(dt)
    env.hold()