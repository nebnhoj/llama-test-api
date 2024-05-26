# Llama 3 Test API with MongoDB connector

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This project provides a sample implementation of LLaMA 3 (Large Language Model for Assisting), an advanced language model designed to demonstrate capabilities in natural language understanding and generation. The implementation includes necessary scripts and dependencies to set up and run the LLaMA 3 server and application components. It is connected to MongoDB.

## Getting Started <a name = "getting_started"></a>

Before you begin, ensure you have met the following requirements:
Llama3 installed in your machine and running
Python 3.8 or higher installed on your machine
Pip (Python package installer)
Git for version control

### Prerequisites

What things you need to install the software and how to install them.

```
git clone git@github.com:nebnhoj/llama-test-api.git
cd llama-test-api

```

### Installing

A step by step series of examples that tell you how to get a development env running.

1. Create python virtual environment

```
python3 -m venv venv
```

2. Use the current environment

```
source venv/bin/activate
```
3. Install required libraries

```
pip freeze > requirements.txt
```

4. Start index_server.py

```
python index_server.py
```
5. Start app.py after the index_server started

```
python app.py
```
## Usage <a name = "usage"></a>

Test the api by using curl or postman
```
curl http://127.0.0.1:5601/query?text=your query
```
