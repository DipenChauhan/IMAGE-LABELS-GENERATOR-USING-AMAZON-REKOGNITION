# IMAGE-LABELS-GENERATOR-USING-AMAZON-REKOGNITION
An Image Labels Generator using Amazon Rekognition is a system or application that automatically analyzes images and generates descriptive labels (tags) that identify objects, scenes, activities, and concepts present in the image.

STEP 1: Create an AWS Account
1.	Go to https://aws.amazon.com
2.	Click Create an AWS Account
3.	Complete verification & login to AWS Management Console
________________________________________

STEP 2: Create an IAM User (Security Best Practice)
2.1 Open IAM
  •	Services → IAM
  •	Click Users → Add user
2.2 User Details
  •	User name: USER1
  •	Access type: ✅ Programmatic access
2.3 Permissions
  •	Attach policies directly:
    o	AmazonRekognitionFullAccess
    o	AmazonS3ReadOnlyAccess
->>>Ethier attch policy 
2.4 Save Credentials
⚠️ Download Access Key & Secret Key (important)

________________________________________
STEP 3: Create an S3 Bucket
1.	Services → S3
2.	Click Create bucket
3.	Bucket name: image-labels-project
4.	Region: same as Rekognition (example: us-east-1)
5.	Block all public access → ✅ Keep enabled
6.	Click Create bucket
7.	Upload images (.jpg, .png)
________________________________________

STEP 4: Install Python & AWS CLI
4.1 Install Python
Download from https://www.python.org
Check:
python --version
4.2 Install AWS CLI
pip install awscli
Verify:
aws --version

________________________________________
STEP 5: Configure AWS CLI
aws configure
Enter:
•	AWS Access Key ID
•	AWS Secret Access Key
•	Region: ap-south-1
•	Output format: json
________________________________________

STEP 6: Install Required Libraries
pip install boto3

________________________________________
STEP 7: Write Python Code (Image Label Detection)
7.1 Create File
image_labels.py

________________________________________

STEP 8 : Create AWS Lambda Function (Automation) 
1.	Services → Lambda
2.	Create function → Author from scratch
3.	Function name: ImageAnalyzer
4.	Runtime: Python 3.9
5.	Permissions → Create new role
________________________________________

STEP 9: Connect S3 Trigger to Lambda
•	S3 → Bucket → Properties
•	Event notification → ObjectCreated
•	Destination → Lambda function
STEP 10: Create Web UI (Streamlit)
pip install streamlit
Create app.py
Run app :- streamlit run app.py

