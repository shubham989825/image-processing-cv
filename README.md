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
│   └── image_processor.py
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

The project generates:

* `resized.jpg` — resized input image
* `grayscale.jpg` — grayscale version
* `blurred.jpg` — blurred grayscale image
* `threshold.jpg` — binary threshold image
* `edges.jpg` — detected edges using Canny edge detection

## Error Handling

If the specified input image cannot be loaded, the program displays an error message.

Example:

```bash
python src\main.py --input input\test.jpg
```

## Testing

The project can be tested from the command line.

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

The valid input test verifies the complete image-processing pipeline, while the invalid input test verifies input error handling.

## Technologies Used

* Python
* OpenCV
* NumPy

## Author

Shubham Pratap Singh




