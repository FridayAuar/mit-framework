"""
MIT Framework - Simple Intervention Demo
"""

from mit_framework import MITSystem, compute_mu

def main():
    print("🛠️  MIT Framework - Intervention Demo")
    print("=" * 50)
    
    # Create a challenging system
    system = MITSystem.pathfinding(
        grid_size=(25, 25),
        obstacles=[(12, i) for i in range(5, 20)],  # Vertical wall
        start=(0, 0),
        goal=(24, 24)
    )
    
    print(f"Initial system:")
    print(f"  Grid size: {system.grid_size}")
    print(f"  Obstacles: {len(system.obstacles)}")
    
    # Measure initial impossibility
    mu_initial = compute_mu(system)
    print(f"  Initial impossibility: μ = {mu_initial:.3f}")
    
    # Simulate intervention (remove some obstacles)
    print(f"\n🔧 Applying intervention: Remove 5 obstacles")
    
    # Create improved system with fewer obstacles
    original_obstacles = list(system.obstacles)
    reduced_obstacles = original_obstacles[5:]  # Remove first 5 obstacles
    
    improved_system = MITSystem.pathfinding(
        grid_size=(25, 25),
        obstacles=reduced_obstacles,
        start=(0, 0),  # Use simple tuples
        goal=(24, 24)  # Use simple tuples
    )
    
    mu_final = compute_mu(improved_system)
    improvement = mu_initial - mu_final
    
    print(f"  Obstacles after intervention: {len(improved_system.obstacles)}")
    print(f"  Final impossibility: μ = {mu_final:.3f}")
    print(f"  Improvement: Δμ = {improvement:.3f}")
    
    if improvement > 0:
        print(f"✅ Success! Intervention reduced impossibility by {improvement:.3f}")
        percent_improvement = (improvement / mu_initial) * 100
        print(f"   That's a {percent_improvement:.1f}% improvement!")
    else:
        print(f"⚠️  Intervention had minimal effect")

if __name__ == "__main__":
    main()