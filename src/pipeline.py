import cv2

from image_processor import (
    resize_image,
    convert_to_grayscale,
    blur_image,
    threshold_image,
    detect_edges
)


def process_image(image):
    resized = resize_image(image)
    gray_image = convert_to_grayscale(resized)
    blurred = blur_image(gray_image)
    threshold = threshold_image(blurred)
    edges = detect_edges(blurred)

    return resized, gray_image, blurred, threshold, edges