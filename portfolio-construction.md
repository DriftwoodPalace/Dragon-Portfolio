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


So, that's the allocation I plan of using. However, I think that you can modify the individual buckets smarter then simply buying a global equity ETF and US-treasuries. I might fool myself, but I'm going to mix it up with some allocation to emerging markets and company bonds.

Lets look at the various components.


### Equity-linked

At start I will split this "bucket" the following way:
* 100% Global equities (developed markets)
* Over time I will mix in some emerging market (ex China) equities

I'm using global equities (MSCI World) to get a broad exposure to the largest companies in the world. I also would like some exposure to emerging markets. However I don't like the idea of buying and holding an emerging market ETF over longer time periods (say 3 years+). Most EM ETFs are fairly illiquid which could cause some serious risks to your capital (it could for example decouple from the underlying assets as arbitrages are harder). Verdad Capital has an interesting paper for how to smarter invest in Emerging markets. It's called "Emerging markets crisis investing". It's basically saying that for the last decades most of the gains in emerging markets has been after large crashes. That's the time to invest. So, I'm implementing a variation of that strategy here. It will be implemented both for equties and bonds. 

"My strategy" will be very similar to the one in the paper. But as I can't access sovereign debt for individual EM-countries, I have to replace bonds with equities in most of the cases: 

* Look at 14 individual emerging markets (South Korea, Taiwan, India, Malaysia, Turkey, Saudi Arabia, Brazil, Thailand, Indonesia, South Africa, Mexico, Poland, Russia and Philippines). China, Vietnam, Chile and Greece are in the paper as well. But as of now I don't have easy access to investing in the last 3 and I'm excluding China for personal reasons.
* Look for when a markets index (MSCI) for any specific country has dropped 50% or more from the top.
* Wait 3 months after that and then invest in the equity index for that country.
* Hold for 24 months and then sell whatever has happened. If the index hasn't recovered (surpassed previous entry point) at the point of sale, wait 12 months before investing in that country again.
* Allocate 5% of the equity portfolio if a country meats the definition (so a maximum of 70% of the equity part and 16.6% of the total portfolio would be allocated here). 
* If we have an Emerging market crisis without a global crisis (defined as a >20% drop in the S&P500 within 3 months of the drop in the last EM-index that took the total above 50%), reduce the "EM-equity part" with 50% and buy a broad Emerging Markets bond ETF representing the weight. Emerging market crisis is defined if >50% of the country indices has dropped >50% from the ATH. The equity part would then be max 35% emerging market (2.5% per country). Same rules for the bond part.


To implement this I'm using the following instruments:

* Global equities - "SPDR MSCI World UCITS ETF (SPPW)". Fee 0.12%
* Emerging market equities - "MSCI Index ETFs"


I'm using ETFs, so it is easy to get in and out when I like. For MSCI World exposure I'm simply looking for a fund with a low fee. 


### Fixed income

This one is probably the bucket I found hardest to implement. European bonds barely pays anything. Sure they can fall further below 0, but I'm not playing that game. So, how should you divide this bucket? The only developed country where you can get any yield today is basically the US. It's still the "cleanest shirt in the laundry" and pays higher yield then most other sovereign debt. So, I'm putting 75% in long US bonds. Then 25% in company bonds to reach for some yield (and get a bit more diversification). I'm staying away from Emerging market debt unless we see a specific Emerging market crisis:

* 50% US treasury bonds (20+ years)
* 25% US treasury bonds (7-10 years)
* 25% Corporate bonds (highly rated companies in the developed world)

Vehicles to use for this:

* US bonds 20y+ - "iShares $ Treasury Bond 20+yr UCITS ETF (IS04)". Fee 0.07%
* US bonds 7-10y - "iShares $ Treasury Bond 7-10yr UCITS ETF USD (Dist)". Fee 0.07%
* Company bonds - "iShares Global Corporate Bond EUR Hedged UCITS ETF (IBCQ)". Fee 0.25%
* (EM bonds - "iShares J.P. Morgan $ EM Bond UCITS ETF USD (IUS7)". Fee 0.45%)

I'm paying 5 basis points to hedge the company bonds to Euro. I have plenty of USD exposure elsewhere so figured it could be worth to reduce that here. 

If US bonds are within 10 basis points of the 0 bound, I will sell. So say that the 7-10 year reaches 0.10% (on average), I'll sell and buy 20 year+ if they still have a higher yield. I'll the sell the 20 year+ if it reaches 0.10%. The same goes for corporate bonds, but there my limit is 1% (yields around 2% as of the beginning of 2021). I'll divide it between the US bonds bucket if there is room in both. If it's only in say 20y+, I'll put 100% of my bond exposure in that bucket (but I'll never put more then 25% in corporate bonds). 

What if we reach 0% yield on the US 30 year bond then? My current thinking is to split this bucket in 2. 50% cash and 50% high quality, high dividend "value companies" (something like "SPDR MSCI USA Value UCITS ETF"). If US-yields backs up to >0.5% I'll start deploying the cash, if they back up to >1% I'll sell the "value stocks" and put it back in to the bonds.

If US would lose it's world dominance (defined as DXY below 50 for >6 months), I'll substitute US-bonds for global bonds in developed markets if they are within my criteria. Otherwise I'll go for the cash+"value stocks" option.

If the emerging market crisis strategy for bonds plays out, I'll reduce all holdings with the same ratio (max 46.1% of the total bond bucket would be invested).


### Gold

This one is fairly easy. I'm going to divide it like this;

* 75% Physical gold
* 25% Gold ETF ("paper gold")

In the paper it is suggested to put everything in physical gold. But, for tax reasons and ease of rebalancing, 25% is going in an ETF. This gives me the following:

* Physical gold - Your preferred site. I like bullionstar.com as it's founder is a Swedish veteran and I've had a great experience there. I've had a bad experience with goldmoney.com (and their fee structure sucks for smaller investors). But no recommendations, DYOR.
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

This is IMO the most interesting "bucket". This is the insurance policy that should protect you if all else fails. With the correct insurance policy you can be long with other parts of your portfolio and still have a peace of minds. 

In the paper, funds in "Eurekahedge CBOE Long Volatility Hedge Fund Index" is suggested as alternatives. As before, very hard to find information. But here I managed to dig out the components from 2019 at least. 11 funds (but only 8 different companies). One of these funds looks readily available to European investors. That's the fund "Amundi Fds Volatil Wld". That fund has been around since 2007 and must be one of the longest standing actors in this space. 

Another fund in the index is "Seeyond Volatility Strategy (NVOLACI LX Equity)" [https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610](https://www.im.natixis.com/latam/funds/seeyond-equity-volatility-strategies/lu0935232610). From what I can find, it should be possible for European investors to invest with a minimum investment of €50 000. However I have not found any way for me in Sweden to do this. But maybe it's easier in other countries. The same goes for the fund "Bréhat Class I" [https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI](https://www.vivienne-investissement.com/EN/OurFunds.php?p=BI). It's not in the long vol index (at least as of 2019), but it's a long vol fund. Minimum investment in Brehat is €100 000, but haven't found a way to invest from Sweden here either.

If you have $100 000 to invest in this bucket there's a fairly new "fund of funds" you could look into. It's called "Mutiny Fund" [https://mutinyfund.com/](https://mutinyfund.com/) and gives you exposure to funds like Logica and Artemis Capital. It is open to European investors, but you need to be an accredited investor. 

I'm planning on using Mutiny myself. Firstly because I will get exposure to many more funds. Secondly because long volatility is a complex "asset class" and Mutiny will handle the allocation between funds for me. It reduces the risk to allocate to something else then you thought (especially if you are a novice like me). "Long volatility" is easiest to achieve with options, with that comes a high risk and high expense. You'll most likely better of if you let experts handle as much as possible of this for you. 

If you don't have $100k to put in the volatility bucket, Mutiny offers a combination of exposure to S&P and long vol as well (still min $100k but you can take some of your equity exposure and put here maybe), contact them for more info. Otherwise you'll have to put everything in Amundis fund. It's most likely a fine fund, but I'd like a bit more diversification then that. The entry fee to Amundis fund is 4.5%, so you would lose that capital up front. My allocation will be this:

* 100% - "Mutiny Fund". Fee 1% + 10% performance fee.

I might however put some money in Amundis fund after a while as well.

### Conclusion

I've tried to minimize the number of vehicles in the first three buckets and maximize them in the last two. It wasn't easy, but I believe the end result is fairly close to the "Dragon portfolio". As I am investing in Swedish Krona (SEK) there is some currency risk for some of the instruments. But I can live with that.

The portfolio will then look like this:

![Figure_24](../assets/Figure_24.png)


Next, let's backtest this portfolio and decide for a strategy on how to implement it: [Backtest](../backtest)
