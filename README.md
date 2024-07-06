# Audiobook - Convert PDF to Audio

This project allows users to upload a PDF document and convert it into an audiobook. The implementation uses Python to handle the conversion and serves the interface via a simple web application.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)

## Introduction
The Audiobook project converts PDF documents into audio files, making it easier to consume written content through listening. This repository contains the necessary scripts and web application to perform the conversion.

## Features
- Upload a PDF document
- Convert PDF text to speech
- Download the resulting audio file

## Setup
To set up the project, follow these steps:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/MayurPimpude/Audiobook.git
    cd Audiobook
    ```

2. **Install Dependencies**
    Make sure to install the required dependencies listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**
    Start the web application using the following command:
    ```bash
    python app.py
    ```

## Usage
1. **Upload PDF**: Use the web interface to upload a PDF document.
2. **Convert to Audio**: The application processes the PDF and converts the text to an audio file.
3. **Download**: Once the conversion is complete, download the audio file.

