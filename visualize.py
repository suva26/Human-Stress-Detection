import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# Function to load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to create Box Plot of Heart Rate (hr) by Stress Level (sl)
def create_boxplot_hr(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='sl', y='hr', data=data)
    plt.title('Box Plot of Heart Rate by Stress Level')
    plt.xlabel('Stress Level')
    plt.ylabel('Heart Rate')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

# 
# Function to create Pie Chart of Stress Levels (sl)
def create_pie_chart_sl(data):
    plt.figure(figsize=(8, 8))
    data['sl'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
    plt.title('Pie Chart of Stress Levels')
    plt.ylabel('')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

# Function to call all visualizations and return their URLs
def create_all_visualizations():
    data = load_data('data/Stress.csv')
    boxplot_hr_url = create_boxplot_hr(data)
   
    pie_chart_sl_url = create_pie_chart_sl(data)
    
    return {
        'boxplot_hr_url': boxplot_hr_url,
        
        'pie_chart_sl_url': pie_chart_sl_url
    }
