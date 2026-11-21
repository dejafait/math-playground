# Joint low spatial moments — working step 87

Invocation-start assessment: `literature/2026-11-03-inner-spatial-rational-response.md`,
unchanged EXPLORE. The approved target is the uniform original-D bound
for V_(1/32) in L666's full independently displaced unit-residue cube.
The supplied overview and DAG were used before the targeted proofs.
Existing notebook changes are preserved.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. The intermediate test is

    max_(|u|=1, 0<=k<=J) (1/32)^k |c_k(u)| >= exp(-n/1000),
    J=floor(sqrt(n)).

L687's exact coefficient extraction makes this a sufficient lower
certificate for V. Together with L661's audited diagonal envelope,
its rate would fit strictly inside the required 1/48 rate (the
remaining exponential margin is 79/30000 before the 1/1000 charge).
The downstream L683 implication remains unaudited; H/support and
actual-Xi realization/signs remain independent.

Continue if exact common-product relations yield the displayed uniform
block bound, a useful fully charged intermediate input, or an admissible
sequence defeating the entire angular/moment block. A single small
moment, unrelated auxiliary coefficients, or a finite sampled minimum
does not settle this test. Retain one displacement vector at all angles.

Read L666's exact definitions/pole formula, L687's coefficient extraction,
L688's Taylor-filter statement and coefficient proof, L661's envelope
statement, and L664/L683's qualified downstream statements. Compared
the recorded joint-moment finite-search failure and step 86's C672a
relaxation stop. The older search concerned the first M moments in a
broader family; it supplies neither the present block lower bound nor
an admissible full-cube countersequence. Ready literature coverage is
reused; no new source input is proposed.

Unfinished mechanism: preserve the common angular rational product and
the unit residues when relating simultaneous low moments. Exterior
anchor values alone are inadequate by C672a. Investigate the finite
algebraic relations before any claim of coercivity; the target is still
unresolved at this checkpoint. No numerical evidence or lemma is yet
claimed.

## Completed attempt and overlap check

The attempted closure used the continued moment vector at angular
u=0. The exact product in L666 (6) gives W_a(0)=x/a, so the proposed
unit-residue normalization was

    c_1(0)=x*M/R^2,
    c_k(0)=x*R^(-k-1)*sum_a a^(k-1).

These are continued rational values, not circle means of the original
meromorphic functions. The first identity retains the unit residues
and is independent of the displacement vector. The hope was that the
whole low-moment block would transfer this normalization inexpensively
to the angular circle.

The necessary common-pole cancellation led to the already canonical
[C645p](../lemmas/C645p-angular-projection-zero-evaluation-cost.md),
especially Sections 1--3. Its inner multiplier has precisely the poles
p_j=t_j*x/U as zeros. The complete multiplier at zero is

    pi_n=(80/121)^(n-1)*(n-1)!/n^(n-1),
    -log(pi_n)/n -> 1+log(121/80).

C645p already proves the noncancelling value, the exact ambient
continuation cost, and its failure even with the entire spatial
continued response retained. Its Fourier projection is not being
identified with the present full response. Rather, multiplying the
present moment functions by that same inner factor cancels their
interior poles and encounters the same value pi_n at zero; the outside
poles remain outside the disk. This is a reproduction of its mechanism,
not an independent coercivity input or an admissible countersequence.

For the proposed first-moment use, the resulting candidate lower
certificate is pi_n*(1/32)*d*M/R^2. Its decay rate exceeds one,
whereas the desired block certificate has rate 1/1000. The full
continued spatial response in C645p is only O(M); there is no
compensating exponential gain from merely retaining more of its
moments. The exact formula and proof of the costly multiplier remain
canonical in C645p; they are not duplicated as a new lemma here.
No proof was found that simultaneous moment smallness forces an
additional cancellation or a better family-specific transfer.

This is an inconclusive mathematical exploration with a detected
overlap. It establishes no new mathematical input and supplies no new
counterexample or informative negative beyond C645p. In particular the
sharpness of its ambient continuation operator is not sharpness on
L666's prescribed unit-residue vectors. The full low-moment block and
the approved V/original-D estimate are still open. Stop this origin-value
closure; do not repeat it using more continued moments.

## Concrete continuation within the unchanged ready norm target

Use the explicit full-support displaced nodes of L673, with its fixed
parameter 1/10, and keep every original residue equal to one. Its
auxiliary interpolation weights, and L681's different Robin weights,
are not those residues. The targeted check of L673, L681 Sections 1--2,
C681b's hypotheses/conclusion and the recorded Robin stops found no
unit-residue estimate for this test. L681 already supplies the entire
function

    D_n(z)=z*cosh(lambda*z)+rho*sinh(lambda*z),
    lambda=pi/h, rho=h/10, h=27/(10*n),

with exactly the required simple zeros in its finite rectangle. Its
audited zero census and the saved finite residue theorem can be reused.
The proposed new mechanism is to test the logarithmic-derivative
kernel D_n'/D_n for the original unit weights. No contour identity,
error estimate or positivity for that changed kernel is asserted here.
L665's absolute perturbation-kernel stop must remain in force; the new
test must retain signed terms and the full finite boundary.

Bounded test for the next invocation: determine whether this fixed
L673 subfamily has c_0(-1)>=1/(4R) beyond one absolute onset. Symmetry
makes the proposed inequality real. Success would give V>=1/(4R),
which L661's audited envelope would convert to the approved original-D
rate for this full-support subfamily only. It would not prove the
full-cube bound. Failure of this fixed-angle certificate must not be
reported as failure of V: stopping the norm target would still require
its full angular/spatial normalized countersequence. Record the signed
main term and every finite-edge remainder, or the precise obstruction.

Essential inputs to read next are L666, L673, L681's zero census,
L664's complete-product contour bounds and L661's diagonal envelope.
The general full-cube correlation inequality, L683 audit, L657/L658
qualifications, H/support, realization and Xi signs remain unresolved.
This is a proposed finite contour specialization under the unchanged
EXPLORE norm assessment, not a newly approved source theorem. No
fresh general sampling result or literature refresh is required.

No lemma, DAG, PROOF.md, mathematical script or source assessment was
changed. Outcome EXPLORATION, classification REPRODUCTION: the new
attempt reached an existing obstruction and did not close its intended
block estimate. Count one inconclusive mathematical attempt after the
zero reported at invocation; no scheduler or recovery state was edited.
