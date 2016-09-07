import cv2
import json

POINTS = []
WIDTH = None
HEIGHT = None
CHANNELS = None

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="input image")
    parser.add_argument("-o", dest="outputf", help="output json file")
    parser.add_argument("-i", dest="inputf", help="inputf json file")
    args = parser.parse_args()
    return args

def on_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        POINTS.append((x, y))
        draw_image_with_points("image", param)


def draw_image_with_points(name, image):
    image = image.copy()
    print POINTS
    for x, y in POINTS:
        cv2.circle(image, (x,y), 2, (0,255,0), -1)
    cv2.imshow(name, image)

def main(image=None, outputf=None, inputf=None):
    global POINTS
    nim = cv2.imread(image)
    HEIGHT, WIDTH, CHANNELS = nim.shape
    print "shape: %s" % list(nim.shape)

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_event, nim)

    if inputf is not None:
        with open(inputf) as fh:
            POINTS = json.load(fh)
            print "points: %s" % len(POINTS)
        
    draw_image_with_points("image", nim)
    cv2.waitKey()

    if outputf is not None:
        with open(outputf, "w") as fh:
            json.dump(POINTS, fh)


if __name__ == '__main__':
    args = parse_args()
    main(**args.__dict__)
