#!/usr/bin/env python
# coding: utf-8

# # COGS 108 - Final Project 

# ## Permissions

# Place an `X` in the appropriate bracket below to specify if you would like your group's project to be made available to the public. (Note that PIDs will be scraped from the public submission, but student names will be included.)
# 
# * [  ] YES - make available
# * [  ] NO - keep private

# # Overview

# *Fill in your overview here*

# # Names
# 
# - Toland (Venti)
# - Chongyun (Daiki)
# - GO
# - cw

# # Group Members IDs
# 
# - A15747306(Kyle)
# - A14136586
# - A######## (Gary)
# - A######## (Cary)

# # Research Question

# How does a games genre, merchandise, critic score, online/total players count, player base affect a games popularity and sales?

# ## Background and Prior Work

# This question is interesting because:
# We will be able to see the current trends in gaming.
# When a game is released by a company, the critic score, the company its made by, and the genre can predict how well the game does in the market. These all influence the popularity of a game. So according to these variables, we want to predict how popular a game is and if it is worth playing. Recently some popular games such as among us and Genshin impact have skyrocketed in popularity and sales, so we want to investigate what exactly makes games like this popular so fast.
# References (include links):
# - 1)https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.549.6080&rep=rep1&type=pdf
# - 2)

# # Hypothesis
# 

# According to the paper above, adventure games and strategy games are the highest rated genres due to their storylines, graphics, and stimulating gameplay. We expect games that fit this category to have the highest sales, ratings, and playerbase.

# # Dataset(s)

# *Fill in your dataset information here*
# 
# (Copy this information for each dataset)
# - Dataset Name: Metacritic Games Stats 2011-2019
# - Link to the dataset: https://www.kaggle.com/skateddu/metacritic-games-stats-20112019?select=metacritic_games.csv
# - Number of observations: 4018
# 
# 1-2 sentences describing each dataset. 
# 
# If you plan to use multiple datasets, add 1-2 sentences about how you plan to combine these datasets.

# *Fill in your dataset information here*
# 
# (Copy this information for each dataset)
# - Dataset Name: Video Game Sales
# - Link to the dataset: https://www.kaggle.com/gregorut/videogamesales?select=vgsales.csv
# - Number of observations: 16596
# 
# 1-2 sentences describing each dataset. 
# 
# If you plan to use multiple datasets, add 1-2 sentences about how you plan to combine these datasets.

# *Fill in your dataset information here*
# 
# (Copy this information for each dataset)
# - Dataset Name: IGN Games of 20 Years
# - Link to the dataset: https://raw.githubusercontent.com/john7obed/ign_games_of_20_years/master/ign.csv
# - Number of observations: 18624
# 
# 1-2 sentences describing each dataset. 
# 
# If you plan to use multiple datasets, add 1-2 sentences about how you plan to combine these datasets.

# # Setup

# Let's begin by importing some packages for analysis.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

import patsy
import statsmodels.api as sm
import scipy.stats as stats
from scipy.stats import ttest_ind, chisquare, normaltest


# In[2]:


# Configure libraries
# The seaborn library makes plots look nicer
sns.set()
sns.set_context('talk')

# Don't display too many rows/cols of DataFrames
pd.options.display.max_rows = 7
pd.options.display.max_columns = 8

# Round decimals when displaying DataFrames
pd.set_option('precision', 2)


# Let's also import the 3 datasets listed for the analysis.

# In[3]:


metacritic = pd.read_csv('metacritic_games.csv')
ign = pd.read_csv('ign.csv', index_col='Unnamed: 0')
vgsales = pd.read_csv('vgsales.csv')


# To make sure that our data is imported properly:

# In[4]:


metacritic.head()


# In[5]:


ign.head()


# In[6]:


vgsales.head()


# # Data Cleaning

# Describe your data cleaning steps here.

# In[7]:


## YOUR CODE HERE
## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION


# # Data Analysis & Results

# Include cells that describe the steps in your data analysis.

# In[8]:


## YOUR CODE HERE
## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION


# # Ethics & Privacy

# *Fill in your ethics & privacy discussion here*

# # Conclusion & Discussion

# *Fill in your discussion information here*

# # Team Contributions

# *Specify who in your group worked on which parts of the project.*
