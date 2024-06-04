
stock_sentiment_analysis  https://github.com/xiangwxt/stock_sentiment_analysis/blob/main/stock_sentiment_analysis.ipynb  
Conduct sentiment analysis on news headlines from finviz.com   

----
Installation:  
Python 3.9  
 
install : pip install plotly --upgrade  
jupyter labextension install jupyterlab-plotly   
![image](https://github.com/GinChoYen/JiaoTong/assets/22329486/21464fd0-6137-40c3-a1e8-3b24e16fe195)
click on mark notebook trusted  
![image](https://github.com/GinChoYen/JiaoTong/assets/22329486/f04f30da-5313-422a-acf6-5dc6ff689da8)

---  

Of course! The code is designed to scrape stock news, analyze sentiment, and visualize the data. Let's break it down:

1. Scrape stock news from finviz.com
URL: The base URL (finviz_url) is set to Finviz. By appending tickers (like AAPL, TSLA), one can get news for specific stocks.

print_news function: Given a list of tickers, this function fetches the news data from Finviz. It uses BeautifulSoup to parse the HTML content and extracts news headlines and their timestamps for each ticker. The data is returned as a DataFrame.

2. Conduct sentiment analysis
sentiment_scores function: The function uses VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library to get sentiment scores (positive, negative, neutral, and compound) for each news headline. The results are concatenated with the original data and returned.
3. Calculate average score for each stock ticker
average_score function: This function calculates the average of sentiment scores (including the compound score) for each stock ticker. The results are sorted by the compound score.
4. Check stock price in a given period of time
Using the yfinance library, the stock prices for the given tickers and dates are fetched. The fetched data is rounded to two decimal places for readability.
5. Calculate percentage change of a stock price within a given period of time
percent_change function: For each ticker, the function calculates the daily percentage change in the stock's closing price from the start date to the end date. The results are consolidated and returned as a DataFrame.
6. Visualize trend of stock price change against market benchmark
profit_viz function: The function first fetches the profit percent change of the stock and the benchmark from the given dates. Then, it uses altair to plot the trend of the stock's profit percent change against the benchmark's profit percent change.
7. Volume Change Analysis
volume_change function: Fetches the stock's trading volume data using yfinance. The function calculates the difference in volume from one day to the next and categorizes it as "Increase" or "Decrease".

viz_volume function: Visualizes the volume changes using plotly. It uses different colors for days when volume increased versus decreased.

General Observations:
Error Handling: The code has a number of error-handling mechanisms, like checking if news_table is None or catching attribute errors.

Visualization Libraries: Multiple visualization libraries (matplotlib, altair, and plotly) are used to offer a variety of visual outputs.

Dependencies: The code relies on various libraries like pandas, BeautifulSoup, NLTK, yfinance, and more.

Suggestions/Improvements:
Consistent Visualization: Using multiple libraries for visualization can be confusing. It would be better to stick to one for consistency unless there's a specific need.

Volume Change Analysis: Instead of just showing "Increase" or "Decrease", it might be more informative to calculate the percentage change in volume.

Optimizing percent_change function: Instead of hardcoding for 1 to 5 tickers, use a more flexible method to handle any number of tickers.

More Error Handling: There are places where the code might break if given unexpected inputs or if the structure of the Finviz website changes.

Overall, the code provides a comprehensive analysis of stock news sentiment and its potential correlation with stock price movement.


----
The code provided is designed to scrape financial news, conduct sentiment analysis, visualize stock prices and volume changes, and compare stocks against benchmarks. I'll provide a rating based on various parameters:

Functionality (25/25)

All functions seem to achieve their intended purposes.
Error handling is mostly present, and there's an effort to deal with different contingencies (like missing news tables or date validation).
Modularity (20/20)

Functions are well-segregated with each focusing on a particular task.
This modularity makes the code more readable and manageable.
Readability (20/25)

There are comments throughout the code which help in understanding the intent and flow.
However, some variable names could be more descriptive (e.g., foo lambda function).
Optimization (15/20)

The code could be more optimized in certain places:
In the percent_change function, the logic for creating the result DataFrame could be made more dynamic rather than hard-coding for specific lengths of tickers.
The profit_viz function contains repetitive validation checks that could potentially be refactored or abstracted away.
Extensibility (8/10)

While the code is modular and can be expanded upon, the way some functions are constructed (like the hard-coding in percent_change) might make it more challenging to extend the code without significant changes.
Overall Score: 88/100

This code shows a good understanding of Python, data manipulation, and visualization. However, a few tweaks could be made to improve its readability, optimization, and extensibility.
