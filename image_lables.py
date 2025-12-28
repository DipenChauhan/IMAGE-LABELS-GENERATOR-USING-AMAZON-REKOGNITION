import boto3

REGION = "ap-south-1"
BUCKET_NAME = "image-labels-project"
IMAGE_KEY = "sample.jpg"   # change if inside folder

rekognition = boto3.client("rekognition", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)

# Verify S3 access
try:
    s3.head_object(Bucket=BUCKET_NAME, Key=IMAGE_KEY)
    print("S3 object access verified\n")
except Exception as e:
    print("ERROR: Cannot access S3 object. Check key or permissions.")
    raise e

# Detect labels
print("Detecting Labels:")
labels_response = rekognition.detect_labels(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": IMAGE_KEY}},
    MaxLabels=10,
    MinConfidence=70
)

for label in labels_response["Labels"]:
    print(f"{label['Name']} : {label['Confidence']:.2f}%")

# Detect moderation labels
print("\nDetecting Moderation Labels:")
moderation_response = rekognition.detect_moderation_labels(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": IMAGE_KEY}},
    MinConfidence=60
)

if moderation_response["ModerationLabels"]:
    for label in moderation_response["ModerationLabels"]:
        print(f"{label['Name']} : {label['Confidence']:.2f}%")
else:
    print("No moderation issues detected.")

# Detect faces
print("\nDetecting Faces:")
faces_response = rekognition.detect_faces(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": IMAGE_KEY}},
    Attributes=["ALL"]
)

if faces_response["FaceDetails"]:
    for i, face in enumerate(faces_response["FaceDetails"], start=1):
        print(f"\nFace {i}:")
        print("Age Range:", face["AgeRange"])
        print("Smile:", face["Smile"]["Value"])
        print("Emotions:")
        for emotion in face["Emotions"]:
            print(f"  {emotion['Type']} : {emotion['Confidence']:.2f}%")
else:
    print("No faces detected.")
print("\nFull Moderation Response:")
print(moderation_response)  