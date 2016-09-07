import cv2

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path")
    parser.add_argument("-o", dest="outputf", default="labels.txt", help="output json file")
    args = parser.parse_args()
    return args

def main(args):
    import glob
    import os

    seen = []
    with open("labels.txt") as fh:
        for l in fh:
            seen.append(l.rsplit(" ", 1)[0].strip())
    print seen

    images = glob.glob(os.path.join(args.path, "*/*.jpg"))

    for i in images:
        print i
        if i in seen:
            print "skipping %s" % i
            continue
        try:
            im = cv2.imread(i)
            cv2.imshow("image", im)
            key = cv2.waitKey()
        except:
            continue
        if key == ord("l"):
            c = 1
        else:
            c = 0
        line = " ".join([i, str(c)])
        with open(args.outputf, "a") as fh:
            fh.write(line + "\n")

if __name__ == '__main__':
    args = parse_args()
    main(args)
