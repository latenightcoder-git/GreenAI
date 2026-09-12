# 🌿 GreenAI Monitor

### A GenAI-Powered Sustainable AI Usage Analyzer

GreenAI Monitor is a Streamlit-based application that analyzes AI usage data to estimate **energy consumption and CO₂ emissions** and provide sustainability recommendations using **Google Gemini**.

The project combines **Sustainable AI, Generative AI, Data Analytics, and Responsible AI** principles into an educational dashboard.

> ⚠️ **Important:** The energy and CO₂ values displayed by this application are educational estimates based on dummy usage data and assumed energy-consumption and carbon-intensity values. They do not represent measurements from an actual AI data center.

---

## 🚀 Project Overview

As the use of Artificial Intelligence grows, understanding its environmental impact becomes increasingly important.

GreenAI Monitor helps users explore:

- 🤖 AI request volumes
- ⚡ Estimated AI energy consumption
- 🌍 Estimated CO₂ emissions
- 🏗️ Energy consumption by AI model
- 🏢 Energy consumption by department
- 📈 Daily CO₂ trends
- 💚 A sustainability score
- 🔍 Responsible AI checks
- 🧠 AI-generated sustainability recommendations

The application uses calculated data as input to Gemini so that recommendations are grounded in the project's own dataset and calculations.

---

## ✨ Key Features

### 📊 Sustainability Dashboard

The dashboard displays four main metrics:

- Total AI Requests
- Total Estimated Energy Consumption
- Total Estimated CO₂ Emissions
- Sustainability Score

---

### 📋 AI Usage Data

The application loads AI usage information from `ai_usage.csv` using Pandas.

The dataset contains:

| Column | Description |
|---|---|
| `date` | Date of AI usage |
| `department` | Department generating AI requests |
| `model` | AI model category |
| `requests` | Number of AI requests |
| `tokens` | Number of tokens processed |
| `energy_per_request_wh` | Assumed energy consumed per request in Wh |

---

### ⚡ Energy Calculation

Energy consumption is estimated using:

```text
Energy (Wh) = AI Requests × Energy per Request (Wh)
````

 The result is then converted into kilowatt-hours:

```
Energy (kWh) = Energy (Wh) / 1000
```

---

 ### 🌍 CO₂ Calculation

 The project uses a simplified carbon-intensity assumption:

```
CARBON_INTENSITY = 0.4 kg CO₂/kWh
```

 CO₂ emissions are estimated using:

```
CO₂ (kg) = Energy (kWh) × Carbon Intensity
```

 This is an educational assumption and should not be interpreted as actual grid or data-center carbon intensity.

---

 ## 💚 Sustainability Score

 GreenAI Monitor calculates a simple sustainability score based on total estimated energy consumption.

 | Total Energy | Score |
| --- | --- |
| Less than 10 kWh | 90 |
| 10–19.99 kWh | 75 |
| 20–29.99 kWh | 60 |
| 30 kWh or more | 40 |

 The score is intentionally simple and explainable so that students can easily understand how it is generated.

---

 ## 🏗️ Energy Analysis

 The application analyzes energy consumption across different AI models.

 Example model categories in the dataset:

 - `SmallModel`
- `MediumModel`
- `LargeModel`

 This helps demonstrate how choosing smaller models for suitable tasks can potentially reduce estimated energy consumption.

 The application also identifies the department with the highest estimated energy consumption.

---

 ## 📈 Visualizations

 GreenAI Monitor provides several visualizations:

 ### Energy by AI Model

 A bar chart compares total estimated energy consumption across AI models.

 ### Energy by Department

 A bar chart compares estimated energy consumption between departments.

 ### Daily CO₂ Estimate

 A line chart shows estimated daily CO₂ emissions over time.

 These visualizations make it easier to identify usage patterns and potential areas for optimization.

---

 ## 🤖 Gemini Sustainable AI Advisor

 The project integrates Google's Gemini API to generate sustainability recommendations.

 Gemini receives the calculated summary:

```
- Total AI requests
- Total energy
- Estimated CO₂
- Sustainability score
- Highest-energy AI model
- Highest-energy department
```

 The AI advisor is instructed to provide:

 1. Overall sustainability assessment
2. Main sustainability problem
3. Three practical recommendations
4. Ways smaller AI models could help
5. Ways unnecessary AI requests can be reduced
6. A Responsible AI recommendation

 ### 🔒 Grounded AI Approach

 The Gemini prompt explicitly instructs the model to:

 - Use only supplied data
- Avoid inventing measurements
- Clearly identify energy and CO₂ as estimates
- Avoid claiming that the values are actual data-center measurements
- Provide explanations suitable for students

 This helps demonstrate the principle of **grounded Generative AI**.

---

 ## 🔍 Responsible AI Audit

 GreenAI Monitor includes a basic Responsible AI audit.

 The audit checks:

 ### 1\. Data Completeness

 Verifies that all required dataset columns are available.

 Required columns:

```
date
department
model
requests
tokens
energy_per_request_wh
```

 ### 2\. Missing Critical Values

 Checks whether required fields contain missing values.

 ### 3\. Transparent Calculation

 Checks that calculated energy and CO₂ metrics are present in the summary.

 ### 4\. Explainable Score

 Ensures the sustainability score remains within:

```
0–100
```

 ### 5\. Human Oversight

 Gemini provides recommendations, while humans remain responsible for interpreting and acting on those recommendations.

 ### 6\. Grounded in Data

 The AI advisor receives calculated project data rather than being asked to invent sustainability measurements.

 ### 7\. Sustainability Estimate Disclosure

 The application clearly communicates that energy and CO₂ values are estimates.

---

 ## 🌟 Responsible AI & Digital Trust Principles

 The project demonstrates several Responsible AI principles.

 | Principle | Implementation |
| --- | --- |
| 🔍 Transparency | Energy and CO₂ calculations are visible |
| 📖 Explainability | Sustainability score uses simple rules |
| 👤 Human Oversight | Humans make final decisions |
| 🌱 Sustainability | Encourages efficient AI usage |
| 🔒 Digital Trust | Dataset and calculations can be inspected |
| 🧠 Grounding | Gemini receives calculated project data |
| ⚠️ Disclosure | Estimates and assumptions are explicitly communicated |

---

 ## 📁 Project Structure

```
GreenAI/
│
├── app.py
├── sustainability.py
├── gemini_ai.py
├── ai_usage.csv
├── .env
├── .gitignore
└── README.md
```

 ### `app.py`

 Main Streamlit application.

 Responsible for:

 - Dashboard UI
- Loading and processing data
- Charts
- Responsible AI audit display
- Gemini sustainability report generation

 ### `sustainability.py`

 Contains the core sustainability calculations.

 Functions include:

```
load_data()
calculate_energy()
calculate_co2()
calculate_score()
get_summary()
responsible_ai_audit()
```

 ### `gemini_ai.py`

 Handles communication with the Gemini API and generates sustainability recommendations.

 ### `ai_usage.csv`

 Contains the sample AI usage dataset.

 ### `.env`

 Stores the Gemini API key locally.

 > 🔐 Never commit your `.env` file or API key to GitHub.

---

 ## 🛠️ Technologies Used

 - 🐍 Python
- 📊 Pandas
- 🎨 Streamlit
- 🤖 Google Gemini API
- 🔐 python-dotenv
- 📈 Streamlit Charts
- 🌱 Sustainable AI concepts
- 🔍 Responsible AI principles

---

 ## ⚙️ Installation

 ### 1\. Clone the Repository

```
git clone https://github.com/latenightcoder-git/GreenAI.git
```

 Move into the project directory:

```
cd GreenAI
```

---

 ### 2\. Create a Virtual Environment

```
python -m venv venv
```

 Activate it on Windows:

```
venv\Scripts\activate
```

 On macOS/Linux:

```
source venv/bin/activate
```

---

 ### 3\. Install Dependencies

 Install the required Python packages:

```
pip install pandas streamlit google-genai python-dotenv
```

---

 ## 🔑 Gemini API Configuration

 Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

 The application loads the API key using:

```
load_dotenv(find_dotenv())
```

 and:

```
mykey = os.getenv("GEMINI_API_KEY")
```

 ### ⚠️ Security Notice

 Do not upload your API key to GitHub.

 Add this to `.gitignore`:

```
.env
venv/
__pycache__/
```

---

 ## ▶️ Running the Application

 Start the Streamlit application with:

```
streamlit run app.py
```

 Streamlit will provide a local URL where you can open the dashboard in your browser.

---

 ## 🔄 Application Workflow

 The application follows this workflow:

```
             ┌─────────────────┐
             │   ai_usage.csv  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Load Dataset  │
             │     Pandas      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Energy Estimate │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ CO₂ Estimation  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Summary Metrics │
             └────────┬────────┘
                      │
             ┌────────┴─────────┐
             ▼                  ▼
    ┌─────────────────┐  ┌──────────────────┐
    │ Responsible AI  │  │ Streamlit        │
    │     Audit       │  │ Dashboard        │
    └─────────────────┘  └────────┬─────────┘
                                   │
                                   ▼
                         ┌──────────────────┐
                         │ Gemini AI Advisor│
                         └──────────────────┘
                                   │
                                   ▼
                         Sustainability
                         Recommendations
```

---

 ## 📐 Core Calculation Example

 Suppose an AI model receives:

```
1,000 requests
0.8 Wh per request
```

 Estimated energy:

```
1,000 × 0.8 = 800 Wh
```

 Convert to kWh:

```
800 / 1000 = 0.8 kWh
```

 Using the project's carbon-intensity assumption:

```
0.8 × 0.4 = 0.32 kg CO₂
```

 Therefore:

```
Estimated Energy = 0.8 kWh
Estimated CO₂ = 0.32 kg
```

 Again, these are **model-based educational estimates**, not real-world measurements.

---

 ## 🌱 Why Smaller AI Models Matter

 One of the sustainability ideas demonstrated by this project is **model selection**.

 Not every AI task requires a large model.

 For simpler tasks, a smaller model may potentially provide sufficient results while requiring fewer computational resources.

 A sustainable AI strategy can therefore consider:

```
Task complexity
      ↓
Select appropriate model
      ↓
Avoid unnecessary large-model usage
      ↓
Potentially reduce computational energy
```

 The project does not claim a universal energy saving for smaller models. Actual energy consumption depends on many factors, including model architecture, hardware, workload, infrastructure, and serving conditions.

---

 ## ♻️ Reducing Unnecessary AI Requests

 Organizations can potentially reduce AI resource consumption by:

 - Avoiding duplicate AI requests
- Caching repeated results where appropriate
- Improving prompts to reduce unnecessary iterations
- Using smaller models for simple tasks
- Removing unnecessary automated AI calls
- Reviewing high-volume AI workflows
- Applying human judgment before repeated AI generation

 The goal is not simply to use less AI, but to use AI **more efficiently and appropriately**.

---

 ## ⚠️ Limitations

 This project is designed as an educational Sustainable AI demonstration.

 Important limitations include:

 ### Dummy Dataset

 The included `ai_usage.csv` contains sample data and does not represent real organizational AI usage.

 ### Estimated Energy

 Energy consumption is calculated using a fixed energy-per-request assumption supplied in the dataset.

 ### Simplified Carbon Intensity

 The project uses:

```
CARBON_INTENSITY = 0.4
```

 This is a simplified assumption and does not account for real-time electricity-grid carbon intensity.

 ### No Data Center Measurements

 The project does not directly measure:

 - CPU/GPU power
- Data-center electricity consumption
- Hardware utilization
- Cooling energy
- Network energy
- Actual inference energy

 ### Gemini Recommendations

 Gemini's recommendations are AI-generated and should be reviewed by humans before being used for operational or organizational decisions.

---

 ## 🔐 Responsible Use

 GreenAI Monitor should be treated as an **educational sustainability analytics tool**, not as a certified carbon-accounting system.

 For real-world sustainability reporting, organizations should use validated measurements, appropriate emissions factors, documented methodologies, and relevant environmental accounting standards.

---

 ## 🎯 Project Goals

 The main goals of GreenAI Monitor are to demonstrate:

 - How AI usage can be analyzed from structured data
- How estimated energy consumption can be calculated
- How estimated CO₂ emissions can be derived
- How sustainability metrics can be visualized
- How Generative AI can provide grounded recommendations
- How Responsible AI checks can be incorporated into an AI application
- Why transparency and human oversight matter in AI systems
- How model selection can be considered as part of Sustainable AI

---

 ## 🚀 Future Improvements

 Potential future enhancements include:

 - [ ] Real-time electricity carbon-intensity data
- [ ] Hardware-level energy monitoring
- [ ] More detailed model efficiency analysis
- [ ] Cost estimation
- [ ] Carbon emissions comparison over time
- [ ] CSV upload through the Streamlit interface
- [ ] Downloadable sustainability reports
- [ ] Interactive date filters
- [ ] Department-level sustainability targets
- [ ] Model recommendation based on task complexity
- [ ] Historical sustainability tracking
- [ ] More advanced Responsible AI checks
- [ ] Cloud deployment

---

 ## 📚 Educational Value

 This project demonstrates how multiple areas of modern technology can work together:

```
Python
  +
Data Analytics
  +
Streamlit
  +
Generative AI
  +
Responsible AI
  +
Sustainable AI
```

 It can be used as a learning project for students interested in:

 - Artificial Intelligence
- Generative AI
- Green AI
- Data Science
- Python
- Responsible AI
- Environmental sustainability
- AI governance

---

 ## 👩‍💻 Author

 **Madhuchhanda Das**

 GitHub Repository:

 https://github.com/latenightcoder-git/GreenAI.git

---

 ## 🌿 Project Philosophy

 > **Build AI responsibly. Measure what you can. Make assumptions transparent. Use AI efficiently. Keep humans in the loop.**

 GreenAI Monitor is a small step toward understanding how AI systems can be designed with **sustainability, transparency, explainability, and digital trust** in mind.


---

 ⭐ **If you find this project useful, consider starring the repository on GitHub!**

---
