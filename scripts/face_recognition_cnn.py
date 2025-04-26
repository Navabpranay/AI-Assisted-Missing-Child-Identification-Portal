import os
import sys
import warnings
import cv2
from deepface import DeepFace

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings("ignore")

# Check arguments
if len(sys.argv) < 3:
    print("Usage: python face_recognition_cnn.py <database_image_path> <uploaded_image_path>")
    sys.exit(1)

db_image_path = sys.argv[1]
uploaded_image_path = sys.argv[2]

# Check if image files exist
if not os.path.exists(db_image_path):
    print(f"Database image not found: {db_image_path}")
    sys.exit(1)

if not os.path.exists(uploaded_image_path):
    print(f"Uploaded image not found: {uploaded_image_path}")
    sys.exit(1)

try:
    # Read images with OpenCV first to verify they can be loaded
    db_img = cv2.imread(db_image_path)
    uploaded_img = cv2.imread(uploaded_image_path)
    
    if db_img is None:
        print("Cannot read database image - check file format or corruption.")
        sys.exit(1)
    
    if uploaded_img is None:
        print("Cannot read uploaded image - check file format or corruption.")
        sys.exit(1)
    
    # DeepFace face verification
    result = DeepFace.verify(
        img1_path=db_image_path,
        img2_path=uploaded_image_path,
        model_name='Facenet512',
        distance_metric='cosine',
        enforce_detection=False,
        detector_backend='opencv'
    )
    
    # Print detailed result for debugging
    print(f"Distance: {result.get('distance', 'N/A')}, Threshold: {result.get('threshold', 'N/A')}")
    
    if result.get("verified"):
        print("Match found!")
    else:
        print("No match found.")
        
except Exception as e:
    print(f"Error during face recognition: {str(e)}")
    sys.exit(1)