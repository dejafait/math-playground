# Reed–Solomon grand MCA challenge: argument overview

The [source audit](foundations/01-target-and-source-audit.md) confirms the official rates and error target.
The July ABF26 definition remains unread. A [pinned ArkLib model](foundations/02-pinned-affine-line-model.md) supplies an exact affine-line support event and adjacent-grid convention; it is not identified with ABF26.

## Endpoint candidate review

For the frozen model, L001 proves that a nonempty proper safe set is right-open
and has no largest real member. C001a supplies a smooth length-16, dimension-one
RS code over \(\mathbb F_{5^{56}}\) with error \(1/5^{56}<2^{-128}\) below
radius \(1/16\), and at least \(6/5^{56}>2^{-128}\) at radius \(7/8\).
The critical review found no error in these model-only arguments, but the challenge-level disproof lacks certified definition, endpoint, and field-size hypotheses.
L002 gives \(E_C(\delta)\le\binom n2/q\) at every radius for a length-n constant code.
At length 16 all radii are safe once \(q\ge120\cdot2^{128}\), with a smooth example over \(\mathbb F_{5^{60}}\).
The smaller-field witness cannot refute an eventual assertion at fixed length;
if an attained maximum is assumed, the witness is excluded by that hypothesis.

## Unresolved gap

The ABF26 event, allowed parameters, and field-size and endpoint qualifications remain uncertified.
For the frozen event, small and some distance-boundary cells are exact and one smooth code has a proved crossing; wider sharp radii and terminal field-size qualifications remain. At H of order sixteen in F_97^* and q=97^20, deciding the four-omission cell now reduces to L010's nonpersistent sixteen-count equality.
Changing the field changes the code; a grid maximum, supremum, and attained maximum differ.

## Partial results

L003 covers every RS dimension \(1\le k<n\). Interpolation compresses a failing
restriction to k+1 coordinates, each supplying at most one bad challenge.
With \(N=\binom n{k+1}\), this gives \(E_C(\delta)\le\min\{1,N/q\}\).
Taking \(b_i=x_i^k\) and avoiding \(\binom N2\) hyperplanes attains N distinct
challenges when \(q>\binom N2\), yielding exact error N/q for \(\delta\ge1-(k+1)/n\).

Thus \(q\ge N2^{128}\) suffices for all-radius safety. A smooth length-16 domain over \(F_{5^{64}}\) satisfies this for all four rates; at n=256,k=128 the threshold exceeds \(2^{379}\).

L004 retains radius information: a direction failing on s coordinates fails on
at least \(\binom{s-1}k\) of their (k+1)-subsets. Different challenges use disjoint
certificates. With \(m=\max\{k+1,\lceil n(1-\delta)\rceil\}\),
\[
 E_C(\delta)\le\min\left\{1,\frac1q
 \left\lfloor\frac{\binom n{k+1}}{\binom{m-1}k}\right\rfloor\right\}.
\]
This certifies safety at \(2^{-128}\) for \(\delta<90/256\) when n=256,k=128,
\(q=257^{32}\), on a smooth domain, although the all-radius test fails there.
The local factor is sharp for one altered coordinate; the error bound need not
be sharp, and failure of its sufficient test does not prove unsafety.

L005's exact one-omission result is retained. L006 extends it to
\(E_C(\delta)=(r+1)/q\) for \(r/n\le\delta<(r+1)/n\),
\(r\ge1\), and \(3r\le n-k\). A discrepancy of three errors is a codeword
of weight at most 3r, forcing an affine family. Coordinate-root counting and an
explicit construction give equality; safety is equivalent to \(q\ge(r+1)2^{128}\).
The two-omission cell has error 3/q for all listed rates on smooth domains
of length at least 16; at n=256,k=128 the theorem determines cells through r=42.

L007 handles the boundary n-k+1=3r: either all errors have a common affine
lift, or their supports are disjoint r-sets. This bounds the bad count by
max{r+1,floor(n/r)}. The r+1 construction still applies, giving the exact
count 44 for n=256,k=128,r=43, through the excluded endpoint 44/256.
This remains short of L004's sufficient interval. On the smooth domain F_17^*
over every F_(17^s), with k=8, five split cubic fibers attain the other branch:
the error is exactly 5/q on [3/16,1/4), rather than 4/q. Its exact budget
is q>=5*2^128; q=17^32 meets it while L004's count 23 does not certify it.

L008 gives \(E_C(\delta)\ge(2r+2)/q\) for n-k=2r, r>=1, k>=2, and delta>=r/n.
Two disjoint (r+1)-sets provide overlapping errors within two affine families.
For the length-16, dimension-8 code on F_17^*, this supplies ten bad challenges at delta=1/4 over every F_(17^s).
Since \(5\cdot2^{128}\le17^{32}<10\cdot2^{128}\), L007 and monotonicity give the exact safe set [0,1/4) at q=17^32:
largest safe grid radius 3/16, real supremum 1/4, and no attained maximum.
Its count 130 at n=256,k=128,r=64 is insufficient for q=257^32. Wider sharp errors remain open.

L009 limits a full two-dimensional syndrome orbit to weighted order-four cosets and four projective directions; general lines remain open.
L010 bounds a general affine pencil by sixteen bad parameters when its Hankel determinant and all coordinate locators are nonzero polynomials.
Singular parameter values are included through root multiplicity. Equality requires split squarefree quartics whose roots each occur at exactly four coordinates, with nonzero Hankel determinant there.
Thus sixteen would require sixteen distinct four-error supports, each coordinate used four times; its existence remains unresolved.
L011 covers nonzero-D pencils with a persistent coordinate locator: puncturing leaves at most three errors, including at singular parameters.
Loss of original input failure forces a common four-coordinate residual family with at most four bad parameters; otherwise the cited punctured MCA bound gives twelve.
L012 covers D identically zero: the pointwise rank identity excludes weight-four representatives, and enlargement of the agreement support preserves input failure, so the original bad set equals the three-error bad set and has at most five parameters by L007.
For H of order sixteen in F_97^* and q=97^20, L010–L012 exhaust all pairs: nonzero D with no persistent locator, nonzero D with one, and zero D, with counts at most sixteen, twelve, and five respectively.
L013 excludes the prescribed two-block family as a sixteen-count witness: its actual locator is a divided difference, with count 10, 11 or 15 determined by one fiber. C013a exhibits a partition with a four-point fiber, attaining eleven and improving the global interval to \(11/q\le E_C(\delta)\le16/q\) on [1/4,5/16). The allowable count is fifteen; L010's equality remains undecided. L014 encodes it by coefficient equations and inverse affine-moment compatibility. L015 reduces pencils representable on five coordinates to 330 rational points in projective four-space: sixteen would require eleven collinear points. The complete finite configuration test reports at most six; its class exclusion depends on that computation and supplies no bound for arbitrary pencils. The eleven-count witness is proved by the displayed L013 specialization independently of the enumeration. L016 removes the compulsory zero-syndrome kernel for the saved common-coordinate triple at 0,1,2; affine quotient equations reduce arbitrary extension-field weights to a complete rational certificate, giving at most five bad parameters for that fixed triple, attained by an actual pencil. This exclusion depends on the finite certificate and leaves arbitrary triples open.

## Known traps checked

The preliminary web page, unread July paper, and library transcription are
not silently interchanged. The bad support may depend on the challenge, and
failure is tested on that same support; ordinary correlated agreement is not
substituted. The support bounds are uniform over both input words, including
degenerate directions; each bad support is reduced only after it has been
chosen. Shrinking a support can lose the radius's size requirement, so L003's
exact converse is restricted to terminal radii. L004 does not infer global
sharpness from a sharp local factor. L005 handles zero quotient directions
and lines through the origin. L006 uses its strict distance condition and
same-support failure even when its entire affine family is r-sparse.
L007 treats equality separately. L008 proves same-support failure and degree bounds over every extension and makes no global-sharpness claim. L011 treats lost original-support failure and allows nonsmooth punctured domains; closeness alone is not counted as badness. L012 uses singularity only for an already witnessed sparse error and retains failure on an enlarged support; its five count is not an attainment claim on H.
No common codeword is assumed; L009's orbit obstruction and L010 alone do not give global bounds. L010 proves same-support failure and the converse locator test, including lower-weight multiplicities; the global sixteen count uses the exhaustive L010–L012 partition. L013 verifies its locator on actual moments; C013a checks its exact fiber and residual root over the full field. L014 retains exact splitting and a kernel vector with nonzero actual Hankel determinant. L015 proves the extension-field passage before its finite point test; the recorded maximum is computational evidence and its five-coordinate class leaves general pencils open. L016 retains full weights, universal systems, lower-weight checks and projective infinity after quotienting; its fixed-triple count is conditional on the complete exact certificate, rather than a prime-field sample. Neither balanced incidence nor a fourth-power resultant alone ensures affine-moment compatibility or a global fifteen bound.
The terminal-radius hypothesis \(q>\binom N2\) is not dropped when claiming
necessity of the field threshold. The threshold examples have smooth
domains, listed rates, and exact comparisons with \(2^{-128}\). A nonempty
safe set does not establish an unspecified field-size hypothesis, and one
field does not settle an eventual assertion or a different code. Algebra proves
the results; finite searches, punctured-code checks, and arithmetic are auxiliary.
No experiment, library claim, endpoint observation, or prize-adjudication rule is presented as a verified resolution.
