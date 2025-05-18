import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load synthetic data (can be replaced with real data)
data = {
    'Community': [f'EuroVillage-{i}' for i in range(1, 11)],
    'Population': [1000, 1500, 2000, 1200, 1800, 1600, 1400, 1100, 1900, 1300],
    'Agricultural_Area_ha': [100, 150, 120, 130, 160, 140, 110, 90, 170, 125],
    'Total_Biomass': [688.0, 1032.0, 1176.0, 850.6, 1188.4, 1060.0, 918.8, 755.2, 1222.2, 882.6],
    'Biochar_tons': [240.8, 361.2, 411.6, 297.71, 415.94, 371, 321.58, 264.32, 427.77, 308.91],
    'BioOil_tons': [309.6, 464.4, 529.2, 382.77, 534.78, 477, 413.46, 339.84, 549.99, 397.17],
    'Syngas_tons': [137.6, 206.4, 235.2, 170.12, 237.68, 212, 183.76, 151.04, 244.44, 176.52],
    'Total_Revenue_EUR': [125560.0, 188340.0, 214620.0, 155234.5, 216883.0, 193030.0, 167313.0, 137542.0, 221330.5, 159864.0],
    'Total_Profit_EUR': [119560.0, 182340.0, 208620.0, 149234.5, 210883.0, 187030.0, 161313.0, 131542.0, 215330.5, 153864.0],
    'Payback_Years': [0.42, 0.27, 0.24, 0.34, 0.24, 0.27, 0.31, 0.38, 0.23, 0.26]
}

# Create dataframe
df = pd.DataFrame(data)

# Sidebar
st.sidebar.title("Pyrolysis Digital Twin")
st.sidebar.markdown("Simulate micro-energy systems in rural European communities.")

# Main
st.title("Community-Level Pyrolysis Simulator")

page = st.sidebar.selectbox("Navigate", ["Community Overview", "Pyrolysis Simulation", "Economic Analysis"])

if page == "Community Overview":
    st.header("Virtual Community Biomass Availability")
    st.dataframe(df[['Community', 'Population', 'Agricultural_Area_ha', 'Total_Biomass']])
    st.bar_chart(df.set_index('Community')['Total_Biomass'])

elif page == "Pyrolysis Simulation":
    st.header("Annual Pyrolysis Product Yield")
    st.dataframe(df[['Community', 'Biochar_tons', 'BioOil_tons', 'Syngas_tons']])
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['Community'], df['Biochar_tons'], label='Biochar')
    ax.bar(df['Community'], df['BioOil_tons'], bottom=df['Biochar_tons'], label='Bio-oil')
    ax.bar(df['Community'], df['Syngas_tons'], bottom=df['Biochar_tons'] + df['BioOil_tons'], label='Syngas')
    ax.set_ylabel("Tons/year")
    ax.set_title("Pyrolysis Product Distribution")
    ax.legend()
    st.pyplot(fig)

elif page == "Economic Analysis":
    st.header("Cost and Payback Analysis")
    st.dataframe(df[['Community', 'Total_Revenue_EUR', 'Total_Profit_EUR', 'Payback_Years']])
    st.subheader("Net Profit by Community")
    st.bar_chart(df.set_index('Community')['Total_Profit_EUR'])
    st.subheader("Payback Period (Years)")
    st.bar_chart(df.set_index('Community')['Payback_Years'])
