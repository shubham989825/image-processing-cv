import os
import cv2


def create_output_directory(path):
    os.makedirs(path, exist_ok=True)


def save_results(output_dir, resized, gray_image, blurred, threshold, edges):
    cv2.imwrite(f"{output_dir}/resized.jpg", resized)
    cv2.imwrite(f"{output_dir}/grayscale.jpg", gray_image)
    cv2.imwrite(f"{output_dir}/blurred.jpg", blurred)
    cv2.imwrite(f"{output_dir}/threshold.jpg", threshold)
    cv2.imwrite(f"{output_dir}/edges.jpg", edges)