# 🐍 Learning Python at the University of Glasgow

This repository contains Python teaching materials for students at the **James Watt School of Engineering, University of Glasgow**.

The materials include lecture notes, lecture slides, programming examples, and optional projects. Although the repository is primarily intended for University of Glasgow students, anyone interested in learning Python is welcome to use it.

---

## ⚠️ Required topics for the course and examination

Students only need to study the following seven topics:

1. **Variables and operators**
2. **Control flow**
3. **Built-in data structures**
4. **Functions**
5. **Object-oriented programming**
6. **NumPy**
7. **Matplotlib**
   - Only simple plotting of \(y\) against \(x\) is required.

> [!IMPORTANT]
> To achieve the best possible result, students should focus on mastering these seven topics rather than attempting to study every file in the repository.

The following chapters are provided as optional materials for independent study:

- **Errors and exceptions**
- **Pandas**

Other materials on topics such as CuPy, PyTorch, numerical integration, curve fitting, and GPU computing are also optional unless stated otherwise by the lecturer.

---

## 📂 Repository structure

```text
uog-python/
├── lecture_notes/
│   ├── pdf/
│   ├── html/
│   └── ipynb/
├── slides/
│   ├── pdf/
│   └── html/
├── projects/
├── advanced_learning/
├── QandA.ipynb
└── run_live_lecture.ipynb
```

### `lecture_notes`

This directory contains the main course notes.

The original notes are written as **Quarto source files** with the `.qmd` extension. These files are compiled into three formats:

- `lecture_notes/pdf`: PDF files for reading, printing, and annotation
- `lecture_notes/html`: HTML files for reading in a web browser
- `lecture_notes/ipynb`: Jupyter Notebooks for running and modifying the Python code

Students who want to practise the examples should use the `.ipynb` files. Students who only want to read the materials may use the PDF or HTML versions.

Students are not required to learn Quarto for this course. Those interested in Quarto can visit the [official Quarto website](https://quarto.org/).

### `slides`

This directory contains the lecture slides. The original slides are also written as Quarto `.qmd` files.

The generated slides are organised into:

- `slides/pdf`: PDF versions for reading, downloading, and annotation
- `slides/html`: browser-based versions of the presentations

The HTML versions may include navigation, animations, syntax-highlighted code, and other interactive presentation features.

If an HTML file has a corresponding directory ending in `_files`, keep the HTML file and that directory together.

### `projects`

This directory contains optional programming and numerical-computing projects, including topics such as:

- Curve fitting
- Numerical integration
- Adaptive integration
- Gaussian quadrature
- Roman numeral calculation

These projects provide additional practice but are not automatically part of the examination.

### `advanced_learning`

This directory contains optional materials on more advanced topics, such as GPU computing and CuPy.

### Root-level notebooks

- `QandA.ipynb` contains supplementary questions, answers, and examples.
- `run_live_lecture.ipynb` is used for demonstrations and live coding during lectures.

The presence of material in these notebooks does not automatically mean that it is examinable.

---

## 🚀 Opening the lecture notes

The `.ipynb` files can be opened using:

- Jupyter Notebook
- JupyterLab
- Visual Studio Code with the Jupyter extension
- Anaconda Navigator

To start Jupyter Notebook from a terminal, run:

```bash
jupyter notebook
```

To start JupyterLab, run:

```bash
jupyter lab
```

Navigate to `lecture_notes/ipynb` and open the required notebook.

---

## ⬇️ Downloading the repository

### Download as a ZIP file

1. Select the green **Code** button on this repository.
2. Select **Download ZIP**.
3. Extract the downloaded ZIP file.

### Clone using Git

```bash
git clone https://github.com/khiemnguyen0407/uog-python.git
```

To download later updates:

```bash
cd uog-python
git pull
```

The repository is updated throughout the teaching period, so students should update their local copy regularly.

---

## 📌 Final reminder

For the course and examination, focus on:

1. Variables and operators
2. Control flow
3. Built-in data structures
4. Functions
5. Object-oriented programming
6. NumPy
7. Simple plotting with Matplotlib

**Errors and exceptions, Pandas, projects, and advanced-learning materials are optional.**