
   Data found via Kaggle (https://www.kaggle.com/datasets/tanayatipre/store-sales-forecasting-dataset?resource=download)

Write-up:
    I built this project to dive into retail sales data and transform it into something that makes sense for business decisions.  
   
   Starting from a RAW dataset, I set up a full pipeline:
    - Cleaned and processed the data into a more efficient format
    - Explored the trends, seasonality, and profitability through Jupyter
    - Found some interesting patterns - like bookcases and tables consistently hurting profits across a majority of the regions
    - Noticed a sharp profit drop around November across all categories, suggesting seasonal planning opportunities
    - Built an interactive dashboard using Streamlit where the user can explore a few of these insights themselves with filters on product, region, and time.
    The goal was simple: explore the data and have found along the way

    Tools used:
    Python (Pandas, Matplotlib, Seaborn)
    Streamlit
    Jupyter Notebook

How to run:
1. Clone Repo
2. Instal packages:
    pip install -r requirements.txt
3. Launch Dashboard:
    streamlit run dashboard/app.py
    
