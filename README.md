# Student Attendance System with Facial Recognition

This project is an automated **Student Attendance System** leveraging facial recognition to identify students, record their attendance time, and store the data in a `.csv` file.
It's designed to simplify and optimize the attendance tracking process, making it faster and more accurate.

## Features
- **Real-Time Facial Recognition**: Detects and identifies faces from a live webcam feed.
- **Automated Attendance Logging**: Records the student's name and the time of attendance in a `.csv` file.
- **Efficient Encoding**: Preloads face encodings for fast and reliable matching.

## How It Works
1. **Image Database**: The system uses images stored in the `images` folder as a database to recognize students.
2. **Encoding Faces**: Encodes the images in the database for comparison with live webcam input.
3. **Matching Faces**: Matches live faces to the encoded database to identify students.
4. **Attendance Logging**: Logs the name and time of attendance in a `attendance.csv` file.

## Technologies Used
- **Python**: Programming language for the project.
- **OpenCV**: For webcam capture and image processing.
- **Face Recognition Library**: To handle face detection and recognition.
- **NumPy**: For numerical operations.
- **CSV**: For storing attendance records.

## Project Structure
```plaintext
├── images/                 # Folder containing student images for recognition
├── attendance.csv          # Output file for storing attendance data
├── Atend_project1.py       # Main Python script
└── README.md               # Project documentation
