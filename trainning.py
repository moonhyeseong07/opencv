import cv2
import matplotlib.pyplot as plt
import numpy as np

points = []

def onclick(event):
    if len(points) < 4:
        points.append((event.xdata, event.ydata))
        plt.plot(event.xdata, event.ydata, 'ro')
        plt.draw()
        if len(points) == 4:
            plt.close()

image_path = 'img13.jpg'
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image file not found at {image_path}")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots()
ax.imshow(image)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

if len(points) == 4:
    src_points = np.array(points, dtype=np.float32)

    width = max(int(np.linalg.norm(src_points[0] - src_points[3])), int(np.linalg.norm(src_points[1] - src_points[2])))
    height = max(int(np.linalg.norm(src_points[0] - src_points[1])), int(np.linalg.norm(src_points[3] - src_points[2])))

    dst_points = np.array([
        [0, height],
        [0, 0],
        [width, 0],
        [width, height]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    transformed_image = cv2.warpPerspective(image, matrix, (width, height))

    plt.imshow(transformed_image)
    plt.show()
else:
    print("4개의 점을 모두 클릭하지 않았습니다.")
