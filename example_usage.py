"""
Example Usage: Quantitative Pupillary Light Reflex (PLR) Dynamics.
Demonstrates non-invasive calculation of constriction kinetics and autonomic balance.
"""

from client import PupilLightReflexClient


def main():
    client = PupilLightReflexClient()
    print("=== Quantitative Pupillary Light Reflex (PLR) Demo ===")

    # Test Case 1: Healthy alert adult
    res1 = client.evaluate_pupillary_dynamics(
        baseline_diameter_mm=4.3,
        minimum_diameter_mm=2.6,
        constriction_latency_ms=225.0,
        constriction_velocity_mm_s=4.9,
        redilation_velocity_mm_s=1.85
    )
    print("\nTest Case 1: Healthy Alert Adult")
    print(f"  Baseline: {res1['baseline_diameter_mm']} mm | Nadir: {res1['minimum_diameter_mm']} mm")
    print(f"  Constriction Amplitude: {res1['constriction_amplitude_mm']} mm ({res1['constriction_percentage']}%)")
    print(f"  Latency: {res1['constriction_latency_ms']} ms | MCV: {res1['constriction_velocity_mm_s']} mm/s")
    print(f"  Autonomic Velocity Ratio: {res1['autonomic_velocity_ratio']}")
    print(f"  Pupillomotor Resilience Score: {res1['pupillomotor_resilience_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Sluggish parasympathetic / cognitive fatigue
    res2 = client.evaluate_pupillary_dynamics(
        baseline_diameter_mm=3.9,
        minimum_diameter_mm=2.9,
        constriction_latency_ms=290.0,
        constriction_velocity_mm_s=2.8,
        redilation_velocity_mm_s=1.4
    )
    print("\nTest Case 2: CNS / Ocular Fatigue Pattern")
    print(f"  Constriction: {res2['constriction_percentage']}% | Latency: {res2['constriction_latency_ms']} ms")
    print(f"  Score: {res2['pupillomotor_resilience_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
