# Complete exact-kernel lobes: representation and high-zero tail

TARGET: Test whether complete exact-K_n lobes inside [n,2n] admit a fully compensated explicit-formula representation with an absolutely summable zero tail above exp(n), bounded in aggregate by 100*(n+2)^6.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step308's positive-lobe review searched exact Laguerre/von-Mangoldt/lobe terms and explicit-formula regularity; compared stops233/235/243/307, reviews241/304 and L988's sharp-endpoint restriction. No matching complete-root-lobe arithmetic/tail theorem was identified; no novelty claim. Reuse ready source assessments249/251/288 on their stated scopes.
SOURCE_EVIDENCE: Montgomery-Vaughan, Multiplicative Number Theory I (2007), Theorem12.13/Lemma12.14 pp410-416, https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf ; DLMF18.18.18 https://dlmf.nist.gov/18.18.E18 ,18.9.23 https://dlmf.nist.gov/18.9.E23 ,18.14.8 https://dlmf.nist.gov/18.14.E8 ; Hasanalizade-Shen-Wong arXiv2107.06506v1 Cor1.2/(1.5) p2 https://arxiv.org/pdf/2107.06506v1 . Complete proof-case assessments reused from reviews249/251/288; audited L988 supplies exact derivative and zero-shell bounds.
COMPARISON: Known explicit-formula, global polynomial-derivative and counting inputs cover ingredients. L988 removes nonzero sharp endpoint terms; the changed hypothesis here is exact kernel-root endpoints on multiple complete lobes. The missing work is admissibility, arithmetic compensation, absolute convergence and aggregate n-uniform bookkeeping, not a reproof of the general theorems or an estimate for low zeros.
GAP: No complete-lobe representation, bound by the displayed polynomial, positive-lobe budget or bound for clipped endpoint pieces has been established here. Test these exact representation/high-tail obligations only; the signed low-zero contribution and both logarithmic complements stay open.
REASON: The completed source review identifies a bounded specialization that isolates a technical obligation for the positive-contribution budget without repeating the window-energy estimate. Save it for separate next-turn approval; no mathematical attempt occurred during step308.
LITERATURE_REASON: Complete exact-root endpoints and the nonlinear positive-lobe application are outside the previous sharp-block remainder and Gaussian-germ targets; reuse their adequate theorem coverage rather than reopen their searches.
SCOPE: Integers n>=2, actual Lambda including prime powers, exact K_n from review241/L985, all actual nontrivial zeros with analytic multiplicity, complete root-to-root intervals wholly inside [n,2n], spectral cutoff H=exp(n) excluded from the high tail. No RH, zero simplicity, hypothetical zero realization, uniform root spacing, new zero-free region, or signed low-zero premise.

## Exact proposed objects

Use K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
with the constant correction in L985's connection retained.
Let I_n be the finite collection of intervals [a,b] whose endpoints
are consecutive distinct real zeros of K_n and n<=a<b<=2n.
Do not assume simple roots, a spacing asymptotic, or nonempty I_n.
This collection omits intervals clipped by n or 2n unless the clipped
endpoint itself is an exact kernel zero.

For I=[a,b] in I_n define the proposed arithmetic and spectral objects

    C_(n,I)=sum_(exp(a)<m<=exp(b)) Lambda(m)*K_n(log m)/m
                                      -integral_a^b K_n(u)du,
    T_(n,I)(s)=integral_a^b exp((s-1)*u)*K_n(u)du.

The requested numerical threshold, to prove or reject, is

    sum_(I in I_n) sum_(rho, |Im rho|>exp(n)) |T_(n,I)(rho)|
                                      <=100*(n+2)^6,  n>=2.

This is a chosen test threshold, not an estimate derived in this
literature turn. Count actual zero multiplicities, not synthetic
quartets; zeros at the cutoff belong to the finite low-zero part.
Also obtain the exact representation of each C_(n,I) from the named
explicit formula, retaining the pole, trivial-zero/archimedean terms
and every endpoint convention. Do not assume that representation
merely because the spectral integrals are defined.

## Ready imported contracts and remaining specialization

Reuse review288's full inspection of Montgomery-Vaughan Theorem12.13:
for some fixed delta>0 its measurable test F has finite integrals
of exp((1/2+delta)*2*pi*|x|) against |F(x)|dx and |dF(x)|,
has midpoint jump values, and satisfies
F(x)+F(-x)=2F(0)+O(|x|) near zero. The transform is
Phi(s)=integral_R F(x)*exp(-(s-1/2)*2*pi*x)dx.
The primitive principal character modulo1 is allowed. The zero
sum is initially symmetric; all prime, pole and gamma terms remain.
Lemma12.14 handles the conditional gamma integral for its L1/BV test
with the stated O(|x|) behavior at zero. Its zero/nonzero origin
cases were inspected in review288. Import these results, not a
fresh contour proof. Supply the correct F and normalization and
check every hypothesis; a source's test-dependent constants are
not degree-uniform error bounds.

Reuse audited L988's exact K_n derivative bounds, including n=2,
and its actual-zero shell bound (10). Their external inputs are
DLMF18.9.23, the global inequality18.14.8 for alpha>=0 and u>=0,
and Hasanalizade-Shen-Wong Corollary1.2 for every real T>=e.
The prior assessments inspect the multiplicity, height-endpoint and
small-height cases, with external numerical inputs imported rather
than independently rerun. No asymptotic O term may be differentiated.
L988's conclusion on [n,2n] is not automatically a theorem about
[a,b]; prove the needed finite-interval specialization and keep both
derivative boundary terms. Justify the number of complete intervals
and the aggregate constants without root-location numerics.

A fixed finite-degree absolute convergence proof must precede an
identification or rearrangement of the infinite zero sum. Full prime
power weights must be reconciled with the source's midpoint convention,
including a hypothetical prime-power endpoint at exp(a) or exp(b).
The compact support and continuity claims for the proposed test must
be checked, not replaced by a smooth-test theorem on a changed weight.
Retain the lower compensator endpoint exactly. Do not silently transfer
this result to either clipped lobe or to the whole L984 moving cutoff.

## Use, test and stopping boundary

The main gap remains L030-L032/C032a and L966/L968, with L984(H)
unpaid. A successful result would remove the high-zero and leading
endpoint-series obligation for complete-lobe representations. It
could permit a later signed analysis of the finite low-zero terms
in the positive compensated lobe budget. It supplies no such sign
analysis, no bound for sum max(C_(n,I),0), and no full bulk estimate.

Continue only if the exact representation and the displayed uniform
high-tail threshold are justified with all costs. A failed formula
hypothesis, surviving leading endpoint term, or insufficient aggregate
tail is a precise failure or unfinished obligation, not evidence that
the actual positive resource grows exponentially. Stop after this
one test; a passing tail alone does not justify a chain of sharper
absolute bounds. A later research direction needs a concrete signed
low-zero input or a materially different mechanism.

This is REPRODUCTION specialization, not a creative central proof
attempt. Creative routing remains blocked by an independently justified
signed aggregation mechanism. Relevant inputs: review241, L981/L982
endpoint normalization, L985's exact connection, audited L988 and
reviews249/251/288. L983 and C999b are comparisons, not premises.
Low-zero signs, partial lobes, both logarithmic complements and any
subsequent regulator/infinite-degree exchange remain open. No
cross-notebook input. Full matching Mathlib coverage is unchecked
and unknown; ordinary finite calculus and series estimates are
supporting facts, not a claimed full matching formalization.

Prepared in step308; newly written ready scope requires separate
literature approval next turn before a mathematical invocation.
