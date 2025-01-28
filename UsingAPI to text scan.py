# ANN to chart topic treatment
# Model will source text written in five target languages 
# Thereby assessing similarity of descriptive words
# As well as hinting at regional political perspectives
# five target languages are:
# Arab, English, French, Russian, Spanish, Turkish
# Topic for this computation is The Israel/Palestine conflict 
# Start by leveraging an API 

import requests
import pandas as pd
from datetime import datetime, timedelta
import time
from collections import defaultdict


class ConflictMentionsCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/everything'
        self.languages = {
            'ar': 'Arabic',
            'en': 'English',
            'fr': 'French',
            'ru': 'Russian',
            'es': 'Spanish'
        }
        
        # Search queries for each language
        self.queries = {
            'ar': 'إسرائيل فلسطين غزة حرب',  # Arabic
            'en': 'Israel Palestine Gaza war conflict',  # English
            'fr': 'Israël Palestine Gaza guerre conflit',  # French
            'ru': 'Израиль Палестина Газа война конфликт',  # Russian
            'es': 'Israel Palestina Gaza guerra conflicto'  # Spanish
        }

    def get_articles_for_period(self, start_date, end_date, language):
        params = {
            'q': self.queries[language],
            'apiKey': self.api_key,
            'language': language,
            'from': start_date,
            'to': end_date,
            'pageSize': 100,
            'sortBy': 'publishedAt'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get('totalResults', 0)
            else:
                print(f"Error {response.status_code} for {language}: {response.text}")
                return 0
        except Exception as e:
            print(f"Request failed for {language}: {e}")
            return 0

    def collect_monthly_data(self, start_date, end_date):
        monthly_counts = defaultdict(lambda: {lang_code: 0 for lang_code in self.languages})
        
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
        
        while current_date <= end_datetime:
            month_key = current_date.strftime('%Y-%m')
            month_end = min(
                (current_date.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1),
                end_datetime
            )
            
            print(f"\nCollecting data for {month_key}")
            
            for lang_code in self.languages:
                count = self.get_articles_for_period(
                    current_date.strftime('%Y-%m-%d'),
                    month_end.strftime('%Y-%m-%d'),
                    lang_code
                )
                monthly_counts[month_key][lang_code] = count
                print(f"{self.languages[lang_code]}: {count} mentions")
                
                # Respect API rate limits
                time.sleep(1)
            
            current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)
        
        return monthly_counts

    def save_to_csv(self, monthly_counts, output_file='conflict_mentions_by_language.csv'):
        data = []
        for month, lang_counts in monthly_counts.items():
            row = {'date': month}
            row.update({self.languages[lang]: count for lang, count in lang_counts.items()})
            data.append(row)
        
        df = pd.DataFrame(data)
        df.sort_values('date', inplace=True)
        df.to_csv(output_file, index=False)
        print(f"\nData saved to {output_file}")
        return df

def main():
    api_key = 'c0468d73733143cf83d3ce428461b429'  # Replace with your NewsAPI key
    collector = ConflictMentionsCollector(api_key)
    
    # Collect data from October 7, 2023 to present
    monthly_data = collector.collect_monthly_data('2024-12-27', '2025-01-28')
    
    # Save and display results
    df = collector.save_to_csv(monthly_data)
    
    # Print summary statistics
    print("\nTotal mentions by language:")
    for lang_code, lang_name in collector.languages.items():
        total = sum(counts[lang_code] for counts in monthly_data.values())
        print(f"{lang_name}: {total:,} mentions")

if __name__ == "__main__":
    main()