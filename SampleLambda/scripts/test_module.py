#  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with
#  the License. A copy of the License is located at
#      http://aws.amazon.com/apache2.0/
#  or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and
#  limitations under the License.

import unittest
import json
import boto3


class TestPolicies(unittest.TestCase):
    def test_policy(self):
        policy = readFile("iam_policy.json")
        actions = json.loads(readFile("actions.json"))
        source = readFile("source.txt")

        evaluation_results = simulatePrincipalPolicy(source, actions, [policy])
        failed = [x for x in evaluation_results if isDenied(x)]
        if len(failed) > 0:
            self.fail("Some actions were denied\n" + prettyPrintResults(failed))


def readFile(file_name):
    with open(file_name, "r") as f:
        read_data = f.read()
    return read_data


def simulateCustomPolicy(actions, policies):
    """Simulate a set of actions against a custom policy"""
    client = boto3.client("iam")
    response = client.simulate_custom_policy(
        PolicyInputList=policies, ActionNames=actions
    )
    return response["EvaluationResults"]

def simulatePrincipalPolicy(source, actions, policies):
    """Simulate a set of actions from a specific principal against a custom policy"""
    client = boto3.client("iam")
    response = client.simulate_principal_policy(
        PolicySourceArn=source, PolicyInputList=policies, ActionNames=actions
    )
    return response["EvaluationResults"]

def isDenied(evaluationResults):
    return evaluationResults["EvalDecision"] != "allowed"


def prettyPrintResults(evaluationResults):
    """prettyPrintResults returns a string formatting the results of a simulation evaluation result"""
    output = ""
    for er in evaluationResults:
        message = (
            f"Evaluated Action Name: {er['EvalActionName']}\n"
            f"\tEvaluated Resource name: {er['EvalResourceName']}\n"
            f"\tDecision: {er['EvalDecision']}\n"
        )
        output += message
    return output


if __name__ == "__main__":
    unittest.main()
