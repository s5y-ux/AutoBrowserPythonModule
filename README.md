# SeleniumEasyMethods: Python Module for Easy Web Browser Automation

## Overview

SeleniumEasyMethods is a Python module designed to simplify web browser automation using the Selenium framework. This module provides easy-to-use methods for common actions such as visiting websites, clicking elements, sending keys, scrolling, and more.

## Installation

To use SeleniumEasyMethods, you need to have Python installed. You can install the module using pip:

```bash
pip install SeleniumEasyMethods
```

Make sure you have the Chrome browser installed on your system, as this module uses the Chrome WebDriver for automation.

## Getting Started

```python
from SeleniumEasyMethods import Browser

# Create a new instance of the Browser class
browser = Browser()

# Visit a website
browser.visit("example.com")

# Click an element using XPath
browser.click("//button[@id='exampleButton']")

# Send keys to an input field
browser.send_keys("//input[@id='exampleInput']", "Hello, Selenium!")

# Scroll to a specific position on the page
browser.scroll_to(500)

# Close the browser
browser.browser.quit()
```

## Available Methods

### `visit(website_parameter)`

Visit a website by providing the website parameter.

### `direct_visit(website_parameter)`

Directly visit a website by providing the complete URL.

### `click(xpath_parameter)`

Click an element on the page using its XPath.

### `fast_click(xpath_parameter)`

Repeatedly click an element on the page using its XPath until stopped manually.

### `send_keys(xpath_parameter, input_parameter, press_enter=False)`

Send keys to an input field identified by XPath. Optionally, press Enter after sending keys.

### `scroll_to(y_position)`

Scroll to a specific Y position on the page.

### `delay(int_parameter)`

Introduce a delay in seconds to wait for page elements to load.

## Example Usage

```python
# Create a new instance of the Browser class
browser = Browser()

# Visit GitHub
browser.visit("github.com")

# Search for "Selenium" on GitHub
browser.send_keys("//input[@name='q']", "Selenium", press_enter=True)

# Click on the first search result
browser.click("(//ul[@class='repo-list']//a)[1]")

# Close the browser
browser.browser.quit()
```

Feel free to explore and customize the methods to suit your automation needs.

## Note

Ensure that you have the appropriate permissions to automate websites, and use this module responsibly and in compliance with the terms of service of the websites you interact with.

Happy automating!
