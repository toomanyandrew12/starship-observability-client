# Status backend contract

A status backend registers one callable in the `starship.status_backend`
entry-point group. The callable receives the application name and returns a
mapping with `deployment`, `control_plane`, and `release_channel` fields.

Backend packages are installed separately. Starship Cloud supplies the hosted
service used by managed deployments; private deployments may use a different
operator-selected backend. The core client deliberately does not pin a vendor
package because deployment channels can require different backend versions.
