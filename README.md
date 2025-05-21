## 🏃‍♂️ Heart Rate Zone Calculation Methods

This application supports three popular heart rate training zone calculation methods. Below is a description of each method and how they differ.

---

### 1. %MHR Method (Percentage of Maximum Heart Rate)

**Formula:**  
Target HR = MHR × Intensity

**Where:**
- **MHR** = Maximum Heart Rate (commonly estimated as `220 - age`)

**Example:**

For **MHR = 196** and **Zone 1 (50–60%)**:  
Target HR = 196 × 0.50 to 196 × 0.60 → 98–117 bpm  

✅ **Pros**: Simple and commonly used  
⚠️ **Cons**: Doesn't account for individual resting heart rate

---

### 2. Karvonen Method (Heart Rate Reserve Method)

**Formula:**  
HRR = MHR − RHR  
Target HR = RHR + (HRR × Intensity)  

**Where:**
- **RHR** = Resting Heart Rate

**Example:**

For **MHR = 196**, **RHR = 55**, **HRR = 141**, **Zone 1 (50–60%)**:  
Target HR = 55 + (141 × 0.50 to 0.60) → 125–139 bpm  

✅ **Pros**: More personalized, considers resting heart rate  
⚠️ **Cons**: Slightly more complex to compute

---

### 3. MAF Method (Maximum Aerobic Function – Dr. Phil Maffetone)

**Formula:**
MAF HR = 180 − Age + Adjustment  

**Adjustment Guidelines:**
- `+5` → Experienced athlete, consistent training  
- ` 0` → Average individual with regular training  
- `−5` → Beginner, recent injury, or recovering

**Example:**

For **Age = 45**, no adjustment:  
MAF HR = 180 − 45 = 135 bpm (typically Zone 2 base)  

✅ **Pros**: Focused on building aerobic base, great for endurance  
⚠️ **Cons**: Not a full zone model, less applicable for high-intensity training
