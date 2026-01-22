# KeyFlow  —  costumizable keypad for your favorite shortcuts

**Built for faster workflow and maximum productivity**

---

## Main

**Keyflow** is a small macropad, designed to give the user the fastest ways to control your enviroment

---

## Standart layout

>  **Important:**
> The key mapping listed below is the fabric standart, we will launch a software that can change all the functions automaticly later on.

### 🔘 Keys

| Key   | Function                 |
| ----- | ------------------------ |
| Key 1 | Screenshot        |
| Key 2 | Play / Pause media       |
| Key 3 | Lock screen              |
| Key 4 | Focus mode               |
| Key 5 | Clean desktop            |
| Key 6 | Microphone mute / unmute |

### Rotary Encoder (Knob)

* **Rotate:** System volume control
* **Press:** Audio mute / unmute

---

## Project Structure

```
KeyFlow/
├─ CAD/
│   ├─KeyFlow_TOP
│   ├─KeyFlow_BASE
│   └─ KeyFlow_complete_WITH_PCB.step
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

## Attachments


* PCB
<img width="1215" height="691" alt="image" src="https://github.com/user-attachments/assets/6514ee26-ae91-4564-a6c4-a81fb0778fe8" />

* Schematic
<img width="681" height="564" alt="image" src="https://github.com/user-attachments/assets/ff6be921-9912-4641-bb0c-a507a5ce5952" />

* 3D case render
<img width="1438" height="656" alt="image" src="https://github.com/user-attachments/assets/6ae4af51-f90d-49bf-ae08-b4f7dd82973f" />

* Assembly preview
<img width="1520" height="722" alt="6c189676-9e64-4411-9dcd-47980507e1f8" src="https://github.com/user-attachments/assets/9dc7e77d-6523-4deb-b9ab-d005c8c81839" />


---

## BOM

| Component                       | Quantity |
| ------------------------------- | -------- |
| Seeed XIAO RP2040               | 1        |
| Mechanical switches (MX-style)  | 6        |
| EC11 Rotary Encoder (with push) | 1        |
| Custom PCB                      | 1        |
| USB cable                       | 1        |
| 3D printed case                 | 1        |

---

## License

MIT License

---

## Special Thanks:
* HackClub 
* Shadow (1st to reviewing the project, ty for the tips btw)
* My Dad
* My Mom
