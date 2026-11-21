# Linked reciprocal factors and a Hermitian realization — source comparison

TARGET: Assess whether the linked identity b c=1 yields a Hermitian block-operator realization of the projection-weighted J-Q with an independently checkable inertia bound, without global real-zero or generalized-Nevanlinna membership assumptions.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step448 searched reciprocal Toeplitz/Hankel products, indefinite Birman-Schwinger/Schur inertia, Krein completion and polynomial root/minor obstructions; inspected primary statements and complete relevant proof cases below. Reused ready Fredholm, Schur, divided-difference and class-scope assessments. Targeted duplicate checks found different reciprocal-density quartics, not the proposed local-factor test. No novelty inference.
SOURCE_EVIDENCE: Böttcher-Widom math/0604009v1 (1)-(2), Theorem1.1 pp.2-3 and Section3 p.5; Berkolaiko-Kuchment, J. Spectr. Theory12 (2022),83-104, Lemma2.3, Theorem2.7, Remark2.8, Lemma2.9 and complete proof pp.87-91, DOI10.4171/JST/395; Contino-Maestripieri-Marcantognini 1809.01695v4, Theorem4.17 and Proposition4.18 with complete proofs pp.20-21. Direct links and hypotheses below.
COMPARISON: The reciprocal Toeplitz identity gives a generally non-Hermitian product and full-operator invertibility, not compressed inertia. Indefinite Schur theory permits negative blocks but retains adjoint/domain/kernel conditions and residual index. Krein completion retains a range condition and a nonnegative remainder for the prescribed bottom block. No inspected theorem supplies an independent actual-Xi bound for J-Q.
GAP: An independently controlled actual-Xi realization, residual index and strict nullity bound are missing; neither reciprocity nor freedom to choose a completion supplies them. General grouping, extension of L782 beyond its fixed pair, orders/radii and other mixed minors remain unproved.
REASON: New theorem-hypothesis/proof-case evidence parks the automatic linked-factor-to-index import, without claiming nonexistence. Nominate one exact polynomial local-factor diagnostic with separate approval, rather than another class import, positive-block test or actual-pair sign replay.
LITERATURE_REASON: This new target asks about linked-factor Toeplitz/Hankel and indefinite block-operator structure, which the ready divided-difference/determinant assessment and the inspected global-class theorems do not cover.
SCOPE: Completed literature-only step448; original nomination below retained as historical scope. No new realization, inertia value, counterexample, lemma or mathematical script was derived. The separate new model-test assessment receives approval next turn before mathematics.

## Original nomination: mathematical purpose and bounded review

The main gap is actual-Xi all-degree mixed positivity. The intermediate
question is whether keeping the exact inverse relation between b and c
offers a separately testable source of signed-inertia control. A usable
realization could connect a structural operator estimate to the actual
determinant while permitting L780's adverse blocks. It would still leave
global grouping, uniformity and other mixed minors unresolved.

Use L777's b=p/F, c=F/p, A=Q_r H(b)H(tilde c)Q_r and A=UCY*.
Use L782's exact definitions h_r,K,E,J,Q at (r,R)=(3,2048) to fix
conventions; L779 supplies only that pair's independently certified
real/simple negative nodes and complete residues under its retained
arithmetic contracts. L776 and L017/L018/L021 remain inherited inputs.
No identity for a different pair has been proved by L782. The broader
candidate setting would have L777's admissible r, k=r-1, independently
certified simple negative interior nodes and zero-free local F, without
assuming anything about other zeros. Its weighting generalization is
an obligation, not an imported result.

Review relevant primary Toeplitz/Hankel inverse-product identities,
Hermitian Schur-complement/inertia theorems and indefinite operator
realizations. Retrieve exact hypotheses and the proof cases concerning
indefinite blocks, domains and nullspaces before longer source extracts.
Reuse the existing finite-rank determinant and Schur coverage. Do not
assume that bc=1 is a positivity premise or that a formal Hermitian
linearization determines its index.

Continuation test: identify a primary theorem whose hypotheses map to
the actual linked factors and a specific additional estimate that can
be tested without assuming the desired sign, global real zeros, or
half-plane class membership. Record all missing analytic/domain and
uniformity conditions. Only then nominate a separately reviewed bounded
mathematical target. A fixed-pair sign recomputation merely reproducing
L779 is insufficient. No parameter sweep or Taylor-index test is proposed.

Abandonment test: if the source only rewrites the target determinant or
requires the unpaid inertia, positive eliminated blocks, or global
real-zero/class membership, park that import and name the precise
obstruction. Such a scope failure would not ban all indefinite methods.
An explicit new premise must be identified before repeating this lead.

Checked local comparisons: the step443 reciprocal-inertia assessment
and automatic-index-import stop; step444's closed nondiscriminating
Taylor test; the ready balanced-Schur comparison and L780's statement;
L782's new audit. This is a proposed source question, not evidence of
novelty or a mathematical result. Full matching Mathlib coverage is
unchecked. No cross-notebook result is needed.

No covered creative attempt is currently available: L782 pays a local
normalization, not a new index mechanism. This review prepares essential
coverage rather than labeling its known-method audit creative. A later
creative nomination must name a concrete new structural claim and a
discriminating finite test; it is not preapproved here.

## Completed review — step448, 2026-11-05

The main gap is actual-Xi all-degree mixed positivity. This review asks
whether linked factors provide independently controlled Hermitian blocks
whose inertia could sign the exceptional determinant while allowing
L780's adverse blocks. Global grouping and all mixed minors would remain
separate. No realization or index estimate is derived in this turn.

### Primary interfaces and essential proof cases

A. Böttcher and H. Widom, *Szegő via Jacobi*,
[math/0604009v1](https://arxiv.org/pdf/math/0604009v1), 1 April2006,
(1)-(2), Theorem1.1, pp.2-3 and complete Section3, p.5. Reuse the ready
Fredholm assessment; the new inspection concerns its inverse-product
proof. The symbol is nonvanishing, zero winding and C^beta, noninteger
beta>1/2. Its normalized Wiener-Hopf factors give bc=1 and

    I-H(b)H(tilde c)=T(b)T(c).

The proof establishes full-operator invertibility by triangular factors,
then obtains the projected determinant by Jacobi's theorem. No Hermitian
or positive-symbol premise is imposed. L777 supplies annular smoothness
and the identified factor normalization for its fixed admissible pair.
The theorem asserts no inertia or invertibility for every tail
compression; its product is not presented as T(b)T(b)*. Scalar inversion
c=1/b is not the additional adjoint relation that such an argument would
need. No new sign bound is imported.

G. Berkolaiko and P. Kuchment, *Spectral shift via “lateral” perturbation*,
J. Spectr. Theory **12** (2022),83-104,
[publisher PDF](https://ems.press/content/serial-article-files/33861),
DOI10.4171/JST/395, Lemma2.3/Theorem2.7/Remark2.8/Lemma2.9 and complete
proofs, pp.87-91. For a selfadjoint H=[A B;B* D], the orthogonal block
projection must preserve Dom(H), with the stated closed selfadjoint
diagonal blocks. Part1 assumes 0 outside the essential spectrum of D
and ||Bx||<=C||Dx|| on its domain. With any generalized inverse D^+,

    n_-(H)=n_-(D)+n_-(A-BD^+B*),
    n_0(H)=n_0(D)+n_0(A-BD^+B*),

assuming relevant indices finite. Read also Part2's two-sided comparison
and its additional symmetric A-condition. The proof establishes
ker(D) subset ker(B), range inclusion, independence of BD^+B*, and
bounded BD^+ for a suitable choice; an invertible triangular congruence
then preserves index/nullity. Negative D is allowed. In finite dimension
the kernel condition is equivalent to the displayed estimate. Nullity
alone does not require finite negative index, as Remark2.8(5) qualifies.
These identities retain the remaining Schur complement's index.

M. Contino, A. Maestripieri and S. Marcantognini, *Schur complements of
selfadjoint Krein space operators*,
[1809.01695v4](https://arxiv.org/pdf/1809.01695v4), 19 July2019,
Theorem4.17 and Proposition4.18 with complete proofs, pp.20-21.
W is bounded and Krein-selfadjoint, S regular, and
W=[w11 w12;w12# w22]. For a polar factorization w11=dd#,
Theorem4.17 requires ran(w12) subset ran(d); the complement is
w22-y#y, where dy=w12 has the specified unique bounded solution.
Proposition4.18 additionally assumes finite negative squares of w11.
Completions with the same negative index exist exactly under that range
condition; their bottom blocks have w22=y#y+z, with z=z# nonnegative
in the Krein form. The proofs translate to Hilbert-selfadjoint JW and
polar factors, retaining this remainder. Existence of a permissible
completion does not certify a prescribed w22. Nor does the result give
automatic strict nullity control.

### Comparison and route decision

L782 already makes J-Q symmetric at (3,2048). Embedding that matrix in
a tautological Hermitian linearization adds no independent index bound.
L777's A=UCY* retains distinct U,Y and both projections. It supplies
neither the adjoint cross-block identification of a proposed larger
operator nor an estimate of its remaining Schur complement. L782's
complete-series similarity adds neither premise.

No unbounded operator was constructed here. A later proposal must check
its domains, invariant projections, spectral gaps, inverse bounds and
kernel/range conditions. For a finite realization, domains are automatic
but residual inertia/nullity remain obligations. In the Krein theorem,
allowing negative blocks still requires the prescribed completion to
satisfy a residual form inequality. No inspected source identifies Xi's
linked factors with such a completion. This is missing mathematical
payment, not missing source access.

The immediate-import continuation threshold therefore fails. Park the
automatic linked-factor-to-index import. This is new source-scope
evidence, not proof that no realization exists or new mathematics beyond
the sources. The automatic-class, positive-block and nondiscriminating
Taylor stops remain intact; L780 does not ban other signed methods.

### Search, duplicate checks and separate continuation

Queries included `Toeplitz Hankel b c reciprocal identity I H(b) H tilde c
Borodin Okounkov Basor Widom`; `Haynsworth inertia additivity formula
singular block Hermitian matrix theorem primary`; `indefinite Birman
Schwinger inertia Schur complement J finite rank sign changing
perturbations theorem`; `selfadjoint block operator matrices Schur
complement inertia finite negative index bounded theorem Tretter`;
`Toeplitz determinant three by three polynomial two negative roots
complex conjugate zeros Pólya frequency zeros sector`; and
`"Toeplitz" "inertia" "reciprocal" Hankel`.
The inspected statements concern general product/Schur/completion
interfaces, not the requested actual-Xi bound. General block monographs,
the main lateral-perturbation theorem and search-returned polynomial
sector results remain leads, not imported estimates. No absence or
novelty inference is made.

Read the needed L777 normalizations, complete L782 proof/audit and
L780 statement. Reused ready exact-projection, interior-zero, exceptional
Fredholm, signed-Schur and step443 class assessments. Targeted reads of
the reciprocal-density assessments distinguish their quartic Green
kernels and degree-eight bilateral-transform model from this local-factor
J-Q diagnostic. No identical test was found in the inspected paths;
this does not certify originality. No sibling notebook was consulted.

Nominate only the single rational quartic model in
`2026-11-05-reciprocal-quartic-inertia-test.md`. Its roots, coefficient
conditions, complete projection weighting and inertia must all be checked
later; no model value was calculated here. An adverse inertia would
demonstrate insufficiency of the local premises, not an Xi counterexample.
A passing model closes that diagnostic without supporting a universal
claim. This differs from replaying L779's sign or increasing Taylor size.

The new SPECIALIZE assessment requires separate approval next turn.
This is an ordinary known-method obstruction calculation, not a creative
Xi mechanism. The blocker to a justified creative realization remains
an independent structural estimate; a realization identity alone cannot
be relabeled as one. No mathematical exploration budget was spent or
reset; all needed primary sources were accessible. Full matching Mathlib
coverage remains unchecked. No lemma/script, PROOF.md, DAG.md or
supervisor state was changed; existing unfinished work was preserved.
