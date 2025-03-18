# Module-Progress-Calculator

## Overview
This project is a **Student Progress Tracker** that evaluates students' academic progress based on their credit scores in pass, defer, and fail categories. The system categorizes students into different outcomes and provides a histogram representation.

## Features
- **User Input Validation**
  - Ensures only integers are accepted
  - Restricts inputs to valid credit ranges (0-120 in steps of 20)
- **Categorization of Student Progress**
  - `Progress`: 120 pass credits
  - `Progress (Module trailer)`: 100 pass credits
  - `Module retriever`: 60 or 80 pass credits
  - `Exclude`: 80 or more fail credits
- **Data Storage & Output**
  - Displays results in real-time
  - Generates a histogram visualization
  - Saves outcomes in a text file (`20222163_shakinya.txt`)
  - Uses a dictionary to store student results

## Installation & Setup
### Prerequisites
- Python 3.x installed

### Running the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/student-progress-tracker.git
   ```
2. Navigate to the project directory:
   ```sh
   cd student-progress-tracker
   ```
3. Run the script:
   ```sh
   python progress_tracker.py
   ```

## Usage
- Follow the prompts to enter student credit data.
- The system will determine and display the student's progress category.
- You can enter multiple students' data before exiting and viewing results.
- A histogram is generated to visualize all outcomes.

## File Storage
- The program stores results in `20222163_shakinya.txt`, listing students' outcomes.
- It also uses a dictionary (`student_dict`) to hold student records.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to your fork and submit a pull request.


