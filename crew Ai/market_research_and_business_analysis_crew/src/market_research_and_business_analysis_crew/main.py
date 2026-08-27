import os
from dotenv import load_dotenv
from market_research_and_business_analysis_crew.crew import MarketResearchAndBusinessAnalysisCrew

load_dotenv()

def run():
    inputs = {
        'product_idea': (
            'An AI-native tool that automatically summarizes YouTube videos '
            'and auto-publishes formatted posts to LinkedIn, Twitter/X, and Instagram.'
        )
    }

    print("\n--- Starting Crew Execution ---")
    result = MarketResearchAndBusinessAnalysisCrew().crew().kickoff(inputs=inputs)
    print("\n--- Execution Completed Successfully ---")
    print("Report generated at: reports/report.md")

if __name__ == "__main__":
    run()