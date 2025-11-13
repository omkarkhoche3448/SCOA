import numpy as np
import matplotlib.pyplot as plt

# ----- Fuzzy Logic Robotic Arm Control -----

class FuzzyRoboticArm:
    """
    Simulated robotic arm controlled by fuzzy logic

    The arm has:
    - Distance from target (input)
    - Speed of arm (output - controlled by fuzzy logic)
    """

    def __init__(self):
        self.position = 0  # Current position
        self.target = 100  # Target position
        self.speed = 0     # Current speed
        self.positions = []  # History for plotting

    def calculate_distance(self):
        """Calculate distance from target"""
        return abs(self.target - self.position)

    # ===== STEP 1: FUZZIFICATION =====
    def fuzzify_distance(self, distance):
        """
        Convert crisp distance to fuzzy values

        Fuzzy sets: NEAR, MEDIUM, FAR
        """
        # NEAR: Close to target (0-40 units)
        if distance <= 20:
            near = 1.0
        elif distance <= 40:
            near = (40 - distance) / 20
        else:
            near = 0.0

        # MEDIUM: Moderate distance (20-80 units)
        if distance <= 20:
            medium = 0.0
        elif distance <= 50:
            medium = (distance - 20) / 30
        elif distance <= 80:
            medium = (80 - distance) / 30
        else:
            medium = 0.0

        # FAR: Very far from target (50+ units)
        if distance <= 50:
            far = 0.0
        elif distance <= 70:
            far = (distance - 50) / 20
        else:
            far = 1.0

        return {'near': near, 'medium': medium, 'far': far}

    # ===== STEP 2: FUZZY RULES =====
    def apply_rules(self, fuzzy_distance):
        """
        Fuzzy Rules:
        1. IF distance is NEAR THEN speed is SLOW
        2. IF distance is MEDIUM THEN speed is MEDIUM
        3. IF distance is FAR THEN speed is FAST
        """
        rules = {
            'slow': fuzzy_distance['near'],
            'medium': fuzzy_distance['medium'],
            'fast': fuzzy_distance['far']
        }
        return rules

    # ===== STEP 3: DEFUZZIFICATION =====
    def defuzzify(self, fuzzy_speed):
        """
        Convert fuzzy speed to crisp speed value
        Using Center of Gravity (COG) method

        Speed ranges:
        - SLOW: 0-5 units/step
        - MEDIUM: 3-12 units/step
        - FAST: 10-20 units/step
        """
        # Define membership function centers
        slow_center = 2.5     # Center of SLOW range
        medium_center = 7.5   # Center of MEDIUM range
        fast_center = 15.0    # Center of FAST range

        # Calculate weighted average (Center of Gravity)
        numerator = (fuzzy_speed['slow'] * slow_center +
                    fuzzy_speed['medium'] * medium_center +
                    fuzzy_speed['fast'] * fast_center)

        denominator = (fuzzy_speed['slow'] +
                      fuzzy_speed['medium'] +
                      fuzzy_speed['fast'])

        # Avoid division by zero
        if denominator == 0:
            return 0

        crisp_speed = numerator / denominator
        return crisp_speed

    def move_arm(self):
        """
        Main control loop: Move arm towards target using fuzzy logic
        """
        # Get current distance
        distance = self.calculate_distance()

        # STEP 1: Fuzzification
        fuzzy_distance = self.fuzzify_distance(distance)

        # STEP 2: Apply fuzzy rules
        fuzzy_speed = self.apply_rules(fuzzy_distance)

        # STEP 3: Defuzzification
        crisp_speed = self.defuzzify(fuzzy_speed)

        # Move arm towards target
        if self.position < self.target:
            self.position += crisp_speed
        else:
            self.position -= crisp_speed

        # Store position for plotting
        self.positions.append(self.position)

        return distance, fuzzy_distance, fuzzy_speed, crisp_speed

    def simulate(self, steps=30):
        """Run simulation for given number of steps"""
        print("="*60)
        print("FUZZY LOGIC ROBOTIC ARM CONTROL SIMULATION")
        print("="*60)
        print(f"Starting Position: {self.position}")
        print(f"Target Position: {self.target}")
        print("="*60)

        for step in range(steps):
            distance, fuzzy_dist, fuzzy_speed, crisp_speed = self.move_arm()

            print(f"\nStep {step + 1}:")
            print(f"  Position: {self.position:.2f}")
            print(f"  Distance: {distance:.2f}")
            print(f"  Fuzzy Distance: Near={fuzzy_dist['near']:.2f}, "
                  f"Medium={fuzzy_dist['medium']:.2f}, Far={fuzzy_dist['far']:.2f}")
            print(f"  Fuzzy Speed: Slow={fuzzy_speed['slow']:.2f}, "
                  f"Medium={fuzzy_speed['medium']:.2f}, Fast={fuzzy_speed['fast']:.2f}")
            print(f"  Crisp Speed: {crisp_speed:.2f}")

            # Stop if reached target (within 1 unit)
            if distance < 1:
                print(f"\nTarget reached in {step + 1} steps!")
                break

        print("\n" + "="*60)
        print("SIMULATION COMPLETE")
        print("="*60)

    def plot_results(self):
        """Plot the arm's movement over time"""
        plt.figure(figsize=(10, 6))

        # Plot position over time
        plt.subplot(2, 1, 1)
        plt.plot(self.positions, 'b-', linewidth=2, label='Arm Position')
        plt.axhline(y=self.target, color='r', linestyle='--', label='Target')
        plt.xlabel('Step')
        plt.ylabel('Position')
        plt.title('Robotic Arm Movement (Fuzzy Logic Control)')
        plt.legend()
        plt.grid(True, alpha=0.3)

        # Plot distance over time
        plt.subplot(2, 1, 2)
        distances = [abs(self.target - pos) for pos in self.positions]
        plt.plot(distances, 'g-', linewidth=2)
        plt.xlabel('Step')
        plt.ylabel('Distance from Target')
        plt.title('Distance to Target Over Time')
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()


# ===== RUN SIMULATION =====
if __name__ == "__main__":
    # Create robotic arm
    arm = FuzzyRoboticArm()

    # Run simulation
    arm.simulate(steps=30)

    # Plot results
    arm.plot_results()


"""
===== EXPLANATION =====

FUZZY LOGIC CONTROL SYSTEM

This program simulates a robotic arm that moves towards a target position
using fuzzy logic control instead of traditional control methods.

COMPONENTS:

1. FUZZIFICATION:
   - Converts crisp input (distance) to fuzzy values
   - Fuzzy sets: NEAR (0-40), MEDIUM (20-80), FAR (50+)
   - Each distance has membership degree in each fuzzy set

   Example: Distance = 30
   - NEAR: 0.5 (partially near)
   - MEDIUM: 0.33 (partially medium)
   - FAR: 0.0 (not far)

2. FUZZY RULES:
   - IF-THEN rules that mimic human reasoning
   - Rule 1: IF distance is NEAR THEN speed is SLOW
   - Rule 2: IF distance is MEDIUM THEN speed is MEDIUM
   - Rule 3: IF distance is FAR THEN speed is FAST

   Logic: When far, move fast. When close, slow down to avoid overshooting.

3. DEFUZZIFICATION:
   - Converts fuzzy speed back to crisp speed value
   - Uses Center of Gravity (COG) method
   - Formula: (Σ membership × center) / Σ membership

   Example: If SLOW=0.5, MEDIUM=0.3, FAST=0.0
   Speed = (0.5×2.5 + 0.3×7.5 + 0.0×15) / (0.5+0.3+0.0)
         = (1.25 + 2.25 + 0) / 0.8
         = 4.375 units/step

WHY FUZZY LOGIC?

Traditional Control:
- IF distance > 50 THEN speed = 20
- IF distance > 20 THEN speed = 10
- IF distance <= 20 THEN speed = 5
→ Abrupt changes, jerky movement

Fuzzy Control:
- Smooth transitions between speeds
- More human-like decision making
- Gradual acceleration/deceleration
→ Smooth, natural movement

REAL-WORLD APPLICATIONS:
- Robot arm control
- Self-parking cars
- Air conditioning systems
- Washing machines
- Camera autofocus
"""
