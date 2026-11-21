# Finite degree/height Rice edges — source ledger1660

Literature-only working checkpoint, 19 November2026. The exact target
is the three-edge absolute integral specified in assessment1659, with
h_d=d/log(d), c=-1/4, right edge d+1/2, and threshold
exp(-d/(log(d))^2). No estimate for this observable is derived here.

Main gap: L030-L032/C032a actual-Xi algebraic-square positivity;
C028b's H_d=o(d) and a sufficient signed transfer remain unpaid.
The finite-edge target could supply a closing-error budget for a later
signed comparison. Continue only with uniform control of all three
edges, or a rigorous lower bound obstructing the budget. A corner
sample or fixed-d limit does not decide the proposed integral.

Read C048k's finite identity and fixed-d proof, C048a/C048j's exact
hypotheses and conclusions, L828 Section2's unconditional construction,
L829's density/normalization, and L718's hypothesis/conclusion and
imported-input passage. Reused source-notes1656 rather than reopening
the normalized finite-residue proof or component audits. No conditional
Bernstein premise or numerical diagnostic is imported.

Primary sources opened: Flajolet--Sedgewick1995 Section2 Lemma1/(6),
pp104--105, Section4 Theorem2 and both proof cases pp110--111;
NIST DLMF5.11(i)--(ii), particularly sectorial Stirling5.11.1 and its
complex-remainder paragraph. The published Rice PDF text obscures some
equations; the existing readable formula record1656 remains reusable.
That initial checkpoint preceded the completed comparison below. No
mathematical estimate for the target was attempted during the review.

## Primary inputs inspected

**Finite Rice.** P. Flajolet and R. Sedgewick, *Mellin transforms and
asymptotics: Finite differences and Rice's integrals*, Theoret.Comput.Sci.
144(1995),101--124, DOI10.1016/0304-3975(94)00281-M,
[author's final PDF](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf),
Section2 Lemma1/(6) and the product/gamma/beta kernel identities,
pp104--105. Analyticity on the enclosed finite domain, the selected
integer poles, and positive orientation are essential. C048k already
verifies these for actual E. Section2/(7) requires polynomial growth in
the right half-plane; Section4 Theorem2, pp110--111, requires polynomial
control on escaping circles or outside a compact subset of a half-plane.
Both proof cases close contours. None supplies a joint degree/height
error estimate for this E. Reuse the readable formula transcription
and primary/prepublication corroboration in source-notes1656. No
obscured display is used to claim a new kernel identity.

**Uniform gamma input.** NIST DLMF, version1.2.8, release2026-09-15
(version verified on the [chapter page](https://dlmf.nist.gov/5)),
retrieved19November2026. Read
[5.11.1](https://dlmf.nist.gov/5.11#E1) and
[5.11(ii)'s first remainder paragraph](https://dlmf.nist.gov/5.11#ii).
For |arg(z)|<=pi-delta, delta>0, the sectorial expansion is

    Ln Gamma(z) ~ (z-1/2)Log(z)-z+(1/2)log(2pi)
                 + sum_(k>=1) B_(2k)/(2k(2k-1)z^(2k-1)).

After k=n-1, n>=1, the complex remainder is bounded by the first
omitted term's modulus times sec^(2n)(arg(z)/2). The gamma logarithm
uses the source's continued branch, not necessarily principal log of
the gamma value. Read5.11.3 and5.11.10--11 including the K=1 exception;
they are available but unnecessary alternative remainder forms.
Read5.11.9's bounded-real-part qualification and5.11(iii)'s constant
a,b,c restriction before5.11.12--13. Neither licenses a growing shift
treated as fixed. The sectorial expansion uses full arguments instead.
No Stirling reproof is needed.

Read [DLMF5.5.1/5.5.3](https://dlmf.nist.gov/5.5) (gamma recurrence
and reflection; reflection excludes integer arguments), and
[5.2(i)](https://dlmf.nist.gov/5.2#i) (meromorphic gamma with no zeros,
entire reciprocal, poles only at nonpositive integers). These permit
exact rearrangement and compact-region treatment, not deletion of any
contour contribution. No bound for the actual product is derived here.

## Applicability inventory for a later attempt

Retain C048k's definitions, finite identity and scalar Z. C048j is
already audited; its conclusion concerns I(p)/S(p), with p=s+1/2,
not E(s)B_d(s). Its hypotheses are |p|>=e^12 and
Re(p)>=-|p|/(4log|p|), with C048a's principal W branch.
Endpoint substitution gives the following domain checks only:

| Piece | Shifted Mellin argument | Source-domain qualification |
| --- | --- | --- |
| Top/bottom | p=sigma+1/2 +- i h_d, -1/4<=sigma<=d+1/2 | Re(p)>=1/4, |p|>=h_d; eventual large-p sector applies throughout. |
| Right | p=d+1+it, -h_d<=t<=h_d | Re(p)=d+1, |p|>=d+1; eventual large-p sector includes t=0. |

The large-p onset is eventual in d; this review asserts no effective
onset for the desired budget. A proof must retain the quantitative
C048j error and all prefactors, with constants uniform in the edge
parameter. Conjugation from C048k is available for the lower edge.

For E itself the gamma argument is p. For a prospective reflected
kernel, inspect the full arguments s+1 and d+1-s. On the three edges
their real parts are respectively at least3/4 and1/2, so they lie
in the right half-plane sector of the inspected uniform theorem.
This is a source-domain check, not a derivation of that rearrangement.
Its exact identity, parity and sine factor remain calculation work.
At the middle of the right edge d+1-s=1/2-it can remain bounded.
Use exact product/recurrence or compact gamma control there; a claimed
uniform large-argument equivalent on that whole edge is invalid.
No compact piece may simply be omitted. Top and bottom, by contrast,
have growing imaginary modulus. Retaining the original product for
B_d throughout is also within scope and avoids any unproved ratio
formula. Full-argument Stirling and direct products are alternative
tools, not mandatory simultaneous assumptions.

No contour lies on a selected Rice pole. Reflection, if used in the
suggested variable s, encounters no integer s on these boundary pieces:
the horizontal imaginary part is nonzero and the right edge has
half-integer real part. This checks applicability, without supplying
any uniform sine-factor estimate. Taking real parts of an analytic
gamma logarithm for modulus estimates must respect the cited branches.
None of these domain checks compares the actual edge integrals with
exp(-d/(log(d))^2).

## Duplicates, failures and search limits

Read the named passages in source-notes1656 and the completed assessment
`2026-11-17-unshifted-jensen-edge-source-nomination-1344.md`, its ledger
`2026-11-17-unshifted-jensen-edge-source-notes-1345.md` and the distinct
fixed-angle exterior assessment1345. Those ready literature comparisons
are reused, not refreshed. The latter source screen already inspected
Ono2610.38870v1's actual Cauchy circle, full-contour geometric/amplitude
estimates and restricted Gaussian scope, as well as the unpaid local
Airy reference. That representation is known and different. Its
reference/exterior obligations do not supply this Rice-rectangle bound;
no new claim about the source's root-count conclusion is made here.

C048k's fixed-d infinite absolute-opening stop remains accepted. It has
no uniform T_d and does not decide this joint limit. L718 instead uses
a moving-size gamma interpolation with accumulating noninteger-size
poles; it is not this entire E or this finite rectangle. Read its
canonical statement and the recorded failure
`ATTEMPTS/2026-11-03-signed-bump-gamma-rice-size-stop.md`. Its stopping
condition remains valid for its own interpolation, not a global ban.

Read the November5 global-remainder-import and endpoint-review-loop
stops. Their automatic uniformity import was unpaid. The subsequently
assembled/audited C048j now supplies its own exact I/S estimate, which
is the present input. Those old source stops neither refute C048j nor
settle E times the degree-dependent kernel. Preserve them unchanged.

Local duplicate search was restricted to named C048/L718/L828/L829
files and Mellin/Jensen/Rice-named literature/attempt records, using
finite-rectangle, three-edge, d/log and joint-degree-height phrases.
No prior matching budget was located in that search; this is not a
claim of exhaustive notebook coverage or mathematical originality.
The initial notebook-scoped git status emitted excessive untracked
filenames; that truncated output was not mathematical evidence and
was not used to orient through unrelated proofs. No existing work was
reset, discarded or edited outside the current review/checkpoint.

External queries actually issued included:

- `"Rice" "integrals" "growing" contour gamma finite differences saddle`
- `"Jensen polynomials" "Rice" rectangle Mellin`
- `"Norlund-Rice" "Jensen" polynomials`
- `"Mellin" "Rice" "xi" coefficients`
- `"Rice integrals" "gamma" "uniform" contour`
- `"Nörlund–Rice" "Jensen polynomials"`
- `"Rice" "rectangle" "xi" "Mellin"`
- `"Jensen" "finite differences" "Mellin" gamma zeta`

They produced the established finite Rice literature and mostly
unrelated hits, not an inspected matching three-edge theorem. Search
snippets, secondary RH frontier pages and model memory are not theorem
inputs. Flajolet--Vallee2000 and Vallee's2018 depoissonisation paper
appeared as general Rice-method leads; their theorem hypotheses were
not inspected and no result is imported from them. The relevant direct
primary finite theorem and exact gamma remainder were inspected instead.
No claim that these unread leads are mathematically weaker is made.
No essential source access failure remains for the specified attempt.

## Decision and limits

SPECIALIZE: the known finite identity, audited I/S bound and imported
uniform gamma tools cover the required analytic setup. The difference
to be tested is their actual uniform joint-limit product and the entire
three-edge integral. A citation alone does not decide its threshold.
This is a proposed REPRODUCTION specialization of established tools,
not a certified new theorem. No new mathematical assertion about A_d
is accepted in this source turn. The changed ready assessment1659
requires separate approval before mathematical invocation.

The downstream use and discriminator remain those in assessment1659.
A positive answer pays only a closing error. A rigorous integrated
lower bound may stop this budget; a large upper envelope cannot do so.
Signed reference geometry, a margin, extension from x=-1, zero counts,
H_d=o(d), S_F=0 and actual-Xi positivity all remain open. No justified
central creative target is presently ready: this review provides
uniform analytic tools but no new sign or sufficient height mechanism.
Full matching Mathlib coverage was not checked; this is not evidence
of absence. No lemmas or mathematical scripts were written or changed.
