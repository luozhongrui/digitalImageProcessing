# Automatic checking of small holes

## Prerequisite

- Install the python environment
- Installation of dependencies

```bash
pip install -r requirements.txt
```

## File structure
```
src 
├── GeometricTransform.py 
├── auto.py 
├── calculate_coordinates.py 
├── coordinate.csv 
├── gray2bin.py  
├── image 
│ ├── location.npy 
│ ├── location_set.npy 
│ ├── matrix.npy 
│ ├── matrix_set.npy 
│ ├── pcb.bmp 
│ ├── pcb1.jpg 
│ ├── pcb2.jpg 
│ ├── pcb3.jpg  
│ ├── pcb4.jpg 
│ ├── pcb5.jpg 
│ ├── pcb6.jpg  
│ ├── pcb7.jpg 
│ ├── result.csv 
│ ├── scale.csv 
│ ├── scale.jpg 
│ └── warp.jpg 
├── main.py 
├── scale.py 
└── utils.py
```

## Automatic detection

Default open integration camera, if you need usb camera input please modify auto.py file cap = cv2.VideoCapture(0) change to cap = cv2.VideoCapture(1)

```python
if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # Set the width (3) property of the camera
    cap.set(4, 720)
    flag = False
    while True:
        ret, frame = cap.read()
        img = frame.copy()
        if flag:
            draw_roi(frame, location)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            setup_location(img.copy())
            flag = True
            location = np.load("image/location_set.npy")
        if cv2.waitKey(1) & 0xFF == ord('d'):
            matrix = np.load("image/matrix_set.npy")
            run(img.copy(), matrix)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow("frame")
            break
```

## Usage

```bash
cd src
python auto.py
```
