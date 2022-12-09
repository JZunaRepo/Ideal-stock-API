# IDEAL STOCK API 

Ideal stock API allows 

Application programming interfaces are a great way to collect valuable information from a server to your computer. In this project we used the website: https://polygon.io/ to request information of stocks from 2021-03-29 to 2022-05-25 and then apply statistical analysis on the weekly closing price of the desire stock.

In the script use for thisp project, we solely rely on the built-in fucntions and modules available on python. Additionally, you will find csv files where the information of the API was collected, saved, and then used for statistical analysis. 

Please refer to the following section for more information of this project. 

<hr>

# Content
<ol>
<li><b>extract.py</b> 
<p>In this file you will find the starting code to request information from the API. You will need a "key" (not provided) that can be obtained by creating an account in https://polygon.io/</p>
<p>This information is then stored and properly labled in a csv file with its respective stock ticker.</p>
</li>
<li><b>analysis.py</b>
<p>This files retrieves the information stored in the csv file to calculate the weekly standard deviation of each stock (one provided in this example). Additionally, a visualization is provided to better understand the changes of variation of the stock from 2021-03-29 to 2022-05-25</p>
</li>
