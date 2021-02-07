---
layout: page
title: 2. Backtest
---

Lets backtest the portfolio! All my code and data is available at my [Github page](https://github.com/DriftwoodPalace/Dragon-Portfolio/tree/main/code). As data for some of the funds are limited, I've had to make some changes to the portfolio for the backtest. The changes I've made, compared to the portfolio I'm planning to implement are the following:

* "SPDR MSCI World UCITS ETF" changed to "MSCI World, net total return"
* "Lyxor MSCI Emerging Markets ex China UCITS ETF" changed to (MSCI Emerging markets, net total return)
* "iShares $ Treasury Bond 20+yr UCITS ETF" changed to "iShares 20+ Year Treasury Bond ETF (TLT)".
* "iShares Global Corporate Bond EUR Hedged UCITS ETF" changed to "Barclays global Corp" (that it is tracking).
* "WisdomTree Physical Swiss Gold (GZUR)" changed to "SPDR Gold Shares (GLD)".
* Changed weighting in the Commodity trend bucket so "Lynx" carries 75% of that weight and "SEB Asset Selection C SEK - Lux" 25%.
* Changed weighting in the Long volatility bucket so "Amundi Fds Volatil Wld A2 USD" carries 100% of that weight.
* Adjusted all returns to SEK.

The first 3 modifications shouldn't change returns much as it's changed to the index it tracks or to a similar ETF. The change to MSCI Emerging markets includes China, so that could change the returns.

Gold should be the same.

The change in the "CTA bucket" shouldn't do much as Lynx and SEB is the largest parts in my "real" portfolio.

The largest risk is with the change to Amundi Fds Volatil Wld. Mutniy fund has a very limited history, so I have to use something else.   

Amundi Fds Volatil Wld has performed as I expect a long vol fund would perform. Big returns in periods like 2008 and 2020 and small losses along the way and I can get data back to 2007. So, hopefully this change wont do that much. 

With these modification I have data going back to **November 2007**. Ideally I would like more, but this at least captures the financial crisis etc. I'm not using any leverage (except if the funds are using it by themselves) in my calculations. Returns include fees where the index is used and are in Swedish krona (SEK).

### Returns for all components

Before we start, lets look how all individual components have performed. All returns are total returns (dividends reinvested).

![MSCI_World](../assets/MSCI_World.png)

![MSCI_World dd](../assets/MSCI_World_dd.png)

![MSCI_EM](../assets/MSCI_EM.png)

![MSCI_EM dd](../assets/MSCI_EM_dd.png)

![TLT](../assets/tlt.png)

![TLT dd](../assets/tlt_dd.png)

![Comp_bonds](../assets/Comp_bonds.png)

![Comp_bonds dd](../assets/Comp_bonds_dd.png)

![EM_bonds](../assets/EM_bonds.png)

![EM_bonds dd](../assets/EM_bonds_dd.png)

![gold](../assets/gold.png)

![gold dd](../assets/gold_dd.png)

![Lynx](../assets/Lynx.png)

![Lynx dd](../assets/Lynx_dd.png)

![SEB_asset_select](../assets/SEB_asset_select.png)

![SEB_asset_select dd](../assets/SEB_asset_select_dd.png)

![Amundi](../assets/Amundi.png)

![Amundi dd](../assets/Amundi_dd.png)


### First test

We can now implement the dragon portfolio. Lets start by following the same methodology as presented in the paper. Eg. decide the weighting for each individual components and rebalance every month:

![Dragon_every_month](../assets/Dragon_every_month.png)

And max drawdowns:
![Dragon_every_month_dd](../assets/Dragon_every_month_dd.png)

We can compare this to a classic 60/40 portfolio of global equities and US bonds: 

![60-40](../assets/60-40.png)

And drawdowns:

![60-40_dd](../assets/60-40_dd.png)

So yeah, the 60/40 portfolio has performed slightly better over this period. But that was over a period where bond yields collapsed and equities rallied to record valuations. Sure the start date right before the financial crisis affects the result. But the dragon portfolio keeps up well (and was ahead for many years).

So, with this I feel fairly comfortable that "my" dragon portfolio would have performed decent in most environments and that it's not super different then the portfolio in the paper. 

So, I'd like to implement it. But how should I do that? Rebalancing every component every month is not a realistic option. Fees would eat me up (and you wouldn't be the most popular customer in some of the funds).


### Second test

So, lets try to rebalance less often. This happens if we rebalance every 3 months: 

![Dragon_every_3month](../assets/Dragon_every_3month.png)

![Dragon_every_3month_dd](../assets/Dragon_every_3month_dd.png)

As one could imagine, not that much of a difference from 1 month.

Lets try every 6 months:

![Dragon_every_6month](../assets/Dragon_every_6month.png)

![Dragon_every_6month_dd](../assets/Dragon_every_6month_dd.png)

Some difference, but still not that much. 

For the really lazy person, can you get away with rebalancing once a year?

Every 12 months:

![Dragon_every_12month](../assets/Dragon_every_12month.png)

![Dragon_every_12month_dd](../assets/Dragon_every_12month_dd.png)

Your returns would have taken a small hit. But still not that different from rebalancing every month.


### Final plan

So, we can get away with rebalancing the portfolio less often. Can we do it smarter? If a position only has moved a few % in a given time period, it seems unnecessary to pay transaction fees to change that.

What happens if we only rebalance if a position gets more then a set % from it's starting weight? 

Lets start with 10% as a limit. So, if we (in our backtest portfolio) have 80% allocated to global equities in the equity bucket. It means global equities is 19.2% of the total portfolio. This component can then move +-1.92% of the total portfolio before we change it. 

If it moves more, we change it to 19.2% again (and use the positions that's moved in the other direction to rebalance it). This way we can calculate the number of transactions that we need to do as well.

So if component A moves 15% up and component B and C moves 7.5% down. We sell 15% of A and buy 7.5% of B and C. That gives us 3 transactions in total.

Lets start with 10% as a limit:

![Dragon_every_10pct](../assets/Dragon_every_10pct.png)

![Dragon_every_10pct_dd](../assets/Dragon_every_10pct_dd.png)

This portfolio actually performed very similar to the first one.

To follow this plan you would have needed to make 214 transactions over 13 years. That's roughly 4 trades every quarter. Can we increase the limit and get away with fewer transactions?

With 15%:

![Dragon_every_15pct](../assets/Dragon_every_15pct.png)

![Dragon_every_15pct_dd](../assets/Dragon_every_15pct_dd.png)


This actually gives us marginally better returns. The number of transactions to follow this plan is reduced to 114. Less then one transaction a month and about 2 transactions every quarter. Can we get away with 20%?

Returns with 20% limit:

![Dragon_every_20pct](../assets/Dragon_every_20pct.png)

![Dragon_every_20pct_dd](../assets/Dragon_every_20pct_dd.png)

It's starting to affect returns slightly. But you only had to do 59 transactions in 13 years (~1 transaction every quarter). Maybe you could go even higher. But it's a risk I don't want to take. With the limited data I have to work with there might be errors with that strategy that doesn't show up here.

The sweet spot seems to be in the range of 10-20%. I guess it depends on how active you like to be. The number of transactions might of course be slightly higher if you have more components in the different buckets (depending on your strategy).

### Conclusion

I'm personally leaning against setting a limit of a +-15% change for any individual component. You can of course set it for each "bucket" as well if you like that. If we look at the largest component, equities, as a "worst case". This bucket is then allowed to move between 20.4% and 27.6% before any adjustments are made (this is if both global equities and EM equities perform about the same). 

I could live with that for the advantage of doing fewer trades.

The volatility is fairly low and the sharpe ratio is decent. So, using some leverage might increase your returns. If I get a good deal, I might use 10-20% leverage myself.
