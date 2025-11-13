# Assignment 4: Neural Networks for Stock Market Prediction

---

## 📖 START HERE - Simple Explanation

### The Brain Analogy: How Neural Networks Learn

Imagine you're teaching a child to recognize whether it will rain tomorrow:

**👦 Child's Learning Process:**
1. **Observe patterns**: "When clouds are dark AND wind is strong → It usually rains"
2. **Make mistakes**: First few times, wrong predictions
3. **Learn from mistakes**: "Oh! I was wrong. Let me adjust my thinking."
4. **Get better**: After 100 days, the child predicts rain accurately!

**🧠 Neural Network = Artificial Brain**
- Instead of a child, we have a computer program
- Instead of weather, we predict stock prices (UP or DOWN)
- Instead of experience, we show it historical data
- It learns patterns and makes predictions!

---

### What This Assignment Does (In Simple Words)

**Goal**: Predict if Apple (AAPL) stock will go UP ⬆️ or DOWN ⬇️ tomorrow

**Input Data** (What we tell the neural network):
- Opening price today
- Highest price today
- Lowest price today
- Closing price today
- Trading volume (how many stocks sold)

**Output** (What neural network predicts):
- 1 = Stock will go UP tomorrow ⬆️
- 0 = Stock will go DOWN tomorrow ⬇️

**Example:**
```
Today's Data:
  Open = $150, High = $155, Low = $148, Close = $152, Volume = 1M

Neural Network Thinks: "Hmm... closing higher than opening,
                        high volume... I predict UP!"
Prediction: 1 (UP) ⬆️

Tomorrow's Reality: Stock closes at $154
Result: ✓ CORRECT!
```

---

## 🎯 The 5-Step Process

### Step 1: COLLECT DATA - "Get Historical Stock Prices"

**Real Life:** Looking at weather records for past 3 years
**In Code:** Download Apple stock data from 2020-2023

```
Date       | Open  | High  | Low   | Close | Volume
-----------|-------|-------|-------|-------|--------
2020-01-02 | $150  | $155  | $148  | $152  | 1.2M
2020-01-03 | $152  | $158  | $151  | $156  | 1.5M
2020-01-04 | $156  | $157  | $153  | $154  | 1.1M
...        | ...   | ...   | ...   | ...   | ...
```

**Why 3 years?** More data = Better learning (like studying more examples before exam!)

---

### Step 2: PREPARE DATA - "Make It Neural Network Friendly"

#### 2.1: Create Target Labels (What We Want to Predict)

**Question**: Did the stock go UP or DOWN the next day?

```
Today's Close | Tomorrow's Close | Target
--------------|------------------|--------
$150          | $152             | 1 (UP)
$152          | $156             | 1 (UP)
$156          | $154             | 0 (DOWN)
$154          | $160             | 1 (UP)
```

**Formula**: `Target = 1 if (Tomorrow's Close > Today's Close) else 0`

#### 2.2: Normalization (Scaling)

**Problem**: Neural networks don't like big numbers

Original Data:
```
Open = $150, Volume = 1,200,000  ← Huge difference!
```

**Solution**: Scale everything to 0-1 range

After Scaling:
```
Open = 0.45, Volume = 0.62  ← Same scale!
```

**Analogy**: Converting all measurements to same units (like converting feet and inches to meters)

#### 2.3: Split Data (Train vs Test)

**Train Data (80%)**: For learning patterns
**Test Data (20%)**: For checking if it really learned

```
Total Data: 1000 days
├── Train: 800 days → "Study material"
└── Test:  200 days → "Final exam questions"
```

**Why split?** If you memorize exam questions, you didn't really learn! Same with neural networks.

---

### Step 3: BUILD NEURAL NETWORK - "Create the Artificial Brain"

#### The Architecture (Structure of Our Brain)

```
INPUT LAYER          HIDDEN LAYERS           OUTPUT LAYER
(5 neurons)          (64 + 32 neurons)       (1 neuron)

[Open]    ────┐
[High]    ────┤
[Low]     ────┼──→ [64 neurons] ──→ [32 neurons] ──→ [Prediction]
[Close]   ────┤      (Layer 1)        (Layer 2)         0 or 1
[Volume]  ────┘
```

**Layer by Layer Explanation:**

**Layer 1 - Input Layer (5 neurons)**
- Each neuron holds one piece of data
- Neuron 1 = Open price
- Neuron 2 = High price
- Neuron 3 = Low price
- Neuron 4 = Close price
- Neuron 5 = Volume

**Layer 2 - Hidden Layer 1 (64 neurons)**
- Detects simple patterns
- Example patterns:
  - "Close > Open" (upward day)
  - "High - Low is large" (volatile day)
  - "Volume is high" (active trading)

**Layer 3 - Hidden Layer 2 (32 neurons)**
- Combines simple patterns into complex patterns
- Example combinations:
  - "Upward day + High volume = Strong buying signal"
  - "Volatile day + Low volume = Uncertain market"

**Layer 4 - Output Layer (1 neuron)**
- Final decision: UP (1) or DOWN (0)
- Uses all patterns learned to make prediction

---

#### How Neurons Work - The Coffee Shop Analogy

**Imagine a coffee shop decision:**

```
Inputs:
  Weather = Sunny (0.8)
  Temperature = Hot (0.9)
  Day = Weekend (1.0)

Neuron's Job: "Should I go to coffee shop?"

Step 1: Multiply by weights (importance)
  Weather × 0.5 = 0.8 × 0.5 = 0.4
  Temperature × 0.3 = 0.9 × 0.3 = 0.27
  Day × 0.7 = 1.0 × 0.7 = 0.7

Step 2: Add them up
  Total = 0.4 + 0.27 + 0.7 = 1.37

Step 3: Apply activation (decision function)
  If Total > 0.5: "YES, GO!" (output = 1)
  Else: "NO, STAY HOME" (output = 0)

Result: 1.37 > 0.5 → YES! ☕
```

**In stock prediction:**
- Inputs = Open, High, Low, Close, Volume
- Weights = Learned importance of each factor
- Output = Buy (1) or Sell (0)

---

#### Activation Functions - The Decision Makers

**1. ReLU (Rectified Linear Unit)** - Used in hidden layers

```
Function: If input < 0, output = 0
         If input ≥ 0, output = input

Graph:
     |      /
     |     /
     |    /
     |___/___
         0

Example:
  Input: -5 → Output: 0
  Input:  3 → Output: 3
  Input:  7 → Output: 7
```

**Why?** Removes negative noise, keeps positive signals

**2. Sigmoid** - Used in output layer

```
Function: Converts any number to 0-1 range

Graph:
     1|    ___---
      |   /
      |  /
     0|_/________

Example:
  Input: -10 → Output: 0.00004 ≈ 0
  Input:   0 → Output: 0.5
  Input:  10 → Output: 0.99996 ≈ 1
```

**Why?** Perfect for binary decisions (UP or DOWN, YES or NO)

---

#### 🎓 ACTIVATION FUNCTIONS - THEORY & INTUITION

**What is an Activation Function?**

An activation function decides whether a neuron should "fire" (activate) or not, just like neurons in your brain!

**Real-World Analogy:**
```
Think of a light switch with a dimmer:

No Activation Function:
  Input: 5 → Output: 5
  Input: 100 → Output: 100
  Problem: Output can be ANY number (unbounded!)
  Like a broken dimmer that goes to 1000% brightness!

With Activation Function:
  Input: 5 → Process → Output: 0.8
  Input: 100 → Process → Output: 0.99
  Solution: Output is controlled and meaningful
  Like a proper dimmer that stays 0-100%
```

---

##### **1. ReLU (Rectified Linear Unit) - The "Negative Killer"**

**Mathematical Formula:**
```
ReLU(x) = max(0, x)

In simple terms:
  If x is negative → Return 0
  If x is positive → Return x as-is
```

**Why the name "Rectified Linear"?**
- **Rectified**: Fixes negative values (makes them zero)
- **Linear**: For positive values, it's a straight line (y = x)

**Real-World Examples:**

**Example 1: Temperature Sensor**
```
Neuron calculates: "Is it cold or hot?"
  Input: -5 (very cold) → ReLU(-5) = 0 → "Not hot at all"
  Input:  3 (mild)      → ReLU(3) = 3  → "Somewhat hot"
  Input:  25 (hot)      → ReLU(25) = 25 → "Very hot!"

Logic: Negative = no heat signal, Positive = keep the heat signal
```

**Example 2: Stock Pattern Detection**
```
Neuron calculates: "Is volume unusually high?"
  Input: -2.5 (below normal) → ReLU(-2.5) = 0 → "No unusual activity"
  Input:  0.5 (slightly high) → ReLU(0.5) = 0.5 → "Slight activity"
  Input:  5.0 (very high)     → ReLU(5.0) = 5.0 → "Strong activity!"

Logic: Only positive deviations matter for "high" activity
```

**Visual Graph:**
```
Output
   10|        /
     |       /
    5|      /
     |     /
     |    /
    0|___/_________ Input
      -5  0   5  10

Before 0: Flat line (all outputs = 0)
After 0:  Straight line (output = input)
```

**Why ReLU in Hidden Layers?**

1. **Simple & Fast**: Just one comparison (is x > 0?)
   ```
   ReLU: 1 operation
   Sigmoid: 4 operations (exponential, addition, division)

   Speed: ReLU wins! ⚡
   ```

2. **Solves Vanishing Gradient**:
   ```
   During training (backpropagation):

   Without ReLU (using sigmoid everywhere):
     Gradient: 0.1 × 0.1 × 0.1 × 0.1 = 0.0001
     Problem: Gradient becomes tiny! Learning stops!

   With ReLU:
     Gradient: 1 × 1 × 1 × 1 = 1
     Solution: Gradient stays strong! Learning continues!
   ```

3. **Sparse Activation**:
   ```
   Hidden layer with 64 neurons:

   Without ReLU: All 64 neurons output values
     [0.3, 0.7, 0.2, 0.9, 0.1, ..., 0.5]
     All neurons contribute (expensive!)

   With ReLU: Only positive neurons output
     [0, 0.7, 0, 0.9, 0, ..., 0.5]
     Half neurons = 0 (efficient! Memory saved!)
   ```

**ReLU in Our Stock Prediction:**
```
Hidden Layer 1 (64 neurons with ReLU):
  Neuron 1: -2.3 → ReLU → 0     ← Inactive (no pattern detected)
  Neuron 2:  5.7 → ReLU → 5.7  ← Active (strong pattern!)
  Neuron 3:  0.2 → ReLU → 0.2  ← Slightly active
  Neuron 4: -1.1 → ReLU → 0     ← Inactive
  ...

Only neurons with positive signals "fire"!
This creates selective pattern detection.
```

---

##### **2. Sigmoid - The "Probability Maker"**

**Mathematical Formula:**
```
Sigmoid(x) = 1 / (1 + e^(-x))

Where e = 2.718... (Euler's number)
```

**Why the name "Sigmoid"?**
- **S-shaped curve** (looks like an "S")
- Smoothly transitions from 0 to 1

**Real-World Examples:**

**Example 1: Exam Pass Probability**
```
Hours studied → Probability of passing

0 hours:  Sigmoid(-5) = 0.007  → 0.7% chance (almost no chance)
5 hours:  Sigmoid(0) = 0.5     → 50% chance (coin flip)
10 hours: Sigmoid(5) = 0.993   → 99.3% chance (almost certain!)

The more you study, the higher the probability (but never quite 100%)
```

**Example 2: Stock Prediction Confidence**
```
Network's raw output → Confidence of "UP"

Very bearish: Sigmoid(-10) = 0.00004 → 0.004% confident UP (definitely DOWN!)
Neutral:      Sigmoid(0) = 0.5       → 50% confident UP (uncertain)
Very bullish: Sigmoid(10) = 0.99996  → 99.996% confident UP (definitely UP!)
```

**Visual Graph:**
```
Output
    1|         ___---
     |        /
  0.5|-------/-------
     |      /
    0|____/________ Input
      -5  0   5

Asymptotes: Approaches 0 (left) and 1 (right) but never reaches them
Midpoint: (0, 0.5) - at x=0, output is exactly 0.5
```

**Step-by-Step Calculation:**
```
Example: Sigmoid(2)

Step 1: Calculate e^(-2)
  e = 2.718...
  e^(-2) = 1/e^2 = 1/7.389 = 0.135

Step 2: Add 1
  1 + 0.135 = 1.135

Step 3: Take reciprocal
  1 / 1.135 = 0.881

Result: Sigmoid(2) = 0.881 (88.1% confidence)
```

**Why Sigmoid in Output Layer?**

1. **Bounded Output (0 to 1)**:
   ```
   Without Sigmoid:
     Raw output: -100, -5, 0.5, 3, 200
     Problem: What does -100 mean? What's 200?

   With Sigmoid:
     Sigmoid(-100) = 0.0000...00003 ≈ 0
     Sigmoid(-5) = 0.007
     Sigmoid(0.5) = 0.622
     Sigmoid(3) = 0.953
     Sigmoid(200) = 1.0000...00 ≈ 1

     Clear meaning: Probability between 0% and 100%!
   ```

2. **Probabilistic Interpretation**:
   ```
   Output: 0.87

   Interpretation: 87% confident stock will go UP
                   13% confident stock will go DOWN

   Action: 0.87 > 0.5 threshold → Predict UP! ⬆️
   ```

3. **Smooth Gradients**:
   ```
   During training:

   Sigmoid provides smooth, continuous feedback:
     Small change in input → Small change in output

     Input: 0 → Output: 0.5
     Input: 0.1 → Output: 0.525 (smooth transition)

   This helps network learn gradually and stably.
   ```

**Sigmoid in Our Stock Prediction:**
```
Final neuron (with Sigmoid):

Scenario 1: Bearish signals
  Raw output: -3.5
  Sigmoid(-3.5) = 0.029 → 2.9% confident UP
  Prediction: 0.029 < 0.5 → DOWN ⬇️

Scenario 2: Neutral signals
  Raw output: 0.1
  Sigmoid(0.1) = 0.525 → 52.5% confident UP
  Prediction: 0.525 > 0.5 → UP ⬆️ (barely!)

Scenario 3: Bullish signals
  Raw output: 4.2
  Sigmoid(4.2) = 0.985 → 98.5% confident UP
  Prediction: 0.985 > 0.5 → UP ⬆️ (strong conviction!)
```

---

##### **🔍 Why Different Activations for Different Layers?**

**Hidden Layers → ReLU**
```
Job: Detect patterns in data

Need:
  - Fast computation (ReLU is simplest)
  - Strong gradients (for learning)
  - Sparse activation (efficiency)

ReLU provides all three! ✓
```

**Output Layer → Sigmoid**
```
Job: Make final binary decision (UP or DOWN)

Need:
  - Output between 0 and 1 (probability)
  - Clear interpretation (52% = slightly bullish)
  - Smooth gradients near decision boundary

Sigmoid provides all three! ✓
```

**Analogy: Restaurant Decision**
```
Hidden layers (ReLU):
  "Is it Italian? Is it expensive? Is it nearby?"
  → Quick yes/no checks (fast pattern detection)
  → Many factors evaluated (64 neurons)

Output layer (Sigmoid):
  "Overall, should we go?" → 0.73 confidence YES
  → Single probability (0-1 range)
  → Final decision with confidence level
```

---

##### **📊 Comparison Table**

| Feature | ReLU | Sigmoid |
|---------|------|---------|
| **Formula** | max(0, x) | 1/(1 + e^(-x)) |
| **Range** | [0, ∞) | (0, 1) |
| **Shape** | L-shaped | S-shaped |
| **Computation** | Very fast (1 comparison) | Slower (exponential) |
| **Best for** | Hidden layers | Output layer (binary) |
| **Gradient** | 1 (if x>0), 0 (if x<0) | Smooth (can vanish) |
| **Advantage** | Fast, no vanishing gradient | Probabilistic output |
| **Disadvantage** | Can "die" (stuck at 0) | Slow, vanishing gradient |

---

##### **💡 Key Takeaways**

**ReLU (Hidden Layers):**
- ✅ Think: "Pattern detector" - only fires for positive signals
- ✅ Fast and efficient
- ✅ Output: 0 to infinity
- ✅ Used in: All hidden layers (64 and 32 neurons)

**Sigmoid (Output Layer):**
- ✅ Think: "Probability calculator" - converts to 0-1 range
- ✅ Perfect for binary classification
- ✅ Output: 0 to 1 (interpretable as confidence)
- ✅ Used in: Final output neuron (1 neuron)

**Together in Our Network:**
```
Input (5 values)
    ↓
Layer 1: 64 neurons + ReLU → Pattern detection
    ↓
Layer 2: 32 neurons + ReLU → Complex pattern combination
    ↓
Output: 1 neuron + Sigmoid → Final probability (UP or DOWN)
```

This combination gives us the best of both worlds! 🎯

---

### Step 4: TRAIN THE NETWORK - "Teaching the Brain"

#### The Learning Process (Backpropagation)

**Analogy: Throwing Darts**

```
Round 1: Throw dart → Miss target by 5 inches
         Learn: "I threw too hard!"
         Adjust: Throw softer next time

Round 2: Throw dart → Miss by 2 inches
         Learn: "Better, but still too high"
         Adjust: Aim slightly lower

Round 3: Throw dart → Hit bullseye!
         Learn: "Perfect! Remember this technique"
```

**Neural Network Learning:**

```
Epoch 1:
  Prediction: 0 (DOWN)
  Reality: 1 (UP)
  Error: |0 - 1| = 1 (Wrong!)

  Adjustment: Change weights to make "UP" more likely

Epoch 2:
  Prediction: 0.6 (Leaning UP)
  Reality: 1 (UP)
  Error: |0.6 - 1| = 0.4 (Getting better!)

  Adjustment: Small tweaks to weights

...

Epoch 20:
  Prediction: 0.98 (Strongly UP)
  Reality: 1 (UP)
  Error: |0.98 - 1| = 0.02 (Almost perfect!)
```

#### Training Parameters

**Epochs = 20** (Number of complete learning cycles)
- Like reading a textbook 20 times
- Each time, understanding improves

**Batch Size = 32** (How many examples to see before updating)
- Don't update after every example (too chaotic)
- Don't update after all examples (too slow)
- Update after every 32 examples (balanced!)

**Optimizer = Adam** (The smart teacher)
- Automatically adjusts learning speed
- Fast learning when far from target
- Slow, careful learning when close to target

**Loss Function = Binary Crossentropy** (Error measurement)
- Measures how wrong predictions are
- For binary classification (0 or 1)

---

### Step 5: MAKE PREDICTIONS - "Test What We Learned"

#### Prediction Process

```
Test Example:
  Open = 0.45, High = 0.52, Low = 0.43, Close = 0.48, Volume = 0.61

Neural Network Processing:

Layer 1 (Input): [0.45, 0.52, 0.43, 0.48, 0.61]
  ↓ (multiply by weights, add, activate)

Layer 2 (64 neurons): [0.32, 0.78, 0.12, ..., 0.91]
  ↓ (combine patterns)

Layer 3 (32 neurons): [0.54, 0.89, 0.23, ..., 0.67]
  ↓ (final decision)

Layer 4 (Output): 0.87

Interpretation:
  0.87 > 0.5 → Prediction = 1 (UP) ⬆️
```

#### Accuracy Calculation

```
Test Data: 200 days

Predictions vs Reality:
  Day 1:  Predicted = 1, Actual = 1  ✓ Correct
  Day 2:  Predicted = 1, Actual = 0  ✗ Wrong
  Day 3:  Predicted = 0, Actual = 0  ✓ Correct
  Day 4:  Predicted = 1, Actual = 1  ✓ Correct
  ...
  Day 200: Predicted = 0, Actual = 1  ✗ Wrong

Total Correct: 130 out of 200
Accuracy = 130/200 = 0.65 = 65%
```

**What does 65% mean?**
- Better than random guessing (50%)
- Still room for improvement (not 100%)
- In real trading, even 60% can be profitable!

---

## 💻 Complete Code Walkthrough

### Part 1: Import Libraries

```python
import yfinance as yf           # Download stock data
import numpy as np              # Math operations
import matplotlib.pyplot as plt # Plotting graphs
from tensorflow.keras.models import Sequential    # Neural network
from tensorflow.keras.layers import Dense         # Network layers
from sklearn.model_selection import train_test_split  # Split data
from sklearn.preprocessing import MinMaxScaler    # Scale data
from sklearn.metrics import accuracy_score        # Calculate accuracy
```

**What each does:**
- `yfinance`: Free stock data from Yahoo Finance
- `numpy`: Fast array calculations
- `matplotlib`: Draw prediction graphs
- `tensorflow.keras`: Build and train neural networks
- `sklearn`: Data preparation and evaluation tools

---

### Part 2: Load and Prepare Data

```python
# Download Apple stock data (3 years)
df = yf.download('AAPL', '2020-01-01', '2023-01-01')
```

**Downloads:**
```
[*********************100%%**********************]  1 of 1 completed

        Open     High      Low    Close      Volume
Date
2020-01-02  74.06  75.15  73.80  75.09  135480400
2020-01-03  74.29  75.14  74.13  74.36  146322800
...
```

```python
# Create target: 1 if price goes up, 0 if down
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
```

**What `shift(-1)` does:**
```
Close    | Close.shift(-1) | Target
---------|-----------------|--------
74.06    | 74.36           | 1 (UP)
74.36    | 75.15           | 1 (UP)
75.15    | 74.00           | 0 (DOWN)
```

```python
# Remove rows with missing values
df = df.dropna()
```

**Why?** Last row has no "tomorrow" price, so remove it.

```python
# Extract features (X) and target (y)
X = df[['Open', 'High', 'Low', 'Close', 'Volume']].values
X = MinMaxScaler().fit_transform(X)  # Scale 0-1
y = df['Target'].values
```

**Before scaling:**
```
X = [[74.06, 75.15, 73.80, 75.09, 135480400],
     [74.29, 75.14, 74.13, 74.36, 146322800],
     ...]
```

**After scaling:**
```
X = [[0.42, 0.45, 0.41, 0.44, 0.38],
     [0.43, 0.45, 0.42, 0.43, 0.41],
     ...]
```

```python
# Split into train (80%) and test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

**Result:**
- `X_train`: 600 examples for training
- `X_test`: 150 examples for testing
- `y_train`: 600 labels (0 or 1)
- `y_test`: 150 labels (0 or 1)

---

### Part 3: Build Neural Network

```python
model = Sequential([
    Dense(64, input_dim=5, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])
```

**Layer-by-layer breakdown:**

**Layer 1:**
```python
Dense(64, input_dim=5, activation='relu')
```
- `64` neurons in this layer
- `input_dim=5` expects 5 inputs (Open, High, Low, Close, Volume)
- `activation='relu'` removes negative values
- **Job:** Detect 64 different simple patterns

**Layer 2:**
```python
Dense(32, activation='relu')
```
- `32` neurons
- Automatically connected to previous 64 neurons
- **Job:** Combine simple patterns into 32 complex patterns

**Layer 3:**
```python
Dense(1, activation='sigmoid')
```
- `1` neuron (final prediction)
- `activation='sigmoid'` outputs 0-1 probability
- **Job:** Make final decision (UP or DOWN)

---

### Part 4: Compile and Train

```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

**Configuration:**
- `optimizer='adam'`: Smart learning algorithm (adjusts speed automatically)
- `loss='binary_crossentropy'`: Measures error for binary (0/1) predictions
- `metrics=['accuracy']`: Track % of correct predictions

```python
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)
```

**Training process:**
- Show network 600 training examples
- Repeat 20 times (`epochs=20`)
- Update weights after every 32 examples (`batch_size=32`)
- `verbose=0`: Don't print progress (silent training)

**What happens internally:**
```
Epoch 1/20: Loss = 0.68, Accuracy = 52%
Epoch 2/20: Loss = 0.65, Accuracy = 58%
Epoch 3/20: Loss = 0.61, Accuracy = 62%
...
Epoch 20/20: Loss = 0.45, Accuracy = 68%
```

---

### Part 5: Evaluate and Visualize

```python
# Make predictions on test data
y_pred = (model.predict(X_test) > 0.5).astype(int)
```

**What this does:**
1. `model.predict(X_test)`: Get probabilities (0.23, 0.87, 0.45, ...)
2. `> 0.5`: Convert to True/False (False, True, False, ...)
3. `.astype(int)`: Convert to 0/1 (0, 1, 0, ...)

**Example:**
```
Probabilities: [0.23, 0.87, 0.45, 0.92, 0.31]
> 0.5:         [False, True, False, True, False]
As integers:   [0, 1, 0, 1, 0]
```

```python
# Calculate accuracy
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
```

**Output:**
```
Accuracy: 0.65
```

Meaning: 65% of predictions were correct!

```python
# Plot first 100 predictions
plt.figure(figsize=(10,4))
plt.plot(y_test[:100], label='Actual', marker='o')
plt.plot(y_pred[:100], label='Predicted', marker='x')
plt.title('Stock Market Trend Prediction (Up=1, Down=0)')
plt.xlabel('Days (Test Sample)')
plt.ylabel('Trend')
plt.legend()
plt.show()
```

**Creates graph:**
```
Trend
  1 |  o  x  o  x     o  x
    |     x  o     o  x  o
  0 |  x        x        o  x
    |________________________
       Days (Test Sample)

o = Actual    x = Predicted
```

When 'o' and 'x' overlap → Correct prediction! ✓

---

## 🔍 Step-by-Step Example with Real Numbers

Let's trace one prediction through the entire network!

### Input Data (One Test Day)

```
Open:   $150.25  →  Scaled: 0.52
High:   $152.80  →  Scaled: 0.61
Low:    $149.50  →  Scaled: 0.48
Close:  $151.90  →  Scaled: 0.58
Volume: 1.2M     →  Scaled: 0.43
```

### Layer 1: Input Layer (5 neurons)

```
[0.52, 0.61, 0.48, 0.58, 0.43]
```

### Layer 2: Hidden Layer 1 (64 neurons)

Let's trace just first 3 neurons:

**Neuron 1:**
```
Calculation:
  0.52×0.3 + 0.61×0.5 + 0.48×(-0.2) + 0.58×0.8 + 0.43×0.1
  = 0.156 + 0.305 - 0.096 + 0.464 + 0.043
  = 0.872

ReLU activation: max(0, 0.872) = 0.872 ✓
```

**Neuron 2:**
```
Calculation:
  0.52×(-0.4) + 0.61×0.2 + 0.48×0.7 + 0.58×0.3 + 0.43×(-0.1)
  = -0.208 + 0.122 + 0.336 + 0.174 - 0.043
  = 0.381

ReLU activation: max(0, 0.381) = 0.381 ✓
```

**Neuron 3:**
```
Calculation:
  0.52×0.6 + 0.61×(-0.3) + 0.48×0.4 + 0.58×(-0.2) + 0.43×0.9
  = 0.312 - 0.183 + 0.192 - 0.116 + 0.387
  = 0.592

ReLU activation: max(0, 0.592) = 0.592 ✓
```

**... (61 more neurons)**

**Layer 1 Output:** `[0.872, 0.381, 0.592, 0.234, ..., 0.678]` (64 values)

### Layer 3: Hidden Layer 2 (32 neurons)

Takes 64 inputs from Layer 1, produces 32 outputs

**Example calculation for Neuron 1:**
```
Sum of (64 inputs × 64 weights) + bias
= 0.872×0.2 + 0.381×0.5 + ... + 0.678×0.3
= 1.234

ReLU activation: max(0, 1.234) = 1.234 ✓
```

**Layer 2 Output:** `[1.234, 0.876, 0.543, ..., 1.098]` (32 values)

### Layer 4: Output Layer (1 neuron)

```
Calculation:
  Sum of (32 inputs × 32 weights) + bias
  = 1.234×0.4 + 0.876×0.3 + ... + 1.098×0.5
  = 2.145

Sigmoid activation: 1 / (1 + e^(-2.145))
                  = 1 / (1 + 0.117)
                  = 1 / 1.117
                  = 0.895
```

**Final Output:** `0.895`

### Final Prediction

```
Probability: 0.895 (89.5% confident stock will go UP)
Threshold: 0.5
Decision: 0.895 > 0.5 → Prediction = 1 (UP) ⬆️

Reality check:
  Today's Close: $151.90
  Tomorrow's Close: $153.50
  Actual: 1 (UP) ✓

Result: CORRECT PREDICTION! 🎉
```

---

## 🆚 Comparison: Neural Network vs Traditional Methods

### Method 1: Simple Rules (Traditional)

```python
if close > open and volume > average_volume:
    prediction = 1  # UP
else:
    prediction = 0  # DOWN
```

**Pros:** Simple, fast, interpretable
**Cons:** Misses complex patterns, accuracy ~50-55%

### Method 2: Neural Network (Our Method)

```python
model.predict([open, high, low, close, volume])
```

**Pros:** Learns complex patterns, accuracy ~60-70%
**Cons:** Slower, needs more data, "black box"

### Side-by-Side Example

```
Day with complex pattern:
  Open = $150, Close = $151 (Up $1)
  BUT: High = $160, Low = $149 (Very volatile!)
  AND: Volume = 2x average (Unusual activity)

Traditional Rule:
  "Close > Open → Predict UP"
  Tomorrow: Actually goes DOWN (rule failed!)

Neural Network:
  "Hmm... high volatility + unusual volume + small gain
   = Uncertain market → Predict DOWN"
  Tomorrow: Actually goes DOWN (network correct!)
```

---

## 🌍 Real-World Applications

### 1. **Stock Trading (Our Assignment)**
- Predict UP/DOWN trends
- Used by: Hedge funds, algorithmic traders
- Real impact: Millions in profit/loss

### 2. **Cryptocurrency Trading**
```python
# Same code, different data
df = yf.download('BTC-USD', '2020-01-01', '2023-01-01')
```

### 3. **Forex (Currency) Trading**
```python
# Predict EUR/USD exchange rate
df = yf.download('EURUSD=X', '2020-01-01', '2023-01-01')
```

### 4. **Commodity Trading**
- Gold prices
- Oil prices
- Agricultural products

### 5. **Risk Management**
- Banks: Predict loan defaults
- Insurance: Predict claim likelihood
- Credit cards: Fraud detection

### 6. **Portfolio Optimization**
- Which stocks to buy?
- How much of each?
- When to rebalance?

---

## 🎓 Important Concepts Explained

### 1. **Supervised Learning**

**Definition:** Learning from labeled examples

**Analogy:** Teacher showing flashcards
```
Teacher: "A-P-P-L-E spells... ?"
Student: "Apple!"
Teacher: "Correct!" ✓

Teacher: "C-A-T spells... ?"
Student: "Dog!"
Teacher: "Wrong! It's Cat." ✗
Student learns from correction.
```

**In our code:**
- Input: Stock data (Open, High, Low, Close, Volume)
- Label: Target (0 = DOWN, 1 = UP)
- Network learns: "This pattern → UP", "That pattern → DOWN"

### 2. **Binary Classification**

**Definition:** Choosing between two options

**Examples:**
- Email: Spam or Not Spam
- Medical: Disease or Healthy
- Stocks: UP or DOWN ← Our case!

**Why binary?**
- Simpler than predicting exact price ($151.23)
- More accurate (direction easier than magnitude)
- Sufficient for trading decisions

### 3. **Overfitting vs Underfitting**

**Underfitting (Too Simple):**
```
Rule: "If close > open, predict UP"

Training Accuracy: 52%  } Both poor
Test Accuracy: 51%      }

Problem: Doesn't capture patterns
```

**Good Fit (Just Right):**
```
Neural Network: 64→32→1 neurons

Training Accuracy: 68%  } Similar
Test Accuracy: 65%      } performance

Success: Learned real patterns!
```

**Overfitting (Too Complex):**
```
Huge Network: 1000→500→250→1 neurons

Training Accuracy: 99%  } Big gap!
Test Accuracy: 52%      }

Problem: Memorized training data,
         didn't learn general patterns
```

**Our solution:**
- Moderate size (64→32→1)
- Train/test split catches overfitting
- Stop if test accuracy drops

### 4. **Gradient Descent**

**Analogy:** Finding the bottom of a valley blindfolded

```
You're on a mountain (high error):

Step 1: Feel ground slope → Steep downward to left
        Take BIG step left

Step 2: Feel ground slope → Slight downward to left
        Take small step left

Step 3: Feel ground slope → Almost flat
        Take tiny step left

Step 4: At bottom! (minimum error)
```

**In neural networks:**
- Mountain height = Prediction error
- Valley bottom = Best weights
- Slope = Gradient (calculus derivative)
- Step size = Learning rate

**Adam optimizer:**
- Adjusts step size automatically
- Fast steps when far from bottom
- Careful steps when close
- Avoids overshooting

### 5. **Backpropagation**

**Analogy:** Blaming the right people

```
Restaurant messes up order:

Customer: "This is wrong!"
Waiter: "Not my fault, blame the chef!"
Chef: "Not my fault, blame the supplier!"
Supplier: "Okay, I'll fix it."

Error flows backward through chain.
```

**In neural networks:**
```
Output Layer: "Prediction was wrong!"
              ↓ (backpropagate error)
Hidden Layer 2: "Which neurons caused this?"
                "Adjust their weights!"
              ↓ (backpropagate further)
Hidden Layer 1: "Which neurons caused Layer 2's error?"
                "Adjust their weights!"
              ↓
Input Layer: "Adjust how we interpret inputs!"
```

**Math behind it:**
- Uses chain rule from calculus
- Calculates how much each weight contributed to error
- Updates weights proportionally to their blame

### 6. **Epochs and Batches**

**Epoch:** One complete pass through all training data

**Analogy:** Reading a textbook
```
Epoch 1: Read chapters 1-10 (first time)
Epoch 2: Read chapters 1-10 (second time, deeper understanding)
Epoch 3: Read chapters 1-10 (third time, mastery!)
```

**Batch:** Subset of data processed before updating weights

**Analogy:** Doing homework
```
Batch Size = 1: Do 1 problem, check answer, learn
                Do 1 problem, check answer, learn
                (Too slow! Inefficient)

Batch Size = 32: Do 32 problems, check all answers, learn
                 Do 32 problems, check all answers, learn
                 (Efficient! Balanced)

Batch Size = 1000: Do all problems, check all answers, learn once
                   (Too coarse! Might miss details)
```

**In our code:**
- 20 epochs = Read all data 20 times
- Batch size 32 = Update weights after every 32 examples

### 7. **Loss Function (Binary Crossentropy)**

**Purpose:** Measure how wrong predictions are

**Formula:**
```
Loss = -[y×log(p) + (1-y)×log(1-p)]

Where:
  y = actual label (0 or 1)
  p = predicted probability
```

**Example 1:** Good prediction
```
Actual: y = 1 (UP)
Predicted: p = 0.9 (90% confident UP)

Loss = -[1×log(0.9) + 0×log(0.1)]
     = -[1×(-0.105) + 0]
     = 0.105  ← Small loss, good!
```

**Example 2:** Bad prediction
```
Actual: y = 1 (UP)
Predicted: p = 0.1 (10% confident UP)

Loss = -[1×log(0.1) + 0×log(0.9)]
     = -[1×(-2.303) + 0]
     = 2.303  ← Large loss, bad!
```

**Why this function?**
- Heavily penalizes confident wrong predictions
- Slightly penalizes uncertain predictions
- Perfect for probability outputs (0-1)

### 8. **Train/Test Split**

**Purpose:** Prevent cheating!

**Bad Approach:** Test on training data
```
Training Data: Questions 1-100
Test Data: Questions 1-100 (SAME!)

Result: Student memorized answers
        Doesn't understand concepts
        100% on test, but learned nothing!
```

**Good Approach:** Hold out test data
```
Training Data: Questions 1-80
Test Data: Questions 81-100 (DIFFERENT!)

Result: Student must understand concepts
        Can't just memorize
        75% on test, but truly learned!
```

**In our code:**
```python
train_test_split(X, y, test_size=0.2)
```
- 80% training: Questions network sees during learning
- 20% testing: Questions network never saw before
- Test accuracy = True measure of learning

---

## 📊 Understanding the Output

### Accuracy Metric

**Formula:**
```
Accuracy = Correct Predictions / Total Predictions
```

**Example output:**
```
Accuracy: 0.65
```

**Interpretation:**
- 0.65 = 65% correct
- Random guessing = 50% (coin flip)
- Our network = 65% (better than random!)
- Perfect prediction = 100% (impossible in stocks)

**Is 65% good?**
- **In exams:** No! (That's a D grade)
- **In stock trading:** Yes! (Can be very profitable)

**Why 65% is valuable:**
```
Trading Strategy:
  Capital: $10,000
  Trade: 100 times

  Wins (65): +$100 each = +$6,500
  Losses (35): -$100 each = -$3,500

  Net Profit: $6,500 - $3,500 = $3,000
  Return: 30% gain! 🎉
```

### Graph Interpretation

```
     Trend
       1 |  o x o x o x o x
         |  x o x o x o x o
       0 |  o x o x o x o x
         |__________________
            Days (Test)

o = Actual    x = Predicted
```

**What to look for:**

**1. Overlapping points** (o and x together)
```
o x   ← Correct prediction! ✓
```

**2. Mismatched points**
```
o
  x   ← Wrong prediction ✗
```

**3. Overall pattern match**
```
Good Network:
  o x o x o x  ← Follows trend

Bad Network:
  o o o x x x  ← Opposite trend!
```

---

## ❓ Questions & Answers

### Q1: Why use neural networks instead of simpler methods?

**Simple Method:**
```python
if close > open:
    return 1  # Predict UP
else:
    return 0  # Predict DOWN
```
**Accuracy:** ~50% (basically guessing)

**Neural Network:**
```python
model.predict([open, high, low, close, volume])
```
**Accuracy:** ~65% (learns complex patterns)

**Why better?**
- Considers multiple factors together
- Learns non-linear patterns
- Adapts to market conditions
- Example pattern: "High volume + small price change + low volatility = Upcoming reversal"

---

### Q2: How does the network learn from mistakes?

**Example:**

**Mistake 1:**
```
Input: [0.45, 0.52, 0.43, 0.48, 0.61]
Predicted: 0.2 (20% confident UP) → Prediction: 0 (DOWN)
Actual: 1 (UP)
Error: Large! ✗

Learning: "When these inputs occur, increase confidence in UP"
Action: Adjust weights to make neurons fire more for UP
```

**After Adjustment:**
```
Same Input: [0.45, 0.52, 0.43, 0.48, 0.61]
Predicted: 0.6 (60% confident UP) → Prediction: 1 (UP)
Actual: 1 (UP)
Error: Small! ✓

Result: Learning worked!
```

**Process:**
1. Make prediction
2. Compare with reality
3. Calculate error
4. Backpropagate error through network
5. Adjust weights to reduce error
6. Repeat thousands of times

---

### Q3: What do the hidden layers actually learn?

**Layer 1 (64 neurons):** Simple patterns

**Examples:**
- Neuron 1: "Is closing price higher than opening?" (Bullish signal)
- Neuron 7: "Is volume higher than average?" (Unusual activity)
- Neuron 15: "Is the range (High-Low) large?" (Volatility)
- Neuron 23: "Is close near the high?" (Strong buying)

**Layer 2 (32 neurons):** Complex combinations

**Examples:**
- Neuron 3: "Bullish signal + High volume = Strong buy signal"
- Neuron 8: "Large range + Low volume = Indecision"
- Neuron 14: "Close near high + High volume = Momentum"
- Neuron 21: "Small range + Low volume = Consolidation"

**Output Layer (1 neuron):** Final decision

**Logic:**
```
If (multiple strong buy signals):
    Output: 0.9 (Highly confident UP)
Else if (mixed signals):
    Output: 0.5 (Uncertain)
Else:
    Output: 0.1 (Highly confident DOWN)
```

---

### Q4: Why normalize/scale the data?

**Problem without normalization:**

```
Inputs:
  Close: $150      ← Medium number
  Volume: 1,200,000 ← HUGE number!

Network sees:
  Weight for Close: 0.5
  Weight for Volume: 0.5

Calculation:
  Close contribution: 150 × 0.5 = 75
  Volume contribution: 1,200,000 × 0.5 = 600,000

Total: 600,075

Volume dominates! Network ignores price!
```

**Solution with normalization:**

```
Scaled Inputs:
  Close: 0.52      ← 0-1 range
  Volume: 0.43     ← 0-1 range

Calculation:
  Close contribution: 0.52 × 0.5 = 0.26
  Volume contribution: 0.43 × 0.5 = 0.215

Total: 0.475

Balanced! Network considers both!
```

---

### Q5: What is overfitting and how to avoid it?

**Overfitting Example:**

```
Student memorizes exact exam questions from practice test:
  Practice test: 100%
  Real exam: 50% (different questions!)

Problem: Memorization, not understanding
```

**In neural networks:**

```
Overfitted Network:
  Training accuracy: 99%
  Test accuracy: 52%

Problem: Memorized training data patterns,
         didn't learn general market behavior
```

**How to detect:**
```python
# Large gap between train and test accuracy
Train: 99%  }  47% gap!
Test:  52%  }  → Overfitting!
```

**How to prevent:**

**1. Train/Test Split** (What we use)
```python
train_test_split(X, y, test_size=0.2)
```

**2. Smaller Network**
```python
# Bad: Too many neurons
model = Sequential([Dense(1000), Dense(500), Dense(1)])

# Good: Right-sized
model = Sequential([Dense(64), Dense(32), Dense(1)])
```

**3. Dropout** (Not used in our code, but common)
```python
Dense(64, activation='relu'),
Dropout(0.2),  # Randomly ignore 20% of neurons
```

**4. Early Stopping**
```python
# Stop training if test accuracy stops improving
```

---

### Q6: Why 64 and 32 neurons specifically?

**No magic formula!** It's a balance:

**Too few neurons:**
```
model = Sequential([Dense(4), Dense(2), Dense(1)])

Result: Underfitting
  - Can't learn complex patterns
  - Accuracy: ~50% (bad)
```

**Too many neurons:**
```
model = Sequential([Dense(1000), Dense(500), Dense(1)])

Result: Overfitting
  - Memorizes training data
  - Accuracy on new data: ~52% (bad)
```

**Just right:**
```
model = Sequential([Dense(64), Dense(32), Dense(1)])

Result: Good fit
  - Learns patterns without memorizing
  - Accuracy: ~65% (good)
```

**General guidelines:**
- Start with 64-128 neurons in first layer
- Decrease by ~50% each layer (64→32→16)
- Experiment to find best size for your data

**Our choice:**
- 5 inputs → 64 neurons (12x expansion)
- 64 → 32 (narrowing down)
- 32 → 1 (final decision)

---

### Q7: Can this make me rich in real trading?

**Short answer:** It's a good start, but not enough alone.

**What this code does well:**
- ✓ Learns basic patterns
- ✓ Better than random guessing
- ✓ Foundation for trading system

**What it's missing:**

**1. Market Complexity**
```
Our model considers: Open, High, Low, Close, Volume
Real markets affected by:
  - News events
  - Economic indicators
  - Company earnings
  - Global politics
  - Market sentiment
  - Technical indicators
  - Sector trends
```

**2. Transaction Costs**
```
Theory: Buy at $100, sell at $101 → $1 profit

Reality:
  Buy at $100 + $0.50 commission = $100.50
  Sell at $101 - $0.50 commission = $100.50
  Profit: $0 (break even!)
```

**3. Market Dynamics**
```
Problem: If everyone uses same prediction model,
         market changes and model stops working!
```

**To make it production-ready:**

**Add more features:**
```python
X = df[['Open', 'High', 'Low', 'Close', 'Volume',
        'RSI',           # Technical indicator
        'MACD',          # Momentum indicator
        'News_sentiment', # NLP on news
        'Market_cap',    # Company size
        'PE_ratio'       # Valuation
       ]].values
```

**Better architecture:**
```python
# Use LSTM (Long Short-Term Memory)
# Considers time sequences
from tensorflow.keras.layers import LSTM

model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(60, 5)),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])
```

**Risk management:**
```python
# Never risk more than 2% per trade
# Use stop-loss orders
# Diversify across multiple stocks
```

---

## 🎯 Key Takeaways

### 1. **Neural Networks = Pattern Recognition Machines**
- Learn from examples
- Detect complex patterns humans can't see
- Improve with more data

### 2. **Stock Prediction = Binary Classification**
- Simplified to UP (1) or DOWN (0)
- Easier than predicting exact prices
- Good enough for trading decisions

### 3. **Three-Layer Architecture**
- Input layer: Raw data (5 features)
- Hidden layers: Pattern detection (64→32 neurons)
- Output layer: Final prediction (1 neuron)

### 4. **Training = Learning from Mistakes**
- Make prediction
- Compare with reality
- Adjust weights to improve
- Repeat thousands of times

### 5. **Evaluation Matters**
- Train/test split prevents cheating
- Accuracy measures real-world performance
- 65% is good for stock prediction

### 6. **Real Trading Needs More**
- More features (technical indicators, news)
- Better models (LSTM, Transformer)
- Risk management (stop-loss, diversification)

---

## 🔧 How to Run the Code

### Step 1: Install Required Libraries

```bash
pip install yfinance numpy matplotlib tensorflow scikit-learn
```

### Step 2: Run the Script

```bash
python ass5.py
```

### Step 3: Understand the Output

**Console output:**
```
[*********************100%%**********************]  1 of 1 completed
Accuracy: 0.65
```

**Graph window:**
- Blue line (circles): Actual trends
- Orange line (crosses): Predicted trends
- When they overlap → Correct prediction!

### Step 4: Experiment!

**Change stock:**
```python
df = yf.download('GOOGL', '2020-01-01', '2023-01-01')  # Google
df = yf.download('TSLA', '2020-01-01', '2023-01-01')   # Tesla
```

**Change network size:**
```python
model = Sequential([
    Dense(128, input_dim=5, activation='relu'),  # Bigger!
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
```

**Add more epochs:**
```python
model.fit(X_train, y_train, epochs=50, batch_size=32)  # More training
```

---

## 📚 Further Reading

**Neural Networks:**
- 3Blue1Brown YouTube series on neural networks
- "Deep Learning" by Ian Goodfellow

**Stock Prediction:**
- "Algorithmic Trading" by Ernest P. Chan
- Kaggle competitions on financial prediction

**Python Libraries:**
- TensorFlow documentation: tensorflow.org
- Keras tutorials: keras.io

---

## ✅ Test Your Understanding

### Question 1:
**What does a prediction of 0.87 mean?**

<details>
<summary>Click to see answer</summary>

**Answer:** The network is 87% confident the stock will go UP tomorrow.

**Interpretation:**
- 0.87 > 0.5 threshold
- Final prediction: 1 (UP)
- High confidence (far from 0.5)

</details>

---

### Question 2:
**Why do we use ReLU in hidden layers but Sigmoid in output layer?**

<details>
<summary>Click to see answer</summary>

**Answer:**

**ReLU in hidden layers:**
- Removes negative noise
- Keeps positive signals
- Fast to compute
- Good for detecting patterns

**Sigmoid in output layer:**
- Converts any number to 0-1 range
- Perfect for probabilities
- Needed for binary classification
- Output interpretable as confidence

**Example:**
```
Hidden layer with ReLU:
  Input: [-2.3, 0.8, -1.5, 3.2]
  Output: [0, 0.8, 0, 3.2]  ← Removes negatives

Output layer with Sigmoid:
  Input: 2.145
  Output: 0.895  ← Converts to probability
```

</details>

---

### Question 3:
**If training accuracy is 95% but test accuracy is 55%, what's the problem?**

<details>
<summary>Click to see answer</summary>

**Answer:** Overfitting!

**Diagnosis:**
- Large gap between train (95%) and test (55%)
- Network memorized training data
- Didn't learn general patterns

**Solutions:**
1. Use smaller network (fewer neurons)
2. Add dropout layers
3. Get more training data
4. Use regularization
5. Stop training earlier

**Analogy:**
Student memorized practice test answers (95% on practice) but didn't understand concepts (55% on real exam).

</details>

---

### Question 4:
**What happens if we don't normalize the data?**

<details>
<summary>Click to see answer</summary>

**Answer:** Features with large values dominate!

**Example:**
```
Without normalization:
  Close: $150
  Volume: 1,200,000

Network learns: "Volume is important!" (because it's bigger)
                "Price doesn't matter" (because it's smaller)

Result: Poor predictions (ignores price!)

With normalization:
  Close: 0.52
  Volume: 0.43

Network learns: Both are equally important
Result: Better predictions!
```

**Real-world analogy:**
Comparing apples ($2/lb) to cars ($30,000/car) without context. Normalization makes them comparable.

</details>

---

### Question 5:
**Why is 65% accuracy good for stock prediction but bad for an exam?**

<details>
<summary>Click to see answer</summary>

**Answer:** Different standards for different tasks!

**Exam (65% = D grade):**
- Fixed questions with known answers
- 90%+ expected (A grade)
- 65% means you didn't study enough

**Stock Prediction (65% = Good):**
- Unknown future, inherent uncertainty
- Random guessing = 50%
- 65% means you found real patterns!
- Even 60% can be very profitable

**Profitability:**
```
100 trades with 65% accuracy:
  Wins: 65 trades × $100 profit = $6,500
  Losses: 35 trades × $100 loss = $3,500
  Net: $3,000 profit (30% return!)
```

**Why not 100%?**
- Markets are unpredictable
- News, emotions, black swan events
- If it were easy, everyone would be rich!

</details>

---

### Question 6:
**Trace the flow: What happens when we input [0.5, 0.6, 0.4, 0.55, 0.45]?**

<details>
<summary>Click to see answer</summary>

**Answer: Step-by-step flow**

**Step 1: Input Layer**
```
[0.5, 0.6, 0.4, 0.55, 0.45]
  ↓
5 neurons hold these values
```

**Step 2: Hidden Layer 1 (64 neurons)**
```
Each neuron:
  1. Multiply inputs by weights
  2. Add them up
  3. Apply ReLU (remove negatives)

Example neuron:
  0.5×w1 + 0.6×w2 + 0.4×w3 + 0.55×w4 + 0.45×w5
  = 0.872 (after ReLU)

Result: [0.872, 0.381, 0.592, ..., 0.678] (64 values)
```

**Step 3: Hidden Layer 2 (32 neurons)**
```
Each neuron:
  1. Take 64 inputs from Layer 1
  2. Multiply by weights
  3. Add them up
  4. Apply ReLU

Result: [1.234, 0.876, 0.543, ..., 1.098] (32 values)
```

**Step 4: Output Layer (1 neuron)**
```
1. Take 32 inputs from Layer 2
2. Multiply by weights
3. Add them up
4. Apply Sigmoid (convert to 0-1)

Calculation: 1 / (1 + e^(-2.145)) = 0.895
```

**Step 5: Final Prediction**
```
Probability: 0.895
Threshold: 0.5
Decision: 0.895 > 0.5 → Prediction = 1 (UP)
```

</details>

---

### Question 7:
**What does `epochs=20` mean? What happens during each epoch?**

<details>
<summary>Click to see answer</summary>

**Answer:** 20 complete passes through all training data

**During one epoch:**

```
Training data: 600 examples
Batch size: 32

Epoch 1:
  Batch 1: Examples 1-32 → Predict → Calculate error → Update weights
  Batch 2: Examples 33-64 → Predict → Calculate error → Update weights
  Batch 3: Examples 65-96 → Predict → Calculate error → Update weights
  ...
  Batch 19: Examples 577-600 → Predict → Calculate error → Update weights

  End of Epoch 1: All 600 examples seen once

Epoch 2:
  Repeat with ALL 600 examples again
  (But weights are now better from Epoch 1!)

...

Epoch 20:
  Final pass through all data
  Weights now optimized after 20 iterations
```

**Learning progression:**
```
Epoch 1:  Loss=0.68, Accuracy=52%  (Just started learning)
Epoch 5:  Loss=0.59, Accuracy=61%  (Getting better!)
Epoch 10: Loss=0.51, Accuracy=65%  (Good progress)
Epoch 15: Loss=0.47, Accuracy=67%  (Near optimal)
Epoch 20: Loss=0.45, Accuracy=68%  (Well-trained!)
```

**Why 20?**
- Too few (5): Underfitting (not enough learning)
- Just right (20): Good balance
- Too many (100): Overfitting (memorizes training data)

</details>

---

## 🎉 Congratulations!

You now understand:
- ✅ How neural networks work (artificial brains)
- ✅ Stock prediction as binary classification (UP/DOWN)
- ✅ Three-layer architecture (Input → Hidden → Output)
- ✅ Training process (learning from mistakes)
- ✅ Activation functions (ReLU, Sigmoid)
- ✅ Backpropagation (adjusting weights)
- ✅ Evaluation metrics (accuracy, train/test split)
- ✅ Real-world applications and limitations

**You can now explain this to anyone!** 🚀

---

**END OF DOCUMENTATION**
