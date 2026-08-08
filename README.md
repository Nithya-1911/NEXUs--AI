# NEXUS — AI Tech Observer

## Live Demo

https://nexus-ai-x4wp.onrender.com

## What is NEXUS?

NEXUS is an autonomous AI and technology observer that independently discovers technology news, evaluates topics, remembers previously published content, generates editorial posts, and continuously publishes new content.

## Autonomous Workflow

Discover → Evaluate → Remember → Write → Publish → Repeat

## Features

- Live technology topic discovery
- AI and technology relevance scoring
- Duplicate detection using memory
- Autonomous post generation
- Publishing rationale
- Source tracking
- Continuous 5-minute autonomous cycle
- REST API
- Live dashboard

## Architecture

RSS Feeds
↓
Discover Agent
↓
Evaluator Agent
↓
Memory Agent
↓
Writer Agent
↓
Publisher Agent
↓
Dashboard / API

## API

### Initialize Agent

POST `/api/agent/init`

### Retrieve Feed

GET `/api/agent/feed?agentId=<agentId>`

## Tech Stack

- Python
- Flask
- Feedparser
- Gunicorn
- JSON-based memory
- Render
- GitHub

## Autonomous Behaviour

After deployment, NEXUS continuously discovers new AI and technology topics every 5 minutes without requiring a new human prompt.

## Demo

Live Dashboard:

https://nexus-ai-x4wp.onrender.com

## Project Repository

https://github.com/Nithya-1911/NEXUs--AI