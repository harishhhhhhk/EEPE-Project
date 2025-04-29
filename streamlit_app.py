import streamlit as st
import random
import time

# Set page configuration and styling
st.set_page_config(
    page_title="Nutrifit AI - Personal Diet Recommendation System",
    page_icon="🥗",
    layout="wide",
)

# Custom CSS for a more attractive UI
st.markdown("""
<style>
    .main {background-color: #f5f7f9;}
    .stApp {max-width: 1200px; margin: 0 auto;}
    h1, h2, h3 {color: #2c3e50;}
    .stButton button {background-color: #27ae60; color: white; border-radius: 5px; padding: 0.5rem 1rem;}
    .stButton button:hover {background-color: #2ecc71;}
    .recommendation-card {background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;}
    .dark-card {background-color: #1e1e1e; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; color: white;}
    .dark-card h3 {color: white;}
    .header-container {display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;}
    .emoji-icon {font-size: 40px; margin-right: 20px;}
    .health-icons {display: flex; justify-content: space-around; margin: 30px 0;}
    .health-icon {text-align: center; padding: 15px;}
    .health-icon p {margin-top: 10px;}
</style>
""", unsafe_allow_html=True)

# Mock function to simulate backend AI recommendation
def get_diet_recommendations(health_info):
    """Simulate getting diet recommendations from a backend AI model"""
    # In a real application, this would make an API call to the backend
    
    # Simulate API delay
    with st.spinner('Our AI is analyzing your health profile...'):
        time.sleep(2)
    
    # Generate mock recommendations based on health conditions
    recommendations = {
        'diet_plan': [],
        'foods_to_avoid': [],
        'supplements': [],
        'daily_meal_plan': {},
    }
    
    # Basic diet plans based on conditions
    if 'Diabetes' in health_info['conditions']:
        recommendations['diet_plan'].extend([
            "Low glycemic index foods",
            "Portion control for carbohydrates",
            "Regular meal timing to manage blood sugar"
        ])
        recommendations['foods_to_avoid'].extend(["Sugary beverages", "White bread", "Processed snacks"])
        recommendations['supplements'].extend(["Chromium", "Alpha-Lipoic Acid"])
    
    if 'Hypertension' in health_info['conditions']:
        recommendations['diet_plan'].extend([
            "DASH diet approach", 
            "Low sodium intake", 
            "Potassium-rich foods"
        ])
        recommendations['foods_to_avoid'].extend(["Canned soups", "Deli meats", "Salted snacks"])
        recommendations['supplements'].extend(["Magnesium", "Coenzyme Q10"])

    if 'Cholesterol' in health_info['conditions']:
        recommendations['diet_plan'].extend([
            "Increase soluble fiber", 
            "Healthy fats from nuts and olive oil", 
            "Lean protein sources"
        ])
        recommendations['foods_to_avoid'].extend(["Full-fat dairy", "Fried foods", "Red meat"])
        recommendations['supplements'].extend(["Omega-3 fatty acids", "Plant sterols"])
        
    if 'IBS' in health_info['conditions']:
        recommendations['diet_plan'].extend([
            "Low-FODMAP approach", 
            "Smaller, more frequent meals", 
            "Adequate hydration"
        ])
        recommendations['foods_to_avoid'].extend(["Garlic and onions", "Beans and lentils", "Artificial sweeteners"])
        recommendations['supplements'].extend(["Probiotics", "Peppermint oil"])
    
    if 'Weight Management' in health_info['conditions']:
        if health_info['weight_goal'] == 'Lose weight':
            recommendations['diet_plan'].extend([
                "Caloric deficit of 500-750 calories",
                "High protein intake",
                "Focus on nutrient-dense, low-calorie foods"
            ])
        elif health_info['weight_goal'] == 'Gain weight':
            recommendations['diet_plan'].extend([
                "Caloric surplus of 300-500 calories",
                "Protein-rich foods with every meal",
                "Nutrient-dense, higher-calorie foods"
            ])
        else:  # Maintain weight
            recommendations['diet_plan'].extend([
                "Balanced macronutrient intake",
                "Regular meal timing",
                "Mindful eating practices"
            ])
    
    # Add personalized adjustments based on allergies
    if health_info['allergies']:
        allergies_list = [allergy.strip() for allergy in health_info['allergies'].split(',')]
        recommendations['foods_to_avoid'].extend(allergies_list)
        recommendations['diet_plan'].append(f"Avoid all foods containing {', '.join(allergies_list)}")
    
    # Generate a sample daily meal plan
    meal_options = {
        'breakfast': [
            "Greek yogurt with berries and nuts",
            "Vegetable omelet with whole grain toast",
            "Overnight oats with almond milk and fruits",
            "Smoothie bowl with protein powder and seeds"
        ],
        'lunch': [
            "Grilled chicken salad with olive oil dressing",
            "Quinoa bowl with roasted vegetables and avocado",
            "Lentil soup with mixed green salad",
            "Turkey and vegetable wrap with hummus"
        ],
        'dinner': [
            "Baked salmon with roasted Brussels sprouts",
            "Stir-fried tofu with vegetables and brown rice",
            "Lean beef stew with root vegetables",
            "Grilled vegetables with quinoa and tahini dressing"
        ],
        'snacks': [
            "Apple slices with almond butter",
            "Greek yogurt with honey",
            "Mixed nuts and dried fruits",
            "Vegetable sticks with hummus"
        ]
    }
    
    recommendations['daily_meal_plan'] = {
        'breakfast': random.choice(meal_options['breakfast']),
        'lunch': random.choice(meal_options['lunch']),
        'dinner': random.choice(meal_options['dinner']),
        'snacks': [random.choice(meal_options['snacks']), random.choice(meal_options['snacks'])]
    }
    
    # Remove duplicates
    for key in ['diet_plan', 'foods_to_avoid', 'supplements']:
        recommendations[key] = list(set(recommendations[key]))
    
    return recommendations

# Application header with animated effect
def render_header():
    st.markdown("""
    <div class="header-container">
        <div>
            <h1>Nutrifit AI 🥗</h1>
            <h3>Personalized Diet Recommendations Powered by AI</h3>
        </div>
        <div class="emoji-icon">🍎</div>
    </div>
    """, unsafe_allow_html=True)

    # Health icons section
    st.markdown("""
    <div class="health-icons">
        <div class="health-icon">❤️<p>Heart Health</p></div>
        <div class="health-icon">🏃<p>Fitness</p></div>
        <div class="health-icon">🥦<p>Nutrition</p></div>
        <div class="health-icon">⚖️<p>Balance</p></div>
        <div class="health-icon">🧠<p>Mindful Eating</p></div>
    </div>
    """, unsafe_allow_html=True)

# Main application
def main():
    # Session state initialization
    if 'page' not in st.session_state:
        st.session_state.page = 'form'
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = None
    
    render_header()
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Get Recommendations", "How It Works", "About Us"])
    
    with tab1:
        if st.session_state.page == 'form':
            st.markdown("### Tell us about your health profile")
            st.markdown("Our AI nutritionist needs some information to create your personalized diet plan.")
            
            # Create a form to collect health information
            with st.form(key="health_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    age = st.number_input("Age", min_value=18, max_value=100, value=30)
                    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
                    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
                    weight = st.number_input("Weight (kg)", min_value=30, max_value=300, value=70)
                
                with col2:
                    activity_level = st.select_slider(
                        "Activity Level",
                        options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"],
                        value="Moderately Active"
                    )
                    weight_goal = st.selectbox(
                        "Weight Goal", 
                        ["Maintain weight", "Lose weight", "Gain weight"]
                    )
                    allergies = st.text_input(
                        "Food Allergies/Intolerances (comma-separated)", 
                        placeholder="e.g., nuts, dairy, gluten"
                    )
                
                st.markdown("### Health Conditions")
                st.markdown("Select any conditions that apply to you:")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    diabetes = st.checkbox("Diabetes")
                    hypertension = st.checkbox("Hypertension")
                with col2:
                    cholesterol = st.checkbox("High Cholesterol")
                    ibs = st.checkbox("IBS/Digestive Issues")
                with col3:
                    weight_management = st.checkbox("Weight Management")
                    other_condition = st.text_input("Other condition (specify)")
                
                st.markdown("### Dietary Preferences")
                diet_type = st.selectbox(
                    "Diet Type",
                    [
                        "No restrictions", "Vegetarian", "Vegan", "Pescatarian",
                        "Keto", "Paleo", "Mediterranean", "Gluten-Free"
                    ]
                )
                
                meal_prep_time = st.select_slider(
                    "Preferred Meal Preparation Time",
                    options=["Quick (< 15 min)", "Moderate (15-30 min)", "Extended (30+ min)"],
                    value="Moderate (15-30 min)"
                )
                
                submit_button = st.form_submit_button(label="Generate My Diet Recommendations")
                
                if submit_button:
                    # Collect all health conditions
                    conditions = []
                    if diabetes:
                        conditions.append("Diabetes")
                    if hypertension:
                        conditions.append("Hypertension")
                    if cholesterol:
                        conditions.append("Cholesterol")
                    if ibs:
                        conditions.append("IBS")
                    if weight_management:
                        conditions.append("Weight Management")
                    if other_condition:
                        conditions.append(other_condition)
                    
                    # Create health information dictionary
                    health_info = {
                        'age': age,
                        'gender': gender,
                        'height': height,
                        'weight': weight,
                        'activity_level': activity_level,
                        'weight_goal': weight_goal,
                        'allergies': allergies,
                        'conditions': conditions,
                        'diet_type': diet_type,
                        'meal_prep_time': meal_prep_time
                    }
                    
                    # Get diet recommendations
                    st.session_state.recommendations = get_diet_recommendations(health_info)
                    st.session_state.health_info = health_info
                    st.session_state.page = 'results'
                    st.experimental_rerun()
        
        elif st.session_state.page == 'results':
            # Display personalized recommendations
            st.markdown("## Your Personalized Diet Recommendations")
            
            # User profile summary
            with st.expander("Your Health Profile Summary", expanded=False):
                health_info = st.session_state.health_info
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Age:** {health_info['age']}")
                    st.markdown(f"**Gender:** {health_info['gender']}")
                    st.markdown(f"**Height:** {health_info['height']} cm")
                    st.markdown(f"**Weight:** {health_info['weight']} kg")
                    st.markdown(f"**Activity Level:** {health_info['activity_level']}")
                
                with col2:
                    st.markdown(f"**Weight Goal:** {health_info['weight_goal']}")
                    st.markdown(f"**Diet Type:** {health_info['diet_type']}")
                    st.markdown(f"**Allergies:** {health_info['allergies'] if health_info['allergies'] else 'None reported'}")
                    st.markdown(f"**Health Conditions:** {', '.join(health_info['conditions']) if health_info['conditions'] else 'None reported'}")
            
            recommendations = st.session_state.recommendations
            
            # Diet plan recommendations
            st.markdown("""<div class='recommendation-card'>
                <h3>🍽️ Recommended Diet Approach</h3>
            """, unsafe_allow_html=True)
            
            for item in recommendations['diet_plan']:
                st.markdown(f"- {item}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Foods to avoid
            st.markdown("""<div class='recommendation-card'>
                <h3>⛔ Foods to Limit or Avoid</h3>
            """, unsafe_allow_html=True)
            
            if recommendations['foods_to_avoid']:
                for item in recommendations['foods_to_avoid']:
                    st.markdown(f"- {item}")
            else:
                st.markdown("No specific foods to avoid based on your profile.")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Supplement recommendations
            st.markdown("""<div class='recommendation-card'>
                <h3>💊 Suggested Supplements</h3>
                <p><i>Consult with healthcare provider before starting any supplement regimen</i></p>
            """, unsafe_allow_html=True)
            
            if recommendations['supplements']:
                for item in recommendations['supplements']:
                    st.markdown(f"- {item}")
            else:
                st.markdown("No specific supplements recommended based on your profile.")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Sample meal plan
            st.markdown("""<div class='recommendation-card'>
                <h3>📅 Sample Daily Meal Plan</h3>
            """, unsafe_allow_html=True)
            
            meal_plan = recommendations['daily_meal_plan']
            st.markdown(f"**Breakfast:** {meal_plan['breakfast']}")
            st.markdown(f"**Lunch:** {meal_plan['lunch']}")
            st.markdown(f"**Dinner:** {meal_plan['dinner']}")
            st.markdown("**Snacks:**")
            for snack in meal_plan['snacks']:
                st.markdown(f"- {snack}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Disclaimer
            st.info("⚠️ Disclaimer: These recommendations are generated by an AI system for informational purposes only. Always consult with a healthcare professional or registered dietitian before making significant changes to your diet.")
            
            # Reset button
            if st.button("Start Over"):
                st.session_state.page = 'form'
                st.experimental_rerun()
    
    with tab2:
        st.markdown("## How Nutrifit AI Works")
        
        st.markdown("""<div class='dark-card'>
            <h3>🧠 Personalized AI Analysis</h3>
            <p>Our advanced AI system analyzes your unique health profile, including existing health conditions, dietary preferences, and wellness goals.</p>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("""<div class='dark-card'>
            <h3>📊 Evidence-Based Recommendations</h3>
            <p>Your diet plan is created using the latest nutritional science and medical research, customized to address your specific health needs.</p>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("""<div class='dark-card'>
            <h3>🔄 Continuous Improvement</h3>
            <p>As you provide feedback and update your health information, our AI system refines your recommendations for even better results over time.</p>
        </div>""", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("## About Nutrifit AI")
        
        st.markdown("""<div class='dark-card'>
            <h3>Our Mission</h3>
            <p>Nutrifit AI is dedicated to making personalized nutrition accessible to everyone. We believe that proper diet is fundamental to good health and wellbeing.</p>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("""<div class='dark-card'>
            <h3>Our Team</h3>
            <p>Our team consists of nutritionists, developers, and AI experts committed to creating the most effective diet recommendation system.</p>
        </div>""", unsafe_allow_html=True)
        
        st.markdown("""<div class='dark-card'>
            <h3>Contact Us</h3>
            <p>For any questions or feedback, please contact us at support@nutrifit.ai</p>
        </div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
