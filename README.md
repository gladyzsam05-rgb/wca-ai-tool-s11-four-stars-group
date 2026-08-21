#GROUP NAME FOURSTARS
##Eco-Waste-Assistant-Four-Stars-Group-

#PROJECT DESCRIPTION
Eco Waste Assistant is an AI-powered decision assistant designed to help
users identify, classify, and make better decisions about different types
of waste.

The tool uses artificial intelligence to analyze waste items provided by
the user and then produces practical recommendations for handling the
waste responsibly.

## Problem Statement
Waste management is a common challenge in homes, schools, businesses, and
communities. People may have difficulty identifying different types of
waste and deciding how each item should be handled.

Incorrect disposal can result in recyclable materials being mixed with
general waste, electronic waste being disposed of incorrectly, and
organic waste not being separated for possible composting or other
appropriate uses.

There is also a lack of simple, accessible guidance that helps people
move from simply identifying waste to taking practical action.

Eco Waste Assistant addresses these problems by analyzing waste items
and providing users with clear and practical waste-management
recommendations.

## Who Benefits?
The Eco Waste Assistant can benefit:
- Households
- Students
- Schools
- Small businesses
- Community members
- People who want to improve their waste-management practices

## What the Tool Does
The Eco Waste Assistant provides two main AI-powered stages.

### Stage 1: Waste Analysis
The user provides one or more waste items.
For example:Plastic bottle, banana peels, old phone

The first AI stage analyzes the items and identifies information such as:
- Waste item
- Waste category
- Reuse possibility
- Recycling possibility
- Environmental concern

The first AI response is returned in JSON format so that the Python
program can process the information.

### Stage 2: Action Plan
The second AI stage receives the results from Stage 1.
It uses those results to create a practical action plan explaining what
the user can do with each waste item.

The recommendations may include:
- How to separate the waste
- Whether an item may be reused
- Whether an item may be recycled
- Appropriate handling of special waste
- Ways to reduce waste
- Practical waste-management actions

The second stage therefore turns the analysis from Stage 1 into
something the user can act on.

## Main Features
- AI-powered waste analysis
- Waste classification
- Recycling guidance
- Waste separation guidance
- Reuse suggestions
- Waste-reduction recommendations
- Two connected AI API calls
- JSON data handling
- Menu-driven user interaction
- Error handling
- Saved output
- Secure API key management

## How the Tool Works
The basic process is:

    User
      |
      
    Python Menu
      |
      
    User enters waste
      |
      
    AI Call 1
    Waste Analysis
      |
      
    JSON Result
      |
      
    AI Call 2
    Action Plan
      |
      
    Display Result
      |
      
    Save Output to File

The second AI call uses the result produced by the first AI call.

## Menu
The tool will provide a menu such as:
 
       ECO WASTE ASSISTANT
    
    1. Analyze My Waste
    2. Get a Waste Disposable Action Plan
    3. Exit

    Enter your choice:

## Example

### User Input

    Plastic bottle , banana peels , old phone

### Stage 1: Analysis
The AI identifies the waste items and classifies them.
Example:

    Plastic bottle : Plastic/Recyclable
    Banana peels : Organic waste
    Old phone : Electronic waste

### Stage 2: Action Plan
The AI then provides practical guidance for each item.
For example:

    Plastic bottle;
    Separate and prepare it for appropriate recycling.

    Banana peels;
    Separate them from general waste and consider composting.

    Old phone;
    Keep it separate from ordinary household waste and use an
    appropriate electronic-waste collection option.

## Technologies Used
- Python
- Artificial Intelligence API
- JSON
- GitHub
- VS Code
- Environment variables (.env)

## Project Structure

    Eco-Waste-Assistant-Four-Stars-Group
    
    * eco-waste-assistant.py
    *README.md
    *.git ignore
    *.env

The .env file is used locally to store the API key and must not be
committed to GitHub.

## How to Run
The project will be run using Python from the command line or an IDE
such as VS Code.

After the Python environment and required libraries have been installed,
the program can be started with;
    python eco_waste_assistant.py

## API Key Setup
The AI API key will be stored in an environment variable or .env file.

The API key must not be written directly inside the Python source code
and must never be committed to the GitHub repository.

## Error Handling
The program will handle common problems such as:
- Empty user input
- Invalid menu choices
- Failed API requests
- Invalid JSON responses
- Internet or connection problems

The program should display a useful error message instead of crashing.

## Group Members
- Member 1: Gladys M. Samuel
- Member 2: Agnes M. Njoroge
- Member 3: Peninah Barasa 
- Member 4: Selina Wanza Ndunga

## Project Goals
The main goal of the Eco Waste Assistant is to use artificial
intelligence to help users make better decisions about waste.

The project also demonstrates the use of:
- AI instruction design
- Python programming
- API integration
- JSON handling
- Error handling
- Secure API key management
- GitHub collaboration

## Future Improvements
With more development, the Eco Waste Assistant could be improved by
adding:
- A larger waste-item database
- More localized waste-management information
- Support for images of waste items
- More detailed recycling guidance
- Community waste-collection information
- A graphical user interface
- Additional waste-reduction features

## Project Status
The project is ready for submission and demonstrates two connected AI API calls, a menu-driven interface, JSON processing, error handling, and saved output.

