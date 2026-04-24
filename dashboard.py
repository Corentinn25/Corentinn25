import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = {
    'Category': ['Data Eng', 'Data Eng', 'Data Eng', 'ML', 'ML', 'Viz', 'Viz', 'Analysis'],
    'Skill': ['dbt', 'Mage AI', 'Snowflake', 'Scikit-Learn', 'Feature Eng', 'Streamlit', 'PowerBI', 'Pandas'],
    'Level': [85, 75, 80, 70, 75, 90, 85, 95]
}

df = pd.DataFrame(data)
sns.set_theme(style="whitegrid")


plt.figure(figsize=(10, 6))
colors = sns.color_palette("viridis", len(df))

ax = sns.barplot(x='Level', y='Skill', hue='Category', data=df, palette="magma")


plt.title('Technical Skills Proficiency', fontsize=16, fontweight='bold', color='white')
ax.set_facecolor('#0d1117') # Couleur de fond GitHub Dark
plt.gcf().set_facecolor('#0d1117')
plt.xticks(color='white')
plt.yticks(color='white')
plt.xlabel('Mastery (%)', color='white')
plt.ylabel('', color='white')


plt.tight_layout()
plt.savefig('skills_dashboard.png', dpi=300, transparent=False)
