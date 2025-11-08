"""
CDCR Inmate Information Scraper - Reusable Script
Queries the CDCR database for inmate records and extracts detailed information
Website: https://ciris.mt.cdcr.ca.gov/
"""

import time
import json
import csv
from typing import List, Dict, Any, Optional
from datetime import datetime


class CDCRInmateScraper:
    """
    Reusable script to query and scrape inmate information from CDCR database
    
    Features:
    - Search by CDCR number
    - Extract personal information (Age, Admission Date, Current Location, etc.)
    - Extract Parole Eligible Date
    - Extract complete Board of Parole Hearings Actions table
    - Export to CSV and JSON formats
    - Batch processing of multiple CDCR numbers
    """
    
    BASE_URL = "https://ciris.mt.cdcr.ca.gov/"
    
    def __init__(self):
        """Initialize the scraper"""
        self.results = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def search_cdcr_number(self, cdcr_number: str) -> Dict[str, Any]:
        """
        Search for an inmate by CDCR number and extract all information
        
        Args:
            cdcr_number (str): The CDCR number to search (e.g., 'D54803', 'T97214')
        
        Returns:
            Dict containing:
            - cdcr_number: The CDCR number searched
            - name: Inmate name
            - age: Current age
            - admission_date: Date of admission
            - current_location: Current prison location
            - commitment_county: County of commitment
            - parole_eligible_date: Date eligible for parole
            - board_of_parole_hearings: List of hearing records with Date, Action, Status, Outcome
        
        Workflow Steps:
        1. Navigate to CDCR website
        2. Accept disclaimer
        3. Switch to CDCR Number search mode
        4. Enter CDCR number
        5. Click search button
        6. Extract search results (Name, Age, Admission Date, Current Location, Commitment County)
        7. Click on inmate name to access detailed record
        8. Extract Parole Eligible Date and Board of Parole Hearings table
        9. Return to search for next inmate
        """
        
        inmate_data = {
            "cdcr_number": cdcr_number,
            "name": None,
            "age": None,
            "admission_date": None,
            "current_location": None,
            "commitment_county": None,
            "parole_eligible_date": None,
            "board_of_parole_hearings": []
        }
        
        # IMPLEMENTATION NOTES FOR BROWSER AUTOMATION:
        # This method should be called within a browser automation context
        # The following steps should be executed:
        
        # Step 1: Navigate to CDCR website
        # navigate(url=self.BASE_URL, reasoning="Navigate to CDCR inmate search website")
        # wait(seconds=2, description="page to load")
        
        # Step 2: Accept disclaimer
        # actWithClick(action="click the AGREE button", reasoning="Accept the disclaimer to access the inmate search functionality")
        # wait(seconds=2, description="disclaimer to be accepted")
        
        # Step 3: Switch to CDCR Number search mode
        # actWithClick(action="click the CDCR Number radio button", reasoning="Switch to CDCR Number search method")
        # wait(seconds=1, description="search mode to switch")
        
        # Step 4: Enter CDCR number
        # actWithType(action=f"type '{cdcr_number}' into the CDCR Number input field", 
        #             value=cdcr_number, reasoning="Enter the CDCR number to search")
        # wait(seconds=1, description="input to be entered")
        
        # Step 5: Click search button
        # actWithClick(action="click the SEARCH button", reasoning="Execute the search")
        # wait(seconds=2, description="search results to load")
        
        # Step 6: Extract search results
        # search_results = extract(
        #     template="search results",
        #     schema="z.object({ name: z.string().optional(), age: z.string().optional(), admissionDate: z.string().optional(), currentLocation: z.string().optional(), commitmentCounty: z.string().optional() })",
        #     instruction="Extract the inmate name, age, admission date, current location, and commitment county from the search results table",
        #     reasoning="Extract basic inmate information from search results"
        # )
        
        # inmate_data["name"] = search_results.get("name")
        # inmate_data["age"] = search_results.get("age")
        # inmate_data["admission_date"] = search_results.get("admissionDate")
        # inmate_data["current_location"] = search_results.get("currentLocation")
        # inmate_data["commitment_county"] = search_results.get("commitmentCounty")
        
        # Step 7: Click on inmate name to access detailed record
        # actWithClick(action=f"click the {inmate_data['name']} name link", 
        #              reasoning="Click on the inmate name to access the detailed record")
        # wait(seconds=2, description="detailed record to load")
        
        # Step 8: Extract detailed information
        # detailed_data = extract(
        #     template="inmate details and parole hearings",
        #     schema="z.object({ paroleEligibleDate: z.string().optional(), boardOfParoleHearings: z.array(z.object({ date: z.string().optional(), action: z.string().optional(), status: z.string().optional(), outcome: z.string().optional() })).optional() })",
        #     instruction="Extract the Parole Eligible Date and all rows from the Board of Parole Hearings Actions table with Date, Action, Status, and Outcome fields",
        #     reasoning="Extract parole eligibility and hearing history"
        # )
        
        # inmate_data["parole_eligible_date"] = detailed_data.get("paroleEligibleDate")
        # inmate_data["board_of_parole_hearings"] = detailed_data.get("boardOfParoleHearings", [])
        
        # Step 9: Return to search for next inmate
        # actWithClick(action="click the RETURN TO SEARCH RESULT link", reasoning="Return to search results")
        # wait(seconds=1, description="search results page to load")
        # actWithClick(action="click the RETURN TO SEARCH link", reasoning="Return to search form")
        # wait(seconds=2, description="search form to load")
        
        return inmate_data
    
    def search_multiple_cdcr_numbers(self, cdcr_numbers: List[str]) -> List[Dict[str, Any]]:
        """
        Search for multiple inmates by CDCR numbers
        
        Args:
            cdcr_numbers (List[str]): List of CDCR numbers to search
        
        Returns:
            List of dictionaries containing inmate information for each CDCR number
        """
        
        results = []
        
        for i, cdcr_number in enumerate(cdcr_numbers, 1):
            print(f"\n[{i}/{len(cdcr_numbers)}] Searching for CDCR number: {cdcr_number}")
            inmate_data = self.search_cdcr_number(cdcr_number)
            results.append(inmate_data)
            print(f"✓ Successfully retrieved data for {cdcr_number}")
            if i < len(cdcr_numbers):
                time.sleep(1)  # Brief pause between searches
        
        self.results = results
        return results
    
    def export_to_csv(self, results: Optional[List[Dict[str, Any]]] = None, 
                     filename: Optional[str] = None) -> str:
        """
        Export results to CSV file
        
        Args:
            results (List[Dict]): List of inmate data dictionaries (uses self.results if None)
            filename (str): Output CSV filename (auto-generated if None)
        
        Returns:
            str: Path to the exported CSV file
        """
        
        if results is None:
            results = self.results
        
        if filename is None:
            filename = f"cdcr_inmates_{self.timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'cdcr_number', 'name', 'age', 'admission_date', 
                'current_location', 'commitment_county', 'parole_eligible_date',
                'num_parole_hearings'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for inmate in results:
                writer.writerow({
                    'cdcr_number': inmate['cdcr_number'],
                    'name': inmate['name'],
                    'age': inmate['age'],
                    'admission_date': inmate['admission_date'],
                    'current_location': inmate['current_location'],
                    'commitment_county': inmate['commitment_county'],
                    'parole_eligible_date': inmate['parole_eligible_date'],
                    'num_parole_hearings': len(inmate['board_of_parole_hearings'])
                })
        
        print(f"\n✓ CSV exported to: {filename}")
        return filename
    
    def export_to_json(self, results: Optional[List[Dict[str, Any]]] = None, 
                      filename: Optional[str] = None) -> str:
        """
        Export results to JSON file
        
        Args:
            results (List[Dict]): List of inmate data dictionaries (uses self.results if None)
            filename (str): Output JSON filename (auto-generated if None)
        
        Returns:
            str: Path to the exported JSON file
        """
        
        if results is None:
            results = self.results
        
        if filename is None:
            filename = f"cdcr_inmates_{self.timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(results, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"✓ JSON exported to: {filename}")
        return filename
    
    def export_parole_hearings_to_csv(self, results: Optional[List[Dict[str, Any]]] = None,
                                     filename: Optional[str] = None) -> str:
        """
        Export Board of Parole Hearings data to separate CSV file
        
        Args:
            results (List[Dict]): List of inmate data dictionaries (uses self.results if None)
            filename (str): Output CSV filename (auto-generated if None)
        
        Returns:
            str: Path to the exported CSV file
        """
        
        if results is None:
            results = self.results
        
        if filename is None:
            filename = f"cdcr_parole_hearings_{self.timestamp}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['cdcr_number', 'inmate_name', 'date', 'action', 'status', 'outcome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for inmate in results:
                for hearing in inmate['board_of_parole_hearings']:
                    # Parse hearing data if it's a JSON string
                    if isinstance(hearing, str):
                        hearing = json.loads(hearing)
                    
                    writer.writerow({
                        'cdcr_number': inmate['cdcr_number'],
                        'inmate_name': inmate['name'],
                        'date': hearing.get('date', ''),
                        'action': hearing.get('action', ''),
                        'status': hearing.get('status', ''),
                        'outcome': hearing.get('outcome', '')
                    })
        
        print(f"✓ Parole Hearings CSV exported to: {filename}")
        return filename
    
    def print_summary(self, results: Optional[List[Dict[str, Any]]] = None):
        """
        Print a summary of the extracted data
        
        Args:
            results (List[Dict]): List of inmate data dictionaries (uses self.results if None)
        """
        
        if results is None:
            results = self.results
        
        print("\n" + "="*80)
        print("CDCR INMATE SEARCH RESULTS SUMMARY")
        print("="*80)
        
        for i, inmate in enumerate(results, 1):
            print(f"\n[{i}] CDCR Number: {inmate['cdcr_number']}")
            print(f"    Name: {inmate['name']}")
            print(f"    Age: {inmate['age']}")
            print(f"    Admission Date: {inmate['admission_date']}")
            print(f"    Current Location: {inmate['current_location']}")
            print(f"    Commitment County: {inmate['commitment_county']}")
            print(f"    Parole Eligible Date: {inmate['parole_eligible_date']}")
            print(f"    Board of Parole Hearings: {len(inmate['board_of_parole_hearings'])} records")
        
        print("\n" + "="*80)


# USAGE EXAMPLE:
if __name__ == "__main__":
    # Initialize scraper
    scraper = CDCRInmateScraper()
    
    # Define CDCR numbers to search
    cdcr_numbers = ["D54803", "T97214"]
    
    # Search for multiple inmates
    results = scraper.search_multiple_cdcr_numbers(cdcr_numbers)
    
    # Print summary
    scraper.print_summary(results)
    
    # Export to CSV and JSON
    scraper.export_to_csv(results)
    scraper.export_to_json(results)
    scraper.export_parole_hearings_to_csv(results)
