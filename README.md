# Youtube_Data_Harvesting_and_Warehousing
A Streamlit web application for extracting YouTube channel, video, and comment details, storing them in MongoDB and MySQL, and performing basic queries and data exploration.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Data Extraction](#data-extraction)
  - [MongoDB Integration](#mongodb-integration)
  - [MySQL Integration](#mysql-integration)
  - [Query Page](#query-page)
  - [Data Exploration](#data-exploration)
- [Contributing](#contributing)

## Features

- Extract YouTube channel, video, and comment details.
- Store data in MongoDB and MySQL databases.
- Perform basic queries and visualize data using Streamlit and Plotly.

## Getting Started
## How to fetch the youtube api?
To use the YouTube Data API in this project, you need to obtain an API key from the Google Cloud Console. Follow the steps below to create your API key:

1. **Create a Project on Google Cloud Console:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the project dropdown in the top right corner and select "New Project."
   - Enter a name for your project and click "Create."

2. **Enable the YouTube Data API:**
   - In the Google Cloud Console, navigate to the "APIs & Services" > "Dashboard" page.
   - Click on "+ ENABLE APIS AND SERVICES."
   - Search for "YouTube Data API" and select it.
   - Click on the "Enable" button.

3. **Create API Key:**
   - In the Google Cloud Console, navigate to the "APIs & Services" > "Credentials" page.
   - Click on "+ CREATE CREDENTIALS" and select "API key."
   - Copy the generated API key.

4. **Restrict API Key (Optional but Recommended for Security):**
   - On the "Credentials" page, click on your newly created API key.
   - Under "Key restriction," you can set restrictions based on HTTP referrers, IP addresses, or applications.
   - Configure restrictions based on your security requirements.

5. **Use the API Key in Your Application:**
   - Use the API key in your application by including it in the API requests to the YouTube Data API.

Keep your API key secure and do not expose it publicly. If you are building a web application, it's recommended to set proper restrictions on the API key to control its usage.

For more detailed instructions and updates, refer to the [official Google Cloud documentation](https://cloud.google.com/docs/authentication/api-keys).

### Prerequisites

- Python 3.x
- Streamlit
- MongoDB
- MySQL

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SG9822/Youtube_Data_Warehouse.git
    cd Youtube_Data_Warehouse
    ```

2. Install dependencies:

    ```bash
    pip install -r libraries_used
    
    ```

3. Set up configuration:

    Create a ``connection`` between python and MonoDB & MySQL:

    ```env
    MONGODB=your_mongodb_url, eg.pymongo.MongoClient('your host') 
    MYSQL=your_mysql_url, eg.mysql://username:password@host:port/database
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run Data.py
    ```

## Usage

### Data Extraction

1. Launch the Streamlit app.
2. Navigate to the "Data" page.
3. Enter a YouTube channel ID and click the "Extract" button to get channel, video, and comment details.

### MongoDB Integration

1. Navigate to the "Data" page.
2. After extracting Data from channel Id, Click the "Insert into MongoDB" button to upload details to MongoDB.

### MySQL Integration

1. Navigate to the "Data" page.
2. Select the Channel from Drop down.
3. Click the "Insert into MySQL" button to load data from MongoDB into a DataFrame and store it in MySQL.

### Query Page

1. Navigate to the "Query" page.
2. Select a query from the dropdown to display a Streamlit DataFrame and a Plotly bar chart.

### Data Exploration

1. Navigate to the "Tables" page.
2. Select a table from the dropdown to explore available data.

## The Images Used are
1. ![YouTube Logo](https://github.com/SG9822/Youtube_Data_Warehouse/blob/main/youtube-logo-download.png)


## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

## Acknowledgments

- Thanks to the YouTube Data API for providing data.
- Shoutout to Streamlit and Plotly for visualization capabilities.
- And for the People at Guvi who clarified the doubts without hesitation.

