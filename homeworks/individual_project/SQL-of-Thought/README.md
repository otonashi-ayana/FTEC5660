# Agentic AI for Business and FinTech - Academic Code Reproduction

## Project Summary
This project aims to reproduce the results from the paper **"SQL-of-Thought: Multi-agentic Text-to-SQL with Guided Error Correction"**. The original framework utilizes a multi-step agentic workflow to convert natural language into SQL queries, breaking the process down into multiple subproblems and incorporating a powerful error correction loop based on the schema and error tracebacks.

**Reproduction Goals & Modifications**:
**Model Swap**: The baseline evaluation initially targeted models like OpenAI (GPT-4) and Anthropic (Claude-3), and substituted the core engine to rely on the **DeepSeekV3 API**.

## Setup Instructions

### 1. Environment Setup

```bash
python3 -m venv venv
source venv/bin/activate

Test 1: Full SQL-of-Thought (Standard)**
```bash
python3 run_eval_single_schemalink.py --ablation none
```

Test 2: Without Error Correction Loop**
```bash
python3 run_eval_single_schemalink.py --ablation no_correction
```

Test 3: Without Query Plan Generation**
```bash
python3 run_eval_single_schemalink.py --ablation no_plan
```
