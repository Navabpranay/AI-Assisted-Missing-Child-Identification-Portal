# Find Me: AI-Assisted Missing Child Identification Portal
*(CNN Based Deep-Learning Model)*

---

## 📖 Abstract

The "**Find Me**" Portal aims to reunite missing children with their families using **AI-driven facial recognition**.  
Built on **CNN architectures** with **Python's DeepFace**, **Node.js**, and **MySQL**, this system automates image matching, sends real-time **email notifications**, and simplifies case management with a secure, user-friendly web portal.

---

## 🛠️ Technologies Used

- **Backend**: Node.js, Express.js
- **Database**: MySQL
- **Facial Recognition**: Python 3 (DeepFace with Facenet512 model)
- **Frontend**: HTML, CSS, EJS
- **Authentication**: bcrypt.js, express-session
- **Email Notification**: Nodemailer (Gmail SMTP)
- **Environment Management**: dotenv

---

## 🖥️ Software Requirements

- Windows 10 / Ubuntu 18.04+
- Node.js
- Python 3.8+
- MySQL Server
- MySQL Workbench
- VS Code / Jupyter / PyCharm
- DeepFace Library
- OpenCV (cv2)

---

## 💻 Hardware Requirements

- Intel i7/i9 or AMD Ryzen 7/9 processor
- 16 GB RAM minimum (32 GB recommended)
- 500 GB SSD minimum
- High-speed Internet
- NVIDIA RTX 3060 GPU or higher (optional for faster DeepFace processing)

---

## 📚 Libraries and Packages

- Node.js: express, mysql2, bcryptjs, body-parser, multer, nodemailer, dotenv, express-session
- Python: deepface, opencv-python (cv2), numpy, tensorflow (backend for deepface)
- Frontend: EJS Templates, HTML5, CSS3

---

## 🔍 Existing System

- Manual poster distribution and TV ads.
- Delayed reporting, non-intelligent search.
- No real-time facial matching or public engagement tools.

## 🚀 Proposed System

- Automated facial recognition using CNNs and DeepFace.
- Web portal for easy child registration and face matching.
- Instant email notifications to community users.
- High-speed, scalable, secure system.

---

## 🏗️ System Design

### 1. Introduction
A robust, modular web architecture combining Node.js backend, MySQL database, and Python facial recognition.

### 2. Architecture Diagram
- Three-tier structure: UI (EJS) → Server (Node.js) → Database (MySQL)
- DeepFace CNN model invoked by Node.js for face verification.

### 3. UML Diagrams / DFD
- Class Diagram
- Sequence Diagram
- Use Case Diagram
- Activity Diagram

---

## 🛠️ Implementation

### 1. Algorithms
- CNN (Convolutional Neural Networks)
- Facenet512 Embedding
- Cosine Similarity for distance matching

### 2. Architectural Components
- Frontend (UI)
- Server (Node.js Express app)
- Face Recognition (Python DeepFace script)
- Database (MySQL)

### 3. Feature Extraction
- Face Detection → Alignment → Embedding Generation → Matching.

### 4. Key Packages
- Python: DeepFace, OpenCV
- Node.js: express, multer, mysql2
- Notifications: Nodemailer

### 5. Source Code
- `app.js` (server)
- `face_recognition_cnn.py` (facial matching)
- `child_details.ejs` (display matched child)

---

## 🖥️ Output Screens

- User Sign Up Page
- Login Page
- Register Missing Child
- Upload Photo for Recognition
- Recognition Result Page
- Email Notifications
- Database Backend (MySQL)

---

## 🧪 System Testing

### 1. Introduction
Tested for functionality, accuracy, security, and scalability.

### 2. Test Cases
| S.No | Test Case | Expected Result | Result |
|:----:|:---------:|:---------------:|:------:|
| 1 | Image Upload | Success | Passed |
| 2 | Image Comparison | Success | Passed |
| 3 | No Match | Display 'No Match' | Passed |
| 4 | Match Found | Child Details Displayed | Passed |
| 5 | Python Script | Executes Successfully | Passed |

### 3. Results
- 100% functional coverage
- Accurate facial matching
- Correct email notification
- Secure image handling

### 4. Datasets
- Children's Face Datasets (custom collected)
- Ethical handling and testing with sample datasets

### 5. Performance Evaluation
- Accuracy: 93–95%
- Precision: 94%
- Recall: 91%
- Response Time: 2–5 seconds

---

## 🏁 Conclusion & Future Enhancements

### Conclusion
Successfully created an AI-powered, scalable, and secure missing child identification system using facial recognition.

### Future Enhancements
- Mobile App for Android/iOS
- Geo-location alerts
- Facial Aging Prediction
- Multilingual support
- Integration with Police and NGO networks
- Use of additional biometrics like fingerprint or iris recognition

---

## 📚 References

- DeepFace Python Documentation
- OpenCV Library
- MySQL Database Documentation
- TensorFlow Deep Learning Framework
- Research papers on CNN and Facial Recognition
- Government and NGO missing child database portals

---

## ✍️ Authors

- Nawab Pranay Goud [21N31A7249]
- Mogili Gopi Prasad [21N31A7241]
- Lavudya Siddharth Nayak [21N31A7233]

**Guided by**:  
Dr. Kannaiah Chattu, Associate Professor

---

## 🏫 Institution

**Malla Reddy College of Engineering and Technology (Autonomous)**  
Affiliated to JNTU Hyderabad | Approved by AICTE | NBA & NAAC ‘A’ Grade Certified

---

# ❤️ Let's use AI to bring children back to their families safely!
