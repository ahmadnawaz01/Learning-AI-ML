# 🚀 Market Research & Business Analysis Multi-Agent Crew

An autonomous multi-agent intelligence pipeline built with **CrewAI** that automates end-to-end market research, competitor benchmarking, product strategy formulation, and executive investment memo generation.

Given a single product concept or startup idea, five specialized AI agents collaborate sequentially to deliver a comprehensive, data-driven business report.

---

## 🏗️ Architecture & Workflow

The pipeline uses a sequential multi-agent architecture where downstream agents build directly upon the findings and data collected by upstream specialists:

```text
                         [ Product Idea ]
                                │
                                ▼
┌──────────────────────────────────────────────────────┐
│  1. Market Research Specialist                       │
│  ──► TAM / SAM / SOM & Industry Growth Trends        │
└──────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────┐
│  2. Competitive Intelligence Lead                    │
│  ──► Competitor Matrix & Market Gaps                 │
└──────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────┐
│  3. Product Strategy Architect                        │
│  ──► ICPs, Value Proposition & MVP Feature Roadmap   │
└──────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────┐
│  4. Financial & Business Analyst                     │
│  ──► Monetization, Pricing & Unit Economics          │
└──────────────────────────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────┐
│  5. Executive Memo Synthesizer                       │
│  ──► Final Investor-Ready Go / No-Go Report          │
└──────────────────────────────────────────────────────┘
                                │
                                ▼
                    [ reports/report.md ]
```

---

## 🤖 The 5 Specialized Agents

### 1. Market Research Specialist

* **Role:** Analyzes macroeconomic trends, industry tailwinds, market adoption curves, and quantifies market opportunities using TAM, SAM, and SOM.
* **Tools:** Live web search and data extraction.

### 2. Competitive Intelligence Lead

* **Role:** Deep-dives into active competitors, evaluates feature parity, analyzes pricing models, and identifies customer complaints to expose untapped market opportunities.
* **Tools:** Targeted search and competitive benchmarking tools.

### 3. Product Strategy Architect

* **Role:** Defines Ideal Customer Profiles (ICPs), maps core user pain points, structures the MVP feature backlog, and identifies the product's competitive moat.
* **Tools:** Strategic product reasoning and specification drafting.

### 4. Financial & Business Analyst

* **Role:** Formulates monetization models, designs SaaS/usage-based pricing tiers, models unit economics, and constructs a risk-mitigation matrix.
* **Tools:** Quantitative analysis and financial synthesis.

### 5. Executive Memo Synthesizer

* **Role:** Compiles all upstream research, strategy, and financial analysis into a cohesive, investor-ready business brief.
* **Output:** Generates a structured Markdown document at `reports/report.md`.
* **Decision:** Provides a definitive **Go / No-Go** recommendation.

---

## 📂 Project Structure

```text
market_research_and_business_analysis_crew/
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
├── reports/
│   └── report.md
│
├── src/
│   └── market_research_and_business_analysis_crew/
│       ├── __init__.py
│       ├── crew.py
│       └── main.py
│
├── .env.example
├── pyproject.toml
└── README.md
```

### Key Files

| File                 | Description                                             |
| -------------------- | ------------------------------------------------------- |
| `config/agents.yaml` | Agent roles, goals, backstories, and LLM configurations |
| `config/tasks.yaml`  | Task definitions, dependencies, and expected outputs    |
| `crew.py`            | Crew definition, tool configuration, and task chaining  |
| `main.py`            | Input configuration and execution entry point           |
| `reports/report.md`  | Generated final executive investment memo               |
| `.env.example`       | Required environment variables                          |
| `pyproject.toml`     | Python project and dependency configuration             |

---

## 🛠️ Tech Stack

* **Orchestration:** [CrewAI](https://github.com/crewAIInc/crewAI)
* **LLM Engine:** Google Gemini / OpenAI GPT / Anthropic Claude
* **Search & Web Intelligence:** Serper API / Tavily API
* **Programming Language:** Python 3.10+
* **Package Management:** `uv` / `pip`
* **Output Format:** Markdown

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadnawaz01/market_research_and_business_analysis_CrewAI-Project.git
cd market_research_and_business_analysis_CrewAI-Project
```

### 2. Set Up Virtual Environment

#### Using `uv` — Recommended

```bash
uv venv
```

Activate the environment:

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

Then install dependencies:

```bash
uv sync
```

#### Using `pip`

```bash
python -m venv .venv
```

Activate the environment:

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

Install the project:

```bash
pip install -e .
```

---

## 🔐 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

---

## 💻 Usage

### 1. Define Your Product Idea

Open:

```text
src/market_research_and_business_analysis_crew/main.py
```

Configure the product idea:

```python
inputs = {
    "product_idea": (
        "An AI-native tool that automatically summarizes YouTube videos "
        "and auto-publishes formatted posts to LinkedIn, Twitter/X, and Instagram."
    )
}
```

### 2. Run the Crew

```bash
crewai run
```

The agents will execute sequentially and pass their findings to the downstream agents.

### 3. View the Final Report

After execution, the final business analysis will be generated at:

```text
reports/report.md
```

---

## 📄 Output Artifacts

The generated report contains the following sections:

### Executive Summary

Provides the core value proposition, business opportunity, and overall market thesis.

### Market Sizing

Includes:

* Total Addressable Market (TAM)
* Serviceable Addressable Market (SAM)
* Serviceable Obtainable Market (SOM)
* Industry growth
* CAGR
* Market adoption trends

### Competitive Analysis

Includes:

* Direct competitors
* Indirect competitors
* Competitor strengths
* Competitor weaknesses
* Feature comparison
* Pricing comparison
* Customer complaints
* Identified market gaps

### Product Strategy & ICPs

Includes:

* Ideal Customer Profiles
* User personas
* Core pain points
* Value proposition
* MVP feature roadmap
* Product differentiation
* Competitive moat

### Financial & Monetization Plan

Includes:

* Business model
* Monetization strategy
* Pricing tiers
* SaaS / usage-based pricing
* Unit economics
* Revenue considerations
* Key financial assumptions

### Risk Matrix & Investment Verdict

Includes:

* Major business risks
* Technical risks
* Market risks
* Competitive risks
* Risk mitigation strategies
* Final **Go / No-Go** recommendation

---

## 🔄 Agent Execution Flow

```text
Product Idea
     │
     ▼
Market Research
     │
     ├── Market Size
     ├── Industry Trends
     └── Growth Opportunities
     │
     ▼
Competitive Intelligence
     │
     ├── Competitors
     ├── Pricing
     └── Market Gaps
     │
     ▼
Product Strategy
     │
     ├── ICPs
     ├── Pain Points
     ├── Value Proposition
     └── MVP Roadmap
     │
     ▼
Financial Analysis
     │
     ├── Monetization
     ├── Pricing
     ├── Unit Economics
     └── Risk Analysis
     │
     ▼
Executive Memo
     │
     ├── Business Summary
     ├── Investment Thesis
     └── Go / No-Go Decision
     │
     ▼
reports/report.md
```

---

## 🎯 Key Features

* 🤖 **Multi-Agent AI Architecture**
* 🔍 **Automated Market Research**
* 📊 **TAM / SAM / SOM Analysis**
* 🏢 **Competitor Intelligence**
* 💡 **AI-Powered Product Strategy**
* 💰 **Pricing & Monetization Analysis**
* 📈 **Unit Economics**
* ⚠️ **Business Risk Assessment**
* 📝 **Automated Executive Memo Generation**
* 🌐 **Live Web Intelligence**
* 🔄 **Sequential Agent Collaboration**

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to open an issue or submit a pull request to improve the project.

---

## 📝 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.
