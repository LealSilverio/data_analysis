# Overview

The purpose of this software is for me, as a programmer, to learn about how stocks works, how to analyze data in a large scale, and the signs of a recession. This software analyzes historical stock price data to identify patterns that shows signs of economic recessions. The dataset was found at [Kaggle - Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data). This dataset "contains historical daily prices for all tickers currently trading on NASDAQ" up to April of 2020. By understanding stocks behaviors and macroeconomic shifts, we can assume when a we are in a recession or about to face one.

[Software Demo Video](https://youtu.be/bmijhoq6OWc)

# Data Analysis Results

### Questions
1. How do stock prices behave before and during recessions? What are their patterns?
    - Before a recession the close prices range is smaller(signs of a more stable economy). The average low prices during the 2 quarters before the recession also tends to be higher, in price, than the average high prices during the recession. During a recession, there's a clear downwards trend in the stock prices, reaching the lowest price possible in those quarters. There was less of a clear downwards trend in the 2001 recession when looking at individual companies, but the trend was there when looking at multiple companies together. The images used for this analysis are found at the images folder. 
2. How's recessions compared to stable economic periods?
    - During a stable economic period, the close prices are clearly higher than the average during or before a recession (the only variable that changes this are found when looking at individual companies due to major events in such company). The difference between the lowest and the highest prices is also smaller during stable economic periods.

# Development Environment

* VSCode
* Python 3.12
* Pandas and Matplotlib Libraries

# Useful Websites

* [Kaggle - Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data)
* [Investopedia - Recession](https://www.investopedia.com/terms/r/recession.asp)
* [Matplot Library](https://matplotlib.org/stable/tutorials/pyplot.html)

# Future Work

* Improve the combined CSV stock file retains the integrity of all the other files
* Question: Can you predict a recession by predicting stocks? If so, how far ahead? 