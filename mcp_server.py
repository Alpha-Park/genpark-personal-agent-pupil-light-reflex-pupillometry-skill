"""
MCP Server for Quantitative Pupillary Light Reflex (PLR) Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing pupil constriction dynamics and autonomic tone.
"""

import sys
import json
from typing import Dict, Any
from client import PupilLightReflexClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_pupillary_dynamics",
                "description": "Calculates quantitative pupillometry metrics: constriction amplitude, constriction velocity, autonomic ratio, and pupillomotor resilience score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_diameter_mm": {
                            "type": "number",
                            "description": "Resting pupil diameter in mm prior to light stimulus (e.g. 4.4 mm)."
                        },
                        "minimum_diameter_mm": {
                            "type": "number",
                            "description": "Peak constriction minimum pupil diameter in mm (e.g. 2.7 mm)."
                        },
                        "constriction_latency_ms": {
                            "type": "number",
                            "description": "Latency from stimulus flash to initial constriction in milliseconds (e.g. 225.0 ms)."
                        },
                        "constriction_velocity_mm_s": {
                            "type": "number",
                            "description": "Maximum constriction velocity in mm/s (e.g. 4.9 mm/s)."
                        },
                        "redilation_velocity_mm_s": {
                            "type": "number",
                            "description": "75% recovery redilation velocity in mm/s (e.g. 1.8 mm/s)."
                        }
                    },
                    "required": [
                        "baseline_diameter_mm",
                        "minimum_diameter_mm",
                        "constriction_latency_ms",
                        "constriction_velocity_mm_s",
                        "redilation_velocity_mm_s"
                    ]
                }
            }
        ]
    }


def handle_request(client: PupilLightReflexClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_pupillary_dynamics":
            res = client.evaluate_pupillary_dynamics(
                baseline_diameter_mm=float(args.get("baseline_diameter_mm", 4.2)),
                minimum_diameter_mm=float(args.get("minimum_diameter_mm", 2.6)),
                constriction_latency_ms=float(args.get("constriction_latency_ms", 230.0)),
                constriction_velocity_mm_s=float(args.get("constriction_velocity_mm_s", 4.6)),
                redilation_velocity_mm_s=float(args.get("redilation_velocity_mm_s", 1.8))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = PupilLightReflexClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
