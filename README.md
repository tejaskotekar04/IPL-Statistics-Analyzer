<div align="center">

# 🏏 IPL Cricket Statistics Analyzer

### *Comprehensive Cricket Analytics Platform for Indian Premier League (2008-2024)*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
**[Report Bug](https://github.com/tejaskotekar04/ipl-statistics-analyzer/issues) • [Request Feature](https://github.com/tejaskotekar04/ipl-statistics-analyzer/issues)**

![IPL Dashboard Preview](https://tejaskotekar04-ipl-statistics-analyzer-app-kwqbvw.streamlit.app/)

*Interactive analysis platform for cricket enthusiasts and analysts*

</div>

---

## 🌟 Overview

**IPL Cricket Statistics Analyzer** is a powerful, interactive analytics platform built with **Streamlit** that provides comprehensive insights into 17 years of Indian Premier League cricket data (2008-2024). Analyze player performance, team statistics, match outcomes, and historical trends with intuitive visualizations.

### 💡 Why This Project?

- 🏏 **Cricket Analytics**: Deep dive into IPL statistics with professional-grade analysis
- 📊 **Massive Dataset**: 1 million+ ball-by-ball records across 1,000+ matches
- 🎯 **Multi-Dimensional**: Player stats, team performance, match insights, head-to-head comparisons
- 🚀 **Interactive**: Real-time filtering, dynamic charts, and comprehensive player search

---

## ✨ Key Features

<table>
  <tr>
    <td width="50%">
      
### 🏠 **Home Dashboard**
- 📊 Tournament overview statistics
- 🏆 Season-wise highlights
- 🎯 Quick access to key metrics
- 📈 Historical IPL trends

    </td>
    <td width="50%">
      
### 👤 **Player Analysis**
- 🏏 Batting statistics (runs, average, strike rate)
- ⚾ Bowling statistics (wickets, economy, average)
- 🔝 Top performers leaderboards
- 📊 Career progression tracking

    </td>
  </tr>
  <tr>
    <td width="50%">
      
### 🏆 **Team Analysis**
- 📈 Team performance metrics
- 🎯 Win/loss records
- 📊 Season-wise trends
- ⚔️ Head-to-head comparisons

    </td>
    <td width="50%">
      
### 📊 **Match Insights**
- 🎲 Toss impact analysis
- 🏟️ Venue statistics
- 📅 Season-wise matches
- 🏆 IPL winners history

    </td>
  </tr>
  <tr>
    <td width="50%">
      
### ⚖️ **Player Comparison**
- 🔄 Compare 2-5 players
- 📊 Side-by-side statistics
- 🏏 Batting vs Bowling comparison
- 📈 Performance visualization

    </td>
    <td width="50%">
      
### 🔍 **Advanced Filtering**
- 📅 Season-based filtering
- 🏟️ Venue-specific analysis
- 🏆 Team-wise filtering
- 🎯 Custom metrics selection

    </td>
  </tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

```bash
✅ Python 3.8 or higher
✅ pip package manager
✅ Git (optional)
```

### ⚡ Installation (3 Minutes)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/tejaskotekar04/ipl-statistics-analyzer.git
cd ipl-statistics-analyzer

# 2️⃣ Install dependencies (Only 3!)
pip install streamlit pandas numpy

# 3️⃣ Download dataset (see below ⬇️)

# 4️⃣ Validate your data
python validate_data.py

# 5️⃣ Launch the dashboard! 🚀
streamlit run app.py
```

### 📥 Dataset Setup

<div align="center">

**⚠️ Important: CSV files not included in repository**

</div>

**Step-by-step:**

1. 🔗 **Visit Kaggle**: [IPL Complete Dataset (2008-2024)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
2. 📥 **Download** the dataset (free Kaggle account required)
3. 📂 **Extract** the ZIP file - you'll get 2 CSV files:
   - `matches.csv` - Match-level data
   - `deliveries.csv` - Ball-by-ball data
4. 📁 **Place** both files in the `data/` folder

**Your folder structure should look like:**
```
ipl-statistics-analyzer/
└── data/
    ├── matches.csv
    └── deliveries.csv
```

**Validate:**
```bash
python validate_data.py
```

**Expected output:**
```
✅ matches.csv loaded successfully!
   - Rows: 1,000+
   - Columns: 20

✅ deliveries.csv loaded successfully!
   - Rows: 250,000+
   - Columns: 17
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose | Why? |
|:----------:|:-------:|:----:|
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web Framework | Rapid development, native charts |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) | Data Analysis | Powerful cricket statistics processing |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) | Computing | Fast numerical operations |

</div>

**Pure Python Implementation** - Minimal dependencies, maximum performance!

---

## 📊 Dataset Information

<div align="center">

### 🏏 IPL Complete Dataset (2008-2024)

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set)

**1M+ ball deliveries • 1,000+ matches • 17 years of cricket**

</div>

<details>
<summary>📋 <b>Click to view dataset structure</b></summary>

<br>

### matches.csv (Match-Level Data)

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Unique match identifier |
| `season` | Integer | IPL season year |
| `city` | String | Match city |
| `date` | Date | Match date |
| `match_type` | String | Type of match |
| `player_of_match` | String | Best player award |
| `venue` | String | Stadium name |
| `team1` | String | First team |
| `team2` | String | Second team |
| `toss_winner` | String | Toss winning team |
| `toss_decision` | String | Bat or Field |
| `winner` | String | Match winning team |
| `result` | String | Win type |
| `result_margin` | Integer | Win margin |
| `target_runs` | Integer | Target score |
| `target_overs` | Integer | Target overs |
| `super_over` | String | Super over flag |
| `method` | String | D/L method if applicable |
| `umpire1` | String | First umpire |
| `umpire2` | String | Second umpire |

### deliveries.csv (Ball-by-Ball Data)

| Column | Type | Description |
|--------|------|-------------|
| `match_id` | Integer | Match reference |
| `inning` | Integer | Innings number |
| `batting_team` | String | Batting team name |
| `bowling_team` | String | Bowling team name |
| `over` | Integer | Over number |
| `ball` | Integer | Ball number |
| `batter` | String | Batsman name |
| `bowler` | String | Bowler name |
| `non_striker` | String | Non-striker batsman |
| `batsman_runs` | Integer | Runs scored |
| `extra_runs` | Integer | Extra runs |
| `total_runs` | Integer | Total runs |
| `extras_type` | String | Type of extras |
| `is_wicket` | Boolean | Wicket flag |
| `player_dismissed` | String | Dismissed player |
| `dismissal_kind` | String | Dismissal type |
| `fielder` | String | Fielder name |

**Coverage:**
- **Seasons:** 2008-2024 (17 IPL seasons)
- **Matches:** 1,000+ matches
- **Deliveries:** 250,000+ ball-by-ball records
- **Teams:** All IPL franchises (past and present)
- **Players:** 800+ cricketers

</details>

---

## 💻 Project Structure

```
📦 ipl-statistics-analyzer/
┣ 📂 data/
┃ ┣ 📄 matches.csv              # Match data (download separately)
┃ ┗ 📄 deliveries.csv           # Ball-by-ball data (download separately)
┣ 📂 pages/                      # Multi-page Streamlit app
┃ ┣ 📄 player_analysis.py       # Player statistics (117 lines)
┃ ┣ 📄 team_analysis.py         # Team performance (112 lines)
┃ ┣ 📄 match_insights.py        # Match analytics (83 lines)
┃ ┗ 📄 compare_players.py       # Player comparison (76 lines)
┣ 📄 app.py                      # Home dashboard (106 lines)
┣ 📄 analysis.py                 # Analysis functions (394 lines)
┣ 📄 visualizations.py           # Chart functions (95 lines)
┣ 📄 validate_data.py            # Data validation (114 lines)
┣ 📄 requirements.txt            # Dependencies (only 3)
┣ 📄 README.md                   # You are here! 📍
```

**Code Stats:** ~1,000 lines • 9 files • 30+ functions • Each page < 120 lines

---

## 🎨 Usage Guide

### 🧭 Navigation

<div align="center">

**Use the sidebar to navigate between pages** 👈

</div>

```
🏠 Home              → Tournament overview & highlights
👤 Player Analysis   → Batting & bowling statistics
🏆 Team Analysis     → Team performance & trends
📊 Match Insights    → Toss, venue, season analysis
⚖️ Compare Players   → Multi-player comparison
```

### 🎛️ Interactive Features

- **Sliders** 🎚️: Adjust display count (5-20 items)
- **Dropdowns** 📋: Filter by season, team, player
- **Multi-Select** 🔢: Choose multiple players for comparison
- **Real-time Updates** 🔄: Charts update automatically

---

## 📈 Cricket Insights You'll Discover

<table>
  <tr>
    <td align="center" width="33%">
      <h3>🏏 Batting</h3>
      <ul align="left">
        <li>Top run scorers</li>
        <li>Best strike rates</li>
        <li>Highest averages</li>
        <li>Most boundaries</li>
      </ul>
    </td>
    <td align="center" width="33%">
      <h3>⚾ Bowling</h3>
      <ul align="left">
        <li>Top wicket takers</li>
        <li>Best economy rates</li>
        <li>Best bowling averages</li>
        <li>Maiden overs</li>
      </ul>
    </td>
    <td align="center" width="33%">
      <h3>🏆 Teams</h3>
      <ul align="left">
        <li>Win/loss records</li>
        <li>Toss impact</li>
        <li>Venue performance</li>
        <li>Head-to-head stats</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🏆 Project Highlights

<div align="center">

### Why This Project Stands Out

</div>

```diff
+ 🏏 Sports Analytics: Real cricket data analysis with professional insights
+ 📊 Large Scale: Processing 1M+ ball-by-ball records efficiently
+ 🎯 Multi-Dimensional: 5 different analysis perspectives
+ 💡 Interactive: Dynamic filtering and real-time visualizations
+ 🔧 Clean Code: Modular architecture, each component < 120 lines
+ 📚 Well-Documented: Comprehensive README and code comments
+ ✅ Production Ready: Deployed and optimized for performance
```

**Perfect for:**
- 📄 **Portfolio**: Demonstrates data analysis skills with real sports data
- 🎓 **Learning**: Hands-on practice with large datasets
- 🏏 **Cricket Fans**: Explore IPL statistics interactively
- 💼 **Interviews**: Great project for sports analytics discussions

---

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions are **greatly appreciated**.

1. 🍴 Fork the Project
2. 🌿 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. ✅ Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 📊 Code Quality

<div align="center">

![Code Quality](https://img.shields.io/badge/Code%20Quality-A+-brightgreen?style=for-the-badge)
![Documentation](https://img.shields.io/badge/Documentation-Complete-blue?style=for-the-badge)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-success?style=for-the-badge)

</div>

**Features:**
- ✅ Modular architecture
- ✅ Comprehensive error handling
- ✅ Detailed comments
- ✅ Consistent code style
- ✅ Reusable functions
- ✅ Pure Streamlit (no matplotlib)

---

## 🗺️ Roadmap

<details>
<summary>🚀 <b>Planned Features</b> (Click to expand)</summary>

<br>

- [ ] 📊 Advanced statistical analysis (moving averages, trends)
- [ ] 🤖 Player performance prediction models
- [ ] 📈 Season comparison charts
- [ ] 🏆 Fantasy cricket team suggestions
- [ ] 📧 Email alerts for player milestones
- [ ] 🌙 Dark mode support
- [ ] 📱 Mobile-responsive improvements
- [ ] 🔔 Live match integration (future seasons)
- [ ] 📊 Custom dashboard builder
- [ ] 🌍 Multi-language support

</details>

---

## 📧 Contact & Support

<div align="center">

### 💬 Get in Touch

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tejaskotekar04)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tejas-kotekar-0302b6227/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tejaskotekar04@gmail.com)

**Questions? Suggestions? Found a bug?**

[Open an Issue](https://github.com/tejaskotekar04/ipl-statistics-analyzer/issues)

</div>

---

## 🙏 Acknowledgments

<div align="center">

**Special Thanks To:**

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set) • Dataset Provider

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/) • Framework

[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/) • Data Processing

[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/) • Numerical Computing

**IPL & BCCI** • For the amazing tournament

</div>

---

## 📚 Additional Resources

<div align="center">

**Learn More:**

[Streamlit Docs](https://docs.streamlit.io/) • [Pandas Guide](https://pandas.pydata.org/docs/) • [NumPy Documentation](https://numpy.org/doc/) • [Cricket Analytics](https://www.espncricinfo.com/)

</div>

---

<div align="center">

## ⭐ Show Your Support

**If you're a cricket fan or find this project useful, please give it a star!**

[![Star](https://img.shields.io/github/stars/tejaskotekar04/ipl-statistics-analyzer?style=social)](https://github.com/tejaskotekar04/ipl-statistics-analyzer)

---

### 🏏 Ready to analyze IPL cricket data?

**[Get Started Now](#-quick-start) • [View Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) • [Report Issues](https://github.com/tejaskotekar04/ipl-statistics-analyzer/issues)**

---

**Built with ❤️ for Cricket by [Your Name](https://github.com/tejaskotekar04)**

*Bringing statistical analysis to the gentleman's game* 🏏

---

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer)

</div>
