import argparse

from image_processor import load_image
from pipeline import process_image
from config import OUTPUT_DIR
from utils import create_output_directory, save_results


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
        create_output_directory(OUTPUT_DIR)

        image = load_image(args.input)

        results = process_image(image)

        save_results(OUTPUT_DIR, *results)

        print("\nImage processing completed successfully!")
        print("Results saved in the output folder.")

    except FileNotFoundError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()