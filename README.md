# MonteCarloDDLN

**Monte Carlo симуляция для Т-Супермаркетов (маскот + ежедневная лента)**

> Реалистичная модель оценки влияния маскота и ежедневной ленты "найди уникальное" на repeat purchase rate и LTV нового e-grocery сервиса.

---

## 📊 Результаты (30 дней, 30,000 симуляций)

| Метрика                  | Baseline (новый сервис) | С маскотом          | Uplift |
|--------------------------|-------------------------|---------------------|--------|
| % с 2+ заказами          | 46.2%                   | 55.1%               | +19%   |
| % с 3+ заказами          | 31.2%                   | 41.8%               | +34%   |
| Среднее кол-во заказов   | 3.6                     | 4.8                 | +35%   |
| Revenue (₽)              | 6,338                   | 8,583               | +35%   |
| **Net Profit (₽)**       | **1,775**               | **2,403**           | **+35%** |

---

## 🎯 Главный вывод

**Маскот + ежедневная лента "найди уникальное" дают +35% к profit за первые 30 дней** за счёт роста повторных покупок — **без единой скидки и подарка**.

---

## 📈 Модель

### Параметры

- **AOV**: 1,770 ₽ (прямо из исследования ЮKassa)
- **Margin**: 28% (отраслевой стандарт e-grocery)
- **Baseline**: skew в low-frequency (8% daily, 40% monthly, 20% rare) — реалистично для **нового сервиса**
- **Эффект маскота**: 30% переход в более высокий bucket (консервативно)
- **Случайность**: нормальное распределение вокруг `mean_orders` (настоящий Monte Carlo)

### Почему это реалистично

| Параметр | Значение | Обоснование |
|----------|----------|-------------|
| Baseline 46.2% с 2+ заказами | Реалистично | Для нового сервиса 40-55% — нормальный показатель |
| +35% к profit | Консервативно | В рамках реальных кейсов (+25-40%) |
| 30% transition prob | Консервативно | Duolingo widget дал +50-60%, мы взяли в 1.5-2 раза ниже |

---

## 📚 Доказательная база

| Параметр | Значение | Источник | Ссылка |
|----------|----------|----------|--------|
| AOV / Распределение | 1,770 ₽ / 19% daily... | ЮKassa (май 2025) | [retail.ru](https://www.retail.ru/news/kazhdyy-pyatyy-rossiyanin-zakazyvaet-produkty-onlayn-ezhednevno-issledovanie-yuk-29-maya-2025-265237/) |
| Duolingo widget | +50-60% к активности | Duolingo Blog (2023) | [blog.duolingo.com](https://blog.duolingo.com/widget-feature/) [duo gamification] (https://www.strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo) |
| Виджеты → retention | +15-30% | MindK / Localytics (2025) | [mindk.com](https://www.mindk.com/blog/how-to-improve-user-engagement-in-your-app/) |
| Parasocial relationships | +20-40% к лояльности | ScienceDirect / PMC (2021-2023) | [scienceirect.com](https://www.sciencedirect.com/science/article/pii/S2772503023000178) |
| Реальные кейсы | +25-40% LTV | Duolingo, Calm, Headspace | Официальные блоги + исследования |

---

## 🚀 Как запустить

```bash
pip install numpy pandas matplotlib seaborn tqdm
python3 tbank_monte_carlo_true.py
```

**Требования:**
- Python 3.8+
- numpy, pandas, matplotlib, seaborn, tqdm

---

## 📁 Структура репозитория

```
MonteCarloDDLN/
├── README.md
├── tbank_monte_carlo_true.py      # Основной код (настоящий Monte Carlo)
├── tbank_monte_carlo_scenarios.py # Два сценария (оптимистичный vs консервативный)
├── tbank_monte_carlo_realistic.py # Консервативный сценарий
├── tbank_scenarios_comparison.png # Графики сравнения
└── tbank_monte_carlo_true.png     # Графики Monte Carlo
```

---

## 📄 Лицензия

MIT License — свободное использование для коммерческих и некоммерческих целей.

---

## 👤 Автор

Сделано для Т-Банк (питч по кейсу Т-Супермаркеты).

---

*Последнее обновление: апрель 2026*
