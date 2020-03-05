# Cross Account AWS CodePipeline for IAM Policy Tester

This repository accompanies the [IAM Policy Tester Pipeline]() blogpost. 
It contains an example of a secure, cross-account, continous delivery [CodePipeline](https://aws.amazon.com/blogs/devops/aws-building-a-secure-cross-account-continuous-delivery-pipeline/). This pipeline demonstrates the unit testing of an IAM policy to validate permissions in different AWS Accounts.

The same resource, with the same IAM policy attached may not be able authorised for certain actions in an account. External policies, such as SCP's can limit the actions of a resource, despite the IAM policy associated with a resource.

Such conflicts can occur when crossing the boundry from development accounts to production-like accounts that contain further restrictions.
This pipeline demonstrates how this problem can be detected using `iam policy simulator` to validate if an IAM policy and action is permitted within an account.


## Running the example

#### 1. Clone this repository

[Clone](https://help.github.com/articles/cloning-a-repository/) the [AWS Policy Tester Pipeline](https://github.com/aws-samples/iam-policy-tester-pipeline) repository. From your terminal application, execute the following command:

```console
git clone https://github.com/aws-samples/iam-policy-tester-pipeline
```

This creates a directory named `iam-policy-tester-pipeline` in your current directory.


#### 2. Create **AWS CodeCommit** repository in Development Account

Follow the [instructions here](http://docs.aws.amazon.com/codecommit/latest/userguide/getting-started.html#getting-started-create-repo) to create a CodeCommit repository in the Development Account. Name your repository as sample-lambda.  Alternatively, from your terminal application, execute the following command.

```console
aws codecommit create-repository --repository-name sample-lambda --repository-description "Sample Lambda Function"
```

Note the `cloneUrlHttp` URL in the response from above CLI.

You may refer [here](http://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html#how-to-create-repository-cli)
on further details, in order to setup AWS Cli , if required.

#### 3. Add a new remote

From your terminal application, within the `sample-lambda` directory, execute the following command:

```console
git init && git remote add AWSCodeCommit HTTP_CLONE_URL_FROM_STEP_2
```

Follow the instructions [here](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html) for local git setup required to push code to CodeCommit repository.

#### 4. Replace the Policy Source ARN

You need to specify the user, group, or role whose policies you want to include in the simulation. To do this, within the `sample-lambda` directory, modify the value in `scripts/source.txt` file.

#### 5. Push the code AWS CodeCommit

From your terminal application, execute the following commands:

```console
git add *
git commit -am "Initialise the SampleLambda repository"
git push AWSCodeCommit master
```

#### 6. Run the script to generate the Cross Account Pipeline

From your terminal application, back in the `iam-policy-tester-pipeline` directory, execute the following command:

```console
chmod +x single-click-cross-account-pipeline.sh && ./single-click-cross-account-pipeline.sh
```

This last step deploys the entire pipeline. It expects to receive the account numbers to which it will deploy the reference architecture. It creates Amazon S3 buckets for the build artifacts and encryption keys for secure cross-account communication, and sets up CodePipeline, CodeBuild, and CodeDeploy in the account structure described above. After this step, each update in the sample-lambda repository triggers an execution of the pipeline. You can manually release a change in the pipeline after deploying it to ensure it is working.

## License

This sample code is made available under the Apache 2.0 License. See the LICENSE file.
