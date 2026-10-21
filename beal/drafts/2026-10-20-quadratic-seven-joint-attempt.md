# Joint quadratic factor at seven — working attempt

Approved target: test whether one primitive seven-adic fiber of
phi(t)=(3t²+t+1)^5(1−5t) contains Q7 × (Q(sqrt(−3)) tensor Q7)
as a direct product factor. Prior coverage is the unchanged EXPLORE
assessment `literature/2026-10-20-quadratic-minus-three-seven-adic-test.md`.

The main gap is integer elimination of both L095 systems; L093, audited
L103 and audited L104 supply the necessary global context. This attempt
tests only simultaneous local factors, retaining the entire degree-eleven
fiber and one common primitive tuple. It does not assume a local rational
factor is global. No cross-notebook input is used.

Continuation test: first determine the entire quadratic completion and
regular residue fibers, including complete factor multiplicities. One
exact primitive witness with the joint factor stops standalone exclusion
at seven. If none occurs, permit only one normalized branch calculation
to precision at most 7^3; a failed bounded search is not an exclusion.
Both integer systems, the minus-eleven alternative, larger global fields,
global compatibility and all other residual signatures remain open.

Known methods/duplicate checks: reuse the supplied assessment, L104's full
proof and audit, L103's whole-factor proof, L093's interface and audit,
foundations/17 and histories 354,356–357. ATTEMPTS/045's class-backend
park is independent. No completed joint seven-adic test was found in the
specified local records. No fresh external source review is needed.

Initial exact residue test: regular scalars 2,3,4,5,6 have respectively
two, zero, one, one, zero rational residue roots; none has three.
The derivative is phi'(t)=−165t²(3t²+t+1)^4. At s=1 the rational
branch t=0 has multiplicity three. Test only this normalized branch,
with A=7, C=1, s=1−7³=−342 and B the fifth root of −342 near one.
The polynomial g(u)=(1−phi(7u))/7³−1 is integral and reduces to
55u³−1=6u³−1. Its three simple residue roots are 3,5,6. If the full
arithmetic certificate confirms these identities, Hensel gives three
disjoint rational factors in this same fiber. The exact degree-eight
complement is obtained by dividing by those three linear factors;
the explicit derivative proves whole-fiber separability at s=−342.

Initial convenience calculation could not use SymPy (module absent).
Use elementary exact integer/finite-field polynomial arithmetic instead;
this is not a mathematical blocker. Preserve the complete certificate
under `scripts/quadratic-seven/`; a preview is not exact lifting evidence.

Completed: canonical L105 records the exact witness, complete regular
factor table, actual seed errors and uniquely specified exact complement.
The complete /regular, /branch, /quadratic and /checks certificate values
were inspected; all 37 checks pass. The normalized branch used precision
343 and no other branch was tested. Hensel, distinct exact roots and
the whole derivative critical-point check prove existence and etaleness.
Standalone exclusion at seven is stopped in ATTEMPTS/046. This is an
informative NEGATIVE using assessed standard methods, not integer or
global realization. The sole continuation is the independent L105 audit,
whose new assessment remains REVIEW_REQUIRED for separate approval.
