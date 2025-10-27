# AI Sentiment Detector

A simple API that tells you if text is positive, negative, or neutral. Built with FastAPI and TextBlob.

## What it does

Send it some text, get back the sentiment. Pretty straightforward!

- **Positive**: Happy, good vibes
- **Negative**: Sad, angry, bad vibes  
- **Neutral**: Meh, neither here nor there

## Quick Start

1. **Install stuff:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run it:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Use it:**
   Go to `http://localhost:8000/docs` for the interactive docs

## API Endpoints

### Analyze Text
**POST** `/analyze`
```json
{
  "text": "I love pizza!"
}
```

**Response:**
```json
{
  "sentiment": "positive",
  "polarity": 0.8,
  "confidence": 0.8
}
```

### See Recent Analyses
**GET** `/cache` - Shows the last 5 texts you analyzed

## Example Usage

```bash
# Check if text is positive
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is awesome!"}'
```

## Docker

```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

## That's it!

The API docs at `/docs` will show you everything you need to know. Happy analyzing! 🎉