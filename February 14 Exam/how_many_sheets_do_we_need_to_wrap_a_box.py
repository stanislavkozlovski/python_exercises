"""
Given the dimensions of a box and the area of the wrapping paper, calculate how many sheets we will need to wrap the box
When wrapping, there is always a 9.8% loss of paper

input:
area of paper
height of box
width of box
depth of box

sample input:
0.80
1.23
0.78
0.50

expected output:
6
"""
from math import ceil


try:
    wpaper_area = float(input())
    box_height = float(input())
    box_width = float(input())
    box_depth = float(input())

    if wpaper_area <= 0 or box_height <= 0 or box_depth <= 0 or box_width <= 0:
        raise Exception

    box_w_area = box_width * box_height
    box_h_area = box_width * box_depth
    box_d_area = box_height * box_depth

    box_surface_area = (box_d_area * 2) + (box_h_area * 2) + (box_w_area * 2)

    paper_area_needed = box_surface_area
    # because we lose 9.8% of the paper, we need 9.8% more paper!
    paper_area_needed_after_loss = paper_area_needed + (paper_area_needed * 0.098)

    sheets_needed = ceil(paper_area_needed_after_loss / wpaper_area)

    print(sheets_needed)
except Exception:
    print("INVALID INPUT")

# 100/100. This took me some time to even out