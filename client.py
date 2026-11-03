"""
Quantitative Pupillary Light Reflex (PLR) & Autonomic Kinetics Engine.
Provides deterministic, zero-dependency modeling of pupil constriction amplitude,
cholinergic constriction velocity, adrenergic redilation recovery, and autonomic balance.
"""

from typing import Dict, Any, List, Optional


class PupilLightReflexClient:
    """
    Deterministic client for calculating quantitative pupillometry dynamics.
    Assesses autonomic nervous system balance via parasympathetic constriction
    and sympathetic redilation kinetics following standard light stimulation.
    """

    def __init__(self):
        pass

    def evaluate_pupillary_dynamics(
        self,
        baseline_diameter_mm: float,
        minimum_diameter_mm: float,
        constriction_latency_ms: float,
        constriction_velocity_mm_s: float,
        redilation_velocity_mm_s: float
    ) -> Dict[str, Any]:
        """
        Evaluates quantitative PLR parameters.
        Normal resting values:
        - Baseline: 3.0 - 5.5 mm
        - Constriction latency: 200 - 260 ms
        - Relative constriction: 30% - 48%
        - Constriction velocity (MCV): 3.5 - 6.5 mm/s
        - Redilation velocity: 1.2 - 2.8 mm/s
        """
        if baseline_diameter_mm <= minimum_diameter_mm or baseline_diameter_mm <= 0 or minimum_diameter_mm <= 0:
            return {"error": "Invalid pupil diameters: baseline must exceed minimum and both must be positive"}

        constriction_amp = round(baseline_diameter_mm - minimum_diameter_mm, 2)
        constriction_pct = round((constriction_amp / baseline_diameter_mm) * 100.0, 1)

        # Autonomic balance index: ratio of parasympathetic (constriction) to sympathetic (dilation) speed
        if redilation_velocity_mm_s > 0:
            autonomic_ratio = round(constriction_velocity_mm_s / redilation_velocity_mm_s, 2)
        else:
            autonomic_ratio = 0.0

        # Autonomic Alertness & Pupillomotor Score (0 - 100):
        # Target %CA 32-45%, latency 200-245 ms, MCV >= 4.0 mm/s
        score = 80.0
        if 32.0 <= constriction_pct <= 46.0:
            score += 10.0
        elif constriction_pct < 25.0:
            score -= 20.0

        if 200.0 <= constriction_latency_ms <= 250.0:
            score += 10.0
        elif constriction_latency_ms > 280.0:
            score -= 25.0

        if constriction_velocity_mm_s >= 4.2:
            score += 5.0
        elif constriction_velocity_mm_s < 3.0:
            score -= 15.0

        final_score = round(min(100.0, max(5.0, score)), 1)

        if final_score >= 85.0:
            tier = "OPTIMAL_AUTONOMIC_PUPILLARY_REFLEX"
            interp = f"Crisp pupillary reflex (constriction {constriction_pct}%, latency {constriction_latency_ms} ms); robust parasympathetic-sympathetic coordination."
            guidance = "Excellent visual-autonomic processing and neural alertness. Sustain current focus rhythm."
        elif final_score >= 70.0:
            tier = "NORMAL_BALANCED_PUPILLOMETRY"
            interp = f"Intact pupillomotor kinetics (constriction {constriction_pct}%, latency {constriction_latency_ms} ms); normal autonomic responsiveness."
            guidance = "Standard pupillomotor performance. Maintain periodic 20-20-20 visual breaks."
        elif constriction_latency_ms > 275.0 or constriction_pct < 28.0:
            tier = "SLUGGISH_PARASYMPATHETIC_PUPILLOMOTOR_RESPONSE"
            interp = f"Prolonged constriction latency ({constriction_latency_ms} ms) or reduced constriction amplitude; indicates parasympathetic blunting or central fatigue."
            guidance = "Cognitive or ocular exhaustion detected. Reduce digital display glare, hydrate, and take a 10-minute rest period."
        else:
            tier = "SYMPATHETIC_HYPERAROUSAL_PATTERN"
            interp = f"Elevated baseline tone with altered velocity dynamics (autonomic ratio {autonomic_ratio}); points to acute autonomic arousal or stress."
            guidance = "Elevated sympathetic activation. Engage in slow paced diaphragmatic respiration (6 breaths/min) to restore autonomic equilibrium."

        return {
            "baseline_diameter_mm": baseline_diameter_mm,
            "minimum_diameter_mm": minimum_diameter_mm,
            "constriction_amplitude_mm": constriction_amp,
            "constriction_percentage": constriction_pct,
            "constriction_latency_ms": constriction_latency_ms,
            "constriction_velocity_mm_s": constriction_velocity_mm_s,
            "redilation_velocity_mm_s": redilation_velocity_mm_s,
            "autonomic_velocity_ratio": autonomic_ratio,
            "pupillomotor_resilience_score": final_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
