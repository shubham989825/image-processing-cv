import os
import sys
import unittest

sys.path.insert(0, os.path.abspath("src"))

from image_processor import (
    load_image,
    resize_image,
    convert_to_grayscale,
    blur_image,
    threshold_image,
    detect_edges
)


class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        self.image_path = "input/sample.jpg.jpg"

    def test_load_image(self):
        image = load_image(self.image_path)
        self.assertIsNotNone(image)

    def test_resize_image(self):
        image = load_image(self.image_path)
        resized = resize_image(image)
        self.assertEqual(resized.shape[1], 800)

    def test_grayscale_conversion(self):
        image = load_image(self.image_path)
        resized = resize_image(image)
        gray = convert_to_grayscale(resized)
        self.assertEqual(len(gray.shape), 2)

    def test_blur_image(self):
        image = load_image(self.image_path)
        resized = resize_image(image)
        gray = convert_to_grayscale(resized)
        blurred = blur_image(gray)
        self.assertEqual(blurred.shape, gray.shape)

    def test_threshold_image(self):
        image = load_image(self.image_path)
        resized = resize_image(image)
        gray = convert_to_grayscale(resized)
        blurred = blur_image(gray)
        threshold = threshold_image(blurred)
        self.assertEqual(threshold.shape, blurred.shape)

    def test_edge_detection(self):
        image = load_image(self.image_path)
        resized = resize_image(image)
        gray = convert_to_grayscale(resized)
        blurred = blur_image(gray)
        edges = detect_edges(blurred)
        self.assertEqual(edges.shape, blurred.shape)


if __name__ == "__main__":
    unittest.main()