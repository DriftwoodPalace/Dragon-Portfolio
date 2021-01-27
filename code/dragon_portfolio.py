import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

### PORTFOLIO
# 24% EQUITY
# 18% FIXED INCOME
# 19% GOLD
# 18% COMDTY TREND/GLOBAL MACRO
# 21% LONG VOL

### EQUITY
# 50% GLOBAL, 12% of tot
# 25% USA, 6% of tot
# 25 OMXS30, 6% of tot

### FIXED INCOME
# US TSY 50%, 9% of tot
# US NOTES, 25% 4.5% of tot
# SEK BONDS, 25%, 4.5% of tot

### GOLD
# GLD 90%, 17.1% of tot
# GDX 10%, 1.9 of tot

### COMDTY TREND+GLOBAL MACRO
# LYNX 75%, 13.5% of tot
# SEB ASSET SELECTION C LUX 25%, 4.5% of tot
# IPM SYSTEMATIC MACRO UCITS 0%
# NORDKINN 0%

### LONG VOL
# AMUNDI 100%, 21% of tot

# LATEST DATE (START MONTH) 2007-11, AMUNDI

### GLOBAL VARIABLES / DATA ###
start_date = '2007-11'
years = 13.167
global_data_raw = pd.read_csv('SPP_aktiefond_global.csv')
global_data_raw = global_data_raw.set_index('Date')
global_data = pd.DataFrame(global_data_raw.loc[start_date:])
us_data_raw = pd.read_csv('SPP_aktiefond_USA.csv')
us_data_raw = us_data_raw.set_index('Date')
us_data = pd.DataFrame(us_data_raw.loc[start_date:])
avanza_zero_raw = pd.read_csv('Avanza_zero.csv')
avanza_zero_raw = avanza_zero_raw.set_index('Date')
avanza_zero = pd.DataFrame(avanza_zero_raw.loc[start_date:])
tlt_raw = pd.read_csv('TLT_SEK.csv')
tlt_raw = tlt_raw.set_index('Date')
tlt = pd.DataFrame(tlt_raw.loc[start_date:])
SEB_kortranta_raw = pd.read_csv('SEB_kortrantefond_USD_sek.csv')
SEB_kortranta_raw = SEB_kortranta_raw.set_index('Date')
SEB_kortranta = pd.DataFrame(SEB_kortranta_raw.loc[start_date:])
AMF_rantefond_raw = pd.read_csv('AMF_rantefond_long.csv')
AMF_rantefond_raw = AMF_rantefond_raw.set_index('Date')
AMF_rantefond = pd.DataFrame(AMF_rantefond_raw.loc[start_date:])
gld_raw = pd.read_csv('GLD_SEK.csv')
gld_raw = gld_raw.set_index('Date')
gld = pd.DataFrame(gld_raw.loc[start_date:])
gdx_raw = pd.read_csv('GDX_SEK.csv')
gdx_raw = gdx_raw.set_index('Date')
gdx = pd.DataFrame(gdx_raw.loc[start_date:])
lynx_raw = pd.read_csv('Lynx.csv')
lynx_raw = lynx_raw.set_index('Date')
lynx = pd.DataFrame(lynx_raw.loc[start_date:])
SEB_selection_raw = pd.read_csv('SEB_asset_selection_c.csv')
SEB_selection_raw = SEB_selection_raw.set_index('Date')
SEB_selection = pd.DataFrame(SEB_selection_raw.loc[start_date:])
amundi_raw = pd.read_csv('Amundi_long_SEK.csv')
amundi_raw = amundi_raw.set_index('Date')
amundi = pd.DataFrame(amundi_raw.loc[start_date:])
# dfs = [global_data, us_data, avanza_zero, tlt, SEB_kortranta, AMF_rantefond, gld, \
#         gdx, lynx, SEB_selection, amundi]
dfs = [global_data, avanza_zero, tlt, AMF_rantefond, gld, \
        lynx, SEB_selection, amundi]
# cols = ['Global', 'US', 'Ava_Z', 'TLT', 'SEB_kort', 'AMF_ranta', 'GLD',\
#     'GDX', 'Lynx', 'SEB_select', 'Amundi']
cols = ['Global', 'Ava_Z', 'TLT', 'AMF_ranta', 'GLD',\
    'Lynx', 'SEB_select', 'Amundi']
data = pd.concat(dfs, axis=1).reset_index()
data = data.set_index('Date')
data.columns = cols
# initial_weight = np.array([0.18,0.06,0.09,0.09,\
#         0.19, 0.135, 0.045, 0.21])
# initial_weight = np.array([0.18,0.00,0.06,0.09,0.00,0.09,\
#         0.19, 0.00, 0.135, 0.045, 0.21])
# 60/40
initial_weight = np.array([0.6, 0, 0, 0.4, 0, 0,\
        0,0])
### GLOBAL VARIABLES / DATA ###

def get_data_weight_every_month():
    # Balansera varje mån
    monthly_returns = data.pct_change()
    
    # returns = data/data.shift(1)
    monthly_returns_portfolio_mean = monthly_returns.mean()
    allocated_monthly_returns = (initial_weight * monthly_returns_portfolio_mean)
    portfolio_return = np.sum(allocated_monthly_returns)
    # calculate portfolio monthly returns, rebalanserar varje månad (ggr monthly_returns med matris)
    monthly_returns['portfolio_monthly_returns'] = monthly_returns.dot(initial_weight)
    monthly_returns.to_csv('monthly_returns.csv')
    monthly_returns['portfolio_monthly_returns_cum'] = (1+monthly_returns['portfolio_monthly_returns']).cumprod()
    monthly_returns['portfolio_monthly_returns_cum'] = monthly_returns['portfolio_monthly_returns_cum'].fillna(1)
    monthly_returns['portfolio_monthly_returns_cum'] *= 100
    # calc_risk(monthly_returns)

    # Cumulative_returns_monthly = (1+monthly_returns).cumprod()
    # Cumulative_returns_monthly.to_csv('initial_weight.csv')
    # Cumulative_returns_monthly['portfolio_monthly_returns'].plot()
    # matrix_covariance_portfolio = monthly_returns.iloc[:,:-1]
    # matrix_covariance_portfolio = (matrix_covariance_portfolio.cov())*12
    # portfolio_variance = np.dot(initial_weight.T,np.dot(matrix_covariance_portfolio, initial_weight))

    #standard deviation (risk of portfolio)
    # portfolio_standard_deviation = np.sqrt(portfolio_variance)
    # portfolio_risk = []
    # sharpe_ratio_port = []
    # portfolio_risk.append(portfolio_standard_deviation)
    # #sharpe_ratio (risk free rate = 0)
    # RF = 0
    # sharpe_ratio = (((portfolio_return)- RF)/portfolio_standard_deviation)
    # print(sharpe_ratio*12)
    # sharpe_ratio_port.append(sharpe_ratio)
    # portfolio_risk = np.array(portfolio_risk)
    # print(portfolio_standard_deviation)
    # sharpe_ratio_port = np.array(sharpe_ratio_port)
    # print(Cumulative_returns_monthly.tail(5))
    # cagr = (data.iloc[-1]/data.iloc[0])**(1/years) - 1
    # cov = returns.cov()

    # exp_return = []
    # sigma = []
    # for _ in range(20000):
    #   w = random_weights(len(cols))
    #   exp_return.append(np.dot(w, cagr.T))
    #   sigma.append(np.sqrt(np.dot(np.dot(w.T, cov), w)))

    # plt.plot(sigma, exp_return, 'ro', alpha=0.1)
    # plt.show()
    return monthly_returns

def get_data_weight_every_x_month(rebalance_every):
    # Rebalansera var X mån
    monthly_returns = data.pct_change()
    # monthly_returns = monthly_returns.drop('portfolio_monthly_returns', 1)
    weighted_portfolio = pd.DataFrame(monthly_returns.iloc[0])
    # Starta med ett visst värde representerat av vikten, tänk i pengar
    weighted_portfolio = weighted_portfolio.fillna(100).transpose()*initial_weight
    # X månader framåt
    for i in range(len(monthly_returns.index)):
        if i == 0:
            weighted_portfolio['portfolio_monthly_returns_cum'] = weighted_portfolio.sum(axis=1)
        elif i % (rebalance_every) == 0:
            # Rebalance then multiply
            # Räkna först ut hur stor vikt positionen har nu
            new_weight = weighted_portfolio.iloc[-1:].copy(deep=True)
            for name in cols:
                last_val = new_weight[name].iat[0]
                # Viktning av totala:
                new_weight[name] = new_weight[name].iat[0] / new_weight['portfolio_monthly_returns_cum'].iat[0]
                # Skillnad att justera:
                new_weight[name] = weighted_portfolio[name].iat[0] - new_weight[name].iat[0]*100
                # Justera värde:
                new_weight[name] = last_val + (new_weight['portfolio_monthly_returns_cum'].iat[0] * new_weight[name].iat[0]) / 100
                # % förändring på nytt värde
                new_weight[name] = new_weight[name].iat[0] * (monthly_returns[name].iat[i]+1)
            new_weight = new_weight.drop('portfolio_monthly_returns_cum', 1)
            new_weight['portfolio_monthly_returns_cum'] = new_weight.sum(axis=1)
            weighted_portfolio = weighted_portfolio.append(new_weight, ignore_index=True)
        else:
            to_append = weighted_portfolio.drop('portfolio_monthly_returns_cum', 1)
            to_append = to_append.iloc[-1]
            to_append = to_append * (monthly_returns.iloc[i]+1)
            to_append['portfolio_monthly_returns_cum'] = to_append.sum()
            weighted_portfolio = weighted_portfolio.append(to_append, ignore_index=True)
    weighted_portfolio = weighted_portfolio.set_index(monthly_returns.index)
    weighted_portfolio.to_csv('weighted.csv')
    # plt.plot(weighted_portfolio['portfolio_monthly_returns_cum'])
    # plt.show()
    weighted_portfolio['portfolio_monthly_returns'] = weighted_portfolio['portfolio_monthly_returns_cum'].pct_change()
    calc_risk(weighted_portfolio)
    return weighted_portfolio

def get_data_every_pct(pct):
    ### Vikta om vid +-X%
    monthly_returns = data.pct_change()
    dynamic_portfolio = pd.DataFrame(monthly_returns.iloc[0])
    # Starta med ett visst värde representerat av vikten, tänk i pengar
    dynamic_portfolio = dynamic_portfolio.fillna(100).transpose()*initial_weight
    # weight_dict = {'Global':0.18, 'US':0.00, 'Ava_Z':0.06, 'TLT':0.09, 'SEB_kort':0.00, \
    #     'AMF_ranta':0.09, 'GLD':0.19, 'GDX':0.0, 'Lynx':0.135, 'SEB_select':0.045, 'Amundi':0.21}
    weight_dict = {'Global':0.18, 'Ava_Z':0.06, 'TLT':0.09, \
        'AMF_ranta':0.09, 'GLD':0.19, 'Lynx':0.135, 'SEB_select':0.045, 'Amundi':0.21}
    # Kolla viktning
    transactions = 0
    for i in range(len(monthly_returns.index)):
        if i == 0:
            dynamic_portfolio['portfolio_monthly_returns_cum'] = dynamic_portfolio.sum(axis=1)
        else:
            # Kolla vikt
            old_weight = dynamic_portfolio.iloc[-1:].copy(deep=True)
            new_weight_all = dynamic_portfolio.iloc[-1:].copy(deep=True)
            tickers_down = []
            tickers_up = []
            stop = False
            for name in cols:
                last_val = old_weight[name].iat[0]
                # Viktning av totala:
                old_weight[name] = (old_weight[name].iat[0] / 100)
                # Nya vikter av totalen (har ju ökat från 100)
                # Skillnad att justera:
                new_weight_all[name] = (weight_dict[name]*old_weight['portfolio_monthly_returns_cum'].iat[0]/100) 
                # Kolla om någon är +-X% av sin egna viktning
                if old_weight[name].iat[0] >= new_weight_all[name].iat[0]*(1+pct/100):
                    tickers_down.append(name)
                    stop = True
                # elif new_weight[name].iat[0] <= weight_dict[name]*0.9:
                elif old_weight[name].iat[0] <= new_weight_all[name].iat[0]*(1-pct/100):
                    tickers_up.append(name)
                    stop = True
                # Ändra new_weight till det som ska justeras istället för totalvärdet
                new_weight_all[name] = new_weight_all[name] - old_weight[name]
            if stop:
                df_copy = old_weight.copy(deep=True)
                df_copy = df_copy.drop('portfolio_monthly_returns_cum', 1)
                df_copy_all = new_weight_all.copy(deep=True)
                df_copy_all = df_copy_all.drop('portfolio_monthly_returns_cum', 1)
                # Börja med de som ska justeras ner och justera med största värdet i sorterade listan
                # Om det blir mindre än 0 ta bort det. Ordning ska inte spela någon roll då.
                to_change_up = df_copy_all.sort_values(by=i-1, axis = 1, ascending=False)
                tickers_up_sort = list(to_change_up.columns)
                while len(tickers_down) > 0:
                    left_to_change = df_copy_all[tickers_down[0]].iat[0]
                    # Kolla om det som blir kvar om största värdet från andra listan tas > 0
                    # Ta det inom 1% ifall det blir avrundningsfel
                    if left_to_change + df_copy_all[tickers_up_sort[0]].iat[0] < -0.01:
                        # Justera
                        # Ändra det stora värdet
                        df_copy[tickers_down[0]] = df_copy[tickers_down[0]].iat[0] - df_copy_all[tickers_up_sort[0]].iat[0]
                        # Justera värdet som ändrades
                        df_copy[tickers_up_sort[0]] = df_copy[tickers_up_sort[0]].iat[0] + df_copy_all[tickers_up_sort[0]].iat[0]
                        # Räkna ut vad som är kvar att justera och justera
                        df_copy_all[tickers_down[0]] = df_copy_all[tickers_down[0]].iat[0] + df_copy_all[tickers_up_sort[0]].iat[0]
                        # Nollställ den som användes för att justera
                        df_copy_all[tickers_up_sort[0]] = df_copy_all[tickers_up_sort[0]].iat[0] - df_copy_all[tickers_up_sort[0]].iat[0]
                        # Om detta även ska justeras upp, ta bort därifrån
                        if tickers_up_sort[0] in tickers_up:
                            tickers_up.remove(tickers_up_sort[0])
                        # Det behöver inte längre justeras, så kan tas bort
                        tickers_up_sort.pop(0)
                        # Räkna en transaktion för den som tas bort
                        transactions += 1
                    # Om de är lika stora, ta bort båda
                    else:
                        # Justera det som är kvar från största värdet i andra listan
                        # Ändra det stora värdet med sin egna rest
                        df_copy[tickers_down[0]] = df_copy[tickers_down[0]].iat[0] + df_copy_all[tickers_down[0]].iat[0]
                        # Justera största värdet i andra listan med samma summma
                        df_copy[tickers_up_sort[0]] = df_copy[tickers_up_sort[0]].iat[0] - df_copy_all[tickers_down[0]].iat[0]
                        # Nollställ den som användes för att justera
                        df_copy_all[tickers_up_sort[0]] = df_copy_all[tickers_up_sort[0]].iat[0] + df_copy_all[tickers_down[0]].iat[0]
                        # Räkna ut vad som är kvar att justera och justera, ta förändringsvärdet först
                        df_copy_all[tickers_down[0]] = df_copy_all[tickers_down[0]].iat[0] - df_copy_all[tickers_down[0]].iat[0]
                        # Resten är nu 0 och kan tas bort och gå på nästa värde
                        tickers_down.pop(0)
                        # Räkna två transaktioner för den som tar bort & den det justeras med
                        transactions += 2
                # Ta nu de som ska justeras upp (om de finns)
                to_change_down = df_copy_all.sort_values(by=i-1, axis = 1)
                tickers_down_sort = list(to_change_down.columns)
                while len(tickers_up) > 0:
                    left_to_change = df_copy_all[tickers_up[0]].iat[0]
                    if left_to_change + df_copy_all[tickers_down_sort[0]].iat[0] > 0.01:
                        df_copy[tickers_up[0]] = df_copy[tickers_up[0]].iat[0] - df_copy_all[tickers_down_sort[0]].iat[0]
                        df_copy[tickers_down_sort[0]] = df_copy[tickers_down_sort[0]].iat[0] + df_copy_all[tickers_down_sort[0]].iat[0]
                        df_copy_all[tickers_up[0]] = df_copy_all[tickers_up[0]].iat[0] + df_copy_all[tickers_down_sort[0]].iat[0]
                        df_copy_all[tickers_down_sort[0]] = df_copy_all[tickers_down_sort[0]].iat[0] - df_copy_all[tickers_down_sort[0]].iat[0]
                        tickers_down_sort.pop(0)
                        transactions += 1
                    else:
                        df_copy[tickers_up[0]] = df_copy[tickers_up[0]].iat[0] + df_copy_all[tickers_up[0]].iat[0]
                        df_copy[tickers_down_sort[0]] = df_copy[tickers_down_sort[0]].iat[0] - df_copy_all[tickers_up[0]].iat[0]
                        df_copy_all[tickers_down_sort[0]] = df_copy_all[tickers_down_sort[0]].iat[0] + df_copy_all[tickers_up[0]].iat[0]
                        df_copy_all[tickers_up[0]] = df_copy_all[tickers_up[0]].iat[0] - df_copy_all[tickers_up[0]].iat[0]
                        tickers_up.pop(0)
                        transactions += 2
                
                # Vi har nu de nya vikterna (df_copy) och kan multiplicera de med månadsförändringen
                to_append = df_copy * (monthly_returns.iloc[i]+1) *100
                to_append['portfolio_monthly_returns_cum'] = to_append.iloc[0].sum()
                dynamic_portfolio = dynamic_portfolio.append(to_append, ignore_index=True)
            else:
                to_append = dynamic_portfolio.drop('portfolio_monthly_returns_cum', 1)
                to_append = to_append.iloc[-1]
                to_append = to_append * (monthly_returns.iloc[i]+1)
                to_append['portfolio_monthly_returns_cum'] = to_append.sum()
                dynamic_portfolio = dynamic_portfolio.append(to_append, ignore_index=True)
                
    dynamic_portfolio['portfolio_monthly_returns'] = dynamic_portfolio['portfolio_monthly_returns_cum'].pct_change()
    print('Number of transactions:')
    print(transactions)
    dynamic_portfolio = dynamic_portfolio.set_index(data.index)
    calc_risk(dynamic_portfolio)
    # print(dynamic_portfolio)
    return dynamic_portfolio
        
def random_weights(n):
    k = np.random.rand(n)
    return k / sum(k)

def calc_risk(df):
    # Genomsnittlig årlig avkastning
    print(df)
    cagr = (df['portfolio_monthly_returns_cum'].iloc[-1]/df['portfolio_monthly_returns_cum'].iat[0])**(1/years) - 1
    print('ÅRLIG AVKASTNING')
    print(cagr)
    # Std dev & sharpe
    std_dev = df['portfolio_monthly_returns'].std()
    print('STD DEV:')
    print(std_dev*12)
    mean_return = df['portfolio_monthly_returns'].mean()
    sharpe_ratio = mean_return / std_dev
    sharpe_ratio_yearly = sharpe_ratio*12
    print('SHARPE RATIO:')
    print(sharpe_ratio_yearly)

    # Max yearly drawdown
    # Räknar ut mavärdet som varit från start
    roll_max = df['portfolio_monthly_returns_cum'].cummax()
    # Räknar ut maximala nedgången från maxvärdet den dagen.
    monthly_drawdown = df['portfolio_monthly_returns_cum']/roll_max - 1
    max_monthly_drawdown = monthly_drawdown.cummin()
    df['monthly_drawdown'] = monthly_drawdown
    print('MAX DRAWDOWN:')
    print(max_monthly_drawdown.min())
    create_figure(df, 'portfolio_monthly_returns_cum', 'Dragon portfolio (reweight every 10%)')
    create_figure(df, 'monthly_drawdown', 'Dragon portfolio, drawdowns (reweight every 10%)')
    # max_monthly_drawdown.plot()
    # plt.show()

def fire(df):
    print(df)
    start_val = 5000000
    withdrawal_per_year = start_val/25
    # CPI start 2007-11
    cpi = [1.00, 1.025, 1.018, 1.037, 1.062, 1.061, 1.062, 1.060, 1.061, 1.076, 1.096, 1.117, 1.137, 1.139]
    money_left = [start_val]
    num = 0
    for row in df.iterrows():
        if num == 0:
            num += 1
        elif num % 12 == 0:
            new_withdrawal_sum = withdrawal_per_year*cpi[int(num/12)]
            money_left.append((money_left[num-1]-new_withdrawal_sum) * (1+row[-1][-2]))
            num += 1
        else:
            money_left.append(money_left[num-1] * (1+row[-1][-2]))
            num += 1
    df['money_left'] = money_left
    # Calculate expenses per year
    expenses = [withdrawal_per_year]
    num1 = 0
    for i in range(len(money_left)):
        if i == 0:
            pass
        elif i % 12 == 0:
            to_add = expenses[num1] * cpi[num1+1]
            expenses.append(to_add)
            num1 += 1
        else:
            to_add = expenses[num1] * cpi[num1]
            expenses.append(to_add)
    print(money_left[-1]/money_left[0])
    df['expenses'] = expenses
    df['expenses'] *= 25
    create_figure(df, 'money_left', 'Money left (start with 25X yearly expenses) - 60/40', 'expenses', '25X yearly expenses')
    return


def create_figure(df, series_name, label, series_name2=False, label2=False):
    fig, ax1 = plt.subplots(figsize=(10, 8))
    x_start = len(df.index) % 79 - 1
    if x_start < 0:
        x_start = 0
        # x_start = len(df.index) // 53 - 1
    # ax1.set_ylabel('Andel över sitt 200 Day Moving Average', color=color)
    ax1.plot(df.index[x_start:], df[series_name].iloc[x_start:], label=label)
    if series_name2:
        ax1.plot(df.index[x_start:], df[series_name2].iloc[x_start:], label=label2)
    # ax1.tick_params(axis='y')
    every_nth = len(df.index) // 79
    num = 2
    for n, lab in enumerate(ax1.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            lab.set_visible(False)
            num += 1
        else:
            if num % 3 == 0:
                lab.set_visible(False)
                num += 1
    for n, tick in enumerate(ax1.axes.get_xticklines()):
        if n % every_nth != 0:
            tick.set_visible(False)
    ax1.set_xticklabels(df.index[x_start:], rotation=40, ha='right')
    ax1.set_xlim(df.index[x_start], df.index[-1])
    ax1.tick_params(axis='x', rotation=40)
    ax1.legend()
    plt.title(label)
    # ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    # ax1.xaxis_date()
    # ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # ax1.xaxis.set_major_locator(mtick.MaxNLocator(30))

    plt.show()
    # name = str(datetime.now().strftime('%Y-%m-%d') + '_' + label + '.jpg')
    # fig.savefig(name, dpi=250)
    plt.close(fig)

fire(get_data_weight_every_month())
# get_data_weight_every_month()
# get_data_weight_every_x_month(12)
# get_data_every_pct(10)