# Ex-Servicemen Job Discovery Agent (Prototype)

## Overview

The **Ex-Servicemen Job Discovery Agent** is a prototype AI-powered tool designed to assist ex-servicemen in India—particularly **Junior Commissioned Officers (JCOs)** and **Other Ranks (ORs)**—in discovering relevant civilian job opportunities. Built using the [**Google Agent Development Kit (ADK)**](https://google.github.io/adk-docs/), the agent dynamically scrapes job postings from curated job boards, filters them based on relevance and recency, and formats the output in a structured markdown table.

It also includes an optional feature that allows users to generate and send a job summary via email, powered by the **Brevo API**.

---

### 🎯 Problem Statement Alignment

This prototype is developed in response to **Problem Statement No. 6 (2025)** issued by the [**Army Design Bureau**](https://indianarmy.nic.in/content2/adb/introduction-adb), titled:

> *"AI Search Engine for Employment Opportunities of Ex-Servicemen."*

📄 The complete set of problem statements is available in this [official PDF](https://indianarmy.nic.in/writereaddata/images/ADB/cpds_120225.pdf).  
📂 A dedicated copy of this specific problem statement is also provided in the `problem_statement/` folder of this repository.

> ⚙️ **Current Focus — Part-I**  
> The prototype specifically targets **Part-I of the deliverables**:
> 
> ✅ *"AI-based aggregator application to search for jobs on the Internet specifically for Ex-Servicemen."*
>
> This aligns with the recognized need:
> > *"Manual search of vacancy is time consuming and chances of missing out on good vacancies are high."*
---
## Features

- **Job Scraping**: Scrapes job postings from multiple job boards tailored for ex-servicemen using Firecrawl.
- **Dynamic Filtering**: Filters job postings to include only those from the current month, extracting relevant fields like organization, job description, and apply links.
- **Structured Output**: Presents job postings in a markdown table format with fields: Sl. No, Name of Organisation, Govt/PSU/Pvt, Description, Date, Location, Apply Link, and Other Relevant Links.
- **Email Integration**: Allows users to generate and send the job summary via email using Brevo, with a user-driven confirmation workflow.
- **Modular Agent Design**: Employs a multi-agent architecture with sub-agents dedicated to scraping, filtering, drafting, and emailing.

## Project Structure

```
parent_folder/
  job_discovery_agent/
    ├── __init__.py
    ├── agent.py              # Root agent definition
    ├── prompt.py             # Instructions for the root agent
    ├── websites.py           # List of websites to scrape
    ├── .env                 # API keys for Firecrawl and Brevo
    ├── tools/
    │   ├── __init__.py
    │   ├── brevo.py         # Tool for sending emails via Brevo
    │   ├── firecrawler.py   # Tool for scraping websites using Firecrawl
    │   └── get_websites.py  # Tool to retrieve the list of websites
    └── sub_agents/
        ├── scrapy/
        │   ├── __init__.py
        │   ├── agent.py     # Scrapy sub-agent for scraping
        │   └── prompt.py    # Instructions for scrapy sub-agent
        ├── filter/
        │   ├── __init__.py
        │   ├── agent.py     # Filter sub-agent for processing scraped data
        │   └── prompt.py    # Instructions for filter sub-agent
        ├── writer/
        │   ├── __init__.py
        │   ├── agent.py     # Writer sub-agent for drafting emails
        │   └── prompt.py    # Instructions for writer sub-agent
        └── brevo/
            ├── __init__.py
            ├── agent.py     # Brevo sub-agent for sending emails
            └── prompt.py    # Instructions for brevo sub-agent
```

## Prerequisites

- Python 3.9+
- Google ADK (`pip install google-adk`)
- Firecrawl (`pip install firecrawl`) for web scraping
- Brevo API (`pip install sib-api-v3-sdk`) for email functionality
- A local IDE (e.g., VS Code, PyCharm) with terminal access

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ex-servicemen-job-discovery-agent.git
   cd google-adk-job-agent
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv .venv
   ```

   Activate it:

   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`

3. **Install Dependencies**:

   ```bash
   pip install google-adk firecrawl sib-api-v3-sdk
   ```

4. **Configure API Keys**:

   - Open the `.env` file in the `job_discovery_agent/` directory.

   - Add your Firecrawl and Brevo API keys:

     ```
     FIRECRAWL_API_KEY=your_actual_firecrawl_api_key_here
     BREVO_API_KEY=your_actual_brevo_api_key_here
     ```

5. **Run the Agent**:

   - Navigate to the parent directory:

     ```bash
     cd parent_folder
     ```

   - Launch the ADK development UI:

     ```bash
     adk web
     ```

   - Open the provided URL (e.g., `http://localhost:8000`) in your browser to interact with the agent.

## Usage

1. **Generate Job Summary**:

   - In the ADK UI, send the command: `generate`.
   - The agent will scrape job postings, filter them for the current month, and display a markdown table with the following columns:
     - Sl. No
     - Name of Organisation
     - Govt/PSU/Pvt
     - Some Description about Post
     - Date
     - Location
     - Apply Link
     - Other Relevant Links

   Example output:

   ```
   | Sl. No | Name of Organisation | Govt/ PSU/Pvt | Some Description about Post        | Date       | Location    | Apply Link                | Other Relevant Links       |
   |--------|----------------------|---------------|------------------------------------|------------|-------------|---------------------------|----------------------------|
   | 1      | ABC Corp            | Pvt           | Software Engineer                 | 2025-05-01 | Remote      | [Apply](http://abc.com)  | [Details](http://abc.com/info) |
   | 2      | XYZ Govt            | Govt          | Administrative Officer            | 2025-05-05 | Delhi       | [Apply](http://xyz.gov)  |                            |
   ```

2. **Generate and Send Email**:

   - After the table is displayed, the agent will prompt: "Would you like to generate an email with this job summary? Reply 'generate email' to proceed."
   - Reply with `generate email` to draft an email.
   - The agent will show the drafted email and ask: "Here is the drafted email. Reply 'send email' to send it, or 'cancel' to stop."
   - Reply with `send email` to send the email via Brevo, or `cancel` to abort.
   - Screenshot of the same is being shown below:
   - ![image](https://github.com/user-attachments/assets/f9fc7b1a-073b-4801-b52e-8c6f14ce048a)


## Current Limitations (Prototype Stage)

- **❌ Parsing Accuracy**: The agent relies on the LLM to parse markdown content, which may lead to inconsistent field extraction depending on the website structure.
- **📉 Website Coverage**: Limited to a predefined list of websites; more job boards can be added.
- **📅 Date Filtering**: Assumes dates are in a recognizable format; may miss jobs if dates are formatted unusually.
- **📧 Email Functionality**: Requires a valid Brevo API key and assumes a default sender email.

## Future Improvements

- **🧠 Enhanced Matching**: Add NLP-based job matching to user profiles.
- **🔁 Dynamic Searching**: Expand to dynamic location-based filters
- **🌐 User Interface**: Introduce user interface for real-time interaction.
- **📄 Resume matching**: Support resume matching and CV generation (Part-II of the problem)
- **🚨 Error Handling**: Add robust error handling for failed scrapes or email sends.

## Contact

For questions or feedback, please open an issue on GitHub or reach out to the maintainers.

---

*Last Updated: May 18, 2025*
