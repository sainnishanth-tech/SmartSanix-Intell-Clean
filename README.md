<div align="center">

# 💎 SmartSan+ 
### *Stabilized IoT Sanitation Management for Smart Cities*

[![Hardware: ESP32](https://img.shields.io/badge/Hardware-ESP32-blue?style=for-the-badge&logo=espressif)](https://www.espressif.com/)
[![Logic: Stable IoT](https://img.shields.io/badge/Logic-Industrial_Grade-orange?style=for-the-badge)](https://github.com/)
[![Dashboard: Blynk](https://img.shields.io/badge/UI-Blynk_2.0-04D0BB?style=for-the-badge)](https://blynk.io/)

[System Flow](#-logic-architecture) • [Component Breakdown](#-bill-of-materials) • [Installation](#-quick-start)

</div>

---

## 🚀 The Core Philosophy
**SmartSan+** isn't just a sensor array; it is a **Decision Engine**. By implementing advanced software stabilization (Moving Averages and State Confirmation), we eliminate the "noise" common in cheap sensors, delivering a professional-grade facility management tool.

---

## 🧠 Logic Architecture (Anti-Spam System)

Most IoT prototypes fail in real-world scenarios due to sensor fluctuations. SmartSan+ utilizes a **State-Machine Approach**:

* **Odor Analytics:** Uses a 5-sample **Moving Average Filter** on the MQ-135 to ignore momentary spikes in gas levels.
* **Laser Occupancy:** Employs a **Confidence Counter**—the VL53L0X must confirm distance for 3 consecutive cycles before toggling "Occupied."
* **Fluid Verification:** The Water Level sensor validates cleaning only when a steady, averaged reading indicates a meaningful change in moisture levels.
* **One-Shot Alerting:** The Active Buzzer uses a **Cooldown Timer** to prevent infinite, annoying alarm loops.

---

## 📦 Bill of Materials (Project Costing)

Based on our final procurement from **Robocraze**, the total hardware footprint is optimized for high-performance at a low cost:

| Component | Function | Cost (₹) |
| :--- | :--- | :--- |
| **VL53L0X Laser Sensor** | Precise ToF Stall Occupancy | ₹131.00 |
| **MQ-135 Gas Module** | NH3 & Odor Monitoring | ₹111.00 |
| **Water Level Sensor** | Cleaning/Maintenance Verification | ₹21.00 |
| **Active Buzzer Module** | Emergency SOS Audio Output | ₹31.00 |
| **Tactile Push Buttons (10pk)**| SOS & Manual Reset Interface | ₹55.00 |
| **ESP32-WROOM-32** | Dual-Core IoT Processor & WiFi | *Prev. Board* |

---

## 🛠 Tech Stack & Tools

<details>
<summary><b>View Frameworks & APIs</b></summary>

* **Firmware:** MicroPython (v1.20+)
* **IoT Protocol:** Blynk 2.0 (WebSocket-based)
* **Library:** `micropython-vl53l0x`
* **Code Assistant:** ChatGPT/Gemini (Logic Optimization & Architecture)
* **Interface:** I2C (Sensors) & ADC (Analog Stabilization)
</details>

---

## 📸 Visual Documentation

### System Circuit Diagram
> [!IMPORTANT]
> ![Circuit Diagram](<img width="1408" height="768" alt="Gemini_Generated_Image_d48r2pd48r2pd48r" src="https://github.com/user-attachments/assets/59f325e9-12fb-43e2-b086-0d97284bc040" />
)
*Illustration of the ESP32 interfacing with the I2C VL53L0X and Analog MQ-135.*

### Industrial Dashboard
| Real-time Monitoring | Emergency SOS Panel |
| :---: | :---: |
| ![Dashboard 1](INSERT_LINK_HERE) | ![Dashboard 2](INSERT_LINK_HERE) |

---

## 💻 Quick Start

1.  **Environment Setup:** Ensure Thonny IDE is installed with the `micropython-vl53l0x` package.
2.  **Calibration:** * Power the **MQ-135** for 15 minutes before demoing to allow the heater to stabilize.
    * Set `DISTANCE_THRESHOLD` based on your specific restroom stall dimensions.
3.  **Flash:**
    ```bash
    # Upload main.py to ESP32 root
    ampy --port COM3 put main.py
    ```

---

## 📜 Credits & Disclosure
* **Hardware Sourcing:** Robocraze.
* **Software Design:** Developed with **Stabilization Logic** to prevent false triggers.
* **AI Disclosure:** Gemini was utilized for architectural planning, code stabilization logic (Debounce/Averaging), and Markdown documentation structure.

---

<div align="center">
  <p><b>Built for [Hackathon Name] 2026</b></p>
  <i>"Standardizing Hygiene through Accountable IoT"</i>
</div>
