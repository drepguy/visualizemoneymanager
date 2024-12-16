# Visualize Money Manager as Sankey Chart

I use the app money manager to track my expenses. I export the data to an XLS file and use this script
to visualize the data as a sankey chart. This script will generate a sankey string you can import
into a sankey chart generator like SankeyMATIC.

* Money Manager in Google Play Store: [Money Manager Expense & Budget](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree&hl=en)
* SankeyMATIC: [http://sankeymatic.com](http://sankeymatic.com/build/)

## How to set it up

### Export Data from App
* Open the app
* Go to the `More` tab in the bottom right corner
* Click on `Backup`
* Click on `Send Excel File via Email`
* Parametrize the export by date, the app gives some options you might need, a full year dataset is recommended
   * you can also export all data and split the file later to get a file for each year
* Send it via email to your computer, where you can run this script

### Configuration
1. Open the `config.py` file and set the following variables:
    - `FILE_PATH`: Path to the XLS file.
    - `DIVIDE_AMOUNTS_BY`: Usually set to 12 to calculate monthly expenses.
    - `MIDDLE_NODE_NAME`: Name of the node that will be the middle of the tree.
    - `REMAINING_AMOUNT_NAME`: Name for balancing the whole Sankey diagram.
    - `SANKEY_CHART_SETTINGS`: Settings and appearance for the Sankey chart.
      - you can find the settings in the [SankeyMATIC Tool](http://sankeymatic.com/build/), after you have generated a chart
      when you click on `Save My Work` on [SankeyMATIC](http://sankeymatic.com/build/). The
      settings are included in the file

## How to Run the Script

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment (if you did step before):

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

1. Run the main script:

    ```sh
    python main.py
    ```

2. The script will:
    - Log the Python version.
    - Check if the specified file exists.
    - Parse the MoneyManager export file.
    - Calculate the sums for the categories and subcategories.
    - Generate the Sankey raw string.
    - Append the settings to the Sankey string.
    - Print the Sankey string.
    - Copy the Sankey string to the clipboard.

3. Paste the clipboard content into the [SankeyMATIC Tool](http://sankeymatic.com/build/) and generate the chart.

4. Check the logs for any errors or information.

### Additional Information

For more details on how to use the project, refer to the comments in the code and the documentation provided in the repository.