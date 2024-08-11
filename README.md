# Automation Test 02 - Functional Testing Case

## Overview

This project automates a functional test case for a web application using Selenium WebDriver. The test involves logging into a web panel, uploading an XLS file, validating the data, handling a popup, scrolling the page, and capturing a full-page screenshot.

## Features

- **Automated Login**: Logs into the web application using provided credentials.
- **File Upload**: Uploads an XLS file automatically.
- **Data Validation**: Validates the uploaded data and manages the confirmation popup.

- **Screenshot**: Captures a screenshot.

## Requirements

- **Python 3.x**
- **Selenium**: Install via pip:
bash
  pip install selenium
  
- **ChromeDriver**: Download and configure ChromeDriver to match your installed version of Chrome.

## Setup Instructions

1. **Clone the Repository**:
bash
   git clone https://github.com/Rahulrockss/Automation-Test-02---Functional-Testing-Case.git
   cd automation-test-case
   
2. **Install Required Python Libraries**:
bash
   pip install -r requirements.txt
   
*Note: The `requirements.txt` should include at least `selenium`.*

3. **Download and Configure ChromeDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Add ChromeDriver to your system's PATH or specify the path in the script.

4. **Place the XLS File**:
   - Download the `demo-data.xlsx` file.
   - Modify the script to reference the correct file path.

## Running the Test

1. **Update the Script**:
   - Set the correct path to ChromeDriver in the script:
python
     driver = webdriver.Chrome(executable_path='path_to_chromedriver')
     
- Set the correct path to the XLS file:
python
     upload_button.send_keys('path_to_your_file/demo-data.xlsx')
     
2. **Run the Script**:
bash
   python functional_test.py
   
3. **Expected Output**:
   - The script logs into the panel, uploads the XLS file, validates the data, handles the popup, scrolls down, and captures a full-page screenshot.
   - The screenshot is saved as `screenshot.png` in the current directory.

## Notes

- **Headless Mode**: The script is set to run in headless mode. Remove the `--headless` option if you want to see the browser window.
- **Scroll Adjustment**: Modify the scroll position in the script if needed.

## Troubleshooting

- **Element Not Found**: If an element is not found, inspect the website’s HTML and update the XPath or selectors.
- **ChromeDriver Version**: Ensure ChromeDriver’s version matches your Chrome version.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request. For major changes, please open an issue to discuss the proposed changes.
