import math

def calculate_gsc_metrics(query_data, top_n_filter=None):
    """
    Calculates various average position metrics from simulated GSC query data.
    Demonstrates how simple average can be misleading and how weighted average
    or filtering can provide better insights.
    """
    total_impressions = sum(item['impressions'] for item in query_data)
    total_queries = len(query_data)

    # --- Demonstrating the 'misleading' simple average position ---
    # This is similar to how GSC might show an overall average without weighting.
    # It can be misleading because queries with very low impressions but high positions
    # can skew the average, or vice-versa.
    simple_avg_position = sum(item['position'] for item in query_data) / total_queries

    # --- Demonstrating a 'more accurate' weighted average position ---
    # This weights each position by its impressions, giving more importance
    # to queries that generate more visibility. This often reflects the
    # *effective* average position better for users.
    weighted_avg_position_by_impressions = (
        sum(item['position'] * item['impressions'] for item in query_data) /
        total_impressions if total_impressions > 0 else 0
    )

    print(f"\n--- Analysis for {'Top ' + str(top_n_filter) + ' Positions' if top_n_filter else 'All Queries'} ---")
    print(f"Total Queries Analyzed: {total_queries}")
    print(f"Total Impressions: {total_impressions}")
    print(f"Simple Average Position: {simple_avg_position:.2f}")
    print(f"Weighted Average Position (by Impressions): {weighted_avg_position_by_impressions:.2f}")


# Simulate Google Search Console-like data for various queries
# Each dictionary represents a search query with its impressions and average position.
# Note how some queries have high positions (bad) but low impressions,
# while others have good positions (low number) and high impressions.
search_queries_data = [
    {"query": "best coffee maker", "impressions": 1000, "position": 2},
    {"query": "espresso machine review", "impressions": 500, "position": 5},
    {"query": "coffee machine parts", "impressions": 200, "position": 15},
    {"query": "how to clean coffee maker", "impressions": 300, "position": 1},
    {"query": "cheap coffee maker", "impressions": 800, "position": 10},
    {"query": "coffee maker maintenance", "impressions": 100, "position": 30},
    {"query": "coffee maker brands", "impressions": 1500, "position": 4},
    {"query": "coffee maker troubleshooting", "impressions": 50, "position": 60}, # Low impressions, very high position
    {"query": "coffee maker comparison", "impressions": 700, "position": 3},
    {"query": "buy coffee maker online", "impressions": 1200, "position": 6},
    {"query": "coffee maker accessories", "impressions": 150, "position": 25},
    {"query": "coffee maker problems", "impressions": 80, "position": 45} # Low impressions, high position
]

print("Simulating Google Search Console Average Position Data")

# 1. Calculate metrics for ALL queries
calculate_gsc_metrics(search_queries_data)

# 2. Filter for queries ranking in the Top 10 positions
# This is a common strategy to get more actionable data, focusing on visible ranks.
top_10_queries = [item for item in search_queries_data if item['position'] <= 10]
calculate_gsc_metrics(top_10_queries, top_n_filter=10)

# 3. Filter for queries ranking in the Top 3 positions
# Even more focused analysis for high-impact keywords.
top_3_queries = [item for item in search_queries_data if item['position'] <= 3]
calculate_gsc_metrics(top_3_queries, top_n_filter=3)
