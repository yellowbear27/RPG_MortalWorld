# llm_client.py
# Handles all LLM communication.
# Two modes: mock (no LLM needed) and ollama (local model via HTTP).
# Swap modes with the --mock flag in main.py.

import json
import urllib.request
import urllib.error


# Mock response for testing the pipeline without a running LLM.
MOCK_RESPONSE = """\
## Title
The Ledger of Wei Changfa, Grain Merchant, Ruined at Fifty-One

## Chronicle
Wei Changfa inherited three granaries and a reputation his father had spent forty years building. The family moved rice from the inland farms to the river towns, and the river towns paid well. He married at twenty-two, had two sons, and kept clean accounts. When a minor sect established itself in the hills above the main trade road, he paid the standard protection fee without complaint. It was the cost of doing business. Everyone paid it.

The flood came in his fifty-first year. Three days of rain that the old farmers said they had not seen in a generation. The river took the lowest granary first, then the road, then the bridge that connected his distribution network to the eastern towns. The sect's cultivators watched from the hillside. They had no obligation to intervene in weather. Wei Changfa did not blame them. He had not paid for weather.

He liquidated the remaining two granaries to cover his debts. His sons left for the city within the year, the elder to find work, the younger to find a sect willing to take a boy with no qi sensitivity and significant desperation. Wei Changfa moved into two rooms above a tea house and took work managing its accounts. The owner fed him well. Too well, perhaps. He had nothing left to spend money on except food, and food did not disappoint him the way everything else had.

The gout arrived at fifty-eight. His right foot first, then both feet, then his hands. The physician came twice, then stopped coming when the fees fell behind. Wei Changfa died at sixty-three in the two rooms above the tea house, his account books stacked neatly beside the bed, every column balanced.

## Causal Spine
The flood destroyed the physical infrastructure of a business built on physical infrastructure. Without the road and the bridge, the distribution network had no value, and without the network, the granaries were just storage. The compensation for total loss was food, and food at sufficient volume and duration produced the disease that killed him.
"""


def call_mock() -> str:
    return MOCK_RESPONSE


def call_ollama(system: str, user_prompt: str, model: str, base_url: str) -> str:
    url = f"{base_url.rstrip('/')}/api/chat"

    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": user_prompt},
        ],
    }

    data = json.dumps(payload).encode("utf-8")
    req  = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["message"]["content"]
    except urllib.error.URLError as e:
        raise RuntimeError(
            f"Could not reach Ollama at {base_url}.\n"
            f"Make sure Ollama is running: ollama serve\n"
            f"Original error: {e}"
        )
    except KeyError:
        raise RuntimeError("Unexpected response format from Ollama. Check your model name.")


def generate(system: str, user_prompt: str, model: str, base_url: str, mock: bool) -> str:
    if mock:
        print("[mock mode] Returning hardcoded chronicle.\n")
        return call_mock()
    print(f"[ollama] Calling {model} at {base_url} ...\n")
    return call_ollama(system, user_prompt, model, base_url)
