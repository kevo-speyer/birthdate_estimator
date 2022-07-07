# Birthdate Estimator
## How to serve a Machine Learning Model with serverless infrastructure
This service estimates the date of birth from the argentinian DNI (similar to Social Security Number) through an API.

## Build & Deploy Instructions

### Define environment variables
```
ecr_name=dni-bday
aws_account_id=691342082863
region=us-east-1
```

### Build image
`docker build -t ${ecr_name} .`

### Tag new image
`docker tag ${ecr_name}:latest ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_name}:latest`

### Push to ECR in AWS
`docker push ${aws_account_id}.dkr.ecr.${region}.amazonaws.com/${ecr_name}:latest`
### If there is a Failure to authenticate, run. (Make sure ECR repository exists):
`aws ecr get-login-password --region $region | docker login --username AWS --password-stdin ${aws_account_id}.dkr.ecr.${region}.amazonaws.com`

### Deploy
* Create Lambda function from container image or change image to the recently uploaded one
* Create Api Gateway to trigger said Lambda

### Request API
```
api_url="https://arx6ju40h3.execute-api.us-east-1.amazonaws.com/default/dni-bday-backend"
curl -G -XPOST $api_url -d "dnis=[99000000,33023562]" -d "model_info={'filename':'model_date_by_dni.pickle','location':'filesystem','path':'./models'}"
```
or use model from bucket:
```
curl -G -XPOST $api_url -d "dnis=[99000000,33023562]" -d "model_info={'filename':'default_model.pickle','location':'s3','path':'prd','bucket':'dni-bdai-models'}"
```

# Development Workflow

## Local Lambdas Deploy
`docker run -p 9000:8080  ${ecr_name}:latest`

## Local Lambdas trigger
`curl -XGET "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"dnis":"35167045"}'`

### Tech Stack:
AWS Lambda
AWS ECR
AWS Api Gateway
Docker
Python (sklearn, numpy)

References:
1: https://aws.amazon.com/blogs/machine-learning/deploy-multiple-machine-learning-models-for-inference-on-aws-lambda-and-amazon-efs/
2: https://ianwhitestone.work/serverless-ml-deployments/
