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

    Create a `.env` file in the project root and add the following:

    ```env
    MONGODB_URI=your_mongodb_uri, eg.pymongo.MongoClient('your host') 
    MYSQL_URI=your_mysql_uri, eg.mysql://username:password@host:port/database
    ```

    Replace `your_mongodb_uri` and `your_mysql_uri` with your MongoDB and MySQL connection strings.

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

