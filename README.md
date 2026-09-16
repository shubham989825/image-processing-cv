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



