# Tkinter Desktop Converters Suite

A collection of **four lightweight, graphical user interface (GUI) conversion tools** built using Python and Tkinter. This monorepo contains independent desktop utilities designed to perform quick metric-to-imperial and temperature conversions with a clean, grid-based interface.

---

## 🛠️ Project Structure

This repository acts as a single suite containing four separate Python conversion scripts:

```text
├── c_to_f_converter.py      # Celsius to Fahrenheit Desktop App
├── f_to_c_converter.py      # Fahrenheit to Celsius Desktop App
├── km_to_mi_converter.py     # Kilometers to Miles Desktop App
├── mi_to_km_converter.py     # Miles to Kilometers Desktop App
└── README.md                 # Project documentation
```

---

## 🚀 Individual Project Overview

### 1. Celsius to Fahrenheit Converter
* **File:** `c_to_f_converter.py`
* **Description:** Formulates a real-time conversion from Celsius to Fahrenheit degrees.
* **Core Logic:** Rounds the standard mathematical equation `(C × 9/5) + 32` up to 2 decimal places.

### 2. Fahrenheit to Celsius Converter
* **File:** `f_to_c_converter.py`
* **Description:** Provides inverse calculation mapping Fahrenheit parameters back into Celsius.
* **Core Logic:** Evaluates variables dynamically using `(F - 32) × 5/9` rounded to 2 decimal points.

### 3. Kilometers to Miles Converter
* **File:** `km_to_mi_converter.py`
* **Description:** Distance utility built to translate metric kilometers to imperial miles.
* **Core Logic:** Multiplies user inputs by a fixed precision conversion ratio of `0.621371`.

### 4. Miles to Kilometers Converter
* **File:** `mi_to_km_converter.py`
* **Description:** Distance calculator transforming standard miles into precision kilometers.
* **Core Logic:** Computes lengths utilizing the standard ratio `M × 1.60934` capped at 2 decimal places.

---

## 📦 Prerequisites & Installation

To launch these application instances, ensure you have **Python 3.x** environment variables globally mapped on your local desktop.

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sergio-a-juarez-1/Python-Projects
   cd Conversion-Programs
   ```

2. **Verify Tkinter Setup:**
   Tkinter usually ships bundled directly alongside core Python installations. If missing, configure it via standard system packaging tools:
   * **Ubuntu/Debian:** `sudo apt-get install python3-tk`
   * **macOS/Windows:** Automatically provided via official Python installers.

---

## 🖥️ Usage Instructions

Navigate directly inside the repository directory root and invoke the target tool via standard Python executions:

* Run **Celsius to Fahrenheit**:
  ```bash
  python c_to_f_converter.py
  ```
* Run **Fahrenheit to Celsius**:
  ```bash
  python f_to_c_converter.py
  ```
* Run **Kilometers to Miles**:
  ```bash
  python km_to_mi_converter.py
  ```
* Run **Miles to Kilometers**:
  ```bash
  python mi_to_km_converter.py
  ```

---

## 🎨 UI & Layout Specifications

Each application window executes an identical, lightweight structural composition pattern optimized for speed:
* **Input Layer:** Width-bounded single `Entry` widget positioned on grid coordinates `(0, 1)`.
* **Output Display:** Instant interactive dynamic updates via `Label.config()` state mutations.
* **Layout Design:** Strict adherence to Tkinter standard `.grid()` geometric placement maps.
