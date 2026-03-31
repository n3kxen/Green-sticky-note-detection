# Green Sticky Note Detection

A real-time computer vision project that detects green sticky notes using a webcam. Built with Python and OpenCV.

## How It Works

1. Captures video from webcam
2. Applies HSV color filtering to isolate green objects
3. Finds contours and filters by area
4. Draws a bounding box around detected objects

## Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

## Usage

```bash
python main.py
```

Press **Q** to quit.

## Configuration

All parameters are in `config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `FRAME_WIDTH` | 640 | Webcam frame width |
| `FRAME_HEIGHT` | 480 | Webcam frame height |
| `AREA_FROM` | 26000 | Minimum contour area |
| `AREA_TO` | 70000 | Maximum contour area |
| `E_RATIO` | 0.01 | Contour approximation accuracy |
| `ANGLE_COUNT` | 4 | Minimum number of angles to detect shape |

## Project Structure

```
object-detection/
├── main.py        # Entry point, webcam capture loop
├── detector.py    # Detection logic (color, contour, bounding box)
├── config.py      # Configuration parameters
└── README.md
```
## Example
<img width="638" height="477" alt="Screenshot at Mar 31 13-08-49" src="https://github.com/user-attachments/assets/363a163a-64c1-4e61-b2d4-0b1feb4d2abd" />

