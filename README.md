# Visualize Money Manager as Sankey Chart

I use the android app money manager to track my expenses. I export the data to an XLS file and use this script to visualize the data as a sankey chart. This script will 
* generate a sankey string for sankeyMATIC.com,
* try to import that string on sankeyMATIC.com/build using selenium and download the chart as a png file, and
* creates a sankey itself using plotly.

* Click [here](https://github.com/drepguy/visualizemoneymanager) to reach my github repo: [https://github.com/drepguy/visualizemoneymanager](https://github.com/drepguy/visualizemoneymanager)

This script does not support Money Transfers though.

See also:
* Money Manager in Google Play Store: [Money Manager Expense & Budget](https://play.google.com/store/apps/details?id=com.realbyteapps.moneymanagerfree&hl=en)
* SankeyMATIC: [http://sankeymatic.com](http://sankeymatic.com/build/)

<table style="border: none;">
  <tr>
    <td><img src="https://play-lh.googleusercontent.com/ikbN8scDWum2l6zGkmBrLFMsxOQvzTZT6UcIAYJ_dxBDAv9Ub7YE640cliaooDiWMzs=w240-h480" alt="Sankey Chart" width="180" height="180" style="border-radius: 10px;"></td>
    <td><img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Arrow_right_font_awesome.svg" alt="Arrow" width="50" height="50"></td>
    <td><img src="https://sankeymatic.com/gallery/i/1993-thumbnail.png" alt="Sankey Chart2" width="180" height="180" style="border-radius: 10px;"></td>
  </tr>
</table>

## How to set it up
If you have german app export, there is probably not much for you to do, besides setting the `FILE_PATH` in the `config.py` file.

### Export Data from Money-Manager App
* Open the app
* Go to the `More` tab in the bottom right corner
* Click on `Backup`
* Click on `Send Excel File via Email`
* Parametrize the export by date, the app gives some options you might need, a full year dataset is recommended
   * you can also export all data and split the file later to get a file for each year
* Send it via email to your computer, where you can run this script

### Configuration
1. Open the `config.py` file and set the following variables:
    - `FILE_PATH`: Full path to the XLS file.
    - `DIVIDE_AMOUNTS_BY`: Usually set to 12 to calculate monthly expenses.
    - `MIDDLE_NODE_NAME`: Name of the node that will be the middle of the tree.
    - `REMAINING_AMOUNT_NAME`: Name for balancing the whole Sankey diagram.
    - `SANKEY_CHART_SETTINGS`: Settings and appearance for the Sankey chart.
      - you can find the settings in the [SankeyMATIC Tool](http://sankeymatic.com/build/), after you have generated a chart
      when you click on `Save My Work` on [SankeyMATIC](http://sankeymatic.com/build/). The
      settings are included in the file
    - `TRANSFER_TYPE`s: See your excel export file in column G, if you don't use german language you should make changes here


## How to Run the Script

### Prerequisites
****
Make sure you have the following installed on your system:

- Python 3.10 or higher
- pip (Python package installer)
- make sure 'cdn.jsdelivr.net' is not blocked by your browser, adblocker or dns sink, as the script needs it for the SankeyMATIC creation

### Installation

1. Clone the repository to your local machine:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
   
   or download the zip-file from github and open terminal in this directory

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
    - Generate the Sankey raw string and saves it to the clipboard.
    - Append the settings to the Sankey string.
    - Draws the Sankey chart using Plotly.
    - Import the Sankey string to the SankeyMATIC website using Selenium and download the chart as a PNG file.

3. Paste the clipboard content into the [SankeyMATIC Tool](http://sankeymatic.com/build/) and generate the chart.

4. Check the logs for any errors or information.

### Additional Information

For more details on how to use the project, refer to the comments in the code and the documentation provided in the repository.
