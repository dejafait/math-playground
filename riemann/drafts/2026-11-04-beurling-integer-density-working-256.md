# Integer-density compatibility working checkpoint — step 256

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-04-beurling-integer-density-specialization.md`.
This is one REPRODUCTION proof attempt, using audited L735 and the
already inspected Révész/DLMF inputs. No new source discovery or
construction is intended. Existing notebook changes are preserved.

Main gap: unconditional actual-Xi mixed positivity. Intermediate target:
decide whether L735's coefficient-1 psi asymptotic can coexist with
N_P(x)=kappa x+O(x^theta), kappa>0, 0<=theta<3/4, counting all formal
integers and the unit. A negative answer would identify missing
integer-count structure, without paying actual-prime prefix norms,
scalar anchors or complementary residuals. The coarse-kernel stop
does not cover this added hypothesis and is not being reopened.

Planned bounded test: match the Axiom-A continuation with the same
Euler-product zeta, analytically transform the full psi error, then
compare the local logarithmic-derivative residue at b=3/4 with an
integer Taylor order. Abandon the specialization if a necessary
endpoint or common-domain hypothesis cannot be justified. No parameter
sweep, numerical script or global explicit formula is needed.

Partial reasoning, not yet a certified result: use
eta=(theta+b)/2 in (0,b) to match the source's positive exponent,
including theta=0. For E(x)=psi(x)-x+x^b the candidate identity on
Re(s)>1 is -zeta'/zeta=s/(s-1)-s/(s-b)+s integral_1^infinity
E(x)x^(-s-1)dx. E(1)=0; extend its eventual error bound by local
finiteness to C sqrt(x)log(2x). Uniform convergence and first
derivative domination should make the final integral analytic on
Re(s)>1/2. This gives candidate residue -b. Under the N hypothesis,
zeta is holomorphic at b; its local order m would require residue -m.
The common meromorphic identity and all finite endpoint terms still
need to be written out before the incompatibility conclusion.

Duplicate/failure coverage reused the completed coefficient-scope
assessment, L735 including its step-253 audit, and
`ATTEMPTS/2026-11-04-self-generated-coarse-kernel-discrimination-stop.md`.
No prior necessity result is recorded there. This is a specialization
of standard inputs, not a claim of originality or an RH candidate.

## Completion

The full argument is now canonical in L736. It gives incompatibility
by the residue/order comparison after the endpoint and analytic checks.
Outcome NEGATIVE, classification REPRODUCTION; a separate conceptual
audit is still required. The only added DAG row uses L735. No scripts,
power sweep, new construction or actual-prime transfer were attempted.
