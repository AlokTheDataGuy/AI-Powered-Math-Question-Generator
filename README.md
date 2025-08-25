# AI-Powered Math Question Generator (LLM-Oriented)

A Python application that **generates curriculum-aligned math assessment questions** using **local LLMs** (via Hugging Face or Ollama).
It outputs questions in strict tag-based format, creates professional Word documents, and embeds graphs for coordinate geometry problems.

---

## 🌟 Features

* **Curriculum-Aligned** → Strictly follows the Quantitative Math curriculum hierarchy.
* **LaTeX Support** → Preserves equations with `$...$` notation.
* **Multiple Question Types** → Algebra, geometry, fractions/percents, quadratic equations, coordinate geometry, and more.
* **Strict Formatting** → Outputs in exact `@tag` format required by the assignment.
* **Professional Exports**:

  * `assessment_questions.txt` → Tag-structured text file (HR-required format)
  * `math_assessment.docx` → Polished Word document with explanations
  * Auto-generated **graphs** embedded for coordinate geometry problems
* **Free Local LLM Integration**:

  * Hugging Face Transformers (e.g. `mistralai/Mistral-7B-Instruct-v0.2`)
  * Ollama with local models (`mistral:7b`, `llama3.1:8b`, `qwen2.5:7b`)

---

## 📋 Supported Question Types

* **Algebra** → Linear & quadratic equations, word problems, polynomial operations
* **Geometry** → Circles, triangles, coordinate geometry (with graphs)
* **Numbers & Operations** → Fractions, decimals, percentages, sequences
* **Data Analysis & Probability** → Tables, graphs, averages, probability

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd math-question-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install Ollama and pull a model:

```bash
ollama pull mistral:7b
```

---

## 🚀 Usage

### Hugging Face (Transformers)

Run with a local Hugging Face model (requires CPU/GPU resources):

```bash
python main.py --num 2 --llm hf --hf_model mistralai/Mistral-7B-Instruct-v0.2
```

### Ollama (Recommended for local use)

Run with Ollama-installed models:

```bash
python main.py --num 2 --llm ollama --ollama_model mistral:7b
```

Example available models:

* `mistral:7b`
* `llama3.1:8b`
* `qwen2.5:7b`

---

## 📄 Output Format

Generated questions strictly follow the required tag format:

```
@title AI-Generated Quantitative Math Assessment
@description Comprehensive math assessment covering various curriculum topics

@question Question text with $LaTeX$
@instruction Choose the correct option
@difficulty easy/moderate/hard
@Order 1
@option Option A
@option Option B
@@option Correct Answer (marked with @@)
@option Option D
@option Option E
@explanation Step-by-step explanation
@subject Quantitative Math
@unit Geometry and Measurement
@topic Circles (Area, circumference)
@plusmarks 1
```

---

## 📊 Deliverables

* **assessment\_questions.txt** → Strictly formatted text file
* **math\_assessment.docx** → Polished Word doc with graphs embedded
* **question\_\*\_graph.png** → Auto-generated coordinate plane graphs (when required)

---

## 🧪 Sample Questions

**Quadratic Example**

```
@question If $x^2 - 3x - 10 = 0$, what are all possible values of $x$?
@@option $x = -2$ and $x = 5$
@explanation Factor: $(x-5)(x+2)=0$ → $x=-2, 5$
```

**Geometry Example**

```
@question A circle has a radius of 6 units. What is the area of the circle?
@@option $36\pi$
@explanation Using $A = \pi r^2$: $A = \pi \times 6^2 = 36\pi$
```

---

## 🔧 CLI Options

* `--num` → Number of questions (default: 2)
* `--llm hf` → Use Hugging Face Transformers
* `--llm ollama` → Use Ollama (local models)
* `--hf_model` → Hugging Face model name (default: mistralai/Mistral-7B-Instruct-v0.2)
* `--ollama_model` → Ollama model name (default: mistral:7b)
* `--title` → Custom assessment title

---

## 📝 Requirements

* Python 3.8+
* `transformers`, `python-docx`, `matplotlib`, `numpy`
* (Optional) [Ollama](https://ollama.ai) for local inference

---

## 🎓 Educational Standards

All generated questions ensure:

* Clear, unambiguous language
* Balanced difficulty levels
* Step-by-step explanations
* Verified curriculum alignment

