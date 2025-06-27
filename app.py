import streamlit as st
import datetime
import random

# Set page config
st.set_page_config(page_title="GreenPulse Dashboard", layout="wide")

# Header
st.title("🌿 GreenPulse Dashboard")
st.subheader("Real-time Lawn Health & Smart Mowing Insights")

# Simulated health score
health_score = random.randint(65, 95)

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Lawn Overview")
    st.metric("Lawn Health Score", f"{health_score}/100", delta=f"{random.randint(-3,3)} since last week")
    st.progress(health_score / 100)

    st.markdown("---")
    st.markdown("### Lawn Map Preview")
    st.image(
        "https://cdn.pixabay.com/photo/2017/05/10/21/46/garden-2309879_1280.jpg",
        caption="Coverage Map (Simulated)",
        use_container_width=True
    )

with col2:
    st.markdown("### Smart Mow Schedule")
    next_mow = datetime.date.today() + datetime.timedelta(days=random.choice([1, 2, 3]))
    st.success(f"✅ Next best mow: **{next_mow.strftime('%A, %B %d')}**")
    st.button("Skip Next Mow")
    st.button("Confirm Mow Plan")

    st.markdown("---")
    st.markdown("### Weather Snapshot")
    st.write("🌤️ Forecast: Partly Sunny")
    st.write("🌡️ High: 78°F / Low: 63°F")
    st.write("💧 Rain Probability: 10%")

# Insights Section
st.markdown("---")
st.markdown("## 📈 Weekly Lawn Insights")
st.markdown("- Grass growth rate: Moderate 🌱")
st.markdown("- Soil moisture: Adequate 💧")
st.markdown("- Battery efficiency: 92% ⚡")
st.markdown("- Mower coverage: 98% last session 🗺️")

# Footer
st.markdown("---")
st.caption("© 2025 GreenPulse AI - Smarter Lawn Care Starts Here")
