# Corrected even Pólya reference: completed collision source screen

TARGET: Assess the normalized corrected even Polya reference R and the actual-Xi interpolation H_tau=(1-tau)R+tau Xi, seeking source coverage and prior obstructions for the proposed collision threshold (Xi-R)(x) H_tau''(x)<=0 at real double zeros, before any calculation.
CHECKED: 2026-11-05
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Step573 searched corrected xi**, universal-factor, convex-combination and collision terminology; inspected Polya1926 final note and HilfssatzII proof, Gasper0801.2996v1 Section3, Fell1980 Theorem2/proof, and the named local fold/compensation/Gaussian stops. Exact searches and limits below; no novelty inference.
SOURCE_EVIDENCE: Polya1926 Acta Math.48,305–317, DOI10.1007/BF02565336, final note p317 and HilfssatzII pp316–317; Gasper arXiv:0801.2996v1 Section3,(3.1)–(3.6),pp5–6; Fell Pacific J.Math.89(1)(1980),43–50, Theorem2 p46 and Lemma1 proof pp43–45; reused Lessard2016 scalar-fold/contraction coverage in 2026-11-05-theta-compensation-homotopy.md. Polya1927 proof not retrieved.
COMPARISON: The exact corrected even kernel and frequency are now identified. Polya asserts its all-real theorem but omits the extension proof; Gasper refers it to Polya1927 rather than proving it by his xi* square identity. Polynomial paired-zero convexity and the finite fold do not sign this actual entire interpolation. No inspected source supplies the proposed inequality.
GAP: Actual collision sign, nondegeneracy and useful uniformity remain unknown. The primary1927 universal-factor proof is unread; global use of the reference theorem is parked pending that coverage. A local signed-collision diagnostic needs only the explicitly defined kernels and nonzero center, not an all-real-reference premise.
REASON: Complete the source screen without importing an uninspected proof or approving a global RH bridge. Nominate a separately reviewed local actual-kernel mechanism test independent of the blocked real-zero-proof input.
SCOPE: Completed literature-only step573. No new lemma, script, root calculation or deformation identity. Local analytical sign discovery is nominated separately; global tracking, multiplicities and infinity transfer are not covered. Mathlib matching coverage unchecked.

## Original nomination (preserved)

The exact proposed reference is Polya's xi** from the final correction
note on p.317 of [the primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5376-11511_2007_Article_BF02565336.pdf),
not xi* from (6) and not the non-even first theta summand. After verifying
that its central value is nonzero and its frequency convention agrees,
the proposed normalization is R(z)=Xi(0) xi**(z)/xi**(0), with Xi the local
completion on the real-frequency axis. No scalar or variable match for
xi** has yet been approved. The reference is not substituted for Xi.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is source assessment of the specified collision threshold for the actual
entire interpolation, for 0<tau<1 and real x satisfying H_tau(x)=
H_tau'(x)=0 and H_tau''(x)!=0. The inequality above is a proposed test,
not a theorem asserted or derived in step572. A sign controlling departure
of real zeros could support a deformation route to real zeros; multiple
collisions, complex zeros arriving from infinity, uniformity and the
mixed-positivity assembly remain independent unpaid steps. A local fold
calculation or finite-window success would not prove RH.

Inspect the final source note and the invoked real-zero result before
larger passages. Reuse the primary finite-fold hypotheses already assessed
in `2026-11-05-theta-compensation-homotopy.md` and
`2026-11-05-theta-compensation-crossing-test.md`; do not repeat their finite
Gauss-family calculations. Compare the actual-theta signed-compensation
assessment and `ATTEMPTS/2026-11-04-neutral-gaussian-abstract-backward-comparison-stop.md`
for limits of abstract sign transfer. Search exact corrected-reference,
real-zero-preserver and collision terminology, and stronger known results.
Do not treat a generic interpolation criterion as an independently paid
actual-theta inequality. No cross-notebook input is proposed.

Continue only if the exact reference is legitimate and source comparison
leaves a concrete actual-family sign test that is not an exhausted import.
Otherwise record the specific obstruction and park this interpolation.
Any subsequent mathematical target requires separate coverage approval;
a creative attempt is justified only by an actual new signed mechanism
and a bounded discriminating test, not by the age of the scheduling gap.

## Retrieval checkpoint — step573 (superseded by completed comparison below)

Primary 1926 p.317 final note recovered: the proposed xi** is indeed
the even kernel with both cosh(9u/2) and cosh(5u/2), decay
exp(-2pi cosh(2u)), and prefactor 8pi in cosh notation.
Gasper arXiv:0801.2996v1, Section3 (3.5)–(3.6), p.6, repeats this
exact object and points to Polya 1927 for the universal-factor proof;
his own preceding sum-of-squares argument is for xi*, not xi**.
The 1926 final note asserts the corrected conclusion without writing
the extension of HilfssatzII. Primary 1927 theorem/proof access is
still being checked. No local all-real proof or collision sign is
claimed at this checkpoint.

Reused the Lessard scalar-fold hypotheses already extracted in the
finite-compensation assessment. L809 concerns a different polynomial
family and one local real-pair creation; it is no sign input here.
L754's audited abstract Gaussian stop is not an actual-Xi counterexample.
Actual-family sign, degeneracies and infinity control remain unpaid.

## Completed source comparison — step573

The main gap is unchanged. The reviewed intermediate threshold is
(Xi-R)(x) H_tau''(x)<=0 at H_tau=H_tau'=0, for real x and 0<tau<1,
with H_tau''!=0; a fold additionally requires (Xi-R)(x)!=0.
No collision equation, parameter elimination or sign identity was derived.
A usable actual-family sign law could support later deformation control.
Even success would leave degenerate collisions, infinity and mixed transfer.
Continue only with a bounded actual-kernel test independent of those gaps;
park global continuation until its missing inputs have coverage.

### Exact object and source qualifications

[Polya1926 primary PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5376-11511_2007_Article_BF02565336.pdf),
printed p.317, correction dated 5 February1926, defines exactly

    S(z)=8pi integral_0^infinity [2pi cosh(9u/2)-3 cosh(5u/2)]
                         exp(-2pi cosh(2u)) cos(zu) du.

This is xi**, not xi* and not the full first theta summand. Its cosine
frequency is z, agreeing with L020. The proposed reference is
R(z)=Xi(0) S(z)/S(0). This formula is a source transcription and a
normalization specification, not a new local real-zero theorem.
The positive-center applicability check must retain the exact bracket,
2pi>3 and cosh(9u/2)>=cosh(5u/2) for u>=0; L021 supplies Xi(0)>0.
No numerical central-value approximation or variable rescaling is approved.

The note asserts all zeros real and invokes an extension of HilfssatzII
without supplying it. The actual HilfssatzII assumes a real entire genus
0/1 function, only real zeros and at least one zero. Its printed product
modulus proof excludes nonreal zeros of a symmetric imaginary shift sum;
the zero-free exception can vanish identically. This proof was read.
It is not itself a proof for the corrected two-cosh difference. The exact
special-case assertion may be cited as Polya1926 p.317; its extension proof
has not been critically verified here. Do not present it as audited.

[Gasper, arXiv:0801.2996v1](https://arxiv.org/pdf/0801.2996v1),
19 January2008, Section3, pp.5–6: (3.1) proves the shifted-Bessel sum
case via a sign-strict integral. The following (3.3) alternative leaves
a positivity claim conjectural. Equations(3.5)–(3.6) explicitly distinguish
xi** and A cosh(au)-B cosh(bu), A>B>0,a>b>0,c>0. Gasper attributes their
real-zero result to Polya1927. This is supporting identification, not a
primary proof of the corrected theorem. The proposed substitution uses
v=2u, a=9/4,b=5/4,c=2pi,A=2pi,B=3; its harmless scalar and frequency
change must be recorded if that more general theorem is later imported.
His square argument cannot be transferred to Xi-R by replacing a kernel.
No reproof is proposed.

### Stronger known statements and nonduplicates

[H.J.Fell, On the zeros of convex combinations of polynomials](https://msp.org/pjm/1980/89-1/pjm-v89-n1-p05-s.pdf),
Pacific J.Math.89(1)(1980),43–50, Theorem2 p.46, treats monic degree-n
polynomials with each root in a prescribed open interval on one line:
convexity holds exactly for disjoint intervals. Read its proof and the
quotient-trajectory proof of Lemma1, including factoring common roots.
It assumes finite degree and controlled endpoint root locations. Neither
holds as a paid input for this entire actual-Xi pencil; assuming actual
endpoint reality would already pay the target. Its paired-root criterion
is not a collision sign theorem for H_tau.

Reuse Lessard's precise scalar-fold/contraction hypotheses and proof
coverage from the Primary collision theorem and validation method section of
2026-11-05-theta-compensation-homotopy.md and the crossing-test assessment.
For later actual entire use, C2 regularity on a real neighborhood,
H=H_x=0, H_tau!=0 and H_xx!=0 must all be justified; a weak product
inequality alone does not handle a degenerate event. A fixed neighborhood
needs no global real-zero hypothesis. No local orientation is asserted
in this review. A numerical critical point alone would not certify it.

L809's conclusion and imported-method paragraph were read: its polynomial
pencil, actual fifth moments and certified one-pair creation are a distinct
family, with another pair remaining nonreal. It is not a reference sign
for S. The actual product-K compensation assessment identifies missing
signed cofactor control; no such bound was silently reused here.
The audited L754 stop excludes an abstract Gaussian anchor comparison,
not an arithmetic-specific statement for this H. L234's non-even finite
summand obstruction likewise does not apply to this different even S.
No existing exact-S interpolation test was found in the bounded searches.

### Access, search limits and decision

Queries included `Pólya 1926 xi double star corrected 9 cosh 5 cosh real
zeros interpolation`, `Pólya Xi convex combination real zeros double zeros
homotopy`, `Polya "xi**" real zeros 1926 proof`, `Polya "corrected"
"homotopy" zeros`, exact `Riemann`/`interpolation`/`Pólya`/`collision`,
and the exact 1927 title with `pdf`, `universal factors`, `A > B`, `cosh`.
Search snippets and secondary surveys were leads only. No known-absence
or novelty conclusion follows. Local search used the named assessments,
selected theta/cosh/preserver/Polya records and their specific stops;
read L019–L021 and L809's relevant statement/import ranges. No sibling
notebook input or cross-notebook claim is used.

The original1926 text and translation final note were readable. Browser
screenshot calls returned no readable image; the formula was cross-checked
against Gasper's primary displayed(3.5), not an unread image. Attempts at
Polya1927 DOI10.1515/crll.1927.158.6 returned405; Digizeitschriften's
243919689_0158/log6 PDF and resolver/alternate paths were inaccessible;
shell retrieval failed DNS. The essential extension proof remains unread.
No further access loop is the next action. Park the global proof-dependent
branch and nominate a local diagnostic which does not use that premise.
Full matching Mathlib coverage remains unchecked.

The separate proposed analytical target is in
2026-11-05-polya-local-collision-mechanism-test.md. It has no assumed
all-real reference or global continuation. Its new readiness requires a
separate next-turn approval; this literature step contains no mathematics
on that target. No independent signed mechanism has yet been identified,
so creative routing is not justified merely by changing the reference.
