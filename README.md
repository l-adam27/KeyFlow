# KeyFlow  —  Programmable Macro Keyboard

**A compact, customizable 6-key macro pad with a rotary encoder for fast system control.**

---

## 🚀 Overview

The **KeyFlow Pad** is a compact macro keyboard designed to improve productivity and daily workflow efficiency by mapping common system actions to physical keys and a rotary encoder.

It features **six keys and one rotary knob**, providing quick access to frequently used system actions such as screenshots, media control, desktop management, focus tools, and microphone control.

This project was developed as part of the **Hack Club Blueprint** program.

---

## 🔧 Default Key Layout (Current Version)

> ⚠️ **Important:**
> The key mappings listed below are the **default configuration** included in the current firmware.
> These mappings are **not permanent** and serve as a functional starting point.

### 🔘 Keys

| Key   | Function                 |
| ----- | ------------------------ |
| Key 1 | Screenshot tool          |
| Key 2 | Play / Pause media       |
| Key 3 | Lock screen              |
| Key 4 | Focus mode               |
| Key 5 | Clean desktop            |
| Key 6 | Microphone mute / unmute |

### 🎚️ Rotary Encoder (Knob)

* **Rotate:** System volume control
* **Press:** Audio mute / unmute

---

## 🧠 Customization & Future Software

Although the current firmware ships with **predefined default actions**, the KeyFlow Pad is designed to be **fully customizable**.

🚧 **Planned Feature (Future Release):**
A dedicated **KeyFlow desktop application** will be released to allow users to:

* Remap all keys visually
* Assign custom actions or macros
* Change rotary encoder behavior
* Save and switch between profiles

This application will eliminate the need to modify firmware files manually, making customization accessible to all users.

---

## 📂 Project Structure

```
KeyFlow/
├─ CAD/
│   └─ KeyFlow_complete.step
│
├─ PCB/
│   ├─ keyflow.kicadpro
│   ├─ keyflow.kicadsch
│   └─ keyflow.kicad_pcb
│
└─ Firmware/
    ├─ lib
    │   └─ adafruit_hid
    ├─ main.py
    └─config.py
```

---

## 🧪 Firmware

The firmware is built using **KMK (Keyboard Macro Keyboard)** on a **Seeed XIAO RP2040**, running CircuitPython.

* USB HID compliant (plug and play)
* No drivers required
* Handles individual keys and rotary encoder input
* Sends standard keyboard and media events to the operating system

---

## 📸 Screenshots


* PCB layout
<img width="1215" height="691" alt="image" src="https://github.com/user-attachments/assets/6514ee26-ae91-4564-a6c4-a81fb0778fe8" />

* Schematic
<img width="681" height="564" alt="image" src="https://github.com/user-attachments/assets/ff6be921-9912-4641-bb0c-a507a5ce5952" />

* 3D case render
<img width="1438" height="656" alt="image" src="https://github.com/user-attachments/assets/6ae4af51-f90d-49bf-ae08-b4f7dd82973f" />

* Assembly preview
<img width="1520" height="722" alt="6c189676-9e64-4411-9dcd-47980507e1f8" src="https://github.com/user-attachments/assets/9dc7e77d-6523-4deb-b9ab-d005c8c81839" />


---

## 📦 BOM

| Component                       | Quantity |
| ------------------------------- | -------- |
| Seeed XIAO RP2040               | 1        |
| Mechanical switches (MX-style)  | 6        |
| EC11 Rotary Encoder (with push) | 1        |
| Custom PCB                      | 1        |
| USB cable                       | 1        |
| 3D printed case                 | 1        |

---

## 📐 CAD & PCB

* **CAD:** Single assembled model provided as a `.STEP` file
* **PCB:** Complete KiCAD project including schematic and layout
* Designed for compact size and ease of assembly

---

## 📍 Project Status

* ✅ Hardware design: complete
* ✅ PCB design: complete
* ✅ Firmware (default layout): complete
* 🚧 Desktop configuration app: planned future update
* ⏳ Physical testing: pending (parts not yet received)

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* Hack Club & Blueprint Program
* KMK Firmware Framework
* Open-source hardware community
