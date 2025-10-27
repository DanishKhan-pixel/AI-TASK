# AI Sentiment Effect Detector API

A FastAPI application that analyzes text sentiment and reader effect using Google Gemini API.

## Features

- **Sentiment Analysis**: Analyzes text for positive, negative, or neutral sentiment
- **Reader Effect Detection**: Determines how text affects readers (uplifting, concerning, etc.)
- **Caching**: Caches last 5 predictions for improved performance
- **Request Logging**: Logs all requests with timestamps
- **Response Time Tracking**: Tracks and reports average API response times
- **Error Handling**: Comprehensive error handling with helpful messages
- **Docker Support**: Ready-to-run Docker container

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```bash
echo "API_KEY=your_gemini_api_key_here" > .env
```

Replace `your_gemini_api_key_here` with your actual Google Gemini API key.

### 3. Run the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## Docker Usage

### Build the Docker image:

```bash
docker build -t sentiment-detector .
```

### Run the container:

```bash
docker run -e API_KEY=your_gemini_api_key_here -p 8000:8000 sentiment-detector
```

## API Endpoints

### POST /analyze

Analyze text sentiment and reader effect.

**Request:**
```json
{
  "text": "Your text here..."
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "effect": "uplifting",
  "cached": false,
  "response_time_ms": 1250.5
}
```

### GET /

Health check endpoint that returns API status and statistics.

### GET /stats

Returns detailed API statistics including:
- Total requests processed
- Average response time
- Cache information
- Recent cached predictions

## Example Usage

### Using curl:

```bash
# Analyze sentiment
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "I love this beautiful sunny day!"}'

# Check API status
curl "http://localhost:8000/"

# Get statistics
curl "http://localhost:8000/stats"
```

### Using Python requests:

```python
import requests

# Analyze sentiment
response = requests.post(
    "http://localhost:8000/analyze",
    json={"text": "I love this beautiful sunny day!"}
)
print(response.json())
```

## API Response Format

The `/analyze` endpoint returns:

- `sentiment`: The emotional tone (positive, negative, neutral)
- `effect`: How the text affects readers (uplifting, concerning, neutral, etc.)
- `cached`: Whether the result was served from cache
- `response_time_ms`: Time taken to process the request in milliseconds

## Error Handling

The API handles various error scenarios:

- **Missing API Key**: Returns 500 error with helpful message
- **API Rate Limits**: Returns 502 error for external API issues
- **Network Issues**: Returns 503 error for service unavailability
- **Invalid Input**: Returns 422 error for malformed requests

## Logging

All requests are logged to both console and `sentiment_api.log` file with:
- Timestamps
- Request details
- Response times
- Error messages

## Caching

The application caches the last 5 predictions to improve performance for repeated requests. Cache information is available through the `/stats` endpoint.

## Performance Monitoring

The API tracks:
- Response times for all requests
- Average response time over last 100 requests
- Cache hit rates
- Request statistics

## Requirements

- Python 3.12+
- Google Gemini API key
- Internet connection for API calls

## License

This project is open source and available under the MIT License.
# AI-TASK
