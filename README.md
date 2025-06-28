# Qwen Image Generator API Client

A Python client for interacting with Qwen AI's image generation API. This tool allows you to generate high-quality images using natural language prompts through Qwen's powerful AI model.

## Version
v1.0.0

## Overview
This client provides a streamlined interface to Qwen AI's image generation capabilities, handling the complete flow from initial request to image generation, including task status monitoring and result retrieval.

## Features
- 🚀 Asynchronous image generation requests
- 🔄 Automatic task status polling
- ⏱️ Configurable polling intervals and retry attempts
- 📊 Detailed status monitoring and error handling
- 🎨 Support for detailed image generation prompts

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone this repository
2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Basic Example
```python
import requests
import time
from main import generate_image

# Your image generation prompt
prompt = """Product photography, perfume bottle with red liquid inside 
           on top of black rocks surrounded by berries..."""

# The script will handle:
# 1. Initial request submission
# 2. Task ID extraction
# 3. Status polling
# 4. Result retrieval
```

### API Flow
1. Initial request to `/api/v2/chat/completions`
2. Extract task_id from response
3. Poll task status at `/api/v1/tasks/status/{task_id}`
4. Retrieve generated image when task completes

### Configuration
The client includes configurable parameters:
- `max_attempts`: Maximum number of polling attempts (default: 30)
- `poll_interval`: Time between polling attempts in seconds (default: 3)

## Technical Details

### Endpoints
- Chat Completions: `https://chat.qwen.ai/api/v2/chat/completions`
- Task Status: `https://chat.qwen.ai/api/v1/tasks/status/{task_id}`

### Response Handling
The client automatically handles:
- Task ID extraction
- Status polling
- Success/failure detection
- Error reporting

## Important Disclaimer
⚠️ **EDUCATIONAL PURPOSE ONLY**
This code is provided for educational and learning purposes only. Users must:
- Not use this code for any illegal purposes
- Comply with Qwen AI's terms of service
- Respect API rate limits and usage guidelines

## Contact & Support
For questions, issues, or concerns regarding this project, please contact:
📧 Email: hello.kaiiddo@gmail.com

## License
This project is intended for educational purposes. All rights and usage are subject to Qwen AI's terms and conditions.

---
*Note: This is an unofficial client and is not affiliated with or endorsed by Qwen AI.*
