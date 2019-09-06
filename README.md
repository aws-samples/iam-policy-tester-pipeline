# Cross Account AWS CodePipeline for IAM Policy Tester

This reference architecture demonstrates how to push code hosted in [AWS CodeCommit](https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/sample-lambda) repository in Development Account,
use **AWS CodeBuild** to do application build, store the output artifacts in S3Bucket and deploy these artifacts to Test
and Production Accounts using **AWS CloudFormation**. This orchestration of code movement from code checkin to deployment
is securely handled by **AWS CodePipeline**.


## Running the example

#### 1. Clone the sample Lambda function GitHub repository

[Clone](https://help.github.com/articles/cloning-a-repository/) the [AWS LAMBDA sample application](https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/sample-lambda) CodeCommit repository. You will need to have CodeCommit HTTPS credentials to do this.

From your terminal application, execute the following command:

```console
git clone https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/sample-lambda
```

This creates a directory named `sample-lambda` in your current directory, which contains the code for the AWS Lambda function sample application.

#### 2. Create **AWS CodeCommit** repository in Development Account

Follow the [instructions here](http://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html#getting-started-create-repo) to create a CodeCommit repository
in the Development Account.Name your repository as sample-lambda

Alternatively, from your terminal application, execute the following command. You may refer [here](http://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html#how-to-create-repository-cli)
on further details, in order to setup AWS Cli , if required.

```console
aws codecommit create-repository --repository-name sample-lambda --repository-description "Sample Lambda Function"
```

Note the cloneUrlHttp URL in the response from above CLI.

#### 3. Add a new remote

From your terminal application, execute the following command:

```console
git remote add AWSCodeCommit HTTP_CLONE_URL_FROM_STEP_2
```

Follow the instructions [here](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html) for local git setup required to push code to CodeCommit repository.

#### 4. Push the code AWS CodeCommit

From your terminal application, execute the following command:

```console
git push AWSCodeCommit master
```
