# 🚀 NEXUS — AI Tech Observer

NEXUS is an autonomous AI technology observer and creator.

Instead of waiting for a human prompt, NEXUS continuously discovers
technology topics, evaluates their importance, avoids previously
published topics, generates a post, saves it, and repeats the process
automatically.

---

## 🎯 Problem

Most AI-generated social content requires a human to provide the
initial topic or prompt.

NEXUS solves this by creating an autonomous content pipeline that
can independently discover and evaluate technology news.

---

## 💡 Solution

NEXUS operates as a multi-agent autonomous system:

Discover → Evaluate → Remember → Write → Publish → Repeat

---

## 🧠 Agent Architecture

### 1. Discover Agent

Finds technology topics from live information sources.

### 2. Evaluator Agent

Scores topics based on AI and technology relevance.

Low-scoring topics are automatically rejected.

### 3. Memory Agent

Stores previously published topics and prevents duplicate publishing.

### 4. Writer Agent

Converts selected topics into posts using the NEXUS editorial format.

### 5. Publisher Agent

Saves generated posts for publication.

### 6. Autonomous Runner

Continuously executes the complete pipeline every five minutes.

---

## 🔄 Autonomous Workflow

1. Discover new topics
2. Evaluate each topic
3. Reject low-score topics
4. Check publication memory
5. Generate a post
6. Save the post
7. Remember the topic
8. Wait five minutes
9. Start the next cycle automatically

---

## 🌐 Dashboard

NEXUS includes a Flask dashboard showing:

- Autonomous status
- Published post count
- Memory records
- Latest generated posts
- NEXUS scores

---

## 🛠️ Tech Stack

- Python
- Flask
- JSON
- Multi-agent architecture
- Automated scheduling
- HTML/CSS
- VS Code

---

## ▶️ How to Run

Create and activate the virtual environment:

```bash
python -m venv venv