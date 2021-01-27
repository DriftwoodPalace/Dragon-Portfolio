---
layout: page
title: 2. Backtest
---

Lets backtest the portfolio! All my (messy) [code](https://github.com/DriftwoodPalace/Dragon-Portfolio/tree/main/code) and data is available at my Github page. As data for some of the funds are limited, I've had to make some changes to the portfolio for the backtest. The changes I've made, compared to the portfolio I'm planning to implement are the following:

* "Avanza Global" changed to "SPP Global A"
* "Nordea 1 - Long Duration US Bd BP SEK" changed to "iShares 20+ Year Treasury Bond ETF (TLT)". Adjusted TLT to show returns in SEK as well.
* "WisdomTree Physical Swiss Gold (GZUR)" changed to "SPDR Gold Shares (GLD)". Adjusted GLD to show returns in SEK.
* Changed weighting in the Commodity trend bucket so "Lynx" carries 75% of that weight and "SEB Asset Selection C SEK - Lux" 25%.
* Changed weighting in the Long volatility bucket so "Amundi Fds Volatil Wld A2 USD" carries 100% of that weight. Adjusted the returns to SEK.

The first three changes shouldn't change much as the returns for the new funds should be similar. The largest risk is with the two last changes as the performance becomes very dependent on those funds. 

But when looking at the returns I believe they should be pretty representative for those type of funds. Lynx has posted steady returns since its inception in 2000. Nothing spectacular (+ ~40% over the last 10 years), but as expected it has been largely unaffected by periods like 2000, 2008, 2018 and 2020.

Amundi Fds Volatil Wld has performed as I expect a long vol fund to perform. Big returns in periods like 2008 and 2020 and small losses along the way. So, hopefully these changes wont do that much. 

With these modification I have data going back to **November 2007**. Ideally I would like more, but this at least captures the financial crisis etc. I'm not using any leverage (except if the funds are using it by themselves). Returns include all fees except for Amundis entry fee and are measured in Swedish Krona (SEK).

### First test

Lets start by following the same methodology as presented in the paper. Decide the weighting for the individual components and rebalance every month. 

That gives us:

* Total return: 150.8% (2.5X)
* Cumulative aggregate return (yearly return): 7.2%
* Standard deviation: 0.328
* Sharpe ratio: 2.74
* Max drawdown: -11.1%

As we can see, the returns are fairly steady:
![Figure_1](./Figure_1.png)

And max drawdowns are fairly limited:
![Figure_2](./Figure_2.png)

We can compare this to a classic 60/40 portfolio of global equities and US bonds. 

It's had the following returns:

* Total return: 150.2% (2.5X)
* Cumulative aggregate return (yearly return): 7.2%
* Standard deviation: 0.313
* Sharpe ratio: 2.85
* Max drawdown: -13.0%


So, very similar returns to the dragon portfolio:
![Figure_3](./Figure_3.png)

And drawdowns wasn't terribly different either (but it was harder hit by the financial crisis):
![Figure_4](./Figure_4.png)

This is over a period where equities and bonds has rallied a lot. Sure the start date right before the financial crisis affects the result. But still impressive by the dragon portfolio IMO.

If we look at a portfolio with 100% global equities this is the result (remember the results are in SEK):

* Total return: 138.8% (2.4X)
* Cumulative aggregate return (yearly return): 6.8%
* Standard deviation: 0.458
* Sharpe ratio: 1.97
* Max drawdown: -37.1%
  
![Figure_5](./Figure_5.png)

![Figure_6](./Figure_6.png)

Pretty surprising if you ask me (again the start date is of course a big factor here). 

I doubt bonds can post the same gains as before and equities leaves you very vulnerable (6 years in the hole if you've used the fund above). 

So, with this I feel comfortable that "my" dragon portfolio would have performed decent in most environments and that it's not super different then the portfolio in the paper. 

So, I'd like to implement it. But how should I do that? Rebalancing every component every month is not a realistic option. Fees would eat you up (and you wouldn't be the most popular customer in some of the funds).


### Second test

So, lets try to rebalance less often. What happens if we rebalance every 3 months? 

This is the returns:

* Total return: 149.7% (2.5X)
* Cumulative aggregate return (yearly return): 7.2%
* Standard deviation: 0.334
* Sharpe ratio: 2.68
* Max drawdown: -11.0%
![Figure_7](./Figure_7.png)
![Figure_8](./Figure_8.png)

As one could imagine, not that much of a difference from 1 month.

Lets try every 6 months:

* Total return: 146.2% (2.5X)
* Cumulative aggregate return (yearly return): 7.1%
* Standard deviation: 0.341
* Sharpe ratio: 2.60
* Max drawdown: -11.0%
![Figure_9](./Figure_9.png)
![Figure_10](./Figure_10.png)

Some difference, but still not that much. 

For the really lazy person, can you get away with rebalancing once a year?

Every 12 months:

* Total return: 143.0% (2.4X)
* Cumulative aggregate return (yearly return): 7.0%
* Standard deviation: 0.340
* Sharpe ratio: 2.57
* Max drawdown: -11.4%
![Figure_11](./Figure_11.png)
![Figure_12](./Figure_12.png)

Your returns would have taken a small hit. But still not that different from rebalancing every month.

### Final plan

So, we can get away with rebalancing the portfolio less often. Can we do it smarter? If a position only has moved a few % in a given time period, it seems unnecessary to pay transaction fees to change that.

What happens if we only rebalance if a position gets more then a set % from it's starting weight? 

Lets start with 10% as a limit. So, if we (in our backtest portfolio) have 75% allocated to global equities in the equity bucket. It means global equities is 18% of the total portfolio. This component can then move +-1.8% of the total portfolio before we change it. 

If it moves more, we change it to 18% again (and use the positions that's moved in the other direction to rebalance it). This way we can calculate the number of transactions that we need to do as well.

Lets start with 10% as a limit. That gives the following returns:

* Total return: 152.6% (2.5X)
* Cumulative aggregate return (yearly return): 7.3%
* Standard deviation: 0.329
* Sharpe ratio: 2.75
* Max drawdown: -11.0%
![Figure_13](./Figure_13.png)
![Figure_14](./Figure_14.png)

This portfolio actually performed slightly better then the first one.

To follow this plan you would have needed to make 214 transactions over 13 years. That's 4 trades every quarter. Can we increase the limit and get away with fewer transactions?

This is with 15%:

* Total return: 154.8% (2.5X)
* Cumulative aggregate return (yearly return): 7.4%
* Standard deviation: 0.330
* Sharpe ratio: 2.77
* Max drawdown: -10.6%
![Figure_15](./Figure_15.png)
![Figure_16](./Figure_16.png)

This actually gives us better returns. The number of transactions to follow this plan is reduced to 111. Less then one transaction a month and about 2 transactions every quarter. Can we get away with 20%?

Returns with 20% limit:

* Total return: 149.3% (2.5X)
* Cumulative aggregate return (yearly return): 7.2%
* Standard deviation: 0.331
* Sharpe ratio: 2.70
* Max drawdown: -10.4%
![Figure_17](./Figure_17.png)
![Figure_18](./Figure_18.png)

It's starting to affect returns slightly. But you only had to do 63 transactions in 13 years (~1 transaction every quarter). Maybe you could go even higher. But it's a risk I don't want to take. With the limited data I have to work with there might be errors with that strategy that doesn't show up here.

The sweet spot seems to be in the range of 10-20%. I guess it depends on how active you like to be. The number of transactions might of course be slightly higher if you have more components in the different buckets (depending on your strategy).

### Conclusion

I'm personally leaning against setting a limit of a +-15% change for any individual component. You can of course set it for each "bucket" as well if you like that. If we look at the largest component, equities, as a "worst case". This bucket is then allowed to move between 20.4% and 27.6% before any adjustments are made (this is if both global equities and Swedish equities perform about the same). 

I could live with that for the advantage of doing fewer trades.

If you are interested in how a dragon portfolio performs if money is taken out of the portfolio (for example when you retire), check out: [Retiring](/retiring)
