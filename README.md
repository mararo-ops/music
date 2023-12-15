# Local Art Gallery Management System 

## Introduction

The Local Art Gallery Management System is a command-line application designed to assist art galleries in managing artists, artworks, and overall gallery data. This README provides essential information for setting up, using, and contributing to the project.

## Problem Statement

Art galleries often face challenges in efficiently organizing and managing information about artists and their artworks. A lack of a centralized system can lead to difficulties in tracking artists, managing their works, and providing a seamless experience for gallery administrators.

## Solution

The project aims to address these challenges by providing a digital management system for art galleries. This system allows users to add artists, artworks, update artwork details, and view comprehensive data about artists and their creations. It aims to streamline the management process for art galleries, enhancing the overall efficiency and organization of gallery operations.

## Table of Contents

    .Getting Started
        Prerequisites
        Installation
    .Usage
    .Contributing
    .License

    Getting Started
## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

    Python (version 3.6 or higher)
    Pipenv (for managing virtual environments)

## Installation

    Clone the repository:

    bash

git clone <repository-url>
cd artGalleryManagement

Set up a virtual environment using Pipenv:

bash

pipenv install

Activate the virtual environment:

bash

pipenv shell

## Usage

    Adding Artist:

    bash

python cli.py 1

Follow the prompts to provide details such as name, age, birthplace, and style of work.

Adding Artwork:

bash

python cli.py 2

Follow the prompts to add artwork details, including the artist's name, year of making, unique title, style of art, and price.

Deleting Artwork by Title:

bash

python cli.py 3

Enter the unique title of the artwork to delete.

Updating Artwork:

bash

python cli.py 4

Enter the unique title of the artwork to update and follow the prompts to modify details.

Viewing All Data:

bash

python cli.py 5

Enter the password to view all data.

Exiting:

bash

python cli.py 6


## License

This project is licensed under the MIT License. For details, see the LICENSE.md file.

Thank you for contributing to the Local Art Gallery Management System, and we look forward to growing our community of art enthusiasts and gallery administrators together!