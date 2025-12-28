"""
Data Validation Script
Run this script to verify your dataset is correctly loaded
"""

import pandas as pd
import sys

def validate_data():
    """Validate that the CSV files are loaded correctly"""
    
    print("=" * 60)
    print("IPL Dataset Validation")
    print("=" * 60)
    print()
    
    # Try to load matches.csv
    try:
        matches = pd.read_csv('data/matches.csv')
        print("✅ matches.csv loaded successfully!")
        print(f"   - Rows: {len(matches):,}")
        print(f"   - Columns: {len(matches.columns)}")
        print(f"   - Column names: {', '.join(matches.columns.tolist())}")
        print()
    except FileNotFoundError:
        print("❌ ERROR: data/matches.csv not found!")
        print("   Please download the dataset and place matches.csv in the data/ folder")
        print()
        matches = None
    except Exception as e:
        print(f"❌ ERROR loading matches.csv: {e}")
        print()
        matches = None
    
    # Try to load deliveries.csv
    try:
        deliveries = pd.read_csv('data/deliveries.csv')
        print("✅ deliveries.csv loaded successfully!")
        print(f"   - Rows: {len(deliveries):,}")
        print(f"   - Columns: {len(deliveries.columns)}")
        print(f"   - Column names: {', '.join(deliveries.columns.tolist())}")
        print()
    except FileNotFoundError:
        print("❌ ERROR: data/deliveries.csv not found!")
        print("   Please download the dataset and place deliveries.csv in the data/ folder")
        print()
        deliveries = None
    except Exception as e:
        print(f"❌ ERROR loading deliveries.csv: {e}")
        print()
        deliveries = None
    
    # Validate data if both files loaded
    if matches is not None and deliveries is not None:
        print("=" * 60)
        print("Data Statistics")
        print("=" * 60)
        print()
        
        # Matches info
        print("📊 MATCHES DATA:")
        print(f"   - Total matches: {len(matches):,}")
        print(f"   - Seasons: {matches['season'].min()} to {matches['season'].max()}")
        print(f"   - Unique teams: {matches['team1'].nunique() + matches['team2'].nunique()}")
        print(f"   - Unique venues: {matches['venue'].nunique()}")
        print()
        
        # Deliveries info
        print("📊 DELIVERIES DATA:")
        print(f"   - Total deliveries: {len(deliveries):,}")
        print(f"   - Unique matches: {deliveries['match_id'].nunique():,}")
        print(f"   - Unique batters: {deliveries['batter'].nunique():,}")
        print(f"   - Unique bowlers: {deliveries['bowler'].nunique():,}")
        print(f"   - Total runs: {deliveries['total_runs'].sum():,}")
        print(f"   - Total wickets: {deliveries['is_wicket'].sum():,}")
        print()
        
        # Sample data
        print("=" * 60)
        print("Sample Data Preview")
        print("=" * 60)
        print()
        print("MATCHES (First 3 rows):")
        print(matches[['id', 'season', 'date', 'team1', 'team2', 'winner']].head(3).to_string(index=False))
        print()
        print("DELIVERIES (First 3 rows):")
        print(deliveries[['match_id', 'inning', 'batter', 'bowler', 'batsman_runs', 'total_runs']].head(3).to_string(index=False))
        print()
        
        print("=" * 60)
        print("✅ Dataset validation complete! Your data looks good.")
        print("=" * 60)
        print()
        print("You can now run the app with: streamlit run app.py")
        print()
        
    else:
        print("=" * 60)
        print("❌ Dataset validation failed!")
        print("=" * 60)
        print()
        print("NEXT STEPS:")
        print("1. Download the IPL dataset from Kaggle")
        print("2. Extract the ZIP file")
        print("3. Place matches.csv and deliveries.csv in the data/ folder")
        print("4. Run this script again to validate")
        print()
        print("See DATASET_INSTRUCTIONS.md for detailed steps")
        print()
        sys.exit(1)


if __name__ == "__main__":
    validate_data()