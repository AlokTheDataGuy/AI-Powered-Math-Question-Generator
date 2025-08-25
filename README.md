# AI-Powered Math Question Generator (LLM-Oriented)

A Python application that **generates curriculum-aligned math assessment questions** using **local LLMs** (via Hugging Face or Ollama).
It produces questions in strict tag-based format, creates professional Word documents, and can embed graphs for coordinate geometry problems.

---

## 🌟 Features

* **Curriculum-Aligned**: Strictly follows the provided Quantitative Math curriculum hierarchy.
* **LaTeX Support**: Preserves formulas and equations with `$...$` notation.
* **Multiple Question Types**: Algebra, geometry, fractions/percents, quadratic equations, coordinate geometry, and more.
* **Strict Formatting**: Outputs questions in the exact `@tag` format required.
* **Professional Exports**:

  * `assessment_questions.txt` (HR-required tagging format)
  * `math_assessment.docx` (well-structured Word doc with explanations)
  * Graph images embedded in Word doc (when applicable).
* **Free LLM Integration**:

  * Run locally with Hugging Face models (`transformers`)
  * Or use **Ollama** with models like `mistral:7b` or `llama3.1:8b`.

---

## 📋 Supported Question Types

* **Algebra** → Linear & quadratic equations, word problems, polynomial operations
* **Geometry** → Circles, triangles, coordinate geometry (with auto-generated graphs)
* **Numbers & Operations** → Fractions, decimals, percentages, sequences
* **Data Analysis & Probability** → Tables, graphs, averages, probability

---

## 🛠️ Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd math-question-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install Ollama and pull a model (if not already installed):

```bash
ollama pull mistral:7b
```

---

## 🚀 Usage

### Hugging Face (Transformers)

Runs with a local HF model (requires GPU/CPU resources):

```bash
python llm_generator_rev.py --num 2 --llm hf --hf_model mistralai/Mistral-7B-Instruct-v0.2
```

### Ollama (Recommended for local use)

Leverages your installed Ollama models:

```bash
python llm_generator_rev.py --num 2 --llm ollama --ollama_model mistral:7b
```

Available models on your system (example):

* `mistral:7b`
* `llama3.1:8b`
* `qwen2.5:7b`

---

## 📄 Output Format

Questions strictly follow the assignment’s required format:

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
@explanation Detailed step-by-step explanation
@subject Quantitative Math
@unit Geometry and Measurement
@topic Circles (Area, circumference)
@plusmarks 1
```

---

## 📊 Deliverables

* **assessment\_questions.txt** → Raw formatted text (ready for HR)
* **math\_assessment.docx** → Polished Word document with embedded graphs
* **question\_\*\_graph.png** → Auto-generated coordinate plane graphs (when needed)

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

## 🔧 Configuration Options

* `--num` → number of questions (default: 2)
* `--llm hf` → use Hugging Face Transformers
* `--llm ollama` → use Ollama (local models)
* `--hf_model` → choose a Hugging Face model (default: Mistral-7B-Instruct)
* `--ollama_model` → choose an Ollama model (default: mistral:7b)
* `--title` → custom assessment title

---

## 📝 Requirements

* Python 3.8+
* Packages: `transformers`, `torch`, `python-docx`, `matplotlib`, `numpy`
* (Optional) [Ollama](https://ollama.ai) for local inference

---

## 🎓 Educational Standards

All generated questions ensure:

* Clear, unambiguous wording
* Proper difficulty balance
* Step-by-step explanations
* Strict curriculum alignment

