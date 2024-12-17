# Best Practices for Feature Engineering (Structured Data Problems)

## Key Insights
- **Challenge with Structured Data**:  
  - Creating new training examples is difficult due to finite data (e.g., fixed users, products, restaurants).  
  - Instead, focus on **adding features** to existing examples.

- **Approach**:  
  - Use **error analysis** to identify performance gaps.  
  - Add relevant features to improve the model’s ability to capture important information.

---

## Example: Restaurant Recommendation System

### Problem
- **Issue**: System recommends meat-only restaurants to vegetarian users.  
- **Fixed Pool**: Limited users and restaurants make data augmentation impractical.

### Solution
- Add features:  
  1. **User Feature**: Indicate if a user is likely vegetarian.  
     - Use a soft feature (e.g., percentage of vegetarian orders).  
  2. **Restaurant Feature**: Indicate if a restaurant has vegetarian options.  
     - Extract from menus using manual coding or algorithms.

---

## General Steps for Feature Engineering

1. **Start with a Model**: Train the initial model.  
2. **Perform Error Analysis**:  
   - Identify recurring issues or systematic errors.  
   - Sources of insights:  
     - User feedback.  
     - Competitor benchmarks.  

3. **Add New Features**:  
   - Examples:  
     - **Behavioral Features**: Users who only order tea, coffee, or pizza.  
     - **Content Features**: Restaurants’ menu details.  

4. **Iterate and Test**: Evaluate improvements and repeat the process.

---

## Collaborative Filtering vs. Content-Based Filtering

### Collaborative Filtering
- Recommends items based on user similarity (e.g., “users like you liked this”).  
- **Limitation**: Struggles with **Cold Start Problem** – new products or users lack sufficient data.  

### Content-Based Filtering
- Uses item descriptions (e.g., restaurant menus, product features) for recommendations.  
- **Advantage**:  
  - Can recommend new products with little user interaction.  
  - Avoids dependence on historical user behavior.

---

## Data Iteration for Structured Data

- **Process**:  
  1. Train a model.  
  2. Use error analysis, user feedback, or benchmarking to identify gaps.  
  3. Add relevant features to address specific issues.

- **Why Features Matter**:  
  - Structured data often lacks the scale for deep learning to discover features automatically.  
  - Feature engineering can bridge the gap and drive significant performance improvements.

---

## Comparison: Structured vs. Unstructured Data

| Aspect                        | Structured Data                | Unstructured Data           |
|-------------------------------|--------------------------------|-----------------------------|
| **Data Augmentation**         | Hard to create new examples.  | Easier (e.g., noise for audio, flips for images). |
| **Feature Engineering**       | Still critical for performance. | Less needed – models learn features automatically. |
| **Deep Learning Applicability** | Requires feature design for small datasets. | End-to-end learning works well with large datasets. |

---

## Key Insight
- **Structured Data**: Feature engineering remains an effective and important technique.  
- **Unstructured Data**: Modern deep learning models excel at learning features automatically, reducing the need for manual design.  
- **Larger Datasets**: The more data available, the less manual intervention (e.g., feature design) is required.  