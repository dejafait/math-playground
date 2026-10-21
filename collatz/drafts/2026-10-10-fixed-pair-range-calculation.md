# Fixed-pair range calculation — working record

Approved target: determine the maximal initial word-count range excluded
by L050's fixed rational pair and cyclic-product method, retaining L041's
seed, L046's 48/25 transfer and all exact endpoints. Prior coverage is
`drafts/literature/2026-10-10-fixed-pair-cyclic-product-range.md` (SPECIALIZE).

Main gap: universal eventual descent. The intermediate range test can
extend a restricted exclusion and identify this comparison's limitation;
entry, unrestricted cycles and divergence remain independent gaps.
Continue only with rigorously justified substitutions and exact signs;
stop at the first certified failure of the specified sufficient predicate.

Read the complete L050 proof/audit, L041's relevant all-r proof and
L046's real-domain transfer/prefix argument, plus Attempts 019/021–023.
There is no duplicate range result in those records. Reuse the precise
published inputs and their computational/Rhin/Crandall qualifications.
No new source theorem is needed; the ready assessment covers this scope.

For general r, r-1 forward transfers give
K<(15/4)R_r(h_0+1), hence N<A_r log N+B_r by the unchanged seed
and length conversion. All r exact endpoints give
Lambda=sum log(1+eta_i/n_i)<23r/(11n_0), with 0<eta_i<23/11.
With integer counts and a certified ceiling M satisfying
2M epsilon<log2, the same z=Nq-Kp>=1 argument gives
Lambda>log2/(2q)>1/(3q). Thus h_0<log D_r and K<T_r.
These are preliminary reasoning notes, awaiting canonical write-up and
exact certification of every sign. No new exclusion is claimed yet.

Next in this bounded attempt: implement rational enclosures with explicit
positive integral remainder, find and certify the least integer ceiling
by its preceding integer, then test from r=3 only until first failure.
All full operands will be saved under scripts/postspell-word-count/.

## Completed calculation

Canonical proof: L051. All variable-count substitutions are justified;
the exact predicate succeeds for every 3<=r<=22 and fails first at r=23.
The least ceilings at 22/23 are 3386647505/6697335032. At 23 both the
half-log guard and odd-count comparison fail. The generator saves complete
evidence in `scripts/postspell-word-count/fixed-pair-range-certificate.json`;
all 107 sign checks pass, including signs certifying predicate failures.
The full sign list, log2/log3/residual enclosures and boundary rows were
inspected. No unresolved strict comparison remains in this attempt.
Stop this fixed test; separate critical audit and source qualifications
remain. No real-system feasibility or actual cycle is established at 23.
