

"""
Project: Bioengineering - Biosensor Simulation
Description: Simulates detection of a biological marker
             using a simple mathematical biosensor model.

Note: This is an educational simulation, not a real
medical diagnostic tool.
"""

import matplotlib.pyplot as plt
import numpy as np


def biosensor_response(concentration, sensitivity=0.85, noise=0.02):
    """Calculate simulated biosensor output."""
    signal = sensitivity * concentration
    random_noise = np.random.normal(0, noise, len(concentration))
    return signal + random_noise


def main():
    print("=" * 45)
    print("      BIOENGINEERING BIOSENSOR PROJECT")
    print("=" * 45)

    #
    concentration = np.linspace(0, 10, 
    response = biosensor_response(concentration)

    
    estimated_concentration = np.maximum(response / 0.85, 0)

    print("\nSample Biosensor Readings")
    print("-" * 45)
    print(f"{'True Level':<18}{'Sensor Signal':<18}")
    print("-" * 45)

    for i in range(0, len(concentration), 5):
        print(
            f"{concentration[i]:<18.2f}"
            f"{response[i]:<18.3f}"
        )

    
    plt.figure(figsize=(9, 5))
    plt.plot(
        concentration,
        response,
        "o",
        markersize=4,
        label="Simulated sensor readings"
    )
    plt.plot(
        concentration,
        0.85 * concentration,
        label="Ideal calibration curve"
    )

    plt.title("Bioengineering: Biosensor Response")
    plt.xlabel("Biomarker Concentration (arbitrary units)")
    plt.ylabel("Sensor Signal (arbitrary units)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("biosensor_results.png", dpi=300)
    plt.show()

    print("\nSimulation completed successfully!")
    print("Graph saved as biosensor_results.png")


if __name__ == "__main__":
    main()
