import streamlit as st
import boto3

st.title("Image Label Generator")

bucket = st.text_input("S3 Bucket")
image = st.text_input("Image Name")

if st.button("Analyze"):
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image}}

    )

    for label in response['Labels']:
        st.write(label['Name'], label['Confidence'])