import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from tweet_analysis.fonctionnalite9 import *

sns.set(style="white", context="talk")
rs = np.random.RandomState(8)

(pos_tweets,neu_tweets,neg_tweets) = opinion_surcandidat(tweets)
pos = len(pos_tweets)*100/len(tweets)
neu = len(neu_tweets)*100/len(tweets)
neg = len(neg_tweets)*100/len(tweets)

# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)

# Generate some sequential data
x = np.array(["Positif","Neutre","Négatif"])
y = [pos,neu,neg]

sns.barplot(x=x, y=y, palette="rocket", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Sequential")

# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

plt.plot()

