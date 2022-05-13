#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

FROM python:3.7.3

# Install pylint
RUN pip install pylint

# Install git, process tools
RUN apt-get update && apt-get -y install git procps

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;


ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Install any missing dependencies for enhanced language service
RUN apt-get install -y libicu[0-9][0-9]

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Add env variable for pyspark
ENV PYSPARK_PYTHON python3.7

RUN pip install --upgrade pip

RUN mkdir /workspace

COPY ./requirements.txt /workspace

RUN cd /workspace

RUN pip install -r /workspace/requirements.txt

WORKDIR /workspace


