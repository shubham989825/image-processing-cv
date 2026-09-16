import cv2
import argparse
import os

from image_processor import (
    load_image,
    resize_image,
    convert_to_grayscale,
    blur_image,
    threshold_image,
    detect_edges
)


def main():

    parser = argparse.ArgumentParser(
        description="Image Processing and Edge Detection using OpenCV"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image"
    )

    args = parser.parse_args()

    try:
        # Create output directory if it does not exist
        os.makedirs("output", exist_ok=True)

        # Load image
        image = load_image(args.input)

        # Image processing pipeline
        resized = resize_image(image)
        gray_image = convert_to_grayscale(resized)
        blurred = blur_image(gray_image)
        threshold = threshold_image(blurred)
        edges = detect_edges(blurred)

        # Save results
        cv2.imwrite("output/resized.jpg", resized)
        cv2.imwrite("output/grayscale.jpg", gray_image)
        cv2.imwrite("output/blurred.jpg", blurred)
        cv2.imwrite("output/threshold.jpg", threshold)
        cv2.imwrite("output/edges.jpg", edges)

        print("\nImage processing completed successfully!")
        print("Results saved in the output folder.")

    except FileNotFoundError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()