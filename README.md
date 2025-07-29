# ⚽ Soccer Impact Tracker

A comprehensive analytics dashboard for Premier League football data, built with Streamlit and Python. This project provides detailed insights into match statistics, team performance, and player analytics for the 2023/24 Premier League season.

## 🚀 Live Demo

**Streamlit App**: [Premier League Stats Tracker](https://premierleague-stats-tracker-dg8a4vyycb6pkhpfyfrjwd.streamlit.app/)

## 📊 Features

### Dashboard Views
- **Match Summary**: Goals per matchday analysis and common scorelines
- **Team Statistics**: Offensive and defensive performance metrics
- **Top Scorers**: Player performance and goal-scoring statistics

### Key Analytics
- **Match Analysis**: Goals per matchday trends and most common scorelines
- **Team Performance**: Goals scored vs league points correlation
- **Offense vs Defense**: Average goals scored vs conceded analysis
- **Player Statistics**: Top goal scorers and their contributions
- **Goal Difference Analysis**: Correlation between goal difference and final points

### Interactive Visualizations
- Dynamic charts using Plotly
- Responsive design optimized for various screen sizes
- Real-time data filtering and exploration

## 🏗️ Project Structure

```
soccer-impact-tracker/
├── data/                          # Data files and application
│   ├── app.py                     # Main Streamlit application
│   ├── requirements.txt           # Python dependencies
│   ├── matches_clean(st).csv      # Processed match data
│   ├── team_stats(st).csv         # Team performance statistics
│   ├── scorers(st).csv            # Player goal-scoring data
│   └── players_cleaned.csv        # Cleaned player statistics
├── notebooks/                     # Jupyter notebooks
│   ├── fetch_football_data.ipynb  # Data collection and processing
│   └── eda.ipynb                  # Exploratory data analysis
├── .env                          # Environment variables (API keys)
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- API keys for Football-Data.org and API-Football

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/EmmaChris50/soccer-impact-tracker.git
   cd soccer-impact-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r data/requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   # API Keys for Soccer Impact Tracker
   FOOTBALL_DATA_API_TOKEN=your_football_data_api_token_here
   API_SPORTS_KEY=your_api_sports_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run data/app.py
   ```

## 📁 Data Sources

### APIs Used
- **Football-Data.org API**: Match data, team statistics, and standings
- **API-Football**: Detailed player statistics and performance metrics

### Data Files Description

| File | Description | Source |
|------|-------------|---------|
| `matches_clean(st).csv` | Processed match data with goals, teams, and dates | Football-Data.org |
| `team_stats(st).csv` | Team performance metrics and standings | Football-Data.org |
| `scorers(st).csv` | Player goal-scoring statistics | API-Football |
| `players_cleaned.csv` | Comprehensive player statistics | API-Football |

### Data Collection Process

The data collection process is documented in `notebooks/fetch_football_data.ipynb` and includes:

1. **Match Data Collection**: Fetches all Premier League matches for the 2023/24 season
2. **Team Information**: Collects team details, standings, and performance metrics
3. **Player Statistics**: Gathers detailed player performance data
4. **Data Cleaning**: Processes and validates the collected data
5. **Data Export**: Saves cleaned data to CSV files

## 🔧 Configuration

### Environment Variables

The application uses environment variables for secure API key management:

```env
# Football-Data.org API Token
FOOTBALL_DATA_API_TOKEN=your_token_here

# API-Football Key
API_SPORTS_KEY=your_key_here
```

### API Rate Limits

- **Football-Data.org**: 10 requests per minute
- **API-Football**: 100 requests per day (free tier)

## 📈 Key Metrics & Insights

### Match Analysis
- **Goals per Matchday**: Tracks scoring trends throughout the season
- **Common Scorelines**: Identifies most frequent match outcomes
- **Match Distribution**: Analysis of home vs away performance

### Team Performance
- **Goals vs Points**: Correlation between scoring and league position
- **Offense vs Defense**: Balance between attacking and defensive performance
- **Goal Difference**: Impact on final league standings

### Player Analytics
- **Top Scorers**: Leading goal scorers and their contributions
- **Performance Metrics**: Appearances, minutes, assists, and cards
- **Team Distribution**: Player performance across different teams

## 🧪 Development

### Code Quality

This project follows Python best practices:
- **Error Handling**: Comprehensive exception handling for API calls and data processing
- **Code Documentation**: Clear docstrings and comments
- **Modular Structure**: Separated concerns for data loading, processing, and visualization

### Data Processing Pipeline

1. **Data Collection**: Automated API calls with rate limiting
2. **Data Validation**: Checks for missing data and inconsistencies
3. **Data Cleaning**: Handles duplicates, null values, and data type conversions
4. **Data Export**: Saves processed data in standardized formats

### Security Features

- **API Key Protection**: Environment variables for sensitive credentials
- **Error Handling**: Graceful handling of API failures and data issues
- **Input Validation**: Validation of API responses and data integrity

## 🚀 Deployment

### Streamlit Cloud Deployment

The application is deployed on Streamlit Cloud:
1. Connect your GitHub repository
2. Set environment variables in Streamlit Cloud dashboard
3. Deploy automatically on code changes

### Local Development

For local development:
```bash
# Install development dependencies
pip install -r data/requirements.txt

# Run the application
streamlit run data/app.py

# Access at http://localhost:8501
```

## 📊 Sample Insights

### 2023/24 Premier League Highlights
- **Total Matches**: 380 matches analyzed
- **Teams**: 20 Premier League teams
- **Players**: 476 players with 5+ appearances
- **Data Points**: Comprehensive statistics including goals, assists, cards, and more

### Key Findings
- Correlation between goals scored and league points
- Impact of goal difference on final standings
- Distribution of common scorelines
- Performance patterns across different teams

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes** following the existing code style
4. **Add tests** if applicable
5. **Update documentation** as needed
6. **Submit a pull request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add error handling for new features
- Update requirements.txt for new dependencies
- Test API integrations thoroughly
- Document new features in README

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Emmanuel Okonkwo**
- Data Science Portfolio Project
- July 2025
- [GitHub Profile](https://github.com/EmmaChris50)

## 🙏 Acknowledgments

- **Football-Data.org** for providing comprehensive match and team data
- **API-Football** for detailed player statistics
- **Streamlit** team for the excellent web application framework
- **Plotly** for interactive data visualizations
- **Pandas** and **NumPy** for data manipulation and analysis

## 📞 Support & Contact

- **Issues**: Please use the [GitHub Issues](https://github.com/EmmaChris50/soccer-impact-tracker/issues) page
- **Questions**: Open a discussion in the [GitHub Discussions](https://github.com/EmmaChris50/soccer-impact-tracker/discussions)
- **Email**: [your.email@example.com]

## 🔄 Updates & Maintenance

### Recent Updates
- ✅ Environment variable integration for secure API key management
- ✅ Enhanced error handling and data validation
- ✅ Improved code structure and documentation
- ✅ Updated dependencies with version specifications

### Planned Features
- [ ] Real-time data updates
- [ ] Additional statistical analyses
- [ ] Historical data comparison
- [ ] Mobile-responsive design improvements
- [ ] Export functionality for reports

---

**Note**: This project is for educational and portfolio purposes. Please respect API rate limits and terms of service when using external data sources. The data is collected from publicly available APIs and is used in accordance with their respective terms of service.
