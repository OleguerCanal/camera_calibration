import apriltag
import cv2
import numpy as np

def get_corners(img, boardSize, subpixel = False):
    # Convert to grayscale if its not
    if (len(img.shape) != 2):
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    found, corners = cv2.findChessboardCorners(img, boardSize)

    if not found or not subpixel:
        return False, corners

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)  # termination criteria
    corners_subpx = cv2.cornerSubPix(img, corners, boardSize, (-1,-1), criteria)  # subpixel accuracy

    # TODO(Oleguer): Detect origin using apriltag and reorient
    return True, corners_subpx

def get_apriltag_center(img):
    pass




if __name__ == "__main__":
    gray_img = cv2.imread("data/calib_example.png", cv2.IMREAD_GRAYSCALE)
    boardSize = (4, 4)

    found, corners = get_corners(gray_img, boardSize, False)

    # Show
    rgb_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
    rgb_img = cv2.drawChessboardCorners(rgb_img, boardSize, corners, found)
    cv2.imshow("rgb_img", rgb_img)
    cv2.waitKey(0)