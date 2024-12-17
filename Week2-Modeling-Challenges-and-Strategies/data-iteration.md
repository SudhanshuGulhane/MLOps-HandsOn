# Best Practices for Data Augmentation (Unstructured Data)

## Key Principles
- **Purpose of Data Augmentation**  
  - Generate examples that are realistic.  
  - Ensure humans or baselines can still perform well.  
  - Focus on examples the algorithm currently struggles with.

- **Framework for Systematic Decisions**  
  - **Realistic Examples**: The data should mimic the target environment.  
  - **Clear X to Y Mapping**: Humans must easily recognize the data (e.g., speech/text).  
  - **Challenging for the Algorithm**: The algorithm should perform poorly on augmented data while humans perform well.

---

## Checklist for Augmented Data
1. **Does it look/sound realistic?**
2. **Can humans still identify the signal?**
3. **Does the algorithm struggle with it?**

---

## Examples of Data Augmentation

### 1. Speech Recognition
- Add **background noise** (e.g., cafe noise, music) to clean audio.  
- Control parameters:  
  - Type of noise.  
  - Noise loudness relative to speech.  

### 2. Image Data
- **Basic Transformations**:  
  - Flip horizontally.  
  - Adjust contrast/brightness.  
- Avoid overly distorted examples (e.g., too dark to detect scratches).  
- Use tools:  
  - **Photoshop** for synthetic examples.  
  - **GANs** for automatic augmentation (optional and sometimes overkill).

---

## Efficient Data Augmentation Strategy
- Avoid repeatedly training models to validate augmentation parameters.  
- **Sanity check** augmented data first with the checklist.

---

## Model vs. Data Iteration
- **Model Iteration**: Improves performance through error analysis and model changes.  
- **Data Iteration**: Focuses on improving data quality and adding relevant data.  

---

## Key Insight
- Adding realistic, challenging, yet human-interpretable data helps algorithms improve.  
- Augmentation tailored to error analysis (e.g., struggling with cafe noise) leads to faster performance gains.
