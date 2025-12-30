
import os
import boto3
from pathlib import Path
from dotenv import load_dotenv

def upload_data_to_s3():
    """Upload data from data/raw/ to S3 bucket"""
    
    print("Starting data upload to S3...")
    
    # Load environment variables
    load_dotenv()
    
    # Get AWS credentials from .env file
    bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-2')
    
    if not bucket_name:
        print("ERROR: AWS_S3_BUCKET_NAME not found in .env file!")
        return False
    
    print(f"Bucket: {bucket_name}")
    print(f"Region: {region}")
    
    try:
        # Create S3 client
        s3 = boto3.client('s3', region_name=region)
        
        # Create bucket if it doesn't exist
        try:
            s3.head_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' exists")
        except:
            print(f"Creating bucket '{bucket_name}'...")
            if region == 'us-east-2':
                s3.create_bucket(Bucket=bucket_name)
            else:
                s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
            print(f"Bucket created!")

        
        # Find CSV files in data/raw/
        data_folder = Path("../../data/raw")

        #if this folder doesn't exist, try absolute path from project
        if not data_folder.exists():
            data_folder = Path("data/raw")
 
        #if it doesn't exist in the system at all, print error message
        if not data_folder.exists():
            print("Error: Data folder not found")
            print("Make sure you have data/raw with CSV files")
            return False

        # Get list of CSV files

        #find all teh files with .csv from data folder
        csv_files = list(data_folder.glob("*.csv"))

        #if no csv files, print error
        if not csv_files:
            print("Error: No csv files found in {data folder}")
            return False
        
        #return number of csv files found
        print(f"Found {len(csv_files)} files to upload ...")

        # Upload each file
        uploaded_count = 0
        for csv_file in csv_files:
            #create a file path inside the bucket
            s3_key = f"raw-data/{csv_file.name}"

            print(f"Uploading {csv_file.name} ...")
 
            try:
                #upload the file to s3 bucket using key
                s3.upload_file(str(csv_file), bucket_name , s3_key)
                print(f"Successfully uploaded to s3: //{bucket_name}/{s3_key}")
                uploaded_count += 1
            
            #if any failures occur, print error
            except Exception as upload_error:
                print(f"ERROR: Failed to upload {csv_file.name} : {upload_error}")
        
        #report successes and failures
        #no failures
        if uploaded_count == len(csv_files):
            print(f"\nAll {uploaded_count} files successfully uploaded to data lake!")
            return True
        #failures occurred
        else:
            print(f"\nPartial success, {uploaded_count} / {len(csv_files)} uploaded.")
            return False
        
    except Exception as e:
        print(f"ERROR: upload failed: {e}")
        print("Check your AWS credentials and bucket permissions.")
        return False
        

# Verification
def verify_upload():
    print("\nVerify uploads...")

    load_dotenv()
    
    # Get AWS credentials from .env file
    bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-2')

    try:
        # Create S3 client
        s3 = boto3.client('s3', region_name=region)
        response = s3.list_objects_v2(Bucket = bucket_name, Prefix = "raw_data/")

        if "Contents" not in response:
            print("ERROR: No files found in bucket")
            return False
        
        files= response["Contents"]
        print(f"Found {len(files)} in S3:")

        total_size_mb = 0
        
        #calculate total file size:
        for file in files:
            size_mb = file['Size'] / (1024 * 1024)      #mb conversion
            total_size_mb += size_mb
            print(f" {file['Key']} ({size_mb: .2f} MB) ")  

        print(f"Total data size: {total_size_mb : .2f} MB")   
        print("Upload verification complete!")      
        return True 
     
    except Exception as e:
        print(f"ERROR: verification failed: {e}")
        return False
    
if __name__ == "__main__":
    # Run upload
    success = upload_data_to_s3()
    
    # Verify if upload was successful
    if success:
        verify_upload()

    
    print("\nNext step: Data processing and transformation!")
