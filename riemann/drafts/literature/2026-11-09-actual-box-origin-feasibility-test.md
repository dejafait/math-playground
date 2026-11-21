# Fixed actual-box origin test — source-ready nomination

TARGET: Test L921's joint-null-row relaxation with L917's fixed panel-zero normalized moment boxes for exact infeasibility, J>=0, or a box-compatible J<0 witness.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step216 completed changed-scope searches and duplicate/failure comparison in 2026-11-09-actual-box-origin-contact-test.md; reuse the inspected L918 joint-elimination and null-row assessments. No inspected result decides this fixed box-constrained implication; no originality inference.
SOURCE_EVIDENCE: Laurent, updated 2010-02-06, Lemma4.2(i)-(iii) and proofs pp54-55, Theorem3.12 pp35-36, Theorem3.15 p36 and Theorem3.16 with nonstrict qualification p37, https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf ; exact hypotheses inspected. L037/L917 supply positive interval division and accepted complete panel0 moments; L921's audited finite algebra supplies the existing coefficient and origin-sign interface.
COMPARISON: Known raw-moment necessary conditions and exact polynomial certificate methods cover the procedure, not feasibility or J's sign on this set. Adding the fixed actual-theta boxes changes L921's premises. L917/L922's determinant stops, generic covariance and heat identities do not decide the strengthened test.
GAP: The fixed set's exact feasibility and J sign remain uncomputed. A finite witness need not have a representing measure or theta realization; actual compact residual/flux, initialization/equality, other panels/degrees and global continuation remain open.
REASON: One independently testable strengthening uses actual-family data explicitly absent from the stopped relaxation; no numerical refinement or new signed mechanism is claimed. This newly saved ready nomination receives separate approval before research.
SCOPE: Exactly the TARGET and the finite set below; full/supporting Mathlib coverage unchecked. Known-method finite specialization, not protected creative work. No source theorem guarantees bounded success.

## Essential inputs and unchanged goal

Use L019/L037/L058/L874/L917/L918/L921. L922 is stop evidence only.
The main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
A local contact exclusion or origin sign could screen L918's fixed W_*
residual; it supplies no full residual sign or global continuation.
L918 as a whole remains unaudited; its finite -J origin interface is
accepted only to the extent checked in L921's step211 audit.

## Exact fixed relaxation to be tested

Use the seven complete intervals in
`scripts/heat/low-time-h2-uniform-195.json`, `/panels/0/moments`,
with saved lambda interval `/panels/0/lambda`=[0,1/5120]. Let l_k,U_k
be the exact rational lower/upper endpoints of the saved moment M_(2k),
0<=k<=6. Parse every decimal string exactly, retaining all digits.
Do not use a JSON preview, abbreviated diagnostic, binary float or
factorial-normalized coefficient in place of these endpoints.
The proposed fixed bounds are

    l_k/U_0 <= y_k <= U_k/l_0,  1<=k<=6;   y_0=1.

L037's positive interval-division rule applies because L917 certifies
l_0>0 and all these moments positive. The complete endpoint values were
inspected in step216, but these ratios have not yet been calculated.
The research implementation must save all input endpoints and exact
ratio bounds in its certificate and verify their interpretation against
L917. Using independent ratio intervals loses shared-mass/parameter
correlations; it is deliberately an outer relaxation. Do not silently
strengthen it by restoring correlations or adding extra numerical bounds.

Retain exactly L921's finite coefficient definitions in R[x]/(x^7):

    g(x)=sum_(k=0)^6 (-1)^k y_k x^k/(2k)!,
    log g(x)=-sum_(k=1)^6 S_k x^k/k,
    1/g(x)=sum_(k=0)^6 a_k x^k,
    H2=(S_(i+j+2))_(0<=i,j<=2).

Impose y1>0, M3=(y_(i+j))_(0<=i,j<=3) PSD,
N2=(y_(i+j+1))_(0<=i,j<=2) PSD, H2 PSD,
c0^2+c1^2+c2^2=1, c2!=0, and all three rows H2*c=0.
Use unchanged

    J=sum_(i,j=0)^2 c_i c_j ((i+j+2)a_(i+j+2)+a_(i+j+1)).

This is a specification for a future test, not an asserted nonempty set,
new sign identity or normalization lemma. The existing L917/L921 finite
coefficient identities may be reused with convention checks, not rederived
as new results. The raw conditions use Laurent Lemma4.2 with v=u^2,
t=3, g(v)=v. No representation converse, logarithmic kernel-support
claim, extra null row or higher-order PSD is admissible.

An actual stipulated contact with 0<lambda<=1/5120 is required to satisfy
these necessary constraints under the inherited enclosure contracts.
The relaxation contains no lambda variable, tilt law or equality to the
theta curve. The closed data panel also covers lambda=0; do not replace
the uniform data by endpoint values. Decimal-library correctness remains
assumed. No actual contact is claimed, even from finite feasibility.

## Certificate/witness acceptance and singular cases

Keep the original normalized c coordinates when forming polynomial
constraints. Use all nonempty principal minors for PSD (15 for M3,
7 for N2 and 7 for H2), not just leading minors in singular cases.
The standard real-symmetric principal-minor criterion is the same
known input as in L921. A stronger sufficient certificate may be used
if all its implications are justified; a failure of a sufficient test
is inconclusive. Existing L921 elimination may be reused only with all
singular/zero-coordinate qualifications retained. No inversion of a
zero-containing interval or an unproved positive minor is permitted.
No lower bound for |c2| may be imposed, and no c2=0 limiting behavior
may be used to skip arbitrarily small nonzero c2. Coordinates c0,c1
may vanish and the leading block may be singular.

The polynomial alternative in Laurent Theorem3.15 permits equality,
weak-inequality and disequality constraints without a compactness or
strict-feasibility assumption. For an infeasibility certificate enumerate
the exact polynomial constraint lists and verify the full identity of
that theorem, including SOS decompositions and unrestricted equality
multipliers. Strict y1>0 must be retained as y1>=0 and y1!=0 unless
its redundancy is proved from the exact bounds. For a J>=0 certificate,
exclude J<0 using -J>=0 and J!=0, or supply a directly checked signed
identity with every multiplier justified. All denominator clearings must
retain their sign and nonzero conditions. No identity/certificate has
been computed in this source nomination. General existence, rational
existence and a fixed finite-degree search are different claims; only
soundness of an actual exact certificate is imported.

A countermodel must give exact y values and a full-degree null vector
with exact unit normalization, all 29 principal-minor signs, every box
inequality, all three null rows, the finite coefficients and strict J<0.
A rational nonunit vector normalized as in L921 is an acceptable format
if the entire homogeneous/norm calculation is checked exactly. A real
algebraic witness instead needs exact defining data and verified signs.
A numerical optimizer point, an approximate zero row, J=0, merely
excluding L921's old witness, or finding a feasible tuple without its
required sign is not an informative negative result. No representing
measure or theta realization follows from these finite checks.

## One bounded attempt and decision

Perform one joint-row/fixed-box certificate-or-witness attempt using
finite exact algebra and justified bounds; stop at the first remaining
unsigned decisive expression if none of the promised outputs is obtained.
No general SOS hierarchy, parameter sweep, new support family, quadrature,
new panel, larger degree, precision refinement or L922 replay is covered.
Preserve intermediate expressions and failed bounds rather than tune
this target after an inconclusive run. Certificate checks write complete
evidence to disk and report actual/required bounds and failures concisely.

Continue only on an exact infeasibility certificate, exact J>=0
certificate, or verified box-compatible J<0 witness. Report inconclusive
otherwise. Infeasibility would exclude only these local d=2 contacts;
J>=0 would pay only L918's necessary origin condition. A negative witness
would stop this stronger finite implication without giving an actual
theta contact. Full compact residual/flux, contact initialization/equality,
other parameters/degrees, global continuation and RH remain unresolved.
No automatic continuation, further witness or refinement follows.

The relevant old stops and scope distinctions remain recorded in the
step216 review. No source-ready new signed kernel identity emerged;
this finite known-method strengthening must not be relabeled creative.
No cross-notebook input is used. Full matching and supporting Mathlib
coverage have not been checked; unknown availability is not absence.
