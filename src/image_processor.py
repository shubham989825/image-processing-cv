import cv2


def load_image(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {path}")

    return image


def resize_image(image, width=800):
    height, original_width = image.shape[:2]

    ratio = width / original_width
    new_height = int(height * ratio)

    return cv2.resize(image, (width, new_height))


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def detect_edges(image):
    return cv2.Canny(image, 100, 200)
def threshold_image(image):
    _, threshold = cv2.threshold(
        image,
        127,
        255,
        cv2.THRESH_BINARY
    )

    return threshold   