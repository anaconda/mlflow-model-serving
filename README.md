# MLFlow Model Serving For Anaconda Enterprise

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=coverage)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=shapeandshare_mlflow.model.serving&metric=bugs)](https://sonarcloud.io/summary/new_code?id=shapeandshare_mlflow.model.serving)

Overview
--------
MLFlow native model serving within Anaconda Enterprise.

This project provided a mechanism to launch a mlflow model serving instance within Anaconda Enterprise.

Note that the model will be launched using the conda environment management configuration.  See [Official MLFlow Models Documentation](https://mlflow.org/docs/2.0.1/cli.html#mlflow-models) for additional details.

Configuration
--------
When deploying the solution in Anaconda Enterprise the below variables must be declared:
* `MLFLOW_SERVING_MODEL_NAME`
    
    The name of the registered model.

* `MLFLOW_SERVING_MODEL_STAGE`

    The model stage or version to pull from the registry.

Additionally access to the tracking serber should be defined as Anaconda Enterprise Secrets.  The below secrets are required to be defined:
* `MLFLOW_TRACKING_URI`
* `MLFLOW_REGISTRY_URI`
* `MLFLOW_TRACKING_TOKEN`

Usage Example
--------
The solution is meant to be used as a template from which deployments can be created exposing models as a REST endpoint.

The following details will need to be defined:
1. Define the project name
   1. In the example below we use `dev.mlflow.endpoint.taxi`
2. Define the deployment name
   1. In the example below we use `dev.mlflow.endpoint.taxi`
3. Define the static endpoint name
   1. In the example below we use `dev-mlflow-endpoint-taxi`
4. MLFLOW_SERVING_MODEL_NAME
   1. In the example below we use `taxi_fare_regressor`
5. MLFLOW_SERVING_MODEL_STAGE
   1. In the example below we use `Staging`

### Example Steps

1. Upload the project:
```text
ae5 project upload --name "dev.mlflow.endpoint.taxi" mlflow.model.serving.x.y.z.tar.gz
```

2. Create the deployment:

```text
ae5 project deploy --name "dev.mlflow.endpoint.taxi" --endpoint "dev-mlflow-endpoint-taxi" --command "Serve" --private --variable MLFLOW_SERVING_MODEL_NAME="taxi_fare_regressor" --variable MLFLOW_SERVING_MODEL_STAGE="Staging" "dev.mlflow.endpoint.taxi"
```

3. Create private deployment token:

```text
ae5 deployment token "dev.mlflow.endpoint.taxi"
```

Anaconda Project Runtime Commands
--------
These commands are used during develop for solution management.

| Command          | Environment | Description                    |
|------------------|-------------|:-------------------------------|
| Serve             | Runtime    | Entry point for model hosting. |

Development Requirements
--------
* conda
* anaconda-project

Development Environment Setup
--------
> anaconda-project prepare --env-spec development

Anaconda Project Development Commands
--------
These commands are used during develop for solution management.

| Command          | Environment  | Description                                               |
|------------------|--------------|:----------------------------------------------------------|
| bash             | Development  | Enters a bash shell within the `development` environment. |
| test:unit        | Development  | Runs unit tests                                           |
| test:integration | Development  | Runs integration tests                                    |
| coverage         | Development  | Generates code coverage report                            |
| clean            | Development  | Cleanup temporary project files                           |
| lint             | Development  | Perform code linting check                                |
| lint:fix         | Development  | Perform automated code formatting                         |

Contributing
------------
1. Fork the repository on GitHub
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using GitHub

License and Authors
-------------------
Copyright (c) 2023 Anaconda, Inc.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
