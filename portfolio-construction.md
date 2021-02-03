---
layout: page
title: 1. Portfolio construction
---

According to the paper "The allegory of the hawk and serpent". The dragon portfolio consists of:

* 24% Equity-linked
* 18% Fixed income
* 19% Gold
* 18% Commodity trend
* 21% Long volatility

![Figure_23](../assets/Figure_23.png)


So, that's the allocation I plan of using.

Lets look at the various components.


### Equity-linked

I will split this "bucket" the following way:
* 80% Global equities (developed markets)
* 20% Emerging market (ex China) equities

I'm using global equities (MSCI World) to get a broad exposure to the largest companies in the world and Emerging market equities to get some exposure to other parts of the world. Most emerging markets are mostly heavily China weighted. I'm using a vehicle that's "ex China". Mostly from an ethic standpoint plus that I believe that there's better opportunities in many other parts of the emerging world. What could be debated is if you should split this bucket in another way then 80/20. I'm going with 80/20 to get some exposure to EM without making the position to large.

To implement this I'm using the following instruments:

* Global equities - "SPDR MSCI World UCITS ETF (SPPW)". Fee 0.12%
* Emerging market equities - "Lyxor MSCI Emerging Markets ex China UCITS ETF – Acc (EMXC)". Fee 0.29%

I'm using ETFs, so it is easy to get in and out when I like. For MSCI World exposure I was simply looking for a fund with a low fee. For Emerging markets, Lyxors fund was the only one I found that was ex China.


### Fixed income

This one is probably the bucket I found hardest to implement. European bonds barely pays anything. Sure they can fall further below 0, but I'm not playing that game. So, how should you divide this bucket? The only developed country where you can get any yield today is basically the US. So, I'm thinking about putting 50% in long US bonds. Then 25% in company bonds and 25% in emerging market bonds. Not super happy with that allocation, but it is what it is. So, the following as long as these rates gives me some yield:

* 50% US treasury bonds (20+ years)
* 25% Corporate bonds (highly rates companies in the developed world)
* 25% Emerging market bonds

Vehicles to use for this:

* US bonds - "iShares $ Treasury Bond 20+yr UCITS ETF (IS04)". Fee 0.07%
* Company bonds - "iShares Global Corporate Bond EUR Hedged UCITS ETF (IBCQ)". Fee 0.25%
* EM bonds - "iShares J.P. Morgan $ EM Bond UCITS ETF USD (IUS7)". Fee 0.45%

I'm paying 5 basis points to hedge the company bonds to Euro. I have plenty of USD exposure elsewhere so figured it could be worth to reduce that here. The same option is available for the EM bonds, but I'm keeping it in USD so the fee doesn't get to high.


### Gold

This one is fairly easy. I'm going to divide it like this;

* 75% Physical gold
* 25% Gold ETF ("paper gold")

In the paper it is suggested to put everything in physical gold. But, for tax reasons and ease of rebalancing, 25% is going in an ETF. This gives me the following:

* Physical gold - Your preferred site. I like bullionstar.com as it's founder is a Swedish veteran and I've had a great experience there. I've had a bad experience with goldmoney.com (and there fee structure sucks for smaller investors). But no recommendations, DYOR.
* Gold ETF -  "WisdomTree Physical Swiss Gold (GZUR)". Fee 0.15%.

Finding a great gold ETF in Europe was harder then expected. But I've used the above fund for some time and hopefully they have all of the gold they say they have.


### Commodity trend

This is the interesting stuff.  For a retail investor, getting information about commodity trend or long volatility funds is not easy. It usually requires subscriptions for 1000s of dollars and that you are an accredited investor. I have not managed to find the components of the fund in the paper (HFRX Systematic Macro CTA Index). HFR wanted me to sign a yearly subscription of $3750 to release that information. 

But, I've managed to find the components of the "SG trend index". That's the 10 largest trend following strategy funds in the world. Not strictly commodities as I think the paper talks about. But most of the funds should be "market neutral" which I believe serves it purpose. However, I only found one of those funds that I easily could invest in. That is the Swedish fund "Lynx". 

In the paper, Chris suggests you could use global macro funds as well (but he couldn't backtest that). I'm reading this as that you could put some global macro in this "market neutral" bucket as well. This gives me a few more options. I've found 4 funds that I'm going to use here:

* 50% CTA - "Lynx". Fee 1.02% + 20% performance fee.
* 20% CTA - "SEB Asset Selection C SEK - Lux". Fee 1.15% + 20% performance fee.
* 15% Systematic global macro - "IPM Systematic Macro UCITS A SEK ACC". Fee 2.12% + 20% performance fee.
* 15% Discretionary macro - "Nordkinn". Fee 1.5% + 20% performance fee.

Ideally I would like more funds here. I will keep my eyes open to diversify this bucket. But, this is what I have found now and I think it's OK. As this is mostly Swedish funds you could probably have more (or fewer) alternatives depending on where you live.

You should be able to invest smaller amounts in all of these funds (but may have to pay a higher fee if the amount is small)


### Long volatility

This is IMO the most interesting "bucket". In the paper, funds in "Eurekahedge CBOE Long Volatility Hedge Fund Index" is suggested as alternatives. As before, very hard to find information. But here I managed to dig out the components from 2019 at least. 11 funds (but only 8 different companies). One of these funds looks readily available to European investors. That's the fund "Amundi Fds Volatil Wld". That fund has been around since 2007 and must be one of the longest standing actors in this space. 

Other funds in the index is "Seeyond Volatility Strategy (NVOLACI LX Equity)" [https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610](https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610). From what I can find, it should be possible for European investors to invest with a minimum investment of €50 000. However I have not found any way for me in Sweden to do this. But maybe it's easier in other countries. The same goes for the fund "Bréhat Class I" [https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI](https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI). It's not in the long vol index (at least as of 2019), but it's a long vol fund. Minimum investment in Brehat is €100 000, but haven't found a way to invest from Sweden here either.

If you have $100 000 to invest in this bucket there's a fairly new "fund of funds" you could look into. It's called "Mutiny Fund" [https://mutinyfund.com/](https://mutinyfund.com/) and gives you exposure to funds like Logica and Artemis Capital. It is open to European investors. 

I'm planning on using Mutiny myself. Firstly because I will get exposure to many more funds. Secondly because they handle the allocation between funds for you. It reduces the risk to allocate to something else then you thought (especially if you are a novice like me).

If you don't have $100k to put in the volatility bucket, Mutiny offers a combination of exposure to S&P and long vol as well, contact them for more info. Otherwise you'll have to put everything in Amundis fund. It's most likely a fine fund, but I'd like a bit more diversification then that. The entry fee to Amundis fund is 4.5%, so you would lose that capital up front. My allocation will be this:

* 100% - "Mutiny Fund". Fee 1% + 10% performance fee.

I might however put some money in Amundis fund after a while as well.

### Conclusion

I've tried to minimize the number of vehicles in the first three buckets and maximize them in the last two. It wasn't easy, but I believe the end result is fairly close to the "Dragon portfolio". As I am investing in Swedish Krona (SEK) there is some currency risk for some of the instruments. But I can live with that.

The portfolio will then look like this:

![Figure_24](../assets/Figure_24.png)


Next, let's backtest this portfolio and decide for a strategy on how to implement it: [Backtest](../backtest)
