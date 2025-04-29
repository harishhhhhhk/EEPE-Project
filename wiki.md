# Project Summary
The project is a diet recommendation system website designed to provide personalized diet plans based on users' health conditions and preferences. Utilizing an AI model on the backend, the frontend is developed using Streamlit UI, featuring an attractive interface that collects user information through a form and displays tailored diet recommendations.

# Project Module Description
The main module consists of a Streamlit application that:
1. Collects user health information via a form.
2. Simulates interaction with a backend AI model to generate diet recommendations.
3. Displays personalized diet plans, foods to avoid, supplement suggestions, and a sample daily meal plan.

# Directory Tree
```
streamlit_template/
├── app.py               # Main application code for the diet recommendation system
└── requirements.txt     # List of dependencies required to run the application
```

# File Description Inventory
- **app.py**: Contains the main logic for the diet recommendation system, including user interface design, data collection, and mock backend interaction for generating diet recommendations.
- **requirements.txt**: Specifies the necessary Python packages for the application.

# Technology Stack
- **Streamlit**: A Python library for building web applications.
- **Python**: The programming language used for the application logic.

# Usage
1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```
