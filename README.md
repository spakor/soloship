# solopreneur-accelerator 🚀

Accelerate your solopreneurship!

## Members

Gabriel Alexander Mongalo
Minji Jung
Seongwon Han
Yongwoo Kim

## Overview

Solopreneur-accelerator is an application designed to help solopreneurs gain insights, narrow down business ideas, and receive personalized advice. By answering a series of questions and optionally uploading a CV, users can get tailored feedback to assist in their entrepreneurial journey.

## Description

This application guides solopreneurs through a series of questions to gather information about their business ideas, target audience, resources, goals, and challenges. By leveraging the Upstage AI API, the app provides personalized advice based on the user's input and optionally extracted information from an uploaded CV.

### Main Features

- **Questionnaire**: Collects detailed information about the user's business idea.
- **CV Upload**: Optionally extracts text from an uploaded CV using OCR.
- **Personalized Advice**: Generates tailored advice using the Upstage AI chat model.

## Setup Instructions

### Prerequisites

- Python 3.11.0
- `make` utility
- `pip` package manager

### Steps

1. Set Up the Virtual Environment

   make $(VENV_DIR)/bin/activate

2. Install Dependencies

   make install

3. Set Up Environment Variables

   - Copy `.envrc.template` to `.envrc`

     cp .envrc.template .envrc

   - Edit `.envrc` to add your Upstage API token:

     export UPSTAGE_API_TOKEN=<your_upstage_api_token>

4. Run the Application

   make run

## Makefile Commands

- **Create and Activate Virtual Environment**

  make $(VENV_DIR)/bin/activate

- **Install Dependencies**

  make install

- **Freeze Current Dependencies**

  make freeze

- **Run the Application**

  make run

- **Clean the Virtual Environment**

  make clean

- **Reinstall Dependencies**

  make reinstall

## Requirements

### `requirements.txt`

streamlit==1.36.0
openai==1.35.10

## Resources

- [Upstage AI Documentation](https://developers.upstage.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)

For any issues or contributions, please refer to the repository's issue tracker or contact the maintainers.
