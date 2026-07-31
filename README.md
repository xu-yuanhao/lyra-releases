# Lyra Releases

This is Lyra's official, binary-only distribution repository. It contains signed release metadata and downloadable artifacts produced from Lyra's private source repository.

Published assets may include:

- signed channel catalogs and exact release BOMs;
- component archives and online or offline installers;
- SHA-256 checksums, component SBOMs, size reports, and third-party notices; and
- Lyra release-signing public keys.

This repository does not contain Lyra source code, build credentials, or private signing keys. Its contents do not grant an open-source license to Lyra.

Only manually reviewed Preview releases may be published while Lyra's operating-system code signing, legal-release, and full compatibility gates remain incomplete. Stable distribution and automatic Core replacement stay disabled until those gates are machine-verifiable.

Lyra verifies component signatures, trusted-key scope, catalog sequence, target platform, size, and SHA-256 before activation. For a manual download, compare the asset with the `SHA256SUMS` file attached to the same release.

Security issues should be reported privately as described in [SECURITY.md](SECURITY.md).

