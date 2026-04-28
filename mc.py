from tqdm import tqdm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.size'] = 11

print("=" * 80)
print("MONTE CARLO ДЛЯ Т-СУПЕРМАРКЕТОВ (МАСКОТ)")
print("=" * 80)

AOV = 1770
MARGIN = 0.28
N_SIM = 30000
DAYS = 30

buckets = {
    'daily':   {'prob': 0.08, 'mean_orders': 20, 'std': 5},
    'weekly':  {'prob': 0.18, 'mean_orders': 6,  'std': 2},
    'monthly': {'prob': 0.40, 'mean_orders': 2,  'std': 1},
    'rare':    {'prob': 0.20, 'mean_orders': 1,  'std': 0.5},
    'special': {'prob': 0.14, 'mean_orders': 1,  'std': 0.5}
}

TRANSITION_PROB = 0.30

def simulate(with_mascot=False, seed=42):
    np.random.seed(seed)
    results = []
    for _ in tqdm(range(N_SIM), desc="Симуляция"):
        r = np.random.rand()
        cum = 0
        current = None
        for b, d in buckets.items():
            cum += d['prob']
            if r <= cum:
                current = b
                break
        if with_mascot:
            if np.random.rand() < TRANSITION_PROB:
                order = list(buckets.keys())
                idx = order.index(current)
                if idx > 0:
                    current = order[idx - 1]
        
        # СЛУЧАЙНОЕ количество заказов
        mean = buckets[current]['mean_orders']
        std = buckets[current]['std']
        orders = max(1, int(np.random.normal(mean, std)))
        
        results.append({
            'bucket': current,
            'orders': orders,
            'has_2plus': orders >= 2,
            'has_3plus': orders >= 3,
            'revenue': orders * AOV,
            'profit': orders * AOV * MARGIN
        })
    return pd.DataFrame(results)

df_base = simulate(with_mascot=False, seed=42)
df_mascot = simulate(with_mascot=True, seed=123)

base_2 = df_base['has_2plus'].mean()
base_3 = df_base['has_3plus'].mean()
base_ord = df_base['orders'].mean()
base_rev = df_base['revenue'].mean()
base_prf = df_base['profit'].mean()

msc_2 = df_mascot['has_2plus'].mean()
msc_3 = df_mascot['has_3plus'].mean()
msc_ord = df_mascot['orders'].mean()
msc_rev = df_mascot['revenue'].mean()
msc_prf = df_mascot['profit'].mean()

up_2 = (msc_2 / base_2 - 1) * 100
up_3 = (msc_3 / base_3 - 1) * 100
up_ord = (msc_ord / base_ord - 1) * 100
up_rev = (msc_rev / base_rev - 1) * 100
up_prf = (msc_prf / base_prf - 1) * 100

print("=" * 85)
print("📊 РЕЗУЛЬТАТЫ (MONTE CARLO — 30 дней)")
print("=" * 85)

tbl = pd.DataFrame({
    'Метрика': ['% с 2+ заказами', '% с 3+ заказами', 'Среднее кол-во заказов',
                'Revenue (₽)', 'Net Profit (₽)'],
    'Baseline\n(новый сервис)': [f"{base_2*100:.1f}%", f"{base_3*100:.1f}%", f"{base_ord:.1f}",
                                 f"{base_rev:,.0f}", f"{base_prf:,.0f}"],
    'С маскотом\n(ежедневная лента)': [f"{msc_2*100:.1f}%", f"{msc_3*100:.1f}%", f"{msc_ord:.1f}",
                                       f"{msc_rev:,.0f}", f"{msc_prf:,.0f}"],
    'Uplift': [f"+{up_2:.0f}%", f"+{up_3:.0f}%", f"+{up_ord:.0f}%",
               f"+{up_rev:.0f}%", f"+{up_prf:.0f}%"]
})
print(tbl.to_string(index=False))
print("=" * 85)
