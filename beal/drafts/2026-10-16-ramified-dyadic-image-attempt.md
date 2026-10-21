# Ramified dyadic image — arithmetic milestone

Approved target: Certify the full two-descent Kummer image of L033's E0 over H2=Q2(2^(1/11)) using Bruin–Stoll LocalImage, with complete terminal-disk and square-class certificates.

Gate: drafts/literature/2026-10-16-ramified-dyadic-two-descent-image.md (SPECIALIZE, saved before invocation).

Main gap: primitive integer emptiness. The local image could supply a test for additional supported-unit restrictions; global independence from L077 and localized class contributions remain separate.

Inputs: L046's pi^11=2; L071's s^3-4s^2+6s-2=0 and theta=28-26s+6s^2; L076's entire degree-33 field. L069 fixes the Kummer coordinates. No cross-notebook input. ATTEMPTS/034–036 are parked, with no duplicate local image certificate found.

Work saved before implementation: rho=pi^4/s has candidate equation rho^3-3pi^4 rho^2+2pi^8 rho-pi=0, Eisenstein over H2. Its candidate inverse map is s=4-3pi^7 rho+pi^3 rho^2. Verify these exact identities and maximality first. The basis pi^i rho^j (0<=i<11, 0<=j<3) has candidate valuations 3i+j, giving exact finite arithmetic modulo 8 with error valuation 99.

Next internal stage: implement and prove a complete unit-square normal form through rho-adic digit 66. Required precision is greater than 2v_J(2)=66, rather than the rational-base threshold. A class label is arithmetic infrastructure, not a point image. No image representatives, terminal disks or global dimension change are yet claimed.

Bounded test: continue if a certified arithmetic/precision milestone is obtained; stop this implementation if those obligations fail. The complete target still requires both LocalImage charts, point realization, every terminal/rejected disk and class collisions, with an independent image-size check. A finite sampling cutoff proves no nonmembership.

## Completed attempt

The internal arithmetic stage above was completed. The canonical statement,
full proof, precise citations and Mathlib qualification are in
[L078](../lemmas/L078-ramified-dyadic-maximal-ring-square-test.md), rather than
in this saved planning note. Its [certificate](../scripts/ramified-dyadic-image/arithmetic-certificate.json)
has 79 passing checks and no failures. The selected complete coordinate,
precision, check and fixed-comparison fields were inspected. The proof
establishes every unit-square decision by induction; the numerical tests
do not stand in for that proof.

This meets the allowed concrete arithmetic/precision milestone, so the
local-image mechanism remains justified. The full approved target is
unfinished: no LocalImage terminal/rejected disks, complete point-image
representatives, or global independence certificate were produced. The
new local coordinates do not change fourteen versus eleven or determine
the localized class contribution. This is RESEARCH / REPRODUCTION using
ready coverage, not progress beyond the sources checked. The same exact
target and its unchanged pre-invocation SPECIALIZE assessment remain
applicable; no new target or source scope is proposed.
