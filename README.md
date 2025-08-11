# Shrig Assignment

This repository contains two separate tasks for processing rectangle images:
1. **Task 1: Rectangle Numbering**  
   Assign numbers (1 to 4) inside each rectangle based on the length of a line drawn inside it.  
   - **Shorter line represents Lower number**  
   - **No reordering of the rectangles in the original image**  

2. **Task 2: Rectangle Alignment**  
   Align and straighten all given rectangle images so they are upright (deskewed). 

---

## Folder Structure

| Folder / File Path                              | Description                                                       |
|-------------------------------------------------|-------------------------------------------------------------------|
| **Task1_Numbering/**                            | Contains all files for Task 1 (rectangle numbering)               |
| `Test_code_for_Task1.ipynb`                 | Jupyter Notebook with step by step Task 1 implementation          |
| `rectangle_numbering.py`                    | Clean, organized Python script for Task 1                         |
| `input.png`                                 | Input image used for Task 1                                             |
| **Task2_Alignment/**                            | Contains all files for Task 2 (rectangle alignment)               |
|  `Test_code_for_Task2.ipynb`                 | Jupyter Notebook with step-by-step Task 2 implementation          |
|  `rectangle_alignment.py`                    | Clean, organized Python script for Task 2                         |
| `input.png`                                 | Input image used for Task 2                                             |
| **README.md**                                   | Project documentation                                              |

---

##  Task 1 – Rectangle Numbering

**Algorithm:**
1. **Image Preprocessing**  
   - Convert RGB to Grayscale  
   - Apply Gaussian Blur for noise reduction  
   - Use Canny Edge Detection to detect edges

2. **Rectangle Detection**  
   - Find contours using `cv2.findContours`  
   - Filter shapes with four vertices (rectangles)  
   - Crop each rectangle as Region of Interest (ROI)

3. **Line Detection Inside Rectangle**  
   - Apply Hough Line Transform (`cv2.HoughLinesP`) on ROI  
   - Measure line lengths using Euclidean distance (`np.linalg.norm`)  
   - Sort by length and assign numbers (shorter = lower number)

4. **Result**  
   - Draw the assigned number inside the rectangle  
   - Save output image

---

##  Task 2 – Rectangle Alignment

**Algorithm:**
1. **Image Preprocessing**  
   - Convert RGB to Grayscale  
   - Apply Gaussian Blur for noise reduction  
   - Use Canny Edge Detection to detect edges

2. **Rectangle Detection**  
   - Find contours and approximate polygons  
   - Identify corner points of each rectangle

3. **Deskewing with Perspective Transform**  
   - Order points in consistent order (top-left, top-right, bottom-right, bottom-left)  
   - Calculate rectangle’s width and height  
   - Map corners to a perfect rectangle using `cv2.getPerspectiveTransform`  
   - Apply warp using `cv2.warpPerspective`

4. **Result**  
   - Save aligned (upright) rectangles


## Requirements
Install dependencies before running scripts:
```bash
pip install requirements.txt
```
Or
```bash
pip install opencv-python numpy matplotlib
```