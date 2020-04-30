"""
Copyright (c) 2012-2020 PEQNP. all rights reserved. contact@peqnp.science

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import cv2
import numpy as np
import peqnp as pn


# demo: https://youtu.be/uDWaY742-K8
# ref: https://stackoverflow.com/questions/38827505/detecting-colored-circle-and-its-center-using-opencv

def distance(seq):
    global cir_cen
    return sum(np.linalg.norm(np.asarray(cir_cen[seq[i - 1]]) - np.asarray(cir_cen[seq[i]])) for i in range(len(seq)))


if __name__ == '__main__':
    cir_cen = []

    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()

            frame_gau_blur = cv2.GaussianBlur(frame, (3, 3), 0)

            hsv = cv2.cvtColor(frame_gau_blur, cv2.COLOR_RGB2HSV)

            lower_red = np.array([0, 140, 140])
            higher_red = np.array([255, 255, 255])

            red_range = cv2.inRange(hsv, lower_red, higher_red)
            res_red = cv2.bitwise_and(frame_gau_blur, frame_gau_blur, mask=red_range)
            red_s_gray = cv2.cvtColor(res_red, cv2.COLOR_RGB2HSV)
            canny_edge = cv2.Canny(red_s_gray, 50, 240)

            circles = cv2.HoughCircles(canny_edge, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=10, param2=20, minRadius=1, maxRadius=120)

            cir_cen.clear()
            if circles is not None:
                for i in circles[0, :]:
                    cv2.circle(frame, (i[0], i[1]), 3, (0, 0, 255), 3)
                    cir_cen.append((i[0], i[1]))
                if len(cir_cen) >= 3:
                    seq = pn.hess_sequence(len(cir_cen), oracle=distance, fast=False)
                    for i in range(len(cir_cen)):
                        cv2.line(frame, cir_cen[seq[i - 1]], cir_cen[seq[i]], (0, 255, 0), 3)
            cv2.imshow('circles', frame)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
