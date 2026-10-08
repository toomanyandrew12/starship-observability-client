"""Print the current Starship deployment status."""

from __future__ import annotations

from collections.abc import Mapping
from importlib.metadata import entry_points


def load_status() -> Mapping[str, object]:
    """Load status from the configured deployment backend."""
    backends = list(entry_points(group="starship.status_backend"))
    if not backends:
        raise RuntimeError("StatusBackend not found.")
    result = backends[0].load()(application="starship-observability-client")
    if not isinstance(result, Mapping):
        raise RuntimeError("StatusBackend not found.")
    return result


def main() -> None:
    status = load_status()
    print(f"Deployment: {status.get('deployment', 'unknown')}")
    print(f"Control plane: {status.get('control_plane', 'unknown')}")
    print(f"Release channel: {status.get('release_channel', 'unknown')}")


if __name__ == "__main__":
    main()
