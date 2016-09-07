import numpy as np
import pylab as P


def imgrid(images, normalize=False):
    """
    show a grid viz ofimages
    """
    if isinstance(images, list):
        images = np.array(images)

    if images.ndim < 4:
        images = np.expand_dims(images, axis=2)

    nimages = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]

    if normalize:
        images -= np.min(images)
        images /= np.max(images)

    s = int(np.ceil(np.sqrt(nimages)))

    bordered_image = np.zeros((s*(h+1)+1, s*(w+1)+1, c),dtype=np.float32)
    for i in range(s):
        for j in range(s):
            idx = i*s+j
            y0 = i*(h+1)+1
            y1 = y0 + h
            x0 = j*(w+1)+1
            x1 = x0 + w
            bordered_image[y0:y1, x0:x1, :] = images[idx, :h, :w, :]

    return bordered_image


def imgrid_show(*args, **kwargs):
    grid = imgrid(*args, **kwargs)

    # turn of tick marks
    P.xticks([])
    P.yticks([])
    P.imshow(grid, cmap=P.cm.Greys_r, interpolation='nearest')


if __name__ == '__main__':
    imgrid_show()
