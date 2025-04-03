# Intelligent Diagnostic System for Equipment Health Monitoring

## Overview
Unexpected equipment failures in manufacturing lead to **costly downtime, expensive repairs, and decreased productivity**. Traditional maintenance approaches, such as **reactive or fixed-interval maintenance**, fail to anticipate specific problems in real-time.  

This project develops an **Intelligent Diagnostic System** that continuously monitors machinery, detects **early defect symptoms**, and provides **proactive maintenance recommendations**.  

Using **Bayesian Network modeling**, the system analyzes key indicators such as **noise levels, vibration, temperature, and alignment error** to detect failure patterns and predict potential issues before they occur. This enables **preemptive action**, reducing downtime and repair costs while ensuring **optimal equipment performance**.

---

## **Dataset Description**
The dataset contains **70,000 rows and 8 columns**, capturing real-time machinery performance metrics:

### **Features Used**
- **alignment_error**: Degree of misalignment in equipment.  
- **noise_level**: Measured noise levels from the machinery.  
- **vibration**: Categorized vibration levels (**low, medium, high**).  
- **temp**: Temperature levels of equipment (**low, medium, high**).  
- **emission_level**: Indicator of emission severity (**low, high**).  
- **power_draw**: Electrical power draw by machinery (**low, high**).  
- **system_load**: Operational load on the system (**low, high**).  
- **system_failure**: Binary indicator of system failure (**True, False**).  

---

## **Data Preprocessing**
### **Normalization**
- **alignment_error** and **noise_level** were standardized using **Z-score scaling**.

### **Categorization**
- Features such as **vibration, temp, and emission_level** were mapped into **interpretable levels** (**low, medium, high**).

### **Boolean Transformation**
- **system_failure** was converted into **True/False** string values for compatibility with Bayesian modeling.

---

## **Bayesian Network Modeling**

### **1. Structure Learning**
A **Bayesian Network** was constructed using the **Hill Climbing search algorithm** with **BIC scoring**, identifying relationships between variables. The learned **Directed Acyclic Graph (DAG)** provided insights into the **probabilistic dependencies governing system failures**.

#### **Key Relationships Discovered**
- **system_failure** is influenced by **vibration, emission_level, and alignment_error**.  
- **system_load** depends on **noise_level and vibration**.  
- **alignment_error** is affected by **emission_level and power_draw**.  

---

### **2. Conditional Probability Tables (CPTs)**
Using **Maximum Likelihood Estimation (MLE)**, the model estimated the probability of failures given different conditions. These probabilities inform **predictive maintenance decisions**.
---

## **Key Results & Insights**
- **Bayesian Network** successfully identified hidden dependencies between different factors.
- **Proactive monitoring** of high-risk factors enables early maintenance interventions.  
- The model provides a **probabilistic approach to fault detection**, unlike traditional threshold-based monitoring.  

---

## **Installation & Usage**
### **Dependencies**
```bash
pip install pandas numpy pgmpy scikit-learn matplotlib seaborn
