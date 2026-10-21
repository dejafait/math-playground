# Removal of the fixed survivor at thirteen — stopped

2026-10-13. [L064](../lemmas/L064-thirteen-adic-canonical-class-membership.md)
supplies an exact same-class whole-fiber witness at scalar 3. The entire
canonical and witness algebras are the same unramified degree-twelve
field, both connecting classes are the identity, and one common primitive
triple is obtained by certified Hensel lifting. Independent critical
application audit completed on 2026-10-13 confirms the witness; all 52
independent checks pass in `scripts/thirteen-adic-membership/audit-certificate.json`.

WHY IT FAILS: Failure of the canonical scalar's primitive witnesses does
not exclude its connecting class. The different scalar 3 has common
primitive witnesses and realizes precisely the localization of L062's
fixed global class. Thus this thirteen-adic restricted filter cannot
remove that survivor. This says nothing about full image equality,
other classes or primes, the all-place intersection or integer lifting.
Reopening this exact exclusion requires a concrete defect in the witness;
changing class or local conditions is a different, separately assessed
target. Preserve the quotient, finite-generator and earlier local stops.
