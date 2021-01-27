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

![Figure_23](https://driftwoodpalace.github.io/Dragon-Portfolio/portfolio-construction/_site/assets/Figure_23)


So, that's the allocation I plan of using.

We Europeans have a different problem then the Americans. It's easier to access hedge fund vehicles. But the regulations MiFID II and PRIIP makes it hard to buy North American ETFs. So, I will use different vehicles then the ones suggested in the paper.

Lets look at the various components.


### Equity-linked

I will split this "bucket" the following way:
* 75% Global equities
* 25% Swedish equities

I'm using global equities to get a broad exposure and Swedish equities since that's where I'm based. If you are in another country you should probably replace the Swedish equity part. To implement this I'm using the following instruments:

* Global equities - "Avanza Global". Fee 0.10%
* Swedish equities - "Avanza Zero". Fee 0%

Avanza Global place all its money in "AMUNDI INDEX MSCI WORLD I13SK" (should be this product [https://www.amundietf.fr/professional/product/view/LU1681043599](https://www.amundietf.fr/professional/product/view/LU1681043599)) So, you could get the same exposure by using that fund. My first draft had 25% US equities (and 50% global). But the global fund is mostly USA anyway so you get plenty of exposure with this allocation. If investment sentiment shifts from the US a global fund will probably capture this better as well.


### Fixed income

This one is a bit tricky since European bonds barely pays anything. How should you divide this bucket up? The options in Sweden are pretty limited. The only developed country where you can get any yield is basically the US. So, I'm thinking about dividing it like this:

* 50% US bonds (mostly treasury bonds)
* 50% Swedish bonds (mix of government and highly rates companies)

The funds I've found for this is:

* US bonds - "Nordea 1 - Long Duration US Bd BP SEK". Fee 0.91%
* Swedish bonds - "AMF Räntefond Lång". Fee 0.15%

I'm not very happy about paying a 0.91% fee to get exposure to US bonds that doesn't pay that much more. But my options are very limited. I don't want 100% exposure to Swedish (or other European) bonds either. One option is to put some money in "SEB Korträntefond C USD - Lux". That fund has a fee of 0.5% and buys US notes (2-10 years). But as of this writing that would mean that the fee would be greater then the rate of the 2-5 year notes the fund buys. So, I'm sticking to those two for now.


### Gold

This one is fairly easy. I'm going to divide it like this;

* 75% Physical gold
* 25% Gold ETF ("paper gold")

In the paper it is suggested to put everything in physical gold. But, for tax reasons and ease of rebalancing, 25% is going in an ETF. This gives me the following:

* Physical gold - Your preferred site. I like bullionstar.com as it's founder is a Swedish veteran and I've had a great experience there. I've had a bad experience with goldmoney.com (and there fee structure sucks for smaller investors). But no recommendations, DYOR.
* Gold ETF -  "WisdomTree Physical Swiss Gold (GZUR)". Fee 0.15%.

Finding a great gold ETF in Europe was harder then expected. But I've used the above fund for some time and hopefully they have all of the gold they say they have.


### Commodity trend

Now comes the interesting stuff.  For a retail investor, getting information about commodity trend or long volatility funds is not easy. It usually requires subscriptions for 1000s of dollars and that you are an accredited investor. I have not managed to find the components of the fund in the paper (HFRX Systematic Macro CTA Index). HFR wanted me to sign a yearly subscription of $3750 to release that information. 

But, I've managed to find the components of the "SG trend index". That's the 10 largest trend following strategy funds in the world. Not strictly commodities as I think the paper talks about. But most of the funds should be "market neutral" which I believe serves it purpose. However, I only found one of those funds that I easily could invest in. That is the Swedish fund "Lynx". 

In the paper, Chris suggests you could use global macro funds as well (but he couldn't backtest that). I'm reading this as that you could put some global macro in this "market neutral" bucket as well. This gives me a few more options. I've found 4 funds that I'm going to use here:

* 50% CTA - "Lynx". Fee 1.02% + 20% performance fee.
* 20% CTA - "SEB Asset Selection C SEK - Lux". Fee 1.15% + 20% performance fee.
* 15% Systematic global macro - "IPM Systematic Macro UCITS A SEK ACC". Fee 2.12% + 20% performance fee.
* 15% Discretionary macro - "Nordkinn". Fee 1.5% + 20% performance fee.

Ideally I would like more funds here. I will keep my eyes open to diversify this bucket. But, this is what I have found now and I think it's OK. As this is mostly Swedish funds you could probably have more (or fewer) alternatives depending on where you live.

You should be able to invest smaller amounts in all of these funds (but may have to pay a higher fee if the amount is small)


### Long volatility

This is probably the most interesting "bucket". In the paper funds in "Eurekahedge CBOE Long Volatility Hedge Fund Index" is suggested as alternatives. As before, very hard to find information. But here I managed to dig out the components from 2019 at least. 11 funds (but only 8 different companies). One of these funds looks readily available to European investors. That's the fund "Amundi Fds Volatil Wld". That fund has been around since 2007 and must be one of the longest standing actors in this space. 

So, that seems like a great alternative. Another fund of the index is "Seeyond Volatility Strategy (NVOLACI LX Equity)" [https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610](https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610). From what I can find, it should be possible for European investors to invest with a minimum investment of €50 000. However I have not found any way for me in Sweden to do this. But maybe it's easier in other countries. The same goes for the fund "Bréhat Class I" [https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI](https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI). It's not in the long vol index (at least as of 2019), but it's a long vol fund. Minimum investment in Brehat is €100 000, but haven't found a way to invest from Sweden here either.

If you have $100 000 to invest in this bucket there's a new "fund of funds" you could look into. It's called "Mutiny Fund" [https://mutinyfund.com/](https://mutinyfund.com/) and gives you exposure to funds like Logica and Artemis Capital. It is open to European investors. I'm going to try to invest myself. But there is some hurdles to get over for this to happen (taxes, forms to fill out etc). So, not sure if I will be successful. 

My only other option is to invest everything in Amundis fund. It's most likely a fine fund, but I'd like a bit more diversification then that. The limit for Mutiny is about what I plan to put in this bucket. So, the plan is to divide it like this:

* 80% - "Mutiny Fund". Fee 1% + 10% performance fee.
* 20% - "Amundi Fds Volatil Wld A2 USD C" - Fee 1.6% + 4.5% entry fee. 


### Conclusion

I've tried to minimize the number of vehicles in the first three buckets and maximize them in the last two. It wasn't easy, but I believe the end result is fairly close to the "Dragon portfolio". As I am investing in Swedish Krona (SEK) there is some currency risk for some of the instruments. I've decided to not try to hedge that risk. The risk that I would mess something up trying to do that is probably greater then the currency risk.

The portfolio will then look like this:

![Figure_24](/assets/Figure_24.png)


Next, let's backtest this portfolio and decide for a strategy on how to implement it: [Backtest](/backtest)
