"""
Quick start example for MIT Framework
"""

from mit_framework import MITSystem, compute_mu

def main():
    print("MIT Framework - Quick Start Example")
    print("=" * 40)
    
    # Create a pathfinding system
    system = MITSystem.pathfinding(
        grid_size=(20, 20),
        obstacles=[(5, 5), (5, 6), (5, 7)],
        start=(0, 0),
        goal=(19, 19)
    )
    
    # Compute impossibility measure
    mu = compute_mu(system)
    
    print(f"Grid size: {system.grid_size}")
    print(f"Start: {system.start}")
    print(f"Goal: {system.goal}")
    print(f"Obstacles: {len(system.obstacles)}")
    print(f"Impossibility measure mu = {mu:.3f}")
    
    # Interpret the result
    if mu == float('inf'):
        print("Status: Impossible (goal is blocked)")
    elif mu > 1.0:
        print("Status: Very difficult")
    elif mu > 0.5:
        print("Status: Moderately difficult")
    else:
        print("Status: Achievable")

if __name__ == "__main__":
    main()