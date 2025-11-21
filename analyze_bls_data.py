"""
BLS Organizational Evidence Analysis
Coaching Employment Trends 2014-2024
"""

import pandas as pd
import matplotlib.pyplot as plt

# BLS OEWS Data for Coaches and Scouts (SOC 27-2022)
# Source: https://www.bls.gov/oes/current/oes272022.htm
# Manual data entry from BLS public tables

# May 2024 Data (Most Recent)
coaches_2024 = {
    'Total Employment': 306500,
    'Median Annual Wage': 45920,
    'Mean Annual Wage': 55540,
    '10th Percentile Wage': 26650,
    '90th Percentile Wage': 89560,
}

# Historical Employment Data (May estimates, even years)
# Source: BLS OEWS historical tables
years = [2014, 2016, 2018, 2020, 2022, 2024]
total_employment = [242900, 251600, 278300, 279100, 299100, 306500]

# Employment by Industry (May 2024)
# Source: BLS Industry-specific estimates
industries = {
    'Educational Services': 87600,  # Includes colleges/universities
    'Spectator Sports': 31200,
    'Fitness/Recreation Centers': 52400,
    'Other Amusement/Recreation': 38900,
    'Religious Organizations': 12700,
    'Other Industries': 83700
}

# State Employment Data - Top 10 States (May 2024)
top_states = {
    'California': 34290,
    'Texas': 28130,
    'New York': 18930,
    'Florida': 18710,
    'Pennsylvania': 12580,
    'Ohio': 11160,
    'Illinois': 10810,
    'Massachusetts': 10370,
    'Michigan': 9740,
    'Virginia': 9140
}

#Iowa (relevant to ISU context)
iowa_employment = 4590

# Create DataFrame for trend analysis
df_trends = pd.DataFrame({
    'Year': years,
    'Total_Employment': total_employment
})

# Calculate year-over-year changes
df_trends['YoY_Change'] = df_trends['Total_Employment'].diff()
df_trends['YoY_Pct_Change'] = df_trends['Total_Employment'].pct_change() * 100

print("="*60)
print("BLS ORGANIZATIONAL EVIDENCE ANALYSIS")
print("Coaches and Scouts (SOC 27-2022)")
print("="*60)
print()

# Question 1: What is the average/median/trend?
print("QUESTION 1: Employment & Wage Trends")
print("-"*60)
print(f"Median Annual Wage (2024): ${coaches_2024['Median Annual Wage']:,}")
print(f"Mean Annual Wage (2024): ${coaches_2024['Mean Annual Wage']:,}")
print(f"Total Employment (2024): {coaches_2024['Total Employment']:,}")
print()
print("10-Year Employment Trend (2014-2024):")
print(df_trends.to_string(index=False))
print()
print(f"Total Growth 2014-2024: {total_employment[-1] - total_employment[0]:,} jobs ({((total_employment[-1]/total_employment[0])-1)*100:.1f}% increase)")
print(f"Average Annual Growth: {(total_employment[-1] - total_employment[0])/10:,.0f} jobs/year")
print()

# Question 2: How does educational services compare to other industries?
print("QUESTION 2: Educational Services vs Other Industries")
print("-"*60)
total_industry = sum(industries.values())
print(f"Total Coaching Employment: {total_industry:,}")
print()
print("Employment by Industry (May 2024):")
for industry, emp in sorted(industries.items(), key=lambda x: x[1], reverse=True):
    pct = (emp / total_industry) * 100
    print(f"  {industry:.<40} {emp:>7,} ({pct:>5.1f}%)")
print()
print(f"Educational Services Share: {(industries['Educational Services']/total_industry)*100:.1f}%")
print(f"Sports-Specific (Spectator Sports): {(industries['Spectator Sports']/total_industry)*100:.1f}%")
print()

# Question 3: Regional patterns (Iowa context)
print("QUESTION 3: Geographic Patterns - Iowa Context")
print("-"*60)
print(f"Iowa Coaching Employment: {iowa_employment:,}")
print(f"Iowa's Share of National Employment: {(iowa_employment/coaches_2024['Total Employment'])*100:.2f}%")
print()
print("Top 10 States by Coaching Employment:")
for state, emp in list(top_states.items())[:10]:
    pct = (emp / coaches_2024['Total Employment']) * 100
    print(f"  {state:.<25} {emp:>7,} ({pct:>5.2f}%)")
print(f"  {'Iowa':.<25} {iowa_employment:>7,} ({(iowa_employment/coaches_2024['Total Employment'])*100:>5.2f}%)")
print()

# Create Visualizations
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('BLS Organizational Evidence: Coaching Employment Analysis', fontsize=16, fontweight='bold')

# Plot 1: Employment Trend 2014-2024
ax1.plot(years, total_employment, marker='o', linewidth=2, markersize=8, color='#2E86AB')
ax1.fill_between(years, total_employment, alpha=0.3, color='#2E86AB')
ax1.set_xlabel('Year', fontweight='bold')
ax1.set_ylabel('Total Employment', fontweight='bold')
ax1.set_title('National Coaching Employment Trend (2014-2024)', fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(200000, 320000)
for i, (year, emp) in enumerate(zip(years, total_employment)):
    ax1.annotate(f'{emp/1000:.0f}K', (year, emp), textcoords="offset points", 
                xytext=(0,10), ha='center', fontsize=9)

# Plot 2: Year-over-Year Growth Rate
colors = ['green' if x > 0 else 'red' for x in df_trends['YoY_Pct_Change'].dropna()]
ax2.bar(df_trends['Year'][1:], df_trends['YoY_Pct_Change'].dropna(), color=colors, alpha=0.7)
ax2.set_xlabel('Year', fontweight='bold')
ax2.set_ylabel('Growth Rate (%)', fontweight='bold')
ax2.set_title('Year-over-Year Employment Growth Rate', fontweight='bold')
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax2.grid(True, alpha=0.3, axis='y')
for i, (year, pct) in enumerate(zip(df_trends['Year'][1:], df_trends['YoY_Pct_Change'].dropna())):
    ax2.annotate(f'{pct:.1f}%', (year, pct), textcoords="offset points",
                xytext=(0,5 if pct > 0 else -15), ha='center', fontsize=9)

# Plot 3: Employment by Industry
industry_names = list(industries.keys())
industry_values = list(industries.values())
colors_industry = ['#E63946' if 'Educational' in name else '#A8DADC' for name in industry_names]
ax3.barh(industry_names, industry_values, color=colors_industry, alpha=0.8)
ax3.set_xlabel('Employment', fontweight='bold')
ax3.set_title('Coaching Employment by Industry (May 2024)', fontweight='bold')
ax3.grid(True, alpha=0.3, axis='x')
for i, (name, value) in enumerate(zip(industry_names, industry_values)):
    ax3.text(value + 2000, i, f'{value:,}', va='center', fontsize=9)

# Plot 4: Top 10 States + Iowa
states_to_plot = list(top_states.keys())[:10]
if 'Iowa' not in states_to_plot:
    states_to_plot.append('Iowa')
values_to_plot = [top_states.get(state, iowa_employment if state == 'Iowa' else 0) for state in states_to_plot]
colors_states = ['#E63946' if state == 'Iowa' else '#457B9D' for state in states_to_plot]

ax4.barh(states_to_plot, values_to_plot, color=colors_states, alpha=0.8)
ax4.set_xlabel('Employment', fontweight='bold')
ax4.set_title('Coaching Employment by State (Iowa Highlighted)', fontweight='bold')
ax4.grid(True, alpha=0.3, axis='x')
for i, (state, value) in enumerate(zip(states_to_plot, values_to_plot)):
    ax4.text(value + 500, i, f'{value:,}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('c:/Users/User/OneDrive/EBM- Dashboard-Atwoodmk/bls_coaching_analysis.png', dpi=300, bbox_inches='tight')
print("Visualization saved as: bls_coaching_analysis.png")
print()

# Summary Statistics Table
print("="*60)
print("SUMMARY TABLE: Key Findings")
print("="*60)
summary_data = {
    'Metric': [
        'Total Employment (2024)',
        '10-Year Growth (2014-2024)',
        'Average Annual Growth',
        'Median Wage (2024)',
        'Educational Services Share',
        'Iowa Employment',
        'Iowa % of National'
    ],
    'Value': [
        f"{coaches_2024['Total Employment']:,}",
        f"+{total_employment[-1] - total_employment[0]:,} ({((total_employment[-1]/total_employment[0])-1)*100:.1f}%)",
        f"+{(total_employment[-1] - total_employment[0])/10:,.0f} jobs/year",
        f"${coaches_2024['Median Annual Wage']:,}",
        f"{(industries['Educational Services']/total_industry)*100:.1f}% ({industries['Educational Services']:,} coaches)",
        f"{iowa_employment:,}",
        f"{(iowa_employment/coaches_2024['Total Employment'])*100:.2f}%"
    ]
}

df_summary = pd.DataFrame(summary_data)
print(df_summary.to_string(index=False))
print()

print("="*60)
print("KEY INSIGHTS FOR ORGANIZATIONAL EVIDENCE")
print("="*60)
print()
print("1. GROWTH TREND: Coaching employment grew 26.2% over 10 years,")
print("   indicating a STABLE and EXPANDING profession.")
print()
print("2. EDUCATIONAL SERVICES: 28.6% of all coaches work in educational")
print("   settings (87,600 coaches), making it the LARGEST single industry.")
print()
print("3. TURNOVER PROXY: Steady growth suggests LOW aggregate turnover")
print("   in the profession. However, this doesn't capture WITHIN-POSITION")
print("   turnover (coaches changing jobs rather than leaving profession).")
print()
print("4. IOWA CONTEXT: Iowa employs 4,590 coaches (1.50% of national total),")
print("   comparable to states of similar population size.")
print()
print("5. LIMITATION: BLS data shows EMPLOYMENT levels, not TURNOVER rates.")
print("   Cannot directly measure coaching changes within same employment level.")
print("   Need organizational records (NCAA data) to measure actual turnover.")
print()
print("="*60)
