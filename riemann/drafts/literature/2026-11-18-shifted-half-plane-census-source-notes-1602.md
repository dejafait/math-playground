# Shifted half-plane census: completed source comparison1602

Main gap: L030-L032/C032a actual-Xi all-degree positivity. C028b's
H_d=o(d), or C028g's S_F=0, remains unpaid. The intermediate target was
a multiplicity-safe census beyond a horizontal line, with an independent
coefficient estimate capable of paying total height. Continue only for
such an estimate; abandon automatic payment from a census identity.
The latter threshold fails. This is a literature-only negative result,
not a new polynomial theorem or a computation.

## Primary source and inspected scope

Yong-jian Hu, Xu-zhou Zhan and Gong-ning Chen, *Improvement of
Hermite-Fujiwara Theorem for the Inertia of Polynomials*, Numer. Math.
J. Chinese Univ. (English Ser.) **15**(1), 1-13, October2013,
[author-hosted PDF](https://math.bnu.edu.cn/docs/20150624161407552012.pdf).
Inspected introduction(1.1)-(1.4), pp1-2; (2.1)-(2.6)/Lemma2.1,
pp3-4; Theorem2.2 and its complete proof, pp4-5; Theorem2.3 and
Corollary2.4, pp5-6; final affine-coordinate remark/references, pp12-13.
Sections3-4's interval proofs are not imported.

For complex f, put p=gcd(f,bar f), monic real, m=deg p>=1,
f=p f_1, and p=product_(k in Delta) p_k^k with pairwise coprime
monic real square-free p_k of positive degree. Under singularity of
B(f,bar f), Theorem2.3 states

    In'(f)=In(-i B(f_1,bar f_1))+(A,A,m-2A),
    A=sum_(k in Delta) k n_-(B(p_k,p_k')).

Counts include multiplicity; the third coordinate counts real-axis
roots. Hankel matrices give the alternative expression. Nonsingular
inputs use(1.3), not Theorem2.3. Theorem2.2's proof separates simple
roots by a sufficiently small shift, differentiates its Bezout matrix,
and uses nonsingularity to stabilize inertia. It gives no uniform
separation or actual-coefficient estimate. The final remark permits
affine changes of variable. These are census identities, not height
bounds.

## Applicability and edge-case obligations

C028a fixes a monic real degree-d P_d. For real y, P_d(z+iy) is still
monic degree d; conjugation means conjugating coefficients, not
differentiation. Its roots correspond to the original roots translated
by -iy, preserving algebraic multiplicity. Thus the source's upper,
lower and boundary categories refer respectively to roots above, below
and on the selected original horizontal line. This identifies the
input type and coordinate convention only; no bound or integrated
census identity is derived here.

No fixed gcd degree, residual degree or nonsingularity is available
for the actual family. A singular shift requires the conjugate gcd
and all its multiplicity strata. A derivative gcd is used subsequently
to square-free-factor that real polynomial; it is not a substitute
for the initial conjugate gcd. Boundary roots must remain in the third
coordinate with their full multiplicities. No inference of simplicity
or of boundary absence is justified by writing an inertia matrix.

Degree-one square-free factors lie within the stated m>=1 scope;
the proof's distinct-root separation condition has no pair to check
when only one distinct root exists. Constant p_k are excluded by Delta.
If p has full degree, f_1 is constant: any use of the displayed residual
term must explicitly supply the empty-matrix/zero-count convention,
which is not spelled out in the inspected statement. This review does
not assert a new zero-dimensional extension. Likewise p=1 belongs to
the nonsingular branch, outside Theorem2.3's m>=1 hypothesis. No
all-shift specialization is installed as a local lemma.

The indexed text has a notable inconsistency: Lemma2.1's opening line
writes gcd(f,f'), whereas the introduction and Theorem2.3 use
gcd(f,bar f). Page5 also contains mismatched auxiliary letters in the
shift proof. We do not silently correct these or use them to reject the
whole source. The displayed real-p construction and theorem hypotheses
are sufficient for the present negative scope comparison. A formal
import would need clean source confirmation and explicit conventions.

Access qualification: direct PDF opens initially timed out, local curl
could not resolve the host, and attempted screenshots of pp3,5,6 failed.
The indexed primary PDF text subsequently exposed all the theorem and
proof ranges listed above, including the entire Theorem2.2 proof and
Theorem2.3's assembly. No visual confirmation, fresh transcription of
the ambiguous lines, or independent audit of cited classical source
proofs is claimed. This does not block the conclusion that the inspected
interface leaves matrix inertias to be estimated.

## Comparison, duplicates and decision

The source does not supply an inequality for C028a's actual coefficients,
a bound for the residual positive index, control of the weighted gcd
indices, or degree/height-uniform payment. Exact coefficient evaluation
of a finite inertia is different from an independent asymptotic
estimate. Even a correct census at finitely many shifts would not pay
C028b's total-height threshold. C028f's tail and C028g's limit leave
compact weighted nonreal mass unresolved.

Reuse source-notes1601's DeFranco/Nathanson comparison and the
November4 projection-weighted reciprocal-inertia and November5
linked-factor assessments. Their objects differ, but the missing
independent sign/index input remains a relevant comparison. Read the
actual C028a/b interface and proofs through the applicability/height
criterion; C028f/g hypotheses and conclusions were inspected, without
re-auditing their entire proofs. No cross-notebook result was used.

Searches: `"Improvement of Hermite-Fujiwara" "2.3"`;
`Hu Zhan Chen inertia polynomials 2013 pdf`;
`"Improvement of Hermite-Fujiwara Theorem for the Inertia of Polynomials"`;
`"Hu" "Zhan" "Chen" "Hermite-Fujiwara" theorem 2.3`.
Only the primary text supplies theorem evidence; snippets and secondary
results are leads, not coverage. No novelty conclusion follows.

Park the automatic shifted-census-to-height import. Reopening requires
a specific independently supported actual-coefficient inequality and a
bounded discriminating test. This is new negative source-scope evidence,
not an RH counterexample or an impossibility theorem for inertia methods.
Full matching Mathlib coverage is unchecked and unknown.

For continuation routing only, targeted records show C028i already
audited in1590 and C032z in1585; do not repeat their audits based on
PROOF's stale pending labels. No proofs of these unrelated results were
imported here. There is no justified creative upper-payment mechanism
ready. The next nomination therefore requests bounded discovery of an
actual signed cancellation input, with identity/tail and stopped norm
routes excluded. It establishes or approves no new mathematics.
