![image](https://github.com/user-attachments/assets/3ec53878-33ec-4d48-95bb-4e301102315f)# Distributed-crawler-system-based-on-Scrapy-framework-and-Redis-database-cluster

We design a distributed crawler system based on Scrapy framework and Redis database cluster. 
Scrapy provides efficient data capture and parsing functions, while Redis cluster implements task distribution and deduplication, reducing the space occupancy of string data.

## Development Environment 

Operating system： Ubuntu 24.04.1 

Python version： Python 3.11.4

Redis version：Redis-x64-5.0.14.1

## Test Run 

### Download Package
Download the package using Git command and install environment dependencies.

```shell
git clone https://github.com/SYSU-Zhangyp/Weibo-Comment-Manager-Scrapy-Redis.git
cd weibospider
pip install -r requirements.txt
```

### Replace Cookie

Accessing Weibo PC（ https://weibo.com/ ）Log in to your account, open the developer mode of your browser, and refresh again

Replace cookies (./weibo_spider/weibo_spider/settings.py) in Settings.

### Add proxy IP

Rewrite the fetch_dexy method (./weibo_spider/weibo_spider/middlewares.py), which needs to return a proxy IP address.

### Deploying Redis Cluster

We need to deploy Redis cluster. Please refer to the Redis Cluster Deployment Tutorial for details（ https://blog.csdn.net/Yel_Liang/article/details/132093594 ）Cluster deployment can refer to the Redis cluster folder.

### Run crawler

Open Redis cluster and execute commands on the terminal.

```shell
cd weibo_spider
scrapy crawl weibo_comment
```

Waiting for the request queue to be generated, waiting for the terminal to crawl and output the results.

### Visualize Redis database

Download and Install Redis Desktop Manager.

### Comment Query Platform

Return to the previous directory, run streamlit, and implement user interaction.

```shell
cd ..
cd streamlit
streamlit run visualization.py
```
