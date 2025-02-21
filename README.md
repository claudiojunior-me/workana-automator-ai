# Workana Automator AI

## Description
An AI-powered tool that automatically searches for relevant job opportunities on Workana, analyzes them based on your professional history, and generates personalized proposals for matching jobs.

## How it works

The system follows these steps:

1. **Job Search**: Navigates through Workana using predefined categories and subcategories to find relevant jobs
2. **Data Extraction**: Extracts job details including title, description, budget, and requirements
3. **Job Analysis**: Uses AI to analyze if the job matches your professional profile
4. **Proposal Generation**: For matching jobs, generates a customized proposal
5. **Expert Review**: Reviews the proposal and provides feedback
6. **Output**: Saves all results in a markdown file with timestamp

The system uses several AI agents powered by OpenAI's GPT models:
- VagaMatcher: Analyzes job fit
- PropostaGenerator: Creates proposals
- FreelancingExpert: Reviews and provides feedback

## Running locally

1. Clone the repository
```bash
git clone https://github.com/yourusername/workana-automator-ai.git
cd workana-automator-ai
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file with:
```
MONGO_URI=mongodb://localhost:27017
OPENAI_API_KEY=your-api-key-here
```

5. Create your professional history
Create a `historico.md` file with your professional experience

6. Run the application
```bash
python -m app.main
```

## Running with Docker

1. Build and run using Docker Compose
```bash
docker-compose up --build
```

This will:
- Start a MongoDB container
- Build and run the application container
- Set up the necessary environment variables

2. Stop the containers
```bash
docker-compose down
```

**Note**: Make sure to update the `OPENAI_API_KEY` in the `docker-compose.yml` file with your actual API key before running.

## Requirements

- Python 3.10+
- MongoDB
- Chrome/Chromium (for Selenium)
- OpenAI API key