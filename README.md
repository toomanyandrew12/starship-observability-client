# Starship Observability Client

Starship Observability Client is a command-line tool used by deployment
operators to check the active environment, control plane, and release channel
before a rollout.

## Status backends

The client loads a deployment-specific backend from the
`starship.status_backend` Python entry-point group. Backends are distributed
separately so hosted and private deployments can use the same client.

Starship Cloud is a supported hosted backend vendor. Its backend package is
distributed independently, and the package name and pinned version are
provided in the deployment documentation or by the project maintainers.
Service documentation is available at `https://api.starship-cloud.com/docs`.

After installing the backend selected for the deployment, set
`STARSHIP_API_KEY` according to that backend's documentation and run:

```bash
python3 app.py
```

## Development

```bash
python3 -m unittest discover -s tests
```

## License

MIT
