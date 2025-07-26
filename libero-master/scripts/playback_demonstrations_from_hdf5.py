import h5py
from PIL import Image
import cv2
import numpy as np


#TODO: check path
file_path = "/home/whr/LIBERO/libero/libero-master/backdoored_datasets/backdoored_goal_bddl/BACKDOORED_pick_the_milk_and_place_it_in_the_basket.bddl_demo.hdf5"
f = h5py.File(file_path, "r")

# print(f.keys())
# print(f["data"].keys())
# print(f["data"].attrs.keys())

# print(list(f["data"]["demo_1"].keys()))

# 自动获取第一个 demo 的名字
demo_key = list(f["data"].keys())[0]
frames = f["data"][demo_key]["obs"]["agentview_rgb"][:]


#frames = f["data"]["demo_0"]["obs"]["agentview_rgb"][:]

for i, frame in enumerate(frames):
    frame = np.flipud(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    frame = cv2.resize(frame, (512, 512), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("Agentview", frame)
    key = cv2.waitKey(50)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
