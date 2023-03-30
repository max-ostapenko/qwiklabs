# QwikLabs automation

## How to use

1. Open [a lab](https://www.cloudskillsboost.google/journeys) and write down all the steps that can be automated.
2. Write the code to automate the steps. Consider running as much in parallel, and run long running tasks as soon as possible.
3. Test the automation.
4. Start the lab.
5. Use the given paramaters to authenticate, configure the stack and run automation:

```bash
export PULUMI_CONFIG_PASSPHRASE=
pulumi config set google-native:project qwiklabs-gcp-00-43659ddcdd80
gcloud auth application-default login
pulumi up --skip-preview --yes

```
