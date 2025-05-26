# 👕 Dripolini Vibecheck AI  
### _Your fit. Upgraded._

<p align="center">
  <img src="img\mascot.png" alt="Dripolini Mascot" style="width: 100%; max-width: 700px; border-radius: 12px;" />
</p>


Welcome to **Dripolini Vibecheck AI**, a neural rendering–powered virtual stylist that analyzes your look and suggests outfit improvements using AI.  

Created as part of the **Neural Rendering in 3D** course project at Jagiellonian University.

---


## 🧠 What is this?

Dripolini is a virtual outfit assistant that takes a single photo of a person and:

- Detects the person and extracts fashion-relevant features
- Describes the current outfit using a vision-language model
- Analyzes the face for emotion, age, and gender
- Extracts the dominant color palette from the clothing
- Accepts a context (where are you going?)
- Builds a rich prompt to send to Gemini
- Suggests three potential clothing items from a local dataset
- Applies the selected item using CAT-VTON

All this is done **locally**, with only Gemini running via API.

---

## 🎯 Use Case

This project demonstrates how neural rendering and AI-driven multimodal systems can be used in personal fashion assistants, virtual try-on, and context-aware outfit selection.

---
## 🧱 Architecture Overview

```text
[ Input Image ]
      ↓
[ Feature Extraction ]
  - Face → age, gender, emotion
  - Outfit → Gemini captioning
  - Colors → dominant palette
  - Context → user input
      ↓
[ Prompt Assembly ]
      ↓
[ Gemini: 3 Outfit Suggestions ]
      ↓
[ User picks 1 ]
      ↓
[ CAT-VTON ]
      ↓
[ Virtual Try-On Output ]
```

## 🛠️ Tech Stack

| Component            | Technology                        |
| -------------------- | --------------------------------- |
| 🧠 Face Analysis     | DeepFace (`VGG-Face`)             |
| 🧥 Outfit Captioning | Gemini Pro Vision (1.5 Flash)     |
| 🎨 Color Palette     | OpenCV + KMeans                   |
| 🧍 Detection         | YOLOv8n (Ultralytics)             |
| 👗 Try-On Engine     | CAT-VTON                          |
| 🖥️ Frontend         | Streamlit                         |
| 📦 Dataset           | Custom CSV-based clothing catalog |

## 🚀 How to Run Locally
### 1. Clone the repository
```bash
git clone https://github.com/xFloly/dripolini-vibecheck-ai.git
cd ciuchy
```
### 2. Set up the environment
```bash
conda env create -f environment.yml
conda activate dripolini
```
Make sure you have ultralytics, streamlit, opencv-python, scikit-learn, deepface, and google-generativeai installed.

### 3. Add your Gemini API key

Set your API key as an environment variable before running the app:

```bash
export YOUR_GEMINI_API_KEY="your-real-api-key"
```
### 4. Prepare the dataset
Place your clothing images and clothes.csv file in the data/ folder. Each item should have:
```csv
id,path,description
1,data/hoodie.png,White hoodie with front zip
2,data/jeans.png,Slim-fit light blue jeans
...
```

### 5. Run the app
```bash
streamlit run app.py
```
## 📸 Demo
<img src="demo/demo.gif" width="600"/>

## 📚 Acknowledgements
[DeepFace](https://github.com/serengil/deepface)

[Google Generative AI (Gemini)](https://ai.google.dev/)

[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

[CatVTON](https://github.com/Zheng-Chong/CatVTON)