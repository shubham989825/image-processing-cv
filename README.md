# Image Processing and Edge Detection using OpenCV

A simple Computer Vision project that performs basic image processing operations using Python and OpenCV.

## Features

* Image resizing
* Grayscale conversion
* Gaussian blur
* Binary thresholding
* Canny edge detection
* Command-line execution
* Automatic output directory creation
* Automated unit testing
* Error handling for invalid input images

## Project Structure

```text
image-processing-cv/
├── input/
│   └── sample.jpg.jpg
├── output/
│   ├── resized.jpg
│   ├── grayscale.jpg
│   ├── blurred.jpg
│   ├── threshold.jpg
│   └── edges.jpg
├── src/
│   ├── main.py
│   ├── image_processor.py
│   ├── config.py
│   ├── pipeline.py
│   └── utils.py
├── tests/
│   └── test_image_processor.py
├── .gitignore
├── requirements.txt
├── statement.md
└── README.md
```

## Requirements

* Python 3.x
* OpenCV
* NumPy

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the project from the root directory:

```bash
python src\main.py --input input\sample.jpg.jpg
```

The processed images will be saved in the `output` folder.

## Processing Pipeline

```text
Input Image
    ↓
Resize
    ↓
Grayscale
    ↓
Gaussian Blur
    ↓
Thresholding
    ↓
Canny Edge Detection
    ↓
Output Images
```

## Output

The project generates the following output files:

* `resized.jpg` — resized input image
* `grayscale.jpg` — grayscale version of the image
* `blurred.jpg` — blurred grayscale image
* `threshold.jpg` — binary threshold image
* `edges.jpg` — edges detected using the Canny algorithm

## Error Handling

If the specified input image cannot be loaded, the program displays an error message.

Example:

```bash
python src\main.py --input input\test.jpg
```

Expected result:

```text
Error: Could not load image: input\test.jpg
```

## Testing

The project includes automated unit tests for the image-processing functions.

Run all tests with:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.488s

OK
```

The tests verify:

* Image loading
* Image resizing
* Grayscale conversion
* Gaussian blur
* Thresholding
* Canny edge detection

### Valid Input Test

Command:

```bash
python src\main.py --input input\sample.jpg.jpg
```

Expected result:

```text
Image processing completed successfully!
Results saved in the output folder.
```

### Invalid Input Test

Command:

```bash
python src\main.py --input input\test.jpg
```

Expected result:

```text
Error: Could not load image: input\test.jpg
```

The valid input test verifies the complete image-processing pipeline, the invalid input test verifies error handling, and the unit tests verify individual processing functions.

## Technologies Used

* Python
* OpenCV
* NumPy
* unittest

## Author

Shubham Pratap Singh
