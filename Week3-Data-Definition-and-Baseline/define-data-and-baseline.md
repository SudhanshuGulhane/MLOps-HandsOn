# Why is Data Definition Hard?

## Key Challenges

1. **Ambiguous Labeling Instructions**  
   - Multiple valid ways to label the same data.  

2. **Inconsistent Labels**  
   - Inconsistent labeling conventions lead to poor model performance.  
---

## Best Practices for Data Definition

1. **Define Clear Labeling Instructions**  
   - Ensure all labelers follow the same conventions.  

2. **Consistency is Key**  
   - Avoid mixing different labeling approaches within the dataset.  
   - Choose one clear labeling standard that works for your application.

3. **Clarify Data Inputs and Outputs**  
   - Clearly define what constitutes the input data (`x`) and the labels/outputs (`y`).  

---

## Why Data Definition Matters

- Ambiguous or inconsistent data can undermine model performance.  
- Preparing high-quality, consistent datasets has a larger impact on project success than many realize.  
- Practical applications often require custom datasets rather than pre-downloaded ones.  

---

# More Label Ambiguity Examples

## Key Concepts

### **Label Ambiguity**
- **Ambiguity in Labels**:  
  - Different interpretations of the same data can lead to inconsistent labels.  
  - Examples of ambiguous tasks:  
    - Transcribing noisy audio.  
    - Determining if two user records belong to the same person.  
    - Classifying transactions as fraudulent or legitimate.  

- **Impact of Ambiguity**:  
  - Inconsistent or noisy labels degrade model performance.  
  - Consistent labeling improves algorithm accuracy, even if the ground truth is inherently ambiguous.

---

### **Best Practices to Address Ambiguity**
1. **Clear Labeling Instructions**:  
   - Ensure all labelers follow the same conventions to reduce noise and randomness.  

2. **Input Quality Matters**:  
   - Inputs (`x`) must be of sufficient quality for humans to interpret effectively.  
     - Example: Improve image lighting or resolution if defects are hard to see.  

3. **Define Clear Inputs and Outputs**:  
   - Clearly define what constitutes the input (`x`) and target label (`y`).  

4. **Features for Structured Data**:  
   - For tasks like user ID merge or spam detection, adding relevant features (e.g., GPS location, behavioral patterns) can improve predictions.  
   - Only use data in ways that respect user privacy and permissions.

---

### **Examples of Ambiguous Tasks**
1. **Speech Recognition**:  
   - Transcription differences (e.g., punctuation, spelling variations).  

2. **User ID Merge**:  
   - Deciding if two data records belong to the same individual.  

3. **Bot/Spam Detection**:  
   - Ambiguity in determining if an account is fake or spam.  

4. **Fraud Detection**:  
   - Uncertainty in labeling transactions as fraudulent or legitimate.  

5. **Behavioral Predictions**:  
   - Guessing user intent (e.g., job-seeking behavior on a website).  

---

### **Improving Data for Learning Algorithms**
1. **Addressing Poor Input Quality**:  
   - If inputs are insufficiently informative (e.g., dark images), improve the quality of sensors or data collection.  

2. **Consistency in Target Labels**:  
   - Focus on clear labeling conventions to ensure consistent and meaningful labels.

3. **Systematic Framework for Data Issues**:  
   - Identify and address ambiguities in both inputs (`x`) and target labels (`y`) systematically to improve dataset quality and model performance.

---

## Summary
- Label ambiguity and poor input quality can significantly impact the performance of learning algorithms.  
- Address these issues by ensuring clear labeling conventions, high-quality inputs, and meaningful features.  
- Systematic improvements to data definition and labeling reduce noise and boost model accuracy.

---

# Major Types of Data Problems

### **1. Unstructured Data (Small Data Sets)**
- **Example**: Manufacturing inspection with 100 images.  
- **Best Practices**:  
  - Use **data augmentation** (e.g., image flips, noise for audio).  
  - Ensure **clean, consistent labels**; manually review all examples.  

### **2. Unstructured Data (Large Data Sets)**
- **Example**: Speech recognition with 50M examples.  
- **Best Practices**:  
  - Focus on **data processes** for consistent labeling.  
  - Use **data augmentation** to synthesize more examples.  

### **3. Structured Data (Small Data Sets)**
- **Example**: Predict housing prices from 52 examples.  
- **Best Practices**:  
  - Manually verify and clean data.  
  - Add meaningful features if possible (e.g., user location, timestamps).  

### **4. Structured Data (Large Data Sets)**
- **Example**: Product recommendation with 1M users.  
- **Best Practices**:  
  - Develop detailed **labeling instructions** for large teams.  
  - Difficult to augment or synthesize new structured data.  

### **Data Quality Matters**
- **Small Data Sets**:  
  - Clean labels are critical as errors disproportionately affect performance.  
  - Small labeling teams make it easier to align on consistent conventions.  

- **Large Data Sets**:  
  - Clean labels still help but are harder to ensure due to scale.  
  - Emphasize scalable **data processes** and clear instructions for large labeling teams.  

---

# Small Data and Label Consistency

## Key Concepts

### **Importance of Label Consistency**
- In small datasets, clean and consistent labels are critical.  
- Inconsistent labels make it harder for learning algorithms to fit accurate models.  
- With consistent labels, even small datasets can yield high-performing models.

### **Challenges with Small Data**
1. **Noisy Labels**:  
   - Small datasets are more sensitive to noise in labels.  
   - Clean labels help confidently fit models, even with limited data.

2. **Ambiguous Labeling**:  
   - Different labelers may interpret data differently without clear guidelines.  
   - Example: Agreement on specific thresholds (e.g., scratch length in defect detection) improves consistency.

---

### **Large Datasets with Small Data Challenges**
- Even in big datasets, rare events create "small data" scenarios.  
  - **Examples**:  
    - Rare search queries in web search engines.  
    - Rare but critical occurrences in self-driving cars (e.g., child running across the road).  
    - Long-tail items in product recommendation systems.  

- Ensuring **label consistency** for rare events improves model performance, even in large datasets.

---

## Best Practices for Small Data
1. **Define Clear Labeling Guidelines**:  
   - Establish thresholds or standards to minimize ambiguity.  
   - Align labelers on a single labeling convention.

2. **Manually Review Labels**:  
   - Small datasets allow for thorough manual review to ensure consistency.

---

# Improving Label Consistency

## Key Concepts

### **General Process to Improve Label Consistency**
1. **Identify Inconsistencies**:  
   - Have multiple labelers label the same examples.  
   - Allow labelers to re-label examples after a break to check self-consistency.

2. **Facilitate Discussion**:  
   - Bring labelers together (or subject matter experts) to resolve disagreements.  
   - Define a consistent labeling standard (`y`) and document it.

3. **Update Instructions**:  
   - Revise labeling guidelines based on discussions to improve future labeling.  

4. **Iterate**:  
   - Continue the process until disagreements are minimized.  

---

### **Strategies to Enhance Consistency**
1. **Standardize Definitions**:  
   - Agree on clear definitions for ambiguous labels.  

2. **Merge Classes**:  
   - Combine overlapping or unclear classes (e.g., deep vs. shallow scratches no phone screen) if differentiation isn’t critical.  

3. **Add New Classes for Uncertainty**:  
   - Introduce a "borderline" or "ambiguous" class to handle unclear cases.  

---

### **Special Considerations**
- **Input Quality**:  
  - If inputs (`x`) lack sufficient information (e.g., dark images), consider improving data quality (e.g., better lighting).  

- **Unstructured Data**:  
  - Use consistent labeling conventions for tasks like image annotation or transcription.  
  - Introduce tags like "unintelligible" for ambiguous data.  

- **Small vs. Big Datasets**:  
  - **Small Datasets**:  
    - Few labelers allow for direct discussions and agreement on specific examples.  
  - **Big Datasets**:  
    - A small team defines consistent standards, which are shared with a larger labeling team.

---

### **Cautions with Voting (Consensus Labeling)**
- Voting can reduce noise but is often overused.  
- Focus on improving labeling instructions to reduce noise at the source before relying on voting.

---

# Human Level Performance (HLP)

## Key Concepts

### **Uses of HLP**
1. **Establishing Baselines**:
   - Helps estimate **Bayes error** (irreducible error) and set realistic expectations for achievable performance.  
   - Useful for error analysis and prioritization.  

2. **Handling Unrealistic Expectations**:
   - Helps communicate realistic targets when stakeholders request unreasonably high accuracy (e.g., 99%).  

3. **Academic Benchmarking**:
   - Demonstrating performance exceeding HLP can validate research significance and aid in publication.  

---

### **Limitations of HLP**
1. **Inconsistent Ground Truth**:
   - HLP often measures agreement between humans, not absolute performance.  
   - Disagreement among labelers can lead to misleading benchmarks.  

2. **Machine Learning Advantage**:
   - Models may exploit statistical biases in labels (e.g., consistently choosing one convention) to appear superior without adding practical value.  

3. **Masking Model Errors**:
   - Performance gains in trivial cases (e.g., resolving labeling ambiguities) can overshadow errors in critical tasks, misleading evaluations.

---

### **Best Practices**
1. **Use HLP Cautiously**:
   - Employ HLP for setting baselines and error analysis but avoid over-relying on it to "prove" model superiority.

2. **Focus on Practical Outcomes**:
   - Prioritize building useful applications over achieving performance benchmarks against HLP.

3. **Raise HLP**:
   - Improve human label consistency to elevate both HLP and model performance.

---

# Raising Human Level Performance (HLP)

## Key Concepts

### **HLP in Machine Learning**
1. **Useful for Applications**:  
   - Establishes a baseline of what is achievable for tasks where human performance is a reference point.  
   - Guides error analysis and prioritization.

2. **Ground Truth Types**:  
   - **Externally Defined**:  
     - Example: Medical diagnosis based on biopsy results.  
     - HLP measures how well humans or algorithms predict an objective ground truth.  
   - **Human Defined**:  
     - Example: Labeling X-rays by doctors or classifying visual defects.  
     - HLP reflects agreement between humans rather than absolute accuracy.

---

### **Improving HLP**
1. **Address Inconsistent Labels**:  
   - Discrepancies among labelers often indicate ambiguous instructions.  
   - Define clearer labeling conventions (e.g., thresholds for defects).  

2. **Raise HLP**:  
   - Example: Aligning inspectors to agree on a 0.3mm threshold for scratches in defect detection can raise HLP significantly.  
   - Clean, consistent labels improve both HLP and machine learning model performance.  

---

### **Challenges of Raising HLP**
- **Makes Beating HLP Harder**:  
   - When HLP approaches 100%, it's harder for algorithms to outperform humans.  
   - However, improved data consistency ultimately benefits the application more than surpassing HLP.

- **Structured Data Use Cases**:  
   - While structured data often doesn’t rely on HLP, exceptions exist (e.g., user ID merging, fraud detection, spam classification).  
   - HLP helps identify labeling inconsistencies in such cases.

---

### **Benefits of Raising HLP**
1. **Cleaner Data**:  
   - Improved consistency leads to higher-quality data for model training.  
2. **Better Model Performance**:  
   - Consistent labels improve the ability of learning algorithms to make accurate predictions.  
3. **Useful Baseline**:  
   - Raised HLP sets realistic expectations for model accuracy and application feasibility.

---