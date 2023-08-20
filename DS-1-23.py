#!/usr/bin/env python
# coding: utf-8

# # Sales Prediction of Steam Games

# ## 1. Introduction 

# ### 1.1 Objective
# Steam is a renowned digital gaming platform that serves as a hub for gamers worldwide. Developed and operated by Valve Corporation, Steam has revolutionized the way gamers access and enjoy their favorite video games. Launched in 2003, it quickly gained popularity and became the go-to platform for PC gaming.
# 
# At its core, Steam offers users a vast library of games spanning various genres, ranging from indie titles to blockbuster releases. Players can browse and purchase games directly from the platform, which are then added to their digital library for easy access. Steam also provides a secure and convenient way to install, update, and manage games, eliminating the need for physical media.
# 
# The success of the platform brought huge business prospects and value. According to the information disclosed by Steam’s parent company Vavle, Steam’s annual game revenue (excluding in-game purchases) reached US$6.6 billion in 2021, and the number of monthly active users was 132 million,  which had an increase of 74% compared with three years ago.
# 
# While the cake is getting bigger and bigger, the long tail effect is gradually becoming more obvious. By August 19, 2023, the number of games released on Steam has reached 77,902, and more than 44,000 development teams have released games on Steam. Among them, there were 1622 teams with a revenue of more than 1 million US dollars, accounting for only 3% of the total number, while on the opposite the number of teams with a revenue of less than 1000 US dollars was 25190, accounting for 57%. Selecting the correct type of game and supplementing it with reasonable pricing has become a necessary condition for the survival of game development teams.
# 
# From a commercial point of view, game sales are generally considered to be the complex combined result of game quality and pricing, which can directly reflect the industry's evaluation of games and related revenue.
# 
# The first half of this project will clean and prrpeocess the data, trying to find out the development trend of game sales in the past ten years, and then select some features to analyze game sales, which aims to find an approximate regression equation to assist game developers to make judgments and decisions in the early stage of the project.a.

# Steam 是著名的数字游戏平台，是全球游戏玩家的中心。 Steam 由 Valve Corporation 开发和运营，彻底改变了玩家访问和享受他们喜爱的视频游戏的方式。 它于 2003 年推出，迅速流行并成为 PC 游戏的首选平台。
# 
# Steam 的核心是为用户提供涵盖各种类型的庞大游戏库，从独立游戏到热门游戏。 玩家可以直接从平台浏览和购买游戏，然后将其添加到他们的数字库中以方便访问。 Steam 还提供了一种安全、便捷的方式来安装、更新和管理游戏，无需物理介质。
# 
# 平台的成功带来了巨大的商业前景和价值。根据Steam母公司Vavle披露的消息，2021年Steam全年游戏营收（不含游戏内购）达到66亿美元，月活用户数量为1.32亿人，较三年前同步增长74%。
# 
# 在蛋糕越做越大的同时，长尾效应也逐渐趋于明显。到2023年8月19日，Steam上发布的游戏数量达到77,902款，有超过44000支开发团队在Steam上发布游戏。其中营收金额超过100万美元的团队为1622支，仅占全部人数的3%，而营收金额小于1000美元的团队数量为25190，占到全部人数的57%。选择适合的游戏种类并辅以合理的定价已成为游戏开发团队赖以生存的必要条件。
# 
# 商业角度上，游戏销量一般认为是游戏质量和定价的综合结果，能够直接反映业界对于游戏的评价本项目前半部分将对数据进行清洗和整理，试图找出近十年内游戏销量跟随不同特点的发展趋势，后半部分将选取部分特性作为分析游戏销量的关联因素，并试图找出近似的回归方程以辅助游戏开发者在项目前期做出判断进而做出决策。断进而做出决策。
# 

# ### 1.2 Dataset
# The dataset is a comprehensive collection of data encompassing all games available on the Steam platform, along with their corresponding metadata scraped from Steam and SteamSpy APIs. The dataset includes information about each game, such as its title, release date, developer, publisher, genre, user reviews, ratings, and system requirements. It covers a wide range of game genres, including action, adventure, strategy, role-playing , simulation, sports, and more, providing a diverse and extensive representation of the Steam game library. The dataset was gathered in May 2019 and didn't cover games after that.
# 
# There are 18 features in the source dataset, and we will select the following features as needed:
# 
# 1. AppID - Unique identifier for each title
# 2. Name - Name of the game
# 3. Release date - Release date in format YYYY-MM-DD
# 4. English - Boolean:  1 if the game supported English
# 5. Platforms - Semicolon delimited list of supported platforms. At most includes: windows;mac;linux
# 6. Genres - Semicolon delimited list of game genres, e.g. action;adventure,  which includes many tags
# 7. Positive_ratings - Number of positive ratings from owners
# 8. Negative_ratings - Number of negative ratings from owners
# 9. Owners - Estimated number of owners. Contains lower and upper bound (like 20000-50000).
# 10. Price - Current full price of title in GBP

# 该是一个从Steam及SteamSpy API抓取的全面的数据集合，涵盖 Steam 平台上提供的所有游戏及其相应的元数据。 该数据集包含有关每个游戏的信息，例如标题、发行日期、开发商、发行商、类型、用户评论、评级和系统要求。 它涵盖了广泛的游戏类型，包括动作、冒险、策略、角色扮演、模拟、体育等等，提供了 Steam 游戏库的多样化和广泛的代表性。该数据集于2019年5月创建因此不包含之后的游戏数据。
# 
# 源数据集中存在18个特征，根据需要我们将选取以下特征值作为因子变量：
# 
# 1. AppID - 软件唯一标识码
# 2. 名称 - 游戏名称
# 3. 发布日期 - 游戏发布的时间
# 4. 是否支持英语 - 布尔值： 1 代表支持
# 5. 支持的平台 - 以分号间隔
# 6. 种类 - 游戏的种类，可能包含多个标签
# 7. 好评 - 游戏所有者给出的评分，在一定程度上反映了用户的评价
# 8. 差评 - 游戏所有者给出的评分，在一定程度上反映了用户的评价
# 9. 销量 - 预计游戏的用户量，以区间划分
# 10. 价格 - 游戏的价格，以英镑为单位
# 

# ### 1.3 Problem Statement
# Answer to the following questions are given:
# 
# 1. Which game recieves the highest owners?
# 2. Which game recieves the highest user score?
# 3. Which genre of game has the highest owners?
# 4. How was the trend in the game industry in the last decade?
# 5. How was the correlation between genre, price, rating and owners of games?
# 6. How supported platform and language influenced polularity of games?
# 7. Can we make popularity prediction with the followiing features? 

# 我们将试图回答以下问题：
# 
# 1. 哪些游戏的用户量最高？
# 2. 哪些游戏的用户评价最好？
# 3. 哪个游戏种类的用户量最高？
# 4. 游戏的热门趋势在过去十年中是怎样的？
# 5. 游戏的种类，价格，评价与销量间存在怎样的相关性?
# 6. 游戏支持的语言和平台存在何种影响？
# 7. 能否根据其他因素预计游戏的销量？

# ## 2. Dataset Preprocessing

# ## 2.1 Libraries

# LIBRARIES:
# 
# 1. Library pandas will be required to work with data in tabular representation.
# 2. Library numpy will be required to round the data in the correlation matrix.
# 2. Library fuzzywuzzy will be needed to replace the same values but different in writing.
# 4. Library missingno will be required to visualize missing values in the data.
# 5. Library collections will be required to count the values in the list.
# 6. Library matplotlib, seaborn, plotly required for data visualization.
# 7. Library scipy will be required to test hypotheses.

# 1. pandas 用来以表格形式处理数据。
# 2. numpy 用来对相关性矩阵中的数据进行舍入。
# 3. fuzzywuzzy用来对相同值但表述方式不同的数据进行替换。
# 4. Missingno 用来可视化数据中的缺失值。
# 5. collections用来计算列表中的值。
# 6. matplotlib、seaborn、plotly用来进行数据可视化。
# 7. scipy 用来验证并测试假设。

# In[1]:


import pandas as pd
import numpy as np
import missingno
import fuzzywuzzy
from fuzzywuzzy import process
import collections
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu


# ## 2.2 Data Types

# In[2]:


# Reading Dataset
games = pd.read_csv("steam.csv") #Loading data
games_featured = pd.DataFrame(games,columns=['appid','name','release_date','english','platforms','genres','positive_ratings','negative_ratings','owners','price'])
games_featured.head()


# In[3]:


# Data types deducing
games_featured.dtypes


# ## 2.3 Missing Values

# In[4]:


# loop through the columns and check the missing values
for col in games_featured.columns:
    pct_missing = games_featured[col].isnull().mean()
    print(f'{col} - {pct_missing :.1%}')


# In[6]:


# Build a matrix of missing values
missingno.matrix(games_featured, fontsize = 16)
plt.show()


# 下一步：preprocessing
# 1. 是否需要对发布日期（released_date）进行格式转换以方便计算？
# 2. platforms拆分：可以按是否支持windows/linux/mac拆分成三个fesature，或考虑到windows是目前主流的pc游戏平台，考虑拆分成是否支持windows和支持其他平台两个feature
# 3. genres拆分：存在部分游戏多个tag的情况，考虑按游戏类型拆分成多个feature，或统计出前几名的游戏类型拆分成子feature，如是否为动作游戏/休闲游戏/策略游戏/其他等
# 4. positive/negative：可以用好评/差评的比例创造一个新feature表示好评率，同时需要一个新feature表示好评+差评的总数量表示评价的准确程度（防止样本过少）
# 5. 后面的其他内容建议参考老师给的示例(https://www.kaggle.com/code/ivannatarov/amazon-s-books-eda-plotly-hypothesis-test/notebook#3-TESTING-HYPOTHESES)
# 6. 暂时想到这些，有疑问随时沟通

# In[ ]:




