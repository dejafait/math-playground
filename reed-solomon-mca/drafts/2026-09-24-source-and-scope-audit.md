# Source and scope audit — 2026-09-24

Work saved during the initial source audit. No local prior lemma, failed approach,
or unfinished edit was present; other notebooks' existing changes are untouched.

The [official challenge](https://proximityprize.org/) specifies smooth evaluation
domains, rates in {1/2, 1/4, 1/8, 1/16}, and the largest radius with MCA error at
most a prescribed epsilon (illustratively 2^-128), assuming a sufficiently large
field. It still labels the statements preliminary.

The [ABF26 record](https://eprint.iacr.org/2026/680) identifies Gal Arnon, Dan
Boneh, and Giacomo Fenzi, *Open Problems in List Decoding and Correlated
Agreement*, received 2026-04-07 and last revised 2026-07-06, with three revisions
reported. Its update note says the KKH comparison and concrete attacks changed
and an MCA lower bound was added. These facts do not freeze the error definition.

Access obstacle: the official PDF returned HTTP 403 through the web tool; local
curl could not resolve the host. Author pages inspected so far link back to
ePrint. No secondary account is being substituted for the exact definition.

Gap for this step: the exact quantifiers and error event have not been audited.
Intermediate target: a cited, version-specific definition and a comparison of
one candidate counting bound with the required epsilon. This would prevent a
list-size or ordinary correlated-agreement statement from being mistaken for
MCA. Test: obtain the primary definition and check its quantifier order; if
unavailable, retain an explicitly incomplete scope audit and choose no technical
route based on an assumed definition. No mathematical claim is established here.

## Assessment

The bounded test did not recover the current primary definition. A third-party
reconstruction was found, but it explicitly disclaims being the authors' TeX
and carries an April date; the accompanying PDF was unreadable through the web
tool. The inspected primary metadata makes the version difference material.
Repeated URL variants did not resolve access and are not a technical research
mechanism. The confirmed scope and missing items are retained in
[the source audit](../foundations/01-target-and-source-audit.md).

The step supplies bibliographic and scope information, not a mathematical
advance or an informative mathematical negative result. No lemma is warranted.
The completed-turn decision is recorded in the dated history and compact
checkpoint; this draft does not supply a separate task queue.
