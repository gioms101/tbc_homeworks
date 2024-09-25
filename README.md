# Recipe Scraper and MongoDB Analyzer

This project scrapes recipes from the [Kulinaria.ge](https://kulinaria.ge) website and stores the scraped data into MongoDB for further analysis.
The project includes a web scraper and database operations such as calculating averages and finding the most frequent data points.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Functions and Methods](#functions-and-methods)
  - [Web Scraper](#web-scraper)
  - [MongoDB Operations](#mongodb-operations)
- [License](#license)

## Features
- Scrapes recipe data such as name, ingredients, steps, portion sizes, and more.
- Saves the scraped data in `data.json`.
- Inserts the data into a MongoDB collection for storage.
- Performs operations like finding the recipe with the most portions, average ingredients, and the most frequent author.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.10 or later
- MongoDB
- Required Python packages:
  - `beautifulsoup4`
  - `lxml`
  - `pymongo`
  - `requests`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/recipe-scraper.git
   cd recipe-scraper
