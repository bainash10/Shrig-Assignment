import cv2
import numpy as np

image = cv2.imread("input.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges=cv2.Canny(blur, threshold1=50, threshold2=150)


contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rectangles = []
# Loop through each detected contour
for cnt in contours:
     # Approximate the contour to a polygon with fewer points.
    # 0.02 * arcLength means approximation precision (smaller = more accurate).
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4 and cv2.contourArea(approx) > 500: #area is kept greater than 500 pixels to ignore small noise
        rectangles.append(approx) # If both conditions match, save it to our rectangles list



for i, rect in enumerate(rectangles): #here i is an index and rect is a value
    rect = rect.reshape(4, 2) # reshaping the array rect into a shape with 4 rows and 2 columns.
    # Sort corners to consistent order: top-left, top-right, bottom-right, bottom-left
    # Sort all 4 points by y-coordinate (vertical) 
    rect = sorted(rect, key=lambda p: (p[1], p[0])) 

    # Sort top two points by horizontal position (x)
    top_points = sorted(rect[:2], key=lambda p: p[0])

    # Sort bottom two points by horizontal position (x)
    bottom_points = sorted(rect[2:], key=lambda p: p[0])

    # Arrange points in consistent order:
    # [top-left, top-right, bottom-right, bottom-left]
    ordered_rect = np.array([
        top_points[0],      # top-left : smallest x among top points 
        top_points[1],      # top-right : largest x among top points
        bottom_points[1],   # bottom-right : largest x among bottom points
        bottom_points[0]    # bottom-left : smallest x among bottom points
        ], dtype="float32")

    # Compute width and height for the new aligned rectangle
    width = int(max(
        np.linalg.norm(ordered_rect[0] - ordered_rect[1]),  # top edge length
        np.linalg.norm(ordered_rect[2] - ordered_rect[3])   # bottom edge length
    ))
    height = int(max(
        np.linalg.norm(ordered_rect[0] - ordered_rect[3]),  # left edge length
        np.linalg.norm(ordered_rect[1] - ordered_rect[2])   # right edge length
    ))
    
    # Destination points for the straightened rectangle
    dst = np.array([
    [0, 0],                 # top-left corner
    [width - 1, 0],          # top-right corner
    [width - 1, height - 1], # bottom-right corner
    [0, height - 1]          # bottom-left corner
    ], dtype="float32")
    
    # Calculate perspective transform matrix and warp the rectangle to upright
    M = cv2.getPerspectiveTransform(ordered_rect, dst)
    warped =cv2.warpPerspective(image, M, (width,height))

    # Saving the deskewed/aligned rectangle image
    cv2.imwrite(f"aligned_rectangle_{i+1}.jpg", warped)

print("done alignment and saved photo")
