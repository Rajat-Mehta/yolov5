from utils.utils import *

res = kmean_anchors(path='/raid/rajat/datasets/yolo/gpr_damage_aug/train.txt', n=9, img_size=(640, 640), thr=0.20, gen=1000)

print(res)