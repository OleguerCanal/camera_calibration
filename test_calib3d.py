from camera_calibrator import CameraCalibrator
import numpy as np
import cv2
import pickle
import copy
from glob import glob

def pmat(mat):
    '''Print matrix
    '''
    print(np.round(mat, 2))


# corr = np.array([[0, 0, 1, 0],
#                 [0, 1, 0, 0],
#                 [1, 0, 0, 0],
#                 [0, 0, 0, 1]])

if __name__ == "__main__":
    calib = CameraCalibrator(board_shape=(6, 7), tile_side=0.10, apriltag_families="tag36h10")
    
    Ta_is = []
    Tb_is = []

    paths = glob("data/157*/")

    for path in paths:
        image = cv2.imread(path + "amplitude.png", cv2.IMREAD_GRAYSCALE)
        A_trans = np.load(path + "translation.npy")
        A_rot = np.load(path + "rotation.npy")
        f = open(path + "/xyz.pkl", "rb")
        xyz_coordinates_matrix = pickle.load(f)

        cam_to_world = calib.transquat_to_mat(A_trans, A_rot)
        world_to_cam = np.linalg.inv(cam_to_world) 
        cam_to_chess = calib.chessboard_extrinsics_3D(image, xyz_coordinates_matrix)

        # print("World to cam:")
        # pmat(world_to_cam)

        # print("Cam to chess:")
        # pmat(cam_to_chess)

        world_to_chess = np.dot(cam_to_chess, world_to_cam)
        print("World to chess:")
        pmat(world_to_chess)

        a = raw_input()
        Ta_is.append(world_to_cam)
        Tb_is.append(cam_to_chess)


    # X = calib.eye_in_hand_finetunning(Ta_is, Tb_is)
    # print("X:")
    # print(X)
    # print("Before:")
    # print(Ta_is[0])
    # print("After:")
    # print(np.dot(X, Ta_is[0]))