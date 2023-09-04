"""
Streamlit SeekMate Portal Template

To use as ideas sorter, TODO:

- Well define each feature
- app.py to contain only main
- Scrapping Management: To manually run scrappers
- DB Retrieval: Create backend API to retrieve data from the DB and show in the FE
- User management : user can login and have his personalized resources from the DB

"""

import streamlit as st

def main():
    """
    Main function that runs the Streamlit application.
    """
    st.title("SeekMate: Your Job Seeking Companion")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Search Jobs", "View Applied Jobs", "Run Scrappers", "Scrapping Dashboard"])

    # Dynamic Page Routing
    if selection == "Search Jobs":
        search_jobs()
    elif selection == "View Applied Jobs":
        view_applied_jobs()
    elif selection == "Run Scrappers":
        run_scrappers()
    elif selection == "Scrapping Dashboard":
        scrapping_dashboard()

def search_jobs():
    """
    Function to handle the 'Search Jobs' page.
    """
    st.header("Search Jobs")
    
    keyword = st.text_input("Enter Keyword (e.g., Data Scientist)")
    location = st.text_input("Enter Location (e.g., Luxembourg)")
    st.button("Search")
    
    # TODO: Implement the search logic + display the results
    st.write("Results will appear here.")

def view_applied_jobs():
    """
    Function to handle the 'View Applied Jobs' page.
    """
    st.header("Your Applied Jobs")
    
    # TODO: Fetch applied jobs from the database + display the results
    st.write("List of applied jobs will appear here.")

def run_scrappers():
    """
    Function to handle the 'Run Scrappers' page.
    """
    st.header("Run Scrappers")
    
    if st.button("Run LinkedIn Scrapper"):
        # TODO: Trigger LinkedIn scrapper logic here
        st.write("LinkedIn Scrapper initiated.")

    if st.button("Run Indeed Scrapper"):
        # TODO: Trigger Indeed scrapper logic here
        st.write("Indeed Scrapper initiated.")

    if st.button("Run Moovijob Scrapper"):
        # TODO: Trigger Indeed scrapper logic here
        st.write("Indeed Moovijob initiated.")

def scrapping_dashboard():
    """
    Function to handle the 'Scrapping Dashboard' page.
    """
    st.header("Scrapping Dashboard and Status")
    
    # TODO: Fetch and display scrapper status from logs
    st.write("LinkedIn Scrapper: Last run at 12:34 PM")
    st.write("Indeed Scrapper: Last run at 01:23 PM")

# Entry Point
if __name__ == "__main__":
    main()
