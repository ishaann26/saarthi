
### Python-Based Academic Support & Progress Insight System

Saarthi is a lightweight, offline school-support application designed to
help teachers share academic updates and help students access learning
materials and review their academic performance.

## Features

-   **Teacher Notice Panel:** Post homework, announcements, and
    classroom updates.
-   **Study Material Access:** Let students view learning content saved
    in text files.
-   **Academic Performance Viewer:** Read marks from a CSV file and
    visualize subject-wise performance with charts.
-   **Simple Interface:** A straightforward Tkinter-based interface with
    buttons, menus, and text areas.
-   **Offline File Storage:** Store notices, materials, and marks
    locally using `.txt` and `.csv` files.
-   **Easy Navigation:** Move between the main sections without needing
    an online service or database.

## Tech Stack

-   **Language:** Python
-   **GUI:** Tkinter
-   **Data storage:** Text files (`.txt`) and CSV (`.csv`)
-   **Visualization:** Matplotlib

## How It Works

1.  Choose the Teacher or Student role.
2.  Teachers add notices, homework, or study content.
3.  Students open the relevant section to read announcements and
    learning materials.
4.  The performance module loads marks from a CSV file.
5.  Matplotlib displays a subject-wise performance chart.
6.  Return to the main panel to use another section.

## Project Structure

The application uses local files for simple offline storage. A typical
setup may include:

``` text
saarthi/
├── main.py
├── announcements.txt
├── materials.txt
├── records.csv
└── README.md
```

*Adjust the filenames above to match the files in your repository.*

## Getting Started

### Requirements

-   Python 3 installed
-   Tkinter (usually included with standard Python installations)
-   Matplotlib

### Install Matplotlib

``` bash
python -m pip install matplotlib
```

### Run the Application

After uploading the project files, open a terminal in the repository
folder and run the Python entry-point file. If your main file is named
`main.py`, use:

``` bash
python main.py
```

If your entry-point file has a different name, replace `main.py` with
that filename.

## Data and Privacy

Saarthi stores data locally in text and CSV files and is designed for
offline use. Use sample or anonymized data in public repositories. Do
not upload real student records, personal information, passwords, or
other confidential school data.

## Current Scope

This version focuses on basic academic notices, learning-material
access, local record handling, and performance visualization. Features
and filenames may vary according to the code included in the repository.

## Future Improvements

-   More structured role-based access
-   Improved validation and error handling
-   Exportable academic reports
-   Additional performance insights and dashboard improvements

## Author

**Ishaan Srivastava**

Built as a project exploring how Python, file handling, GUI development,
and data visualization can support everyday academic workflows.
