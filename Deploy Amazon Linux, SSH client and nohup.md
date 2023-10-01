# Deploy streamlit app on EC2 wth Amazon Linux instance and SSH client method

### Connect to ec2 Instance


ssh -i "keys.pem" ec2-user@ec2-18-222-26-148.us-east-2.compute.amazonaws.com


### Create Virtual Environment


python3 -m venv myenv


### Activate Virtual Environment


source myenv/bin/activate


### Copy files from local to ec2


scp -i "keys.pem" requirements.txt ec2-user@ec2-18-222-26-148.us-east-2.compute.amazonaws.com:/home/ec2-user/


### Run streamlit app in background


nohup streamlit run app.py &

(cat nohup.out: checks if the nohup.out file has any error messages or logs that might give you a hint about what's going wrong)